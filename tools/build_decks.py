#!/usr/bin/env python3
"""Build the PowerPoint decks from the slide sources in tools/slides/.

Four documents in this repository exist to be *presented* in a session rather
than read at a desk. They get a .pptx instead of a PDF. The slide sources in
tools/slides/ are condensed rewrites of those documents — a deck is not a
document with the paragraphs shortened — and each source names the markdown
file it came from, so the two can be kept in step.

    python3 tools/slides/make_reference.py    # once, or after a style change
    python3 tools/build_decks.py

Each deck is written beside the document it replaces, the way the PDFs are.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLIDES = ROOT / "tools" / "slides"
REFERENCE = SLIDES / "abcc-reference.pptx"

# slide source  ->  destination, beside the markdown document it replaces
DECKS = {
    "coach_and_ai_rules.md": "03-team/coach_and_ai_rules.pptx",
    "frameworks.md": "04-training/frameworks.pptx",
    "presentation_and_storyline_guide.md":
        "04-training/presentation_and_storyline_guide.pptx",
    "case_type_playbook.md": "06-templates/case_type_playbook.pptx",
}


def build(source: Path, dest: Path) -> int:
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pandoc", str(source),
         "--reference-doc", str(REFERENCE),
         "--slide-level=2",
         "--from", "markdown+fenced_divs+pipe_tables+smart-tex_math_dollars",
         "-o", str(dest)],
        check=True, capture_output=True, text=True,
    )
    with zipfile.ZipFile(dest) as z:
        return len([n for n in z.namelist()
                    if n.startswith("ppt/slides/slide")])


def main() -> int:
    if not shutil.which("pandoc"):
        print("pandoc not found on PATH", file=sys.stderr)
        return 1
    if not REFERENCE.exists():
        print(f"missing {REFERENCE.relative_to(ROOT)} — run "
              "tools/slides/make_reference.py first", file=sys.stderr)
        return 1

    for name, target in DECKS.items():
        source = SLIDES / name
        dest = ROOT / target
        try:
            slides = build(source, dest)
        except subprocess.CalledProcessError as exc:
            print(f"  FAIL {name}\n{exc.stderr}", file=sys.stderr)
            return 1
        print(f"  ok   {source.relative_to(ROOT)}  ->  "
              f"{dest.relative_to(ROOT)}  ({slides} slides)")

    print(f"\n{len(DECKS)} decks built beside their sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
