# Repository Documentation — ABCC 2027 Preparation (HSBI)

**Purpose.** Everything the HSBI team — four Masters students (finance · innovation · computer science · general business administration) plus Prof. Dr. Christoph Weisser as coach and faculty advisor — needs to prepare for and compete at the **Asper Business Case Competition 2027**: fifth annual edition, **February 18–22, 2027**, I. H. Asper School of Business, University of Manitoba, Winnipeg.

**Status.** Documentation verified and updated **2026-08-05**. Calendar position: **Week 1 (Aug 3–9, 2026)** — kick-off week. 29 weeks to the competition.

**Provenance.** All competition facts were researched and validated (July–August 2026) against the official Asper website, the official **ABCC 2025 Event Guide** (the fullest public rulebook), the official past-case PDFs, and UM Today press coverage. The materials then went through a multi-agent adversarial review: rule claims re-checked against the fact base, all exhibit arithmetic recomputed, all official URLs link-checked. Every document flags where 2027 specifics are still TBA.

**Scope of this file.** This is the reference map of the repository: what every file is, when to use it, how the material is maintained, and what has been verified against what. [`README.md`](README.md) is the entry point — read it first if you are new. For rule questions, go to `01-competition/facts_and_rules.md`, the single source of truth.

---

## Contents

1. [Repository layout](#1-repository-layout)
2. [File inventory](#2-file-inventory)
3. [Documentation metrics](#3-documentation-metrics)
4. [Core workflows](#4-core-workflows)
5. [Maintenance rules](#5-maintenance-rules)
6. [Version history](#6-version-history)
7. [Verification log](#7-verification-log)
8. [Conventions and hard rules](#8-conventions-and-hard-rules)
9. [Known limitations and open questions](#9-known-limitations-and-open-questions)

---

## 1. Repository layout

Eight numbered folders follow the lifecycle of the project — *understand the competition → plan → form the team → train → practice → build assets → operate → brief* — plus three documents at the root.

```text
.
├── README.md                  Entry point: the competition, where we are, quick start, rules cheat sheet
├── DOCUMENTATION.md           This file: full inventory, workflows, maintenance, verification
├── CHANGELOG.md               What changed in each version
├── .gitignore                 LaTeX auxiliaries, Office lock files, .DS_Store
├── .markdownlint.json         Markdown style rules for this repository
├── 01-competition/            What the ABCC is: rules, history, judging, past cases + six official PDFs
├── 02-plan/                   When we do what: concept, dated calendar, results log
├── 03-team/                   Who we are: charter, role playbooks (incl. GenAI SOP), coach rules
├── 04-training/               Skill building: presenting, Q&A, math, English, frameworks, exercises/
├── 05-practice-cases/         What we practice on: 3 full cases, 12 mini-cases, model answers
├── 06-templates/              What we build with: slide skeletons, playbook, toolkit, judge brief
├── 07-logistics/              Organizer contact and the competition-day runbook
├── 08-briefing-slides/        The kick-off Beamer deck (LaTeX + PDF)
└── tools/                     Build scripts, LaTeX house style, and the four slide sources
```

**Every markdown document is also published beside itself** — `handbook.md` and `handbook.pdf` sit in the
same folder, the pairing `08-briefing-slides/` already used for its LaTeX deck. Thirty-seven documents
render to PDF; the four that exist to be *presented* render to `.pptx` instead
(`03-team/coach_and_ai_rules`, `04-training/frameworks`,
`04-training/presentation_and_storyline_guide`, `06-templates/case_type_playbook`). Those rendered files
are **build output** — never edit them; edit the markdown and rebuild with `tools/build_handouts.py` and
`tools/build_decks.py` (see `tools/README.md`).

**Every folder opens with its own `README.md`** — a short index that says what is in the folder, in what order to use it, and what the hard rules are. GitHub renders it under the folder's file list, so browsing the repository is self-guiding. Those indexes are navigation; this file is the reference.

Every file has exactly **one** canonical location, and every path quoted in any document is relative to this root. The numbered prefixes encode the lifecycle order and are load-bearing: some forty documents cross-reference each other by path, so folders should not be renamed casually.

**Single source of truth:** `01-competition/facts_and_rules.md`. Every rule claim in every other document defers to it. When the 2027 Competition Guide arrives, update that file **first**, then propagate (§5).

**Authoritative on dates:** `02-plan/week_by_week_plan.md`. Where any two documents disagree about *when*, the calendar wins.

**A note on history.** Until 2026-08-04 the material lived in two layers: a flat working directory plus `asper-abcc-2027.zip`, which held this same eight-folder structure as a nested git repository. That arrangement duplicated eleven files and put half the documentation behind an unzip step, so it was flattened into the single repository you are reading. The nested repository's eight commits (v1–v8) are preserved on the **`archive-history`** branch — `git log archive-history` still shows the full provenance.

---

## 2. File inventory

Paths are relative to the repository root. Counts were re-verified on 2026-08-04 (§7). Each folder's own `README.md` is its index and is not repeated in the tables below.

### 01-competition — know the game

| File | What it is | Use it when |
| --- | --- | --- |
| `01-competition/facts_and_rules.md` | **Source of truth.** Validated key data, the 2025 week pattern, all three round formats plus the final, general rules, the official 7-category rubric, the eleven past cases with URLs, sponsors, sources, and seven open questions for the organizers | Any rule question; first file to update when 2027 information lands |
| `01-competition/handbook.md` | Narrative handbook in 13 sections: what the ABCC is, history and positioning, eligibility and entry, event flow, **the three rounds in forensic detail**, scoring and tie-breaks, the rubric, hand-ins, conduct and device rules, social program, a day-in-the-life of the traditional Saturday, and the **§12 TBA tracker** | First read for every team member (W1) |
| `01-competition/judging_scoresheet.md` | Printable replica of the official rubric (7 categories, ×2.5 … ×1.0, 105 points) with behavioural anchors, a per-round timing checklist, a 15-minute feedback template, and the **briefing for an external judge** (recruiting ask + the six points to cover in 15 minutes) | Print one per judge per team before every simulation |
| `01-competition/past_cases.md` | Practice dossier in three parts: the five editions, **ten client profiles each with a re-crack brief**, and patterns to exploit for 2027 | Choosing simulation material; guessing the 2027 clients in February |
| `01-competition/past-case-pdfs/` | **Six official case PDFs** (2023 prepared + traditional, 2024 boardroom, 2025 prepared/boardroom/traditional), 6.2 MB. © University of Manitoba — confidential, internal use only | Re-crack simulations; the workbook exercises are anchored in these files |

The other five official cases (2024 cases 1 and 3, all three 2026 cases) are **not mirrored** — download them from the URLs in `facts_and_rules.md` before the sessions that need them (W14, W25).

### 02-plan — when we do what

| File | What it is | Use it when |
| --- | --- | --- |
| `02-plan/preparation_plan.md` | The training **concept**: design principles, the four roles, Phases 0–5, in-competition operating rules, risk register, weekly cadence | Understanding the *why* behind the calendar |
| `02-plan/week_by_week_plan.md` | **The calendar — governs on conflicts.** Milestone summary plus dated weeks W1 (Aug 3, 2026) → competition week → debrief, each with session, materials, role homework, and admin milestone; ends with the competition-week rhythm and the debrief protocol | Every single week — this is the operational document |
| `02-plan/simulation_log.md` | Results log pre-filled with all ten planned simulations: rubric scores, score trend, and one carried-forward goal per person per round | The same day as every simulation |

### 03-team — who we are

| File | What it is | Use it when |
| --- | --- | --- |
| `03-team/team_charter.md` | Purpose, commitments, working rules, non-negotiables, escalation path, signature block | Kick-off (W1); any charter discussion |
| `03-team/role_playbooks.md` | The shared team clock, then per-role missions, artifacts, prep minute-maps (**3-h and 4-h columns**), drills and failure modes for finance / innovation / CS & analytics / general-business strategist; the **GenAI standard operating procedure**; the one-page prep-room kit checklist | Role onboarding; before every timed simulation and every real round |
| `03-team/coach_and_ai_rules.md` | One-pager answering the two questions that decide coach behaviour: may the team use AI in competition (**yes, explicitly**), and what may the coach do and not do, round by round | Coach reference; brief the whole team in W1 |

The four roles all run against one shared clock; the **CS & analytics lead is also the designated GenAI operator**.

### 04-training — skills

| File | What it is |
| --- | --- |
| `04-training/presentation_and_storyline_guide.md` | Action titles and horizontal logic, the standard storyline skeleton, the 3-hour production workflow, the 3-minute boardroom pitch formula, seated 22-minute discussion technique, handovers, delivery for non-native speakers, dress and stage presence |
| `04-training/qa_drills.md` | Answer-first protocol, bridging, the Q&A quarterback system, drill formats, and **60 hard questions in five banks** (financial challenge, feasibility attack, ethics and risk, curveball, hostile) with model answer patterns |
| `04-training/business_math_drills.md` | **40 drills** with worked solutions, plus the weekly 30-minute routine |
| `04-training/english_phrasebook.md` | DE–EN terminology, presentation phrase bank, Q&A under fire, boardroom register, numbers out loud, pronunciation traps for German speakers |
| `04-training/vocab_flashcards.csv` | **87 flashcards** (German, English, note). Import into Anki: File → Import, comma-separated, first row is a header |
| `04-training/frameworks.md` | The framework toolbox, opening with a **five-minute selector** that maps each of the six case types to the analyses it actually needs (always-do / usually-worth-it / skip), then eight blocks — problem framing, strategy and market, marketing and brand, finance, innovation and tech, implementation, the storyline skeleton, Q&A — and a closing table of frameworks to handle with care |
| `04-training/exercises/README.md` | **The exercise catalog:** full drill inventory (≈200 solved items) mapped week by week onto the calendar, plus the ground rules and the collapse-priority order. Doubles as the index for `04-training/exercises/` |
| `04-training/exercises/format_quiz.md` | **25 questions** in four blocks (rounds and timing, deliverables and mechanics, rules and conduct, judging and context) with a full answer key — every member scores 25/25 by W3 |
| `04-training/exercises/workbook1_reading_and_structuring.md` | Five exercises: timed speed-reads and ask-decomposition **on the real ABCC case PDFs**, issue trees, case-type classification — with answer keys |
| `04-training/exercises/workbook2_quant_drills.md` | Four sets, ≈30 items: 12 sizing problems (German and Manitoba), exhibit math on the real cases, a sensitivity one-pager, and the weekly arithmetic circuit — worked |
| `04-training/exercises/workbook3_storyline_and_slides.md` | Five exercises, ≈25 items: action-title rewrites, storyline sprints, ordering drills, **implementation-plan drills (the 2.5× muscle)**, the boardroom one-slider — with models |
| `04-training/exercises/workbook4_delivery_drills.md` | Five drill formats: six 3-minute pitch scenarios with a model script, three judge briefs with a marking checklist, **24 number-attack questions** on the original cases, choreography, and the dress-rehearsal protocol |

### 05-practice-cases — material to train on

| File | What it is |
| --- | --- |
| `05-practice-cases/README.md` | Folder entry point **and** the sourcing guide: the three tiers of material in order of value, the recommended re-crack order, the original-case table, the mini-case sets, other sources, and the 2027 client pattern to train against |
| `05-practice-cases/case1_traditional_sparkasse_youth.md` | Original full case, **traditional** format (3 h, 20 + 10): Sparkasse Ostwestfalen winning back the under-30s (archetype: Access Credit Union 2026). **8 exhibits** + coach-only teaching note with solution, traps, and a 100-point rubric |
| `05-practice-cases/case2_boardroom_premium_brand.md` | Original full case, **boardroom** format (4 h, 3-min pitch + 22-min discussion): Manufaktur Lichtwerk, a premium scented-candle maker going luxury (archetype: Coal & Canary 2026). **6 exhibits** + teaching note with ten judge questions |
| `05-practice-cases/case3_prepared_arts_festival.md` | Original full case, **prepared** format (14 days, 25 + 15): Klangfest Bielefeld needing one radical idea (archetype: Jazz Winnipeg 2026). **8 exhibits** + teaching note with a four-option solution space |
| `05-practice-cases/mini_cases.md` | **Mini-cases 1–6** for 30–45-minute weekly drills, each with a 90-second sizing warm-up and a boxed solution sketch |
| `05-practice-cases/mini_cases_set2.md` | **Mini-cases 7–12** — Canadian-leaning and quant-heavier, for November onward; closes with the author-your-own assignment |
| `05-practice-cases/model_answers.md` | Calibration pack: a full worked answer outline (Access Credit Union 2026 re-crack), a filled one-page judge brief (AROW Global 2025), and how to use both |

### 06-templates — competition-legal assets

Prebuilt **own** templates are explicitly permitted (built outside prep time); **third-party** templates are not allowed for the prepared case.

| File | What it is |
| --- | --- |
| `06-templates/team_template.pptx` | The general **14-slide** skeleton: title, executive summary, content patterns, financials, chart, roadmap, risks, the ask, appendix, and the **boardroom one-slide summary**. Anonymity-proof — the placeholder consulting name "Aurora Advisory" is replaced with the fictional name the team registers with the organizers |
| `06-templates/case-type-templates/casetype_A_turnaround_nonprofit.pptx` | Type A — turnaround and revenue sustainability (13 slides) |
| `06-templates/case-type-templates/casetype_B_growth_market_entry.pptx` | Type B — growth and market entry (12 slides) |
| `06-templates/case-type-templates/casetype_C_brand_premiumization.pptx` | Type C — brand repositioning / premiumization (11 slides) |
| `06-templates/case-type-templates/casetype_D_new_product_screen.pptx` | Type D — new product / opportunity screen (11 slides) |
| `06-templates/case-type-templates/casetype_E_digital_customer_engagement.pptx` | Type E — digital customer engagement (12 slides) |
| `06-templates/case-type-templates/casetype_F_talent_and_change.pptx` | Type F — talent, trust and change (12 slides) |
| `06-templates/case_type_playbook.md` | The guide to the six types: classifying the case in the first ten minutes, then per type the core question, decisive analyses, storyline, judge attacks with counters, traps, and self-checks; closes with how to use the templates |
| `06-templates/case_financial_toolkit.xlsx` | Live-formula calculators: market sizing (top-down and bottom-up with cross-check), unit economics and break-even with a sensitivity grid, NPV and payback, CLV cohort. **Blue = inputs, yellow = key assumptions**; ships with a worked example |
| `06-templates/judge_brief_template.docx` | The boardroom one-page black-and-white judge brief, ready to fill: recommendation, three pillars, numbers table, risks, 90-day ask |

Every case-type deck opens with a **red coach-briefing slide — delete it before any round** — followed by a type-tuned storyline with coaching in the speaker notes.

### 07-logistics — operating on the ground

| File | What it is |
| --- | --- |
| `07-logistics/registration_email_draft.md` | Ready-to-send e-mail to `aspercasecomps@umanitoba.ca` covering eligibility, dates, fees, formalities, and all four open questions in one exchange |
| `07-logistics/competition_day_runbook.md` | Hour-by-hour sheets for all five days on the 2025 baseline, TBA-hedged for the 2027 weekday shift, plus standing rules and contingency plans |

### 08-briefing-slides — the kick-off deck

`08-briefing-slides/abcc_overview.tex` / `.pdf` — the kick-off Beamer deck in HSBI house style: **20 frames plus 4 section pages = 24 PDF pages**, covering the competition, the week, all three rounds, the final, deliverables, core rules, anonymity and allowed tools, scoring and tie-breaking, the official rubric, team strengths, the roadmap, and sources.

```bash
cd 08-briefing-slides && pdflatex abcc_overview.tex && pdflatex abcc_overview.tex   # twice, for navigation
```

Or upload the `.tex` to Overleaf. The `.gitignore` keeps LaTeX auxiliaries out of the repository; the built PDF is committed on purpose, so that nobody needs LaTeX to read the deck.

---

## 3. Documentation metrics

As of 2026-08-04, excluding `.git`:

| | Count | Notes |
| --- | --- | --- |
| Source files | **61** | 41 markdown · 7 pptx · 7 pdf · 1 xlsx · 1 docx · 1 csv · 1 tex · 1 .gitignore · 1 .markdownlint.json |
| Build output | **41** | 37 PDFs + 4 decks rendered from the markdown, each beside its source |
| Build tooling | **11** | `tools/`: 4 python scripts · 4 slide sources · 1 preamble · 1 reference deck · 1 README |
| Written material | **41 markdown documents, ≈81,000 words** | ≈6 hours of reading end to end |
| Binary assets | ≈8.5 MB | 6.2 MB official case PDFs · 2.3 MB slide templates |
| Working tree | ≈9.5 MB content | Plus ≈20 MB of packed git history |

Word count by folder: `05-practice-cases` 28,500 · `04-training` 15,800 · `01-competition` 12,200 · `03-team` 4,900 · `02-plan` 4,100 · `07-logistics` 1,900 · `06-templates` 2,600 · `08-briefing-slides` 200 · root documents (README, this file, changelog) 10,400.

Nine of the 41 markdown files are navigation: the three root documents, one `README.md` per lifecycle folder, and the exercise catalog in `04-training/exercises/`. Sixteen of the long documents carry their own table of contents.

Exercise volume: ≈200 solved items — 25 quiz questions, ≈85 workbook items across four workbooks, 40 math drills, 60 Q&A questions, 12 mini-cases, 3 full graded cases, 10 re-crack briefs.

---

## 4. Core workflows

**Kick-off (W1 — the current week).** Present `08-briefing-slides/abcc_overview.pdf` → everyone reads `01-competition/handbook.md` → sign `03-team/team_charter.md` → assign roles per `03-team/role_playbooks.md` → brief the team on `03-team/coach_and_ai_rules.md` → send `07-logistics/registration_email_draft.md`.

**A normal training week (Phases 2–3).** One 3–5 h weekend block per `02-plan/week_by_week_plan.md` (simulation or workshop) → one 60–90 min midweek debrief plus a skill session from `04-training/`, opened by a mini-case → 30 min of individual drills (math routine, flashcards) on a third day. The per-week exercise layer is in `04-training/exercises/README.md`. **If a week collapses, the priority order is simulation > mini-case > workbook item > individual drills** — protect the simulations above all.

**Running a simulation.** Pick the case from the week plan → coach prints `01-competition/judging_scoresheet.md` → run under competition-identical conditions (staggered release, timed prep, one laptop per student, internet and GenAI allowed, **no coach contact**, `.pptx` to the "USB" at the pickup deadline, all four speak, yellow card at 5 min and red at 1) → score on the official rubric → 2 strengths / 2 gaps / 1 drill per person → enter results in `02-plan/simulation_log.md` the same day → goals carry into the next week.

**When a case lands (competition or graded simulation).** Classify the type within ten minutes using `06-templates/case_type_playbook.md` → duplicate the matching skeleton from `06-templates/case-type-templates/`, **delete its red briefing slide**, rename to the round's file convention → storyline pass, **titles first** → parallel build along the role minute-maps in `03-team/role_playbooks.md` → every number through `06-templates/case_financial_toolkit.xlsx` → for boardroom rounds fill `06-templates/judge_brief_template.docx` with wording that mirrors the summary slide.

**Prepared-case sprint (on release, ~2 weeks).** Follow Phase 4 of `02-plan/preparation_plan.md` day by day: deep read and client research → parallel workstreams → storyline plus **coach review, which is allowed in this round** → deck build → dress rehearsals → freeze. Submit the `.pptx` by e-mail **at least 24 h before the deadline**, named `[Team Name] Prepared Case`; the strategist owns submission, the coach confirms receipt.

**Competition week.** `07-logistics/competition_day_runbook.md` is the daily script; the standing rules at its top apply all week. Note the open weekday question: the published window **Feb 18–22, 2027 falls Thursday–Monday**, while all three ABCC-format editions started on a Wednesday, so 2027 would be the first Thursday start since the format change. The runbook and the week plan map the 2025 round order onto the published dates and mark every weekday *expected*; the analysis and the booking consequence are in `01-competition/facts_and_rules.md`, "The 2027 weekday question".

**After.** Debrief in the week of Feb 23: retro against the rubric, archive all decks and scores, write a two-page handover for the next HSBI team, send thank-yous, and update `01-competition/handbook.md` with everything 2027 actually did differently.

---

## 5. Maintenance rules

- **Rules first.** Whenever the organizers publish 2027 information (Competition Guide, agenda, deadlines, fees), update `01-competition/facts_and_rules.md` **first**, then sweep the repository for affected statements. The **TBA tracker in `01-competition/handbook.md` §12** lists exactly what to confirm: the day-by-day schedule and which date carries which round, the case sponsors (watch the sponsor page and @Asper_BCC from autumn — case writing starts around October), the prepared-case release date and deck deadline, the 2027 field, prize amounts, the Round 1 venue, and any rule deltas versus 2025.
- **Propagation order** after a rules change: `01-competition/facts_and_rules.md` → `01-competition/handbook.md` → `01-competition/judging_scoresheet.md` (if the rubric moved) → `02-plan/week_by_week_plan.md` (if dates moved) → `07-logistics/competition_day_runbook.md` → `08-briefing-slides/abcc_overview.tex` (rebuild the PDF twice) → `04-training/exercises/format_quiz.md` (the answer key quotes the rules) → `README.md` and this file.
- **The calendar is authoritative.** Date conflicts resolve in favour of `02-plan/week_by_week_plan.md`. Its phase numbers are calendar phases and deliberately differ from the concept phases in `preparation_plan.md`.
- **Log every simulation the same day** in `02-plan/simulation_log.md`, with rubric scores and one carried-forward goal per person.
- **One canonical copy per file.** If a document is worth reaching quickly, link to it — do not copy it to the root. The two-layer duplication this repository used to carry is exactly what §1 removed.
- **Never commit the HSBI name** into a slide template, judge brief, or any competition-facing asset. Anonymity is a disqualification rule and the assets here are deliberately clean.
- **Keep the repository private.** `01-competition/past-case-pdfs/` holds confidential competition documents.
- **Hand over after the competition.** Write the debrief and the two-page handover, then pass the repository to the next HSBI team (final section of the week plan).

---

## 6. Version history

Full detail in [`CHANGELOG.md`](CHANGELOG.md). Work packages, not semantic versions.

| Version | What it delivered |
| --- | --- |
| v1 | Initial: briefing deck, preparation plan, resources |
| v2 | Validated handbook, past-case dossier + PDFs, three practice cases, training pack, dated calendar; deck and facts aligned to the official 2025 Event Guide rules and rubric |
| v3 | Adversarial review fixes (36 findings), all URLs validated, mini-case pack, role playbooks + GenAI SOP, model answers, phrasebook, scoresheet, simulation log, anonymity-proof team template |
| v4 | Six case-type skeletons + tackling playbook, financial toolkit, judge-brief template, day runbook, flashcards, registration e-mail, team charter |
| v5 | Restructure into the eight numbered lifecycle folders; all cross-references rewritten; `DOCUMENTATION.md` added |
| v6 | Exercise program (≈200 solved items): format quiz, four workbooks anchored in the real ABCC cases, mini-case set 2, week-mapped catalog; coach & AI rules one-pager |
| v7 | Consistency pass: text-corruption repair, drill arithmetic fixes, corrected past-case counts |
| v8 | Documentation overhaul: inventory re-verified and re-pathed, metrics, verification log, changelog |
| v9 | Flattened to a single repository: archive unzipped into the root, eleven duplicated files removed, zip retired, root documents de-duplicated against each other, history preserved on `archive-history` |
| v10 | Material and structure improvement round: a `README.md` index per folder · tables of contents in 16 long documents · one heading convention across the three practice cases · repo-wide markdown normalization plus `.markdownlint.json` · the 2027 weekday question researched and propagated · `frameworks.md` rebuilt around a case-type selector · external-judge briefing added · Q&A-length conflict resolved · `index.md` merged into the practice-cases README |
| **v11** | **Second content audit:** every remaining answer key and teaching note recomputed (model answers, case-1 economics, workbook hooks) · weekday analysis extended to all five editions (three Wednesday starts in a row) and repropagated · boardroom file name added to the compliance card · verification log extended |

**Git.** `main` carries the current material. The **`archive-history`** branch holds the eight commits of the formerly nested repository (v1–v8) — kept for provenance, never merged. To publish privately:

```bash
gh repo create asper-abcc-2027 --private --source=. --push
# or: git remote add origin git@github.com:<user>/asper-abcc-2027.git && git push -u origin main
```

---

## 7. Verification log

What was checked, so the next reader knows what is asserted and what is assumed. Structural checks ran 2026-08-04; the content audit below was extended 2026-08-05.

**Structure**
- 113 files excluding `.git`: 61 source files (41 markdown, 7 pptx, 7 pdf, 1 xlsx, 1 docx, 1 csv, 1 tex, 1 `.gitignore`, 1 `.markdownlint.json`), 41 rendered documents (37 pdf, 4 pptx), and 11 files of build tooling in `tools/`.
- Every folder-qualified cross-reference in every markdown file resolves from the repository root; all **178+ in-page anchors** (the generated tables of contents) resolve to real headings; no anchor is broken.
- No duplicated files (verified by content hash): before the flattening, all eleven workspace duplicates were confirmed **byte-identical** to their canonical counterparts, so nothing was lost when they were deleted. The single exception was `abcc_overview.pdf`, where two builds of the same 25-page deck existed — the newer one (2026-08-01 13:04 UTC) was kept.
- All six official case PDFs present in `01-competition/past-case-pdfs/` (6.2 MB); the other five official cases are URL-only, as documented.
- `archive-history` holds 8 commits, `git fsck` clean.

**Content audit, second pass (2026-08-05)** — the remaining answer keys and teaching notes, read end to end:
- `05-practice-cases/model_answers.md`: the Access CU model economics recomputed ($8.0M = 4.5 + 1.75 + 1.75 and 0.8 + 1.7 + 2.75 + 2.75; ~$670 per member; +12,000 as ≈+6% of membership and ≈+40%/+52% of the youth segment on the 15%/11% base) and the AROW brief's gates (0.6 + 1.6 + 2.0 = 4.2 = the Year-1 investment; Gate 1 ≈ 15% of spend, matching "before 85% of spend").
- Case 1's coach-only teaching note: the CLV path (€19/€87/€261/€378 at 96–98% retention, 8% discount) reproduces to ≈€1,420 — inside the stated €1,100–1,500 before mortgage optionality; the guardrail trap (0.7 + 3.4 + 0.9 + 1.3 = €6.3m > €4.5m), the redesigned package (3.1 + 0.2 + 2.4 + 1.8 = €7.5m), the cliff yield (16–21 pp × 3,400 ≈ +550–700), the funnel yield (21–26 pp × 9,400 ≈ +2,000–2,500), the value at stake (3,700 × €1,500–2,000 ≈ €6–7m), the funding exposure (€427m × 60–90 bp = €2.6–3.8m), and the CIR bridge (≈€4–4.5m against €241m ≈ 1.5–1.9 points) all recompute.
- Every drill hook in workbook 4's number-attack gauntlet exists in the case it targets (the €5,000 interest cap, the €7.5m package, the 6,000–8,000 breakeven, the 78% parent-opened share, Klangfest's €330k floor, the Westkrone and Innovationsfonds dates).
- Workbook 1's answer keys checked against the real case PDFs' facts as profiled in `past_cases.md`; the 2024 edition (Feb 21–24) added to the weekday analysis, making it three Wednesday starts in a row.

**Internal consistency** (checked across all markdown files)
- **Every quantitative answer key in the repository recomputed**, and all of it holds: the 40 drills and anchor numbers in `04-training/business_math_drills.md`; all four exercise sets in `04-training/exercises/workbook2_quant_drills.md` (sizing ladder, exhibit math on the real cases, the sensitivity grid, the arithmetic circuit); and the key calculation in each of the twelve mini-cases, including the derived ones — the overtime premium (€54 × 0.4/1.4), the agency premium (€2.8M × 0.65/1.65), the renter-first lifetime margin, and contribution per bottleneck-hour. One labelling defect was found and fixed: mini-case 7 used "summer contribution: 1.71M × 41%" where 1.71M is the April–October operating season (1.8M less 90k of winter revenue), not the 82% that lands in July–September.
- The 3-hour and 4-hour prep phase clocks match line for line between `03-team/role_playbooks.md` and `07-logistics/competition_day_runbook.md`, and each sums exactly to its window.
- Round formats, score weights (25/30/45), rubric multipliers, and card timings agree wherever they are restated.
- The ten planned simulations in `02-plan/simulation_log.md` match the calendar week for week.
- Two conflicts were found and fixed: `04-training/frameworks.md` claimed a 60-second Q&A answer limit against `qa_drills.md`'s 20–30 seconds (frameworks now defers to the owning file), and the three practice cases used three different heading conventions (now one four-part structure).

Re-run the structural checks with:

```bash
find . -type f -not -path './.git/*' | wc -l                    # expect 54
python3 - <<'EOF'
import re, os, glob
bad = {}
for p in glob.glob('**/*.md', recursive=True):
    t = open(p, encoding='utf-8').read()
    refs = {m for m in re.findall(r'`([^`\n]+)`', t)
            if m.count('/') >= 1 and ' ' not in m and not m.startswith(('http','[','/','git','cd ','gh '))}
    refs |= {m for m in re.findall(r'\]\(([^)\s]+)\)', t) if not m.startswith(('http','mailto','#'))}
    for r in refs:
        r0 = r.split('#')[0].rstrip('/')
        if r0 and '§' not in r0 and not (os.path.exists(r0)
                or os.path.exists(os.path.join(os.path.dirname(p), r0))):
            bad.setdefault(p, set()).add(r)
print(bad or 'all cross-references resolve')
EOF
```

Bare filenames inside the inventory tables of this file are section-scoped, not links; the check above only follows folder-qualified paths. `CHANGELOG.md` legitimately names files that no longer exist — that is what a changelog is for.

**Content counts** (all confirmed against the files): 87 flashcard rows · 40 math drills · 60 Q&A questions in five banks · 25 quiz questions in four blocks · mini-cases numbered 1–6 and 7–12 · exhibits 8 / 6 / 8 in cases 1 / 2 / 3 · `team_template.pptx` 14 slides · case-type decks 13 / 12 / 11 / 11 / 12 / 12 slides (A–F) · briefing deck 20 frames + 4 section pages = 24 PDF pages · 41 markdown files, ≈81,000 words · eleven official cases across ten clients.

**Dates.** February 18–22, 2027 is **Thursday–Monday**. All three ABCC-format editions started on a Wednesday (2024: Feb 21–24; 2025: Feb 19–23; 2026: Feb 18–21 with Sunday departure), so 2027 as published would be the first Thursday start since the format change. This is recorded as an open question in `facts_and_rules.md` and the handbook's §12 tracker, and flagged in the calendar, the runbook, and `README.md`. W1 of the plan is Aug 3–9, 2026.

**Rebuilt.** `08-briefing-slides/abcc_overview.pdf` is rebuilt from source with pdflatex (twice, for navigation) whenever the deck changes; currently 24 pages.

**Not verified here.** Nothing on the official Asper website was re-fetched during these passes; all competition facts still carry their July–August 2026 validation date. Re-validate when the 2027 Competition Guide is published.

---

## 8. Conventions and hard rules

- **Anonymity.** Nothing said, worn, or shown may identify HSBI. The team competes under a **fictional consulting name it chooses and registers with the organizers before the event** (the templates ship with the placeholder "Aurora Advisory"), plus a **division letter A–I drawn at on-site registration** that sets the week's slots. The name is ours; the letter is theirs. Naming your school to a judge is disqualification.
- **Coach silence.** From the release of a boardroom or traditional case until the team has presented, no contact of any kind. Any coach–team communication during a presentation or Q&A, or any coach intervention in the question period, means immediate disqualification. Advisors of finalist teams stay silent until their team has presented. The coach is fully in the game for the prepared case and for everything before the competition.
- **GenAI.** Explicitly permitted during timed prep. The edge is the drilled procedure, not the access: one designated operator, narrow sanctioned tasks, and **no unverified number reaches a slide**. Framing, option choice, and the recommendation are never outsourced. Do not paste confidential case text into consumer tools.
- **Confidentiality.** The case PDFs in `01-competition/past-case-pdfs/` are © University of Manitoba and marked "no reproduction or transmission" — internal team use only. Do not redistribute; keep the repository private.
- **File conventions.** Competition hand-ins follow the organizers' naming (`[Team Name] Prepared Case`, `[Team Name] Traditional Case`). Case data in the original practice cases is fictional and labelled as such. Documents state their own source and validation date at the top.
- **How documents reference each other.** Two deliberate styles: **navigation files** (the root documents and each folder's `README.md`) use clickable *relative* markdown links; **content documents** cite other files as backticked paths from the repository root, e.g. `` `01-competition/facts_and_rules.md` `` — unambiguous when a page is printed, pasted into a chat, or read on paper, which is how the training material is actually used. Do not mix the two within a file.
- **Markdown style.** Enforced by `.markdownlint.json`: line length unconstrained (prose wraps at ~100 characters or per sentence), table delimiter rows padded (`| --- | --- |`), every fenced block carries a language, inline HTML allowed, duplicate headings allowed only between different parents, and **MD025 off** — the practice cases use H1 as part separators (`# THE CASE`, `# EXHIBITS (CASE DATA)`, `# YOUR TASK`, `# === TEACHING NOTE (coach only) ===`), so multiple H1s per file are intentional there.
- **Long documents carry a `## Contents` list** of their H2 sections, placed after the intro. In the three practice cases the list deliberately stops at the teaching-note marker.

---

## 9. Known limitations and open questions

- **The 2027 agenda, deadlines, fees, and field are TBA.** Everything schedule-shaped in this repository is a 2025/2026-baseline assumption, flagged in place. The published Thursday–Monday footprint of Feb 18–22, 2027 would be the first Thursday start in the series, so even the weekday frame is unconfirmed — see `facts_and_rules.md`, "The 2027 weekday question".
- **Original practice material uses fictional data.** The three full cases and all worked model answers are internally consistent inventions, labelled as case data; teaching-note figures are calibration aids, not real-company facts.
- **Eligibility of the specific HSBI student mix needs written confirmation** from the organizers — the top open question in `01-competition/facts_and_rules.md`.
- **Five of the eleven official cases are URL-only** (2024 cases 1 and 3, all three 2026 cases); download them before the sessions that use them (W14, W25).
- **The git history is large for a documents repository** (≈20 MB packed, against a ≈9.4 MB working tree), because six official case PDFs and seven slide decks are versioned and earlier commits also carried a 14 MB zip of the whole repository. This is sunk history; nothing further grows it unless binaries change.

Open questions to put to the organizers after registration (all four are covered by `07-logistics/registration_email_draft.md`): the 2027 agenda and prepared-case release/submission dates · the registration process and fee for an international team and what it covers, plus eligibility confirmation · roster, bio and photo requirements plus advisor registration · whether the 2027 rules package changes anything versus the 2025 baseline, specifically any **new generative-AI clauses**.

**Contacts.** `aspercasecomps@umanitoba.ca` — Judith Jayasuriya (Instructor & Lead, Experiential Learning), Steven Harrison (Case Competition Coordinator, +1 204 396 9631) · Instagram @Asper_BCC · Drake Centre, Asper School of Business, 181 Freedman Crescent, Winnipeg.
