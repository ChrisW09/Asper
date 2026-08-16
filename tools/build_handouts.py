#!/usr/bin/env python3
"""Build a print-ready PDF next to every markdown document in the repository.

Each PDF sits beside its source — `01-competition/handbook.md` builds
`01-competition/handbook.pdf` — the same way `08-briefing-slides` pairs its
LaTeX source with the built deck. The markdown stays the editable original;
the PDF is build output and is never edited by hand.

    python3 tools/build_handouts.py            # build everything
    python3 tools/build_handouts.py 04-training/frameworks.md   # build one file

What the script does beyond a plain `pandoc x.md -o x.pdf`:

* uses the first `# H1` as the PDF title and drops it from the body;
* re-points every `.md` cross-link at the PDF or deck built from that file, so
  the PDFs link to each other the way the markdown does;
* rebalances pipe-table separator rows (`| --- |`) so column widths in the PDF
  are proportional to the actual content instead of all equal — without this,
  a six-column rubric table gets six equal columns and the long criterion text
  turns into a tower;
* adds a table of contents to documents long enough to need one;
* applies the shared house style in tools/pdf-preamble.tex.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREAMBLE = ROOT / "tools" / "pdf-preamble.tex"

# Documents converted to PowerPoint decks instead of PDFs (see tools/slides/).
SLIDE_SOURCES = {
    "03-team/coach_and_ai_rules.md",
    "04-training/frameworks.md",
    "04-training/presentation_and_storyline_guide.md",
    "06-templates/case_type_playbook.md",
}

# Folder label printed in the running head.
FOLDER_LABELS = {
    "01-competition": "01 · Competition",
    "02-plan": "02 · Plan",
    "03-team": "03 · Team",
    "04-training": "04 · Training",
    "04-training/exercises": "04 · Training / Exercises",
    "05-practice-cases": "05 · Practice cases",
    "06-templates": "06 · Templates",
    "07-logistics": "07 · Logistics",
    "08-briefing-slides": "08 · Briefing slides",
    ".": "Repository root",
}

TOC_MIN_WORDS = 1200
TOC_MIN_SECTIONS = 4

SEP_CELL = re.compile(r"^:?-{2,}:?$")
TABLE_TOTAL_DASHES = 130  # > pandoc's --columns default, so widths are honoured


# --------------------------------------------------------------------------
# markdown preprocessing
# --------------------------------------------------------------------------

def split_row(line: str) -> list[str] | None:
    """Split a pipe-table row into cells, or return None if it is not one."""
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    body = stripped[1:]
    if body.endswith("|"):
        body = body[:-1]
    return [c.strip() for c in body.split("|")]


def visible_width(cell: str) -> int:
    """Rough rendered width of a table cell: strip the markdown noise."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cell)      # links
    text = re.sub(r"[*_`]", "", text)                          # emphasis / code
    return len(text.strip())


def rebalance_tables(text: str) -> str:
    """Make separator-row dash counts proportional to real column content.

    Pandoc derives relative LaTeX column widths from the number of dashes in
    the `| --- |` row. All source tables here use three dashes everywhere,
    which yields equally wide columns. This rewrites the separator so a column
    holding a sentence gets more of the page than one holding "×2.5".
    """
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    in_fence = False
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if in_fence or split_row(line) is None or i + 1 >= len(lines):
            out.append(line)
            i += 1
            continue

        sep_cells = split_row(lines[i + 1])
        header_cells = split_row(line)
        if not sep_cells or not all(SEP_CELL.match(c) for c in sep_cells if c):
            out.append(line)
            i += 1
            continue

        # Collect the whole table.
        rows = [header_cells]
        j = i + 2
        while j < len(lines) and split_row(lines[j]) is not None:
            rows.append(split_row(lines[j]))
            j += 1

        ncols = len(sep_cells)
        weights = []
        for c in range(ncols):
            cells = [r[c] for r in rows if c < len(r)]
            widths = [visible_width(cell) for cell in cells]
            longest = max(widths) if widths else 1
            average = sum(widths) / len(widths) if widths else 1
            # A file path in `code` has no break points, so the column has to
            # be at least as wide as its longest unbreakable token.
            token = max((len(t) for cell in cells
                         for t in re.sub(r"[*_`]", "", cell).split()), default=1)
            # Blend max and mean: the max keeps a long sentence from being
            # squeezed, the mean stops one outlier cell from dominating.
            raw = max(0.6 * longest + 0.4 * average, token * 1.25)
            # Compress sublinearly and add a constant for cell padding, so a
            # narrow column ("08:30–10:15") is not starved next to a column
            # holding a whole paragraph — short entries cannot be wrapped and
            # would otherwise run into the neighbouring column.
            weights.append((raw + 4.0) ** 0.70)

        total = sum(weights)
        dashes = [max(3, round(w / total * TABLE_TOTAL_DASHES)) for w in weights]
        alignments = [
            (c.startswith(":"), c.endswith(":")) for c in sep_cells
        ]
        new_cells = []
        for (left, right), n in zip(alignments, dashes):
            core = "-" * max(3, n - int(left) - int(right))
            new_cells.append(f"{':' if left else ''}{core}{':' if right else ''}")

        out.append(line)
        out.append("| " + " | ".join(new_cells) + " |")
        out.extend(lines[i + 2:j])
        i = j
    return "\n".join(out)


