#!/usr/bin/env python3
"""Flag deck slides whose content will not fit on the slide.

There is no PowerPoint renderer available in this environment, so this script
does the arithmetic instead: it reads the generated .pptx, takes each shape's
real geometry from the slide XML (or the master, for inherited placeholders),
estimates how many wrapped lines the text produces at its effective font size,
and reports anything that runs past the bottom of its box.

    python3 tools/check_decks.py [file.pptx ...]

The estimate is deliberately conservative — Calibri metrics are approximated by
an average character width — so treat a flagged slide as "look at this one",
not as a hard failure.
"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"

EMU_PER_PT = 12700
# Calibri: mean advance width and line height as a fraction of the font size.
CHAR_WIDTH = 0.47
LINE_HEIGHT = 1.22
CELL_PAD_PT = 14      # left + right inset inside a table cell
PARA_SPACE_PT = 4

DEFAULT_BODY_PT = 17
DEFAULT_TABLE_PT = 13.5
DEFAULT_TITLE_PT = 26


def text_of(node: ET.Element) -> str:
    return "".join(t.text or "" for t in node.iter(f"{A}t"))


def wrapped_lines(text: str, width_pt: float, size_pt: float) -> int:
    """Line count for `text` wrapped into `width_pt`, at least 1."""
    if not text.strip():
        return 1
    per_line = max(1, int(width_pt / (size_pt * CHAR_WIDTH)))
    # Greedy wrap, so a long unbreakable token still costs one line.
    lines = 0
    current = 0
    for word in text.split():
        need = len(word) + (1 if current else 0)
        if current + need > per_line and current:
            lines += 1
            current = len(word)
        else:
            current += need
    return max(1, lines + (1 if current else 0))


def run_size(paragraph: ET.Element, default: float) -> float:
    sizes = [int(rpr.get("sz")) / 100
             for rpr in paragraph.iter(f"{A}rPr") if rpr.get("sz")]
    return min(sizes) if sizes else default


def shape_geometry(shape: ET.Element, master: dict) -> tuple[float, float] | None:
    """Width and height in points, from the shape or its master placeholder."""
    xfrm = shape.find(f".//{A}off/..")
    if xfrm is not None:
        ext = xfrm.find(f"{A}ext")
        if ext is not None:
            return (int(ext.get("cx")) / EMU_PER_PT,
                    int(ext.get("cy")) / EMU_PER_PT)
    ph = shape.find(f".//{P}ph")
    if ph is None:
        return None
    kind = ph.get("type", "body")
    return master.get("title" if kind == "title" else "body")


def master_geometry(zf: zipfile.ZipFile) -> dict:
    root = ET.fromstring(zf.read("ppt/slideMasters/slideMaster1.xml"))
    out = {}
    for shape in root.iter(f"{P}sp"):
        ph = shape.find(f".//{P}ph")
        ext = shape.find(f".//{A}ext")
        if ph is None or ext is None:
            continue
        out[ph.get("type", "body")] = (int(ext.get("cx")) / EMU_PER_PT,
                                       int(ext.get("cy")) / EMU_PER_PT)
    return out


def table_height(tbl: ET.Element) -> float:
    cols = [int(c.get("w")) / EMU_PER_PT for c in tbl.iter(f"{A}gridCol")]
    total = 0.0
    for row in tbl.iter(f"{A}tr"):
        tallest = 1
        for index, cell in enumerate(row.iter(f"{A}tc")):
            width = (cols[index] if index < len(cols) else cols[-1]) - CELL_PAD_PT
            for para in cell.iter(f"{A}p"):
                size = run_size(para, DEFAULT_TABLE_PT)
                tallest = max(tallest,
                              wrapped_lines(text_of(para), width, size))
        total += tallest * DEFAULT_TABLE_PT * LINE_HEIGHT + 6
    return total


def check(pptx: Path) -> list[str]:
    problems = []
    with zipfile.ZipFile(pptx) as zf:
        master = master_geometry(zf)
        slides = sorted(
            (n for n in zf.namelist()
             if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
            key=lambda n: int(re.search(r"\d+", n.rsplit("/", 1)[1]).group()),
        )
        for number, name in enumerate(slides, 1):
            root = ET.fromstring(zf.read(name))
            title = ""
            for shape in root.iter(f"{P}sp"):
                ph = shape.find(f".//{P}ph")
                if ph is not None and ph.get("type") == "title":
                    title = text_of(shape)

            for shape in root.iter(f"{P}sp"):
                geometry = shape_geometry(shape, master)
                if geometry is None:
                    continue
                width, height = geometry
                ph = shape.find(f".//{P}ph")
                is_title = ph is not None and ph.get("type") == "title"
                default = DEFAULT_TITLE_PT if is_title else DEFAULT_BODY_PT
                used = 0.0
                for para in shape.iter(f"{A}p"):
                    size = run_size(para, default)
                    lines = wrapped_lines(text_of(para), width - 30, size)
                    used += lines * size * LINE_HEIGHT + PARA_SPACE_PT
                if used > height:
                    what = "title" if is_title else "body"
                    problems.append(
                        f"slide {number:>2} · {what} overruns by "
                        f"{used - height:.0f}pt — {title[:52]!r}")

            for frame in root.iter(f"{P}graphicFrame"):
                ext = frame.find(f".//{A}ext")
                tbl = frame.find(f".//{A}tbl")
                if ext is None or tbl is None:
                    continue
                available = int(ext.get("cy")) / EMU_PER_PT
                needed = table_height(tbl)
                if needed > available:
                    problems.append(
                        f"slide {number:>2} · table overruns by "
                        f"{needed - available:.0f}pt — {title[:52]!r}")
    return problems


def main() -> int:
    if sys.argv[1:]:
        targets = [Path(a) for a in sys.argv[1:]]
    else:
        # Only the generated decks — the slide templates in 06-templates/ are
        # hand-built and have their own geometry.
        sys.path.insert(0, str(ROOT / "tools"))
        from build_decks import DECKS
        targets = [ROOT / t for t in DECKS.values()]
    total = 0
    for pptx in targets:
        problems = check(pptx)
        total += len(problems)
        print(f"{pptx.relative_to(ROOT)}: "
              f"{len(problems) or 'no'} slide(s) to look at")
        for problem in problems:
            print(f"    {problem}")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
