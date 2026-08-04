# Repository Documentation — ABCC 2027 Preparation (HSBI)

**Purpose.** Everything the HSBI team (four Masters students: finance, innovation, computer science, general business administration + Prof. Dr. Christoph Weisser as coach) needs to prepare for, travel to, and compete at the **Asper Business Case Competition 2027** — fifth annual edition, February 18–22, 2027, Asper School of Business, University of Manitoba, Winnipeg.

**Provenance.** All competition facts were researched and validated (July–August 2026) against the official Asper website, the official **ABCC 2025 Event Guide** (the fullest public rulebook), the official past-case PDFs, and press coverage; every document flags where 2027 specifics are still TBA. The materials went through a multi-agent adversarial review (rule claims verified against the fact base, all exhibit arithmetic recomputed, all official URLs link-checked).

---

## 1. How this repository is organized

The eight numbered folders follow the lifecycle of the project — *understand the competition → plan → form the team → train → practice → build assets → travel → brief*:

```
asper-abcc-2027/
├── README.md                  Entry point: quick facts + next actions
├── DOCUMENTATION.md           This file: full inventory, workflows, maintenance
├── 01-competition/            What the ABCC is: rules, history, judging, past cases
├── 02-plan/                   When we do what: concept plan, dated calendar, results log
├── 03-team/                   Who we are: charter, role playbooks (incl. GenAI SOP)
├── 04-training/               Skill building: presenting, Q&A, math, English, frameworks
├── 05-practice-cases/         What we practice on: 3 full cases, 12 mini-cases, model answers
├── 06-templates/              What we build with: slide skeletons, toolkit, judge brief
├── 07-logistics/              Getting there: travel, registration, competition-day runbook
└── 08-briefing-slides/        The kick-off Beamer deck (LaTeX + PDF)
```

**Single source of truth:** `01-competition/facts_and_rules.md`. Every rule claim in every other document defers to it. When the 2027 Competition Guide arrives, update that file first, then propagate.

## 2. File inventory

### 01-competition — know the game

| File | What it is | Use it when |
|---|---|---|
| `facts_and_rules.md` | **Source of truth**: validated rules, round formats, official rubric, schedule pattern, past-case links, open questions for the organizers | Any rule question; after registration, update here first |
| `handbook.md` | Narrative handbook: history 2023–2027, eligibility, event flow, forensic round detail, scoring, conduct, day-in-the-life, TBA tracker | First read for every team member (W1) |
| `judging_scoresheet.md` | Printable official-rubric scoresheet (7 categories, ×2.5…×1.0, /105) with behavioural anchors, timing checklists, feedback template | Print for every simulation judge |
| `past_cases.md` | All editions + all 10 past clients profiled, each with a **re-crack brief**; patterns for 2027 | Choosing simulation material; February client-guessing |
| `past-case-pdfs/` | Six official case PDFs 2023–2025 (© University of Manitoba, internal use only) | Re-crack simulations |

### 02-plan — when we do what

| File | What it is | Use it when |
|---|---|---|
| `preparation_plan.md` | The training **concept**: principles, roles, five phases, prepared-case sprint, risks | Understanding the why behind the calendar |
| `week_by_week_plan.md` | **The calendar** (governs on conflicts): dated weeks Aug 3, 2026 → competition + debrief, with sessions, materials, homework, admin milestones | Every week — this is the operational document |
| `simulation_log.md` | Results log pre-filled with all ten planned simulations; rubric scores + one goal per person per round | After every simulation |

### 03-team — who we are

| File | What it is | Use it when |
|---|---|---|
| `team_charter.md` | Commitments, working rules, non-negotiables, escalation; signature block | Kick-off (W1); any charter talk |
| `role_playbooks.md` | Per-role missions, artifacts, prep minute-maps (3-h and 4-h), drills, failure modes; **GenAI standard operating procedure**; prep-room kit checklist | Role onboarding; before every timed simulation |
| `coach_and_ai_rules.md` | One-pager answering: may the team use AI in competition (yes — officially, with our SOP discipline) and what the professor/coach may and may not do, round by round | Coach reference; brief the team in W1 |

### 04-training — skills

