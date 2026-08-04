# Changelog — ABCC 2027 Preparation (HSBI)

All notable changes to the preparation material. Two git histories exist and are tracked separately:
the **archive** (`asper-abcc-2027/`, shipped inside `asper-abcc-2027.zip`) and the **workspace**
(the flat directory that holds the zip). See `DOCUMENTATION.md` §1 for why, and §6 for how the two are
kept in sync.

Dates are the dates of the work, not of any release. Versions are work packages, not semantic versions.

---

## Archive

### v8 — Documentation overhaul · 2026-08-04

- **Two-layer model documented.** `DOCUMENTATION.md` now opens by distinguishing the workspace from the
  archive and states, file by file, which duplicates are byte-identical, which differ by design, and which
  material exists only in the archive. Previously the file described the eight numbered folders as if they
  sat next to the reader, which is only true inside the unpacked archive.
- **Inventory re-pathed and re-verified.** Every entry in the file inventory now carries its full
  archive-relative path instead of a bare filename, and every count in it was checked against the files:
  87 flashcards, 40 math drills, 60 Q&A questions in five banks, 25 quiz questions in four blocks,
  mini-cases 1–12, 8/6/8 exhibits in the three full cases, 14 slides in the team template, 13/12/11/11/12/12
  in the six case-type decks, 21 frames + 4 section pages = 25 pages in the briefing deck, 54 files in total.
- **New: documentation metrics** — 35 markdown files, ≈73,000 words, per-folder word counts, asset sizes,
  exercise volume.
- **New: sync procedure** (§6) with the exact commands for edit → commit → rebuild zip → refresh workspace
  duplicates, plus the rule that the archive is the master.
- **New: verification log** (§9) recording what was checked on 2026-08-04, a re-runnable duplicate-integrity
  script, and an explicit statement of what was *not* re-verified (no official URLs were re-fetched).
- **New: propagation order** (§7) for rules changes — which file to touch after which, ending at the
  briefing deck, the format quiz answer key, and the READMEs.
- **New: conventions section** (§10) collecting the anonymity, coach-silence, GenAI, and confidentiality
  rules that were previously scattered.
- **Weekday shift flagged in the top-level documentation.** February 18–22, 2027 falls Thursday–Monday,
  while the 2025 baseline ran Wednesday–Sunday (registration Wed Feb 19, 2025). The round-to-day mapping is
  therefore explicitly TBA in `DOCUMENTATION.md` and both READMEs, matching the hedges already present in
  `02-plan/week_by_week_plan.md` and `07-logistics/competition_day_runbook.md`.
- **Status dating.** Both READMEs and `DOCUMENTATION.md` now state the verification date and the current
  calendar position (W1, Aug 3–9, 2026) instead of an undated "now".
- **This changelog added**, in both layers.
- Archive `README.md` refreshed: current-week block, corrected next actions, weekday note, pointers to
  `DOCUMENTATION.md` and this file.
- No content documents were changed: the rule base, handbook, calendar, practice cases, workbooks,
  templates, and logistics files are untouched at v7 state.

### v7 — Consistency pass · 2026-08-04

Repaired text corruption, fixed drill arithmetic, corrected the past-case counts to eleven official cases
across ten clients (2023 ran both rounds on Manitoba Hydro), with six PDFs mirrored locally and five linked
by URL.

### v6 — Exercise program · 2026-08-01

Added ≈200 solved exercises: the 25-question format quiz with answer key, four workbooks anchored in the
real ABCC case PDFs (reading and structuring, quant, storyline and slides, delivery), mini-case set 2
(cases 7–12, Canadian-leaning and quant-heavier), and the week-mapped exercise catalog. Added the coach &
AI rules one-pager and integrated the exercise layer into the plan and documentation.

### v5 — Restructure · 2026-08-01

Reorganized everything into the eight numbered lifecycle folders (`01-competition` … `08-briefing-slides`),
rewrote all cross-references, added `DOCUMENTATION.md`, and reduced the archive `README.md` to a lean front
page.

### v4 — Templates and toolkit · 2026-08-01

Added the six case-type slide skeletons (A–F) and the case-type playbook, the financial toolkit (`.xlsx`
with live formulas), the judge-brief template (`.docx`), the competition-day runbook, the vocabulary
flashcards, the registration e-mail draft, and the team charter.

### v3 — Adversarial review · 2026-08-01

Fixed 36 findings from a multi-agent adversarial review, validated every official URL, and added the
mini-case pack (cases 1–6), the role playbooks with the GenAI standard operating procedure, the model
answers, the English phrasebook, the judging scoresheet, the simulation log, and the anonymity-proof team
`.pptx` template.

### v2 — Validation and expansion · 2026-08-01

Added the validated handbook, the past-case dossier with six mirrored official PDFs, three original full
practice cases, the training pack, and the dated week-by-week plan. Updated the briefing deck and the fact
base to the official ABCC 2025 Event Guide rules and rubric.

### v1 — Initial commit · 2026-07-31

The ABCC 2027 briefing deck, the preparation plan, and first resources.

---

## Workspace

### 2026-08-04 — Documentation overhaul

Rewrote `DOCUMENTATION.md`, substantially updated `README.md`, added this changelog, and rebuilt
`asper-abcc-2027.zip` from the archive at v8. Corrected the README's claim that the loose files are
byte-identical to their archive counterparts: `README.md` is a different document by design, and the
archive holds the newer build of `abcc_overview.pdf` — everything else was verified identical.

### 2026-08-04 — Documentation and resource update

Expanded practice cases, exercise catalog, and the team-anonymity clarification (fictional consulting name
chosen by the team, division letter A–I drawn on site); zip refreshed.

### 2026-08-01 — Workspace README

Added the long-form workspace entry point.

### 2026-08-01 — Initial import

Imported the workspace contents: documentation, briefing PDF, slide templates, toolkit, judge brief, coach
and AI rules, exercise catalog, and the archive zip.
