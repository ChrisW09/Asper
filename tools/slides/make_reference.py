#!/usr/bin/env python3
"""Generate tools/slides/abcc-reference.pptx — the house style for the decks.

Pandoc styles a .pptx from a reference presentation. Rather than committing a
binary nobody can diff, this script takes pandoc's own default reference file
and patches the two parts that carry the look: the theme colour scheme and the
slide master's text styles.

    python3 tools/slides/make_reference.py

Result: deep-blue left-aligned titles, body text at a size that fits a
content-dense workshop slide, and Calibri throughout so the deck opens the same
way on any machine with Office installed.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "abcc-reference.pptx"

# HSBI-adjacent house palette, matching tools/pdf-preamble.tex.
COLOURS = {
    "dk2": "1F3864",       # deep blue
    "lt2": "EEF1F6",       # pale blue-grey
    "accent1": "1F3864",
    "accent2": "2E75B6",
    "accent3": "8FA9C9",
    "accent4": "C00000",   # reserved for warnings (disqualification rules)
    "accent5": "7F7F7F",
    "accent6": "A5A5A5",
    "hlink": "1F3864",
}


def patch_theme(xml: str) -> str:
    for name, rgb in COLOURS.items():
        xml = re.sub(
            rf'(<a:{name}>)<a:srgbClr val="[0-9A-Fa-f]{{6}}"/>',
            rf'\g<1><a:srgbClr val="{rgb}"/>',
            xml,
        )
    return xml


def patch_master(xml: str) -> str:
    # Titles: left-aligned, 28 pt, bold, accent blue instead of centred black.
    xml = xml.replace(
        '<p:titleStyle><a:lvl1pPr algn="ctr"',
        '<p:titleStyle><a:lvl1pPr algn="l"',
        1,
    )
    xml = xml.replace(
        '<a:buNone/><a:defRPr sz="3300" kern="1200"><a:solidFill>'
        '<a:schemeClr val="tx1"/></a:solidFill>',
        '<a:buNone/><a:defRPr sz="2600" b="1" kern="1200"><a:solidFill>'
        '<a:schemeClr val="accent1"/></a:solidFill>',
        1,
    )
    # Body: pandoc's 24/21/18 pt defaults overflow a workshop slide.
    body = xml[xml.index("<p:bodyStyle>"):xml.index("</p:bodyStyle>")]
    scaled = body
    for old, new in (("2400", "1700"), ("2100", "1500"),
                     ("1800", "1350"), ("1600", "1250")):
        scaled = scaled.replace(f'sz="{old}"', f'sz="{new}"')
    # Tighter hanging indents: the default leaves a gap between bullet and text.
    scaled = scaled.replace('marL="342900" indent="-342900"',
                            'marL="228600" indent="-228600"')
    scaled = scaled.replace('marL="685800" indent="-342900"',
                            'marL="514350" indent="-228600"')
    return xml.replace(body, scaled, 1)


def patch_title_layout(xml: str) -> str:
    """Title slide: everything left-aligned on one margin, title enlarged."""
    xml = xml.replace('algn="ctr"', 'algn="l"')
    # Subtitle block starts on the same margin as the title.
    xml = xml.replace(
        '<a:off x="1371600" y="2914650"/><a:ext cx="6400800" cy="1314450"/>',
        '<a:off x="685800" y="2790825"/><a:ext cx="7772400" cy="1314450"/>',
    )
    return xml.replace(
        "<a:lstStyle/>", '<a:lstStyle><a:lvl1pPr algn="l">'
        '<a:defRPr sz="3400"/></a:lvl1pPr></a:lstStyle>', 1,
    )


SECTION_RULE = (
    '<p:sp><p:nvSpPr><p:cNvPr id="90" name="Section rule"/><p:cNvSpPr/>'
    '<p:nvPr/></p:nvSpPr><p:spPr>'
    # +91440 EMU: the title placeholder has a 0.1" left inset to line up with.
    '<a:xfrm><a:off x="813753" y="2743200"/>'
    '<a:ext cx="2286000" cy="45720"/></a:xfrm>'
    '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
    '<a:solidFill><a:schemeClr val="accent1"/></a:solidFill>'
    '<a:ln><a:noFill/></a:ln></p:spPr>'
    '<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr lang="en-US"/></a:p>'
    '</p:txBody></p:sp>'
)


def patch_section_layout(xml: str) -> str:
    """Section header: lift the title, enlarge it, underline it with a rule."""
    xml = xml.replace(
        '<a:off x="722313" y="3305176"/>',
        '<a:off x="722313" y="2011680"/>',
    )
    xml = xml.replace('<a:defRPr sz="3000" b="1" cap="all"/>',
                      '<a:defRPr sz="4000" b="1" cap="all"/>')
    return xml.replace("</p:spTree>", SECTION_RULE + "</p:spTree>", 1)


def main() -> int:
    if not shutil.which("pandoc"):
        print("pandoc not found on PATH", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        default = tmpdir / "default.pptx"
        default.write_bytes(
            subprocess.run(
                ["pandoc", "--print-default-data-file", "reference.pptx"],
                capture_output=True, check=True,
            ).stdout
        )

        with zipfile.ZipFile(default) as src, \
             zipfile.ZipFile(TARGET, "w", zipfile.ZIP_DEFLATED) as out:
            for item in src.infolist():
                data = src.read(item.filename)
                if item.filename == "ppt/theme/theme1.xml":
                    data = patch_theme(data.decode("utf-8")).encode("utf-8")
                elif item.filename == "ppt/slideMasters/slideMaster1.xml":
                    data = patch_master(data.decode("utf-8")).encode("utf-8")
                elif item.filename == "ppt/slideLayouts/slideLayout1.xml":
                    data = patch_title_layout(data.decode("utf-8")).encode("utf-8")
                elif item.filename == "ppt/slideLayouts/slideLayout3.xml":
                    data = patch_section_layout(data.decode("utf-8")).encode("utf-8")
                out.writestr(item, data)

    print(f"wrote {TARGET.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
