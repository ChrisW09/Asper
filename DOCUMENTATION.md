# Repository Documentation — ABCC 2027 Preparation (HSBI)

**Purpose.** Everything the HSBI team — four Masters students (finance · innovation · computer science · general business administration) plus Prof. Dr. Christoph Weisser as coach and faculty advisor — needs to prepare for, travel to, and compete at the **Asper Business Case Competition 2027**: fifth annual edition, **February 18–22, 2027**, I. H. Asper School of Business, University of Manitoba, Winnipeg.

**Status.** Documentation verified and updated **2026-08-04**. Calendar position: **Week 1 (Aug 3–9, 2026)** — kick-off week. 29 weeks to the competition.

**Provenance.** All competition facts were researched and validated (July–August 2026) against the official Asper website, the official **ABCC 2025 Event Guide** (the fullest public rulebook), the official past-case PDFs, and UM Today press coverage. The materials then went through a multi-agent adversarial review: rule claims re-checked against the fact base, all exhibit arithmetic recomputed, all official URLs link-checked. Every document flags where 2027 specifics are still TBA.

**Scope of this file.** This is the map of the whole body of material: where it lives, what each file is, when to use it, how the pieces are kept in sync, and what has been verified against what. For the short version, read [`README.md`](README.md). For rule questions, go to `01-competition/facts_and_rules.md` — the single source of truth.

---

## Contents