def normalise(src_rel: Path, path: str) -> str:
    """"07-logistics/../03-team/x.md" -> "03-team/x.md", relative to the root."""
    parts: list[str] = []
    for part in (src_rel.parent / path).as_posix().split("/"):
        if part == "..":
            if parts:
                parts.pop()
        elif part not in (".", ""):
            parts.append(part)
    return "/".join(parts)


def retarget_links(text: str, src_rel: Path) -> str:
    """Point every `.md` cross-link at the PDF or deck built from that file.

    Because the PDF is written beside its source, every other relative link —
    the xlsx toolkit, the docx judge brief, the official case PDFs, a folder —
    already resolves from the PDF's location and is left untouched.
    """
    def repl(match: re.Match) -> str:
        label, target = match.group(1), match.group(2)
        path, _, anchor = target.partition("#")
        if not path.endswith(".md") or path.startswith(("http://", "https://")):
            return match.group(0)
        ext = ".pptx" if normalise(src_rel, path) in SLIDE_SOURCES else ".pdf"
        return f"[{label}]({path[:-3]}{ext}{('#' + anchor) if anchor else ''})"

    return re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", repl, text)


def prepare(src: Path) -> tuple[str, str, bool]:
    """Return (body markdown, title, wants_toc) for a source document."""
    raw = src.read_text(encoding="utf-8")
    rel = src.relative_to(ROOT)

    title = rel.stem.replace("_", " ").title()
    lines = raw.split("\n")
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            del lines[idx]
            break
    body = "\n".join(lines).lstrip("\n")

    body = retarget_links(body, rel)
    body = rebalance_tables(body)

    words = len(body.split())
    sections = sum(1 for line in body.split("\n") if line.startswith("## "))
    # Sixteen documents already carry a hand-written table of contents; adding
    # a generated one on top would print the same list twice.
    has_own_toc = bool(re.search(r"(?im)^#{2,3}\s+(contents|table of contents)\b", body))
    wants_toc = (
        words >= TOC_MIN_WORDS
        and sections >= TOC_MIN_SECTIONS
        and not has_own_toc
    )
    return body, title, wants_toc


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------

def latex_escape(text: str) -> str:
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"),
                 ("$", r"\$"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"),
                 ("}", r"\}"), ("~", r"\textasciitilde{}"),
                 ("^", r"\textasciicircum{}")]:
        text = text.replace(a, b)
    return text


def short_title(title: str) -> str:
    """Trim a long document title down to something a running head can hold."""
    head = re.split(r"\s+[—–-]\s+", title)[0]
    return head if len(head) <= 52 else head[:49].rstrip() + "…"