| File | What it is |
|---|---|
| `presentation_and_storyline_guide.md` | Action titles, storyline skeleton, 3-h deck production workflow, boardroom technique, delivery for non-native speakers |
| `qa_drills.md` | Answer-first protocol, bridging, quarterback system; 60 hard questions with model answer patterns |
| `business_math_drills.md` | 40 drills with worked solutions; weekly 30-minute routine |
| `english_phrasebook.md` | DE–EN terminology, phrase banks (presentation, Q&A, boardroom), numbers out loud, pronunciation traps |
| `vocab_flashcards.csv` | 87 flashcards (German, English, note) — import into Anki: File → Import, comma-separated, first row is header |
| `frameworks.md` | Framework toolkit (problem framing, strategy, marketing, finance, innovation, implementation) + storyline skeleton + Q&A protocol |
| `exercises/README.md` | **Exercise catalog**: full drill inventory (~200 solved items) mapped week by week onto the calendar |
| `exercises/format_quiz.md` | 25-question competition-format quiz with answer key — every member scores 25/25 by W3 |
| `exercises/workbook1_reading_and_structuring.md` | Timed speed-reads and ask-decomposition **on the real ABCC case PDFs**, issue trees, case-type classification — with answer keys |
| `exercises/workbook2_quant_drills.md` | 12 sizing problems (DE + Manitoba), exhibit math on the real cases, sensitivity one-pager, weekly arithmetic circuit — with worked answers |
| `exercises/workbook3_storyline_and_slides.md` | Action-title rewrites, storyline sprints, ordering drills, implementation-plan drills (the 2.5× muscle), boardroom one-slider — with models |
| `exercises/workbook4_delivery_drills.md` | 3-minute pitch scenarios (with a model pitch script), judge-brief writing with marking checklist, 24 number-attack Q&A per original case, choreography, dress-rehearsal protocol |

### 05-practice-cases — material to train on

| File | What it is |
|---|---|
| `index.md` | Practice-material index and the recommended order (real re-cracks first, original cases for graded sims) |
| `case1_traditional_sparkasse_youth.md` | Original full case, traditional format (3 h, 20+10): regional bank winning back under-30s; 8 exhibits + coach-only teaching note with solution, traps, 100-point rubric |
| `case2_boardroom_premium_brand.md` | Original full case, boardroom format (4 h, 3-min pitch + 22-min discussion): premium→luxury candle maker; 6 exhibits + teaching note with 10 judge questions |
| `case3_prepared_arts_festival.md` | Original full case, prepared format (14 days, 25+15): jazz festival needing one radical idea; 8 exhibits + teaching note with 4-option solution space |
| `mini_cases.md` | Six one-page cases for 30–45-min weekly drills, each with a 90-second sizing warm-up and a boxed solution sketch |
| `mini_cases_set2.md` | Six further mini-cases (Canadian-leaning, quant-heavier) for November onward; ends with the author-your-own assignment |
| `model_answers.md` | Calibration: a full worked answer outline (Access CU 2026 re-crack) and a filled one-page judge brief (AROW 2025) |

### 06-templates — competition-legal assets (prebuilt own templates are allowed)

| File | What it is |
|---|---|
| `team_template.pptx` | The general 14-slide skeleton: title, exec summary, content patterns, financials, chart, roadmap, risks, ask, appendix, **boardroom one-slide summary**. Anonymity-proof (placeholder consulting name "Aurora Advisory" — replace at the division draw) |
| `case-type-templates/` (6 files) | Type-specific skeletons A–F (turnaround, growth/entry, premiumization, product screen, digital engagement, talent/change), each opening with a red coach-briefing slide (delete before rounds) and a full type-tuned storyline with speaker-note coaching |
| `case_type_playbook.md` | The guideline for the six types: recognition in 10 minutes, core question, decisive analyses, storyline, judge attacks with counters, traps, self-checks |
| `case_financial_toolkit.xlsx` | Live-formula calculators: market sizing (top-down/bottom-up + cross-check), unit economics & break-even + sensitivity grid, NPV & payback, CLV cohort. Blue = inputs, yellow = key assumptions; pre-filled with a worked example |
| `judge_brief_template.docx` | The boardroom one-page b/w judge brief, ready to fill (recommendation, three pillars, numbers table, risks, 90-day ask) |

### 07-logistics — getting there and operating there

