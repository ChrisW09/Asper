# Changelog — ABCC 2027 Preparation (HSBI)

All notable changes to the preparation material. Dates are the dates of the work, not of any release.
Versions are work packages, not semantic versions.

Until v9 the material lived in two layers — a flat working directory plus `asper-abcc-2027.zip`, which
held the eight-folder structure as a nested git repository. v9 flattened them into the single repository
this file sits in. The two histories are listed separately below; the pre-v9 archive commits are preserved
on the **`archive-history`** branch.

---

## v10 — Material and structure improvement round · 2026-08-04

### Structure

- **A `README.md` index in every lifecycle folder** (01–08). Each says what the folder holds, in what order
  to use it, and which hard rules live there. GitHub renders them under the folder's file list, so browsing
  the repository is now self-guiding. They are navigation; `DOCUMENTATION.md` remains the per-file reference.
- **`05-practice-cases/index.md` merged into that folder's `README.md`** and deleted — the new index made it
  a near-duplicate. Nothing was lost: the recommended re-crack order, the "other sources" list, and the 2027
  client pattern all moved across, and a stale instruction to "create the simulation log on first simulation"
  (it has existed since v3) is gone.
- **Tables of contents added to the 16 documents over ~1,500 words**, generated from their own headings.
  In the three practice cases the list deliberately **stops at the coach-only teaching note**, with a line
  saying so, so a table of contents cannot become a shortcut to the solution.
- **One heading convention across the three practice cases.** They had drifted into three: case 3 marked its
  teaching note with a plain paragraph and used H2 for part separators, case 2 called its narrative
  "CASE NARRATIVE", case 1 "THE CASE". All three now run
  `# THE CASE` → `# EXHIBITS (CASE DATA)` → `# YOUR TASK` → `# === TEACHING NOTE (coach only) ===`.
- **Repo-wide markdown normalization:** 111 table delimiter rows padded to `| --- | --- |` across 24 files,
  the one unlanguaged code fence fixed, trailing newlines made uniform. Codified in a new
  **`.markdownlint.json`** so the editor enforces it from here on.
- **`.gitignore`** now also excludes Office lock files (`~$*`), which appear whenever a `.pptx`/`.xlsx` is
  open.
- **The reference convention is now documented** rather than merely observed (`DOCUMENTATION.md` §8):
  navigation files use clickable relative links, content documents cite root-relative paths in backticks —
  because the training material gets printed and pasted, where a relative link is meaningless.

### Material

- **The 2027 weekday question — researched, resolved as far as it can be, and propagated.** ABCC 2025 ran
  Wed Feb 19 – Sun Feb 23 and ABCC 2026 ran Wed Feb 18 – Sat Feb 21 (departure Sunday): **both started on a
  Wednesday.** The published 2027 window, February 18–22, falls **Thursday–Monday** — the first Thursday
  start in the series. Either the window is exact (registration Thursday, gala Sunday, departure Monday) or
  the real week is Wed Feb 17 – Sun Feb 21. `facts_and_rules.md` now carries the full analysis with the
  edition-by-edition table; the handbook's §12 tracker, the calendar footnote, the runbook intro, the travel
  plan's booking countdown, and both root documents point to it. **Booking consequence, now stated where
  flights are booked:** the planned envelope (arrive Feb 16/17, return Feb 22/23) covers both readings, so it
  is safe — but nothing outside it should be booked non-refundably, and hotel nights should not be tied to a
  round order, until the agenda is published. This replaces the vaguer earlier claim that "the round-to-day
  mapping must shift somewhere".
- **`frameworks.md` rebuilt as a decision tool.** It was a 540-word list of framework names. It now opens
  with a **five-minute selector** — a row per case type (A–F, keyed to `case_type_playbook.md`) giving the
  decision the client faces, the analyses to always do, those usually worth it, and those to skip — and closes
  with a **"frameworks to handle with care"** table (SWOT, Five Forces, BCG, PESTEL, Ansoff: why judges get
  impatient, and the one condition under which each earns its slide). The blocks in between gained the
  judge-facing consequence of each tool rather than just its name.
- **A conflict between two training documents fixed.** `frameworks.md` set a 60-second limit per Q&A answer;
  `qa_drills.md` — which owns the protocol — sets 20–30 seconds standard and 45 as the maximum for a
  financial walk-through. `frameworks.md` now defers to it explicitly instead of restating a different number.
- **Briefing for an external judge added** to `judging_scoresheet.md`. The calendar asks for external judges
  five times (W17, W19, W23–24, both W25 rounds) and there was nothing to hand them: now a recruiting ask
  short enough to send as-is, and the six points to cover in fifteen minutes — play the client's
  decision-maker, Implementation & Resources counts 2.5×, question like a practitioner, the clock is hard,
  feedback as two strengths and two gaps, and the note that a judge who has *not* read the teaching note
  often gives the more useful verdict.
- **The "Training Series — Part N of 3" labels now say what the series is:** the core skills trio —
  delivery, defence, numbers — with each part linking to the other two and to the folder index. The label was
  accurate but unexplained, and three of the six training documents sit outside it.

### Verified

All 40 business-math drills recomputed (every answer and anchor holds) · the 3-hour and 4-hour prep phase
clocks match line for line between the role playbooks and the runbook, and each sums exactly to its window ·
round formats, weights, rubric multipliers and card timings agree wherever restated · the ten simulations
match the calendar week for week · 178+ in-page anchors resolve, no broken links · no duplicate file content
in the repository.

---

## v9 — One repository · 2026-08-04

- **Archive unzipped into the repository root.** The eight lifecycle folders (`01-competition` …
  `08-briefing-slides`) and `.gitignore` now sit at the top level. Every path in every document already
  pointed at this layout, so all cross-references resolve unchanged — verified file by file.
- **Eleven duplicated files removed.** `coach_and_ai_rules.md`, `exercise_catalog.md` (the copy of
  `04-training/exercises/README.md`), `team_template.pptx`, the six `case-type-templates/*.pptx`,
  `case_financial_toolkit.xlsx`, and `judge_brief_template.docx` were confirmed byte-identical to their
  canonical counterparts before deletion. `abcc_overview.pdf` existed in two builds of the same 25-page
  deck; the newer one was kept at `08-briefing-slides/abcc_overview.pdf`.
- **`asper-abcc-2027.zip` retired** (14 MB). Its content is now the repository; earlier revisions of the zip
  remain in git history.
- **Archive history preserved.** The nested repository's eight commits (v1–v8) were fetched into the
  **`archive-history`** branch before its `.git` was discarded — `git log archive-history` still shows the
  full provenance. Never merged; kept as a reference ref.
- **Root documents de-duplicated against each other.** `README.md` had grown a full per-folder file
  inventory that duplicated `DOCUMENTATION.md`; it is now the entry point (competition overview, current
  week, quick start per role, folder-level map, workflow summaries, rubric, rules cheat sheet, timeline,
  sources) and defers all per-file detail to `DOCUMENTATION.md`. Its two README variants collapsed into one.
- **`DOCUMENTATION.md` restructured** from eleven sections to nine: the two-layer explanation and the
  workspace↔archive sync procedure are gone; §1 is now a plain repository layout with a short note on the
  flattening; the verification log became a structural check with a re-runnable cross-reference script.
- **Maintenance rules gained** "one canonical copy per file — link, do not copy", replacing the sync rule.

---

## Archive history (pre-v9, branch `archive-history`)

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

## Workspace history (pre-v9, on `main`)

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
