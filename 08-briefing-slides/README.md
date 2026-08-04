# 08 · Briefing slides — the kick-off deck

[`abcc_overview.pdf`](abcc_overview.pdf) — the deck the coach presents in W1 to bring the whole team to the
same understanding of the competition in one sitting. **25 pages** (21 frames + 4 section pages), Beamer,
HSBI house style, in five parts: the competition at a glance · the format and the three rounds plus the
final · deliverables before we travel · rules and judging incl. the official rubric · our team and the
roadmap.

This is an **internal** deck — it names HSBI and is never shown at the competition. Nothing in
[`../06-templates/`](../06-templates/) may inherit from it.

## Rebuilding

[`abcc_overview.tex`](abcc_overview.tex) is the source. Twice, so the navigation bar resolves:

```bash
pdflatex abcc_overview.tex && pdflatex abcc_overview.tex
```

Or upload the `.tex` to Overleaf. LaTeX auxiliaries are git-ignored; the built PDF is committed on purpose,
so nobody needs a LaTeX installation to read the deck.

**Keep it in step with the rules.** The deck restates the rubric, the round formats, and the schedule — all
of which trace to [`../01-competition/facts_and_rules.md`](../01-competition/facts_and_rules.md). It is the
second-to-last stop in the propagation order when the 2027 guide lands
([`../DOCUMENTATION.md`](../DOCUMENTATION.md) §5): update the source of truth first, this deck near the end,
and rebuild the PDF.

Per-file detail: [`../DOCUMENTATION.md`](../DOCUMENTATION.md) §2.