| File | What it is |
|---|---|
| `registration_email_draft.md` | Ready-to-send e-mail to aspercasecomps@umanitoba.ca covering eligibility, dates, fees, hotel block, formalities |
| `travel_logistics.md` | eTA, flight routings and price bands, Delta hotel, airport transfer, −30 °C clothing list, money/SIM, insurance (GKV does not cover Canada), 7-hour jet-lag plan, booking countdown |
| `competition_day_runbook.md` | Hour-by-hour sheets for all five days (2025 baseline, TBA-hedged) + contingency plans |

### 08-briefing-slides — the kick-off deck

`abcc_overview.tex` / `abcc_overview.pdf` — 25-frame Beamer deck (HSBI house style) covering the competition, the week, all three rounds, the final, deliverables, travel checklist, rules, the official rubric, team roles, and the roadmap. Compile with `cd 08-briefing-slides && pdflatex abcc_overview.tex` (twice, for navigation), or upload the .tex to Overleaf.

## 3. Core workflows

**Kick-off (W1).** Present `08-briefing-slides/abcc_overview.pdf` → everyone reads `01-competition/handbook.md` → sign `03-team/team_charter.md` → assign roles per `03-team/role_playbooks.md` → send `07-logistics/registration_email_draft.md` → start the admin track in `07-logistics/travel_logistics.md`.

**A normal training week (Phases 2–3).** Weekend block per `02-plan/week_by_week_plan.md` (simulation or workshop) → midweek 60–90-min debrief + skill session from `04-training/` → 30-min individual drills (math routine, flashcards). Mini-case drill (`05-practice-cases/mini_cases.md`) opens the midweek session.

**Running a simulation.** Pick the case from the week plan → coach prints `01-competition/judging_scoresheet.md` → run under competition-identical rules (timed, one laptop each, internet + GenAI allowed, no coach contact, .pptx "USB" hand-in at the deadline, all four speak, yellow/red cards) → score → 2 strengths / 2 gaps / 1 drill each → enter results in `02-plan/simulation_log.md` → goals carry into the next week.

**When a case lands (competition or graded sim).** Classify the type in 10 minutes per `06-templates/case_type_playbook.md` → duplicate the matching skeleton from `06-templates/case-type-templates/`, delete its red briefing slide, rename per the round's file convention → storyline pass (titles first) → parallel build per the role minute-maps → numbers through `06-templates/case_financial_toolkit.xlsx` → boardroom rounds: fill `06-templates/judge_brief_template.docx`, wording mirroring the summary slide.

**Prepared-case sprint (on release, ~2 weeks).** Follow Phase 4 of `02-plan/preparation_plan.md` day by day; coach input is allowed in this round; submit the .pptx by e-mail **at least 24 h before the deadline** ("[Team Name] Prepared Case").

**Competition week.** `07-logistics/competition_day_runbook.md` is the daily script; the standing rules at its top apply all week.

## 4. Maintenance rules

Update `01-competition/facts_and_rules.md` **first** whenever the organizers publish 2027 information (Competition Guide, deadlines, agenda, hotel), then sweep the repo for affected statements — the TBA tracker in `01-competition/handbook.md` §12 lists exactly what to confirm. Keep the calendar authoritative: date conflicts resolve in favour of `02-plan/week_by_week_plan.md`. Log every simulation the same day. Never commit anything bearing the HSBI name into slide templates or briefs — anonymity is a disqualification rule, and the repo's assets are deliberately clean. After the competition, write the debrief and hand this repository to the next team (final section of the week plan).

**Git.** The repo ships with full history. To publish privately: `gh repo create asper-abcc-2027 --private --source=. --push` (or add a remote and `git push -u origin main`). Conventions so far: one commit per work package (v1 initial → v2 validated expansion → v3 adversarial review + new material → v4 templates & toolkit → v5 restructure + documentation → v6 exercise program → v7 consistency pass).

## 5. Known limitations

The 2027 agenda, deadlines, fees, and field are TBA until the organizers publish them — everything schedule-shaped is a 2025/2026-baseline assumption, flagged as such in place. The three original practice cases and all worked model answers use **fictional, internally consistent data** (labelled as case data); teaching-note figures are calibration aids, not real-company facts. Eligibility of the specific HSBI student mix needs written confirmation from the organizers (top open question in `01-competition/facts_and_rules.md`). Eleven official past cases exist across ten clients (2023 ran both rounds on Manitoba Hydro); **six PDFs are mirrored locally** and the remaining five (2024 cases 1 and 3, all three 2026 cases) are linked by URL in `01-competition/facts_and_rules.md` and `01-competition/past_cases.md`.