def build_pdf(src: Path) -> tuple[Path, list[str]]:
    """Build one PDF. Returns the destination and any typesetting warnings."""
    rel = src.relative_to(ROOT)
    dest = src.with_suffix(".pdf")

    body, title, wants_toc = prepare(src)
    folder = rel.parent.as_posix()
    label = FOLDER_LABELS.get(folder, folder)

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        md_file = tmpdir / "doc.md"
        md_file.write_text(body, encoding="utf-8")

        head_file = tmpdir / "head.tex"
        head_file.write_text(
            "\\providecommand{\\ABCCdocsource}{}\n"
            "\\providecommand{\\ABCCshorttitle}{}\n"
            f"\\renewcommand{{\\ABCCdocsource}}{{{latex_escape(label)}}}\n"
            f"\\renewcommand{{\\ABCCshorttitle}}{{{latex_escape(short_title(title))}}}\n"
            + PREAMBLE.read_text(encoding="utf-8"),
            encoding="utf-8",
        )

        cmd = [
            "pandoc", str(md_file),
            "--from",
            # -tex_math_dollars: "CA$150 … CA$6-7m" is currency, not maths.
            "markdown+task_lists+pipe_tables+lists_without_preceding_blankline"
            "+smart-raw_html-tex_math_dollars",
            "--standalone",
            "--include-in-header", str(head_file),
            "--columns", "72",
            "--metadata", f"title={title}",
            "--metadata", f"author=ABCC 2027 preparation · {label}",
            "--metadata", "lang=en-GB",
            "-V", "documentclass=article",
            "-V", "papersize=a4",
            "-V", "fontsize=10pt",
            "-V", "geometry:a4paper,top=2.6cm,bottom=2.4cm,left=2.3cm,right=2.3cm",
            "-V", "colorlinks=true",
            "-o", str(tmpdir / "doc.tex"),
        ]
        if wants_toc:
            cmd += ["--toc", "--toc-depth=2"]

        result = subprocess.run(cmd, capture_output=True, text=True, cwd=tmpdir)
        if result.returncode != 0:
            raise RuntimeError(f"{rel}: pandoc failed\n{result.stderr[-3000:]}")

        # Two passes: the second resolves the table of contents and page refs.
        for _ in range(2):
            run = subprocess.run(
                ["lualatex", "-interaction=nonstopmode", "doc.tex"],
                capture_output=True, text=True, cwd=tmpdir,
            )
        log = (tmpdir / "doc.log").read_text(encoding="utf-8", errors="replace")
        pdf = tmpdir / "doc.pdf"
        if not pdf.exists():
            raise RuntimeError(f"{rel}: lualatex failed\n{tail_errors(log)}")
        shutil.copyfile(pdf, dest)

    return dest, collect_warnings(log)


MISSING_CHAR = re.compile(r"Missing character: There is no (\S+) \((U\+[0-9A-F]+)\)")
OVERFULL = re.compile(r"Overfull \\hbox \((\d+\.\d+)pt too wide\)")


def collect_warnings(log: str) -> list[str]:
    """Glyph gaps and badly overrunning lines — the two things that show up
    as visible defects in the printed page."""
    warnings = []
    missing = sorted({f"{m.group(1)} {m.group(2)}" for m in MISSING_CHAR.finditer(log)})
    if missing:
        warnings.append("missing glyphs: " + ", ".join(missing))
    bad = [float(m.group(1)) for m in OVERFULL.finditer(log)]
    severe = [b for b in bad if b > 20]
    if severe:
        warnings.append(f"{len(severe)} line(s) overrun the text block by >20pt")
    return warnings


def tail_errors(log: str) -> str:
    lines = [ln for ln in log.split("\n") if ln.startswith("!")]
    return "\n".join(lines[:12]) or log[-2000:]


def main() -> int:
    if not shutil.which("pandoc"):
        print("pandoc not found on PATH", file=sys.stderr)
        return 1

    targets = sys.argv[1:]
    if targets:
        sources = [ROOT / t for t in targets]
    else:
        sources = sorted(
            p for p in ROOT.rglob("*.md")
            if ".git" not in p.parts
            and "tools" not in p.parts          # slide sources, not documents
            and p.relative_to(ROOT).as_posix() not in SLIDE_SOURCES
        )

    failures = []
    for src in sources:
        rel = src.relative_to(ROOT)
        try:
            dest, warnings = build_pdf(src)
            pages = page_count(dest)
            print(f"  ok   {rel}  ->  {dest.relative_to(ROOT)}  ({pages} p.)")
            for warning in warnings:
                print(f"       ! {warning}")
        except Exception as exc:  # noqa: BLE001 - report and keep going
            failures.append(rel)
            print(f"  FAIL {rel}\n{exc}", file=sys.stderr)

    print(f"\n{len(sources) - len(failures)}/{len(sources)} PDFs built "
          "beside their sources")
    if failures:
        print("failed: " + ", ".join(str(f) for f in failures), file=sys.stderr)
    return 1 if failures else 0


def page_count(pdf: Path) -> str:
    """Page count via ghostscript, if it happens to be installed."""
    if not shutil.which("gs"):
        return "?"
    probe = f"({pdf}) (r) file runpdfbegin pdfpagecount = quit"
    result = subprocess.run(
        ["gs", "-q", "-dNODISPLAY", "-dNOSAFER", "-c", probe],
        capture_output=True, text=True,
    )
    return result.stdout.strip() or "?"


if __name__ == "__main__":
    raise SystemExit(main())