1. [Two layers: workspace and archive](#1-two-layers-workspace-and-archive)
2. [How the archive is organized](#2-how-the-archive-is-organized)
3. [File inventory](#3-file-inventory)
4. [Documentation metrics](#4-documentation-metrics)
5. [Core workflows](#5-core-workflows)
6. [Keeping the two layers in sync](#6-keeping-the-two-layers-in-sync)
7. [Maintenance rules](#7-maintenance-rules)
8. [Version history](#8-version-history)
9. [Verification log (2026-08-04)](#9-verification-log-2026-08-04)
10. [Conventions and hard rules](#10-conventions-and-hard-rules)
11. [Known limitations and open questions](#11-known-limitations-and-open-questions)

---

## 1. Two layers: workspace and archive

The material exists in two layers, and knowing which one you are reading matters, because the folder paths quoted throughout this file only resolve in one of them.

| Layer | What it is | Contains |
|---|---|---|
| **Workspace** (`Asper/`) | The flat working copy in day-to-day use, itself a git repository | This file, the workspace `README.md`, `CHANGELOG.md`, two loose reference documents, the slide templates and toolkit, the briefing PDF, and `asper-abcc-2027.zip` |
| **Archive** (`asper-abcc-2027.zip`) | The complete, structured repository — **54 files** in eight lifecycle folders, **with its own git history** (8 commits) | Everything: rules, plan, team docs, training program, practice cases, templates, logistics, briefing deck, and the six official past-case PDFs |

**If you are reading this inside the workspace,** the numbered folders (`01-competition/` …) are *inside the zip*, not next to you. Unpack first:

```bash
unzip asper-abcc-2027.zip          # → ./asper-abcc-2027/ with full git history
cd asper-abcc-2027 && git log --oneline
```

**If you are reading this inside the unpacked archive,** every path below resolves relative to you, and the "workspace" is the directory the zip came from.

**Why two layers.** The workspace keeps the handful of documents and assets that get opened weekly (the coach one-pager, the exercise catalog, the slide templates, the toolkit, the briefing PDF) reachable without unpacking anything; the archive is the canonical, versioned whole. The workspace copies are duplicates, not variants — see §6 for the rule that keeps them honest and §9 for the last verification.

### What is loose in the workspace

| File / folder | Archive counterpart | Notes |
|---|---|---|
| `README.md` | `README.md` | **Differs by design.** The workspace README is the long entry point (~33 KB); the archive README is a lean repo front page (~5 KB) that points here |
| `DOCUMENTATION.md` | `DOCUMENTATION.md` | Kept byte-identical — this file is written to read correctly from either layer |
| `CHANGELOG.md` | `CHANGELOG.md` | Kept byte-identical |
| `coach_and_ai_rules.md` | `03-team/coach_and_ai_rules.md` | Byte-identical (verified 2026-08-04) |
| `exercise_catalog.md` | `04-training/exercises/README.md` | Byte-identical (verified 2026-08-04) |
| `abcc_overview.pdf` | `08-briefing-slides/abcc_overview.pdf` | Same 25-page deck, **different builds** — the archive holds the newer one (built 2026-08-01 13:04 UTC vs. 12:31 UTC). Rebuild both from the `.tex` when the deck changes |
| `team_template.pptx` | `06-templates/team_template.pptx` | Byte-identical (verified 2026-08-04) |
| `case-type-templates/` (6 × `.pptx`) | `06-templates/case-type-templates/` | All six byte-identical (verified 2026-08-04) |
| `case_financial_toolkit.xlsx` | `06-templates/case_financial_toolkit.xlsx` | Byte-identical (verified 2026-08-04) |
| `judge_brief_template.docx` | `06-templates/judge_brief_template.docx` | Byte-identical (verified 2026-08-04) |
| `asper-abcc-2027.zip` | — | The archive itself (≈14 MB) |

Everything not in that table — the rule base, the handbook, the calendar, the practice cases, the workbooks, the logistics files, the case-type playbook, the LaTeX source — exists **only in the archive**.

---

## 2. How the archive is organized

The eight numbered folders follow the lifecycle of the project: *understand the competition → plan → form the team → train → practice → build assets → travel → brief.*

```
asper-abcc-2027/
├── README.md                  Lean entry point: structure, one-paragraph overview, next actions
├── DOCUMENTATION.md           This file: inventory, workflows, maintenance, verification
├── CHANGELOG.md               What changed in each version, both layers
├── .gitignore                 LaTeX auxiliaries, .DS_Store
├── 01-competition/            What the ABCC is: rules, history, judging, past cases + PDFs
├── 02-plan/                   When we do what: concept, dated calendar, results log
├── 03-team/                   Who we are: charter, role playbooks (incl. GenAI SOP), coach rules
├── 04-training/               Skill building: presenting, Q&A, math, English, frameworks, exercises/
├── 05-practice-cases/         What we practice on: 3 full cases, 12 mini-cases, model answers
├── 06-templates/              What we build with: slide skeletons, playbook, toolkit, judge brief
├── 07-logistics/              Getting there: registration, travel, competition-day runbook
└── 08-briefing-slides/        The kick-off Beamer deck (LaTeX + PDF)
```

**Single source of truth:** `01-competition/facts_and_rules.md`. Every rule claim in every other document defers to it. When the 2027 Competition Guide arrives, update that file **first**, then propagate (§7).

**Authoritative on dates:** `02-plan/week_by_week_plan.md`. Where any two documents disagree about *when*, the calendar wins.

---

## 3. File inventory

Paths are relative to the archive root. Counts were re-verified on 2026-08-04 (§9).

### 01-competition — know the game

| File | What it is | Use it when |
|---|---|---|
| `01-competition/facts_and_rules.md` | **Source of truth.** Validated key data, the 2025 week pattern, all three round formats plus the final, general rules, the official 7-category rubric, the eleven past cases with URLs, sponsors, sources, and seven open questions for the organizers | Any rule question; first file to update when 2027 information lands |
| `01-competition/handbook.md` | Narrative handbook in 13 sections: what the ABCC is, history and positioning, eligibility and entry, event flow, **the three rounds in forensic detail**, scoring and tie-breaks, the rubric, hand-ins, conduct and device rules, social program, a day-in-the-life of the traditional Saturday, and the **§12 TBA tracker** | First read for every team member (W1) |
| `01-competition/judging_scoresheet.md` | Printable replica of the official rubric (7 categories, ×2.5 … ×1.0, 105 points) with behavioural anchors, a per-round timing checklist, and a 15-minute feedback template | Print one per judge before every simulation |
| `01-competition/past_cases.md` | Practice dossier in three parts: the five editions, **ten client profiles each with a re-crack brief**, and patterns to exploit for 2027 | Choosing simulation material; guessing the 2027 clients in February |
| `01-competition/past-case-pdfs/` | **Six official case PDFs** (2023 prepared + traditional, 2024 boardroom, 2025 prepared/boardroom/traditional), 6.2 MB. © University of Manitoba — confidential, internal use only | Re-crack simulations; the workbook exercises are anchored in these files |

The other five official cases (2024 cases 1 and 3, all three 2026 cases) are **not mirrored** — download them from the URLs in `facts_and_rules.md` before the sessions that need them (W14, W25).

### 02-plan — when we do what

| File | What it is | Use it when |
|---|---|---|
| `02-plan/preparation_plan.md` | The training **concept**: design principles, the four roles, Phases 0–5, in-competition operating rules, risk register, weekly cadence | Understanding the *why* behind the calendar |
| `02-plan/week_by_week_plan.md` | **The calendar — governs on conflicts.** Milestone summary plus dated weeks W1 (Aug 3, 2026) → competition week → debrief, each with session, materials, role homework, and admin milestone; ends with the competition-week rhythm and the debrief protocol | Every single week — this is the operational document |
| `02-plan/simulation_log.md` | Results log pre-filled with all ten planned simulations: rubric scores, score trend, and one carried-forward goal per person per round | The same day as every simulation |

### 03-team — who we are

| File | What it is | Use it when |
|---|---|---|
| `03-team/team_charter.md` | Purpose, commitments, working rules, non-negotiables, escalation path, signature block | Kick-off (W1); any charter discussion |
| `03-team/role_playbooks.md` | The shared team clock, then per-role missions, artifacts, prep minute-maps (**3-h and 4-h columns**), drills and failure modes for finance / innovation / CS & analytics / general-business strategist; the **GenAI standard operating procedure**; the one-page prep-room kit checklist | Role onboarding; before every timed simulation and every real round |
| `03-team/coach_and_ai_rules.md` | One-pager answering the two questions that decide coach behaviour: may the team use AI in competition (**yes, explicitly**), and what may the coach do and not do, round by round | Coach reference; brief the whole team in W1 |

The four roles all run against one shared clock; the **CS & analytics lead is also the designated GenAI operator**.

### 04-training — skills

| File | What it is |
|---|---|
| `04-training/presentation_and_storyline_guide.md` | Action titles and horizontal logic, the standard storyline skeleton, the 3-hour production workflow, the 3-minute boardroom pitch formula, seated 22-minute discussion technique, handovers, delivery for non-native speakers, dress and stage presence |
| `04-training/qa_drills.md` | Answer-first protocol, bridging, the Q&A quarterback system, drill formats, and **60 hard questions in five banks** (financial challenge, feasibility attack, ethics and risk, curveball, hostile) with model answer patterns |
| `04-training/business_math_drills.md` | **40 drills** with worked solutions, plus the weekly 30-minute routine |
| `04-training/english_phrasebook.md` | DE–EN terminology, presentation phrase bank, Q&A under fire, boardroom register, numbers out loud, pronunciation traps for German speakers |
| `04-training/vocab_flashcards.csv` | **87 flashcards** (German, English, note). Import into Anki: File → Import, comma-separated, first row is a header |
| `04-training/frameworks.md` | Framework toolkit in eight blocks: problem framing, strategy and market, marketing and brand, finance, innovation and tech, implementation, the storyline skeleton, the Q&A protocol |
| `04-training/exercises/README.md` | **The exercise catalog:** full drill inventory (≈200 solved items) mapped week by week onto the calendar, plus the ground rules and the collapse-priority order |
| `04-training/exercises/format_quiz.md` | **25 questions** in four blocks (rounds and timing, deliverables and mechanics, rules and conduct, judging and context) with a full answer key — every member scores 25/25 by W3 |
| `04-training/exercises/workbook1_reading_and_structuring.md` | Five exercises: timed speed-reads and ask-decomposition **on the real ABCC case PDFs**, issue trees, case-type classification — with answer keys |
| `04-training/exercises/workbook2_quant_drills.md` | Four sets, ≈30 items: 12 sizing problems (German and Manitoba), exhibit math on the real cases, a sensitivity one-pager, and the weekly arithmetic circuit — worked |
| `04-training/exercises/workbook3_storyline_and_slides.md` | Five exercises, ≈25 items: action-title rewrites, storyline sprints, ordering drills, **implementation-plan drills (the 2.5× muscle)**, the boardroom one-slider — with models |
| `04-training/exercises/workbook4_delivery_drills.md` | Five drill formats: six 3-minute pitch scenarios with a model script, three judge briefs with a marking checklist, **24 number-attack questions** on the original cases, choreography, and the dress-rehearsal protocol |

### 05-practice-cases — material to train on

| File | What it is |
|---|---|
| `05-practice-cases/index.md` | Practice-material index and the recommended order (real re-cracks first, original cases for graded simulations), plus the 2027 pattern to train against |
| `05-practice-cases/case1_traditional_sparkasse_youth.md` | Original full case, **traditional** format (3 h, 20 + 10): Sparkasse Ostwestfalen winning back under-30s. **8 exhibits** + coach-only teaching note with solution, traps, and a 100-point rubric |
| `05-practice-cases/case2_boardroom_premium_brand.md` | Original full case, **boardroom** format (4 h, 3-min pitch + 22-min discussion): Manufaktur Lichtwerk from premium to luxury. **6 exhibits** + teaching note with ten judge questions |
| `05-practice-cases/case3_prepared_arts_festival.md` | Original full case, **prepared** format (14 days, 25 + 15): Klangfest Bielefeld needing one radical idea. **8 exhibits** + teaching note with a four-option solution space |
| `05-practice-cases/mini_cases.md` | **Mini-cases 1–6** for 30–45-minute weekly drills, each with a 90-second sizing warm-up and a boxed solution sketch |
| `05-practice-cases/mini_cases_set2.md` | **Mini-cases 7–12** — Canadian-leaning and quant-heavier, for November onward; closes with the author-your-own assignment |
| `05-practice-cases/model_answers.md` | Calibration pack: a full worked answer outline (Access Credit Union 2026 re-crack), a filled one-page judge brief (AROW Global 2025), and how to use both |

### 06-templates — competition-legal assets

Prebuilt **own** templates are explicitly permitted (built outside prep time); **third-party** templates are not allowed for the prepared case.

| File | What it is |
|---|---|
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

### 07-logistics — getting there and operating there

| File | What it is |
|---|---|
| `07-logistics/registration_email_draft.md` | Ready-to-send e-mail to `aspercasecomps@umanitoba.ca` covering eligibility, dates, fees, hotel block, formalities, and all seven open questions in one exchange |
| `07-logistics/travel_logistics.md` | Ten sections: eTA for German citizens, flight routings and price bands, Delta Hotels Winnipeg, airport transfer, campus and daily transfers, **−30 °C clothing list**, money/tipping/SIM, insurance (**statutory German GKV does not cover Canada**), the 7-hour jet-lag plan, and the booking countdown |
| `07-logistics/competition_day_runbook.md` | Hour-by-hour sheets for all five days on the 2025 baseline, TBA-hedged for the 2027 weekday shift, plus standing rules and contingency plans |

### 08-briefing-slides — the kick-off deck

`08-briefing-slides/abcc_overview.tex` / `.pdf` — the kick-off Beamer deck in HSBI house style: **21 frames plus 4 section pages = 25 PDF pages**, covering the competition, the week, all three rounds, the final, deliverables, the travel checklist, core rules, anonymity and allowed tools, scoring and tie-breaking, the official rubric, team strengths, the roadmap, and sources.

```bash
cd 08-briefing-slides && pdflatex abcc_overview.tex && pdflatex abcc_overview.tex   # twice, for navigation
```

Or upload the `.tex` to Overleaf. If the deck changes, refresh **both** PDF copies (§6).

---

## 4. Documentation metrics

As of 2026-08-04, archive content (excluding `.git`):

| Layer | Files | Notes |
|---|---|---|
| Archive total | **54** | 35 markdown · 7 pptx · 7 pdf · 1 xlsx · 1 docx · 1 csv · 1 tex · 1 .gitignore |
| Written material | **35 markdown files, ≈73,000 words** | ≈5–6 hours of reading end to end |
| Binary assets | ≈8.5 MB | 6.2 MB official case PDFs · 2.3 MB slide templates |
| Archive working tree | ≈9.4 MB content + 7.6 MB `.git` | Zip ships at ≈14 MB |

Word count by folder: `05-practice-cases` 27,300 · `04-training` 14,200 · `01-competition` 11,000 · `03-team` 4,600 · `02-plan` 3,800 · `07-logistics` 3,600 · `06-templates` 2,300 · root documents (this file, README, changelog) 6,300.

Exercise volume: ≈200 solved items — 25 quiz questions, ≈85 workbook items across four workbooks, 40 math drills, 60 Q&A questions, 12 mini-cases, 3 full graded cases, 10 re-crack briefs.

---

## 5. Core workflows

**Kick-off (W1 — the current week).** Present `08-briefing-slides/abcc_overview.pdf` → everyone reads `01-competition/handbook.md` → sign `03-team/team_charter.md` → assign roles per `03-team/role_playbooks.md` → brief the team on `03-team/coach_and_ai_rules.md` → send `07-logistics/registration_email_draft.md` → open the admin track in `07-logistics/travel_logistics.md` (passports now, eTAs in W2).

**A normal training week (Phases 2–3).** One 3–5 h weekend block per `02-plan/week_by_week_plan.md` (simulation or workshop) → one 60–90 min midweek debrief plus a skill session from `04-training/`, opened by a mini-case → 30 min of individual drills (math routine, flashcards) on a third day. The per-week exercise layer is in `04-training/exercises/README.md`. **If a week collapses, the priority order is simulation > mini-case > workbook item > individual drills** — protect the simulations above all.

**Running a simulation.** Pick the case from the week plan → coach prints `01-competition/judging_scoresheet.md` → run under competition-identical conditions (staggered release, timed prep, one laptop per student, internet and GenAI allowed, **no coach contact**, `.pptx` to the "USB" at the pickup deadline, all four speak, yellow card at 5 min and red at 1) → score on the official rubric → 2 strengths / 2 gaps / 1 drill per person → enter results in `02-plan/simulation_log.md` the same day → goals carry into the next week.

**When a case lands (competition or graded simulation).** Classify the type within ten minutes using `06-templates/case_type_playbook.md` → duplicate the matching skeleton from `06-templates/case-type-templates/`, **delete its red briefing slide**, rename to the round's file convention → storyline pass, **titles first** → parallel build along the role minute-maps in `03-team/role_playbooks.md` → every number through `06-templates/case_financial_toolkit.xlsx` → for boardroom rounds fill `06-templates/judge_brief_template.docx` with wording that mirrors the summary slide.

**Prepared-case sprint (on release, ~2 weeks).** Follow Phase 4 of `02-plan/preparation_plan.md` day by day: deep read and client research → parallel workstreams → storyline plus **coach review, which is allowed in this round** → deck build → dress rehearsals → freeze. Submit the `.pptx` by e-mail **at least 24 h before the deadline**, named `[Team Name] Prepared Case`; the strategist owns submission, the coach confirms receipt.

**Competition week.** `07-logistics/competition_day_runbook.md` is the daily script; the standing rules at its top apply all week. Note the weekday shift: **Feb 18–22, 2027 falls Thursday–Monday**, whereas the 2025 baseline ran Wednesday–Sunday (registration was Wed Feb 19, 2025), so the round-to-day mapping in the runbook and the week plan is marked TBA until the 2027 agenda is published.

**After.** Debrief in the week of Feb 23: retro against the rubric, archive all decks and scores, write a two-page handover for the next HSBI team, send thank-yous, and update `01-competition/handbook.md` with everything 2027 actually did differently.

---

## 6. Keeping the two layers in sync

The workspace duplicates a handful of archive files (§1). Divergence is the one structural risk in this arrangement, so treat the **archive as the master** and the workspace copies as exports.

**Rule.** Edit inside the unpacked archive, commit there, then rebuild the zip and refresh the workspace copies. Never edit a workspace duplicate and leave it there.

```bash
# 1. unpack and edit
unzip asper-abcc-2027.zip
cd asper-abcc-2027
#    ... make the change ...
git add -A && git commit -m "v8: <what changed>"

# 2. refresh the workspace duplicates (archive → workspace)
cd ..
cp asper-abcc-2027/DOCUMENTATION.md asper-abcc-2027/CHANGELOG.md .
cp asper-abcc-2027/03-team/coach_and_ai_rules.md .
cp asper-abcc-2027/04-training/exercises/README.md exercise_catalog.md
cp asper-abcc-2027/08-briefing-slides/abcc_overview.pdf .
cp asper-abcc-2027/06-templates/team_template.pptx \
   asper-abcc-2027/06-templates/case_financial_toolkit.xlsx \
   asper-abcc-2027/06-templates/judge_brief_template.docx .
cp asper-abcc-2027/06-templates/case-type-templates/*.pptx case-type-templates/

# 3. rebuild the archive, then commit the workspace
rm asper-abcc-2027.zip
zip -qr asper-abcc-2027.zip asper-abcc-2027 -x '*.DS_Store'
rm -rf asper-abcc-2027
git add -A && git commit -m "Update documentation and rebuild archive"
```

The workspace `README.md` is deliberately **not** copied — it is the long entry point and has no archive twin (the archive's own `README.md` is the lean version).

**Verify the sync** with the check in §9; it takes seconds and catches exactly the drift this section exists to prevent.

---

## 7. Maintenance rules

- **Rules first.** Whenever the organizers publish 2027 information (Competition Guide, agenda, deadlines, fees, hotel), update `01-competition/facts_and_rules.md` **first**, then sweep the repository for affected statements. The **TBA tracker in `01-competition/handbook.md` §12** lists exactly what to confirm: the day-by-day schedule and which date carries which round, the case sponsors (watch the sponsor page and @Asper_BCC from autumn — case writing starts around October), the prepared-case release date and deck deadline, the 2027 field, prize amounts, the Round 1 venue, and any rule deltas versus 2025.
- **Propagation order** after a rules change: `facts_and_rules.md` → `handbook.md` → `judging_scoresheet.md` (if the rubric moved) → `02-plan/week_by_week_plan.md` (if dates moved) → `07-logistics/competition_day_runbook.md` → `08-briefing-slides/abcc_overview.tex` (rebuild the PDF twice) → `04-training/exercises/format_quiz.md` (the answer key quotes the rules) → this file and the two READMEs.
- **The calendar is authoritative.** Date conflicts resolve in favour of `02-plan/week_by_week_plan.md`. Its phase numbers are calendar phases and deliberately differ from the concept phases in `preparation_plan.md`.
- **Log every simulation the same day** in `02-plan/simulation_log.md`, with rubric scores and one carried-forward goal per person.
- **Never commit the HSBI name** into a slide template, judge brief, or any competition-facing asset. Anonymity is a disqualification rule and the assets here are deliberately clean.
- **Keep the layers in sync** per §6, and re-run the §9 checks after any change that touches a duplicated file.
- **Hand over after the competition.** Write the debrief and the two-page handover, then pass the repository to the next HSBI team (final section of the week plan).

---

## 8. Version history

Two independent git histories. Full detail in [`CHANGELOG.md`](CHANGELOG.md).

**Archive** (`asper-abcc-2027/.git`, 7 commits, tree clean at `db64f12`) — one commit per work package:

| Tag | Commit |
|---|---|
| v1 | Initial: briefing deck, preparation plan, resources |
| v2 | Validated handbook, past-case dossier + PDFs, three practice cases, training pack, dated calendar; deck and facts aligned to the official 2025 Event Guide rules and rubric |
| v3 | Adversarial review fixes (36 findings), all URLs validated, mini-case pack, role playbooks + GenAI SOP, model answers, phrasebook, scoresheet, simulation log, anonymity-proof team template |
| v4 | Six case-type skeletons + tackling playbook, financial toolkit, judge-brief template, day runbook, flashcards, registration e-mail, team charter |
| v5 | Restructure into the eight numbered lifecycle folders; all cross-references rewritten; `DOCUMENTATION.md` added; lean README |
| v6 | Exercise program (≈200 solved items): format quiz, four workbooks anchored in the real ABCC cases, mini-case set 2, week-mapped catalog; coach & AI rules one-pager |
| v7 | Consistency pass: text-corruption repair, drill arithmetic fixes, corrected past-case counts |
| v8 | Documentation overhaul: two-layer model documented, inventory re-verified and re-pathed, metrics, sync procedure, verification log, changelog |

**Workspace** (3 commits before v8): initial import → workspace README → documentation and resource update with expanded practice cases, exercise catalog, and the team-anonymity clarification.

**Publishing.** To put either layer on a private remote:

```bash
gh repo create asper-abcc-2027 --private --source=. --push
# or: git remote add origin git@github.com:<user>/asper-abcc-2027.git && git push -u origin main
```

Keep it **private** — the mirrored case PDFs are confidential competition documents.

---

## 9. Verification log (2026-08-04)

What was checked, so the next reader knows what is asserted and what is assumed.

**Structure and integrity**
- Archive contains 54 files excluding `.git`; inner working tree clean; 8 commits, HEAD at v8.
- All six official case PDFs present in `01-competition/past-case-pdfs/` (6.2 MB); the other five official cases are URL-only, as documented.
- Every relative path quoted in this file and in both READMEs resolves inside the archive.

**Workspace ↔ archive duplicates.** Byte-identical: `DOCUMENTATION.md`, `CHANGELOG.md`, `coach_and_ai_rules.md`, `exercise_catalog.md` ↔ `04-training/exercises/README.md`, `team_template.pptx`, all six `case-type-templates/*.pptx`, `case_financial_toolkit.xlsx`, `judge_brief_template.docx`. Differing by design: `README.md` (two different documents) and `abcc_overview.pdf` (archive holds the newer build of the same 25-page deck). Re-run with:

```bash
unzip -q -o asper-abcc-2027.zip -d /tmp/abcc && A=/tmp/abcc/asper-abcc-2027
for p in "DOCUMENTATION.md:DOCUMENTATION.md" "CHANGELOG.md:CHANGELOG.md" \
         "coach_and_ai_rules.md:03-team/coach_and_ai_rules.md" \
         "exercise_catalog.md:04-training/exercises/README.md" \
         "team_template.pptx:06-templates/team_template.pptx" \
         "case_financial_toolkit.xlsx:06-templates/case_financial_toolkit.xlsx" \
         "judge_brief_template.docx:06-templates/judge_brief_template.docx"; do
  cmp -s "${p%%:*}" "$A/${p##*:}" && echo "ok   ${p%%:*}" || echo "DIFF ${p%%:*}"
done
for f in case-type-templates/*.pptx; do
  cmp -s "$f" "$A/06-templates/$f" && echo "ok   $f" || echo "DIFF $f"
done
```

**Content counts** (all confirmed against the files): 87 flashcard rows · 40 math drills · 60 Q&A questions in five banks · 25 quiz questions in four blocks · mini-cases numbered 1–6 and 7–12 · exhibits 8 / 6 / 8 in cases 1 / 2 / 3 · `team_template.pptx` 14 slides · case-type decks 13 / 12 / 11 / 11 / 12 / 12 slides (A–F) · briefing deck 21 frames + 4 section pages = 25 PDF pages · 35 markdown files, ≈73,000 words · eleven official cases across ten clients.

**Dates.** February 18–22, 2027 is **Thursday–Monday**; the 2025 baseline ran Wednesday–Sunday with registration on Wed Feb 19, 2025. The one-day shift is flagged in `week_by_week_plan.md`, `competition_day_runbook.md`, and §5 above; the actual round-to-day mapping stays TBA. W1 of the plan is Aug 3–9, 2026 — the current week.

**Not verified here.** Nothing on the official Asper website was re-fetched on 2026-08-04; all competition facts still carry their July–August 2026 validation date. Re-validate when the 2027 Competition Guide is published.

---

## 10. Conventions and hard rules

- **Anonymity.** Nothing said, worn, or shown may identify HSBI. The team competes under a **fictional consulting name it chooses and registers with the organizers before the event** (the templates ship with the placeholder "Aurora Advisory"), plus a **division letter A–I drawn at on-site registration** that sets the week's slots. The name is ours; the letter is theirs. Naming your school to a judge is disqualification.
- **Coach silence.** From the release of a boardroom or traditional case until the team has presented, no contact of any kind. Any coach–team communication during a presentation or Q&A, or any coach intervention in the question period, means immediate disqualification. Advisors of finalist teams stay silent until their team has presented. The coach is fully in the game for the prepared case and for everything before the competition.
- **GenAI.** Explicitly permitted during timed prep. The edge is the drilled procedure, not the access: one designated operator, narrow sanctioned tasks, and **no unverified number reaches a slide**. Framing, option choice, and the recommendation are never outsourced. Do not paste confidential case text into consumer tools.
- **Confidentiality.** The case PDFs in `01-competition/past-case-pdfs/` are © University of Manitoba and marked "no reproduction or transmission" — internal team use only. Do not redistribute; keep both layers private.
- **File conventions.** Competition hand-ins follow the organizers' naming (`[Team Name] Prepared Case`, `[Team Name] Traditional Case`). Case data in the original practice cases is fictional and labelled as such. Documents state their own source and validation date at the top.

---

## 11. Known limitations and open questions

- **The 2027 agenda, deadlines, fees, and field are TBA.** Everything schedule-shaped in this repository is a 2025/2026-baseline assumption, flagged in place. The Thursday–Monday footprint of Feb 18–22, 2027 means the published day-by-day agenda will almost certainly shift rounds against the 2025 pattern.
- **Original practice material uses fictional data.** The three full cases and all worked model answers are internally consistent inventions, labelled as case data; teaching-note figures are calibration aids, not real-company facts.
- **Eligibility of the specific HSBI student mix needs written confirmation** from the organizers — the top open question in `facts_and_rules.md`.
- **Five of the eleven official cases are URL-only** (2024 cases 1 and 3, all three 2026 cases); download them before the sessions that use them.
- **The archive is a binary blob in the workspace's git history.** Every rebuild writes a fresh ~14 MB object; the history is honest but grows. Rebuild only when the content actually changed.

Open questions to put to the organizers after registration (all seven are covered by `07-logistics/registration_email_draft.md`): the 2027 agenda and prepared-case release/submission dates · the registration process and fee for an international team and what it covers · eligibility confirmation · roster, bio and photo requirements plus advisor registration · the 2027 hotel block and booking code · whether the 2027 rules package changes anything versus the 2025 baseline, specifically any **new generative-AI clauses** · a **formal letter of invitation** naming all five travellers and the dates, for the Canadian border and for university travel funding.

**Contacts.** `aspercasecomps@umanitoba.ca` — Judith Jayasuriya (Instructor & Lead, Experiential Learning), Steven Harrison (Case Competition Coordinator, +1 204 396 9631) · Instagram @Asper_BCC · Drake Centre, Asper School of Business, 181 Freedman Crescent, Winnipeg · Delta Hotels Winnipeg (2027 team hotel).
