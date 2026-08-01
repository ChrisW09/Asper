# Asper Business Case Competition 2027 — HSBI Preparation Workspace

Everything the HSBI team needs to **prepare for, travel to, and compete at** the
**Asper Business Case Competition (ABCC) 2027** — fifth annual edition,
**February 18–22, 2027**, I. H. Asper School of Business, University of Manitoba, Winnipeg.

**Team:** four Masters students (finance · innovation · computer science · general business administration)
**Coach / faculty advisor:** Prof. Dr. Christoph Weisser

> This directory is the **working copy** of the preparation project: the loose documents currently in
> active use, plus `asper-abcc-2027.zip`, which holds the **complete, structured repository** (52 files,
> eight lifecycle folders, own git history). See [What is in this directory](#what-is-in-this-directory).

---

## Table of contents

1. [The competition in 60 seconds](#the-competition-in-60-seconds)
2. [What is in this directory](#what-is-in-this-directory)
3. [The full repository (inside the zip)](#the-full-repository-inside-the-zip)
4. [Quick start](#quick-start)
5. [Core workflows](#core-workflows)
6. [The rubric — and what it means for training](#the-rubric--and-what-it-means-for-training)
7. [Rules cheat sheet: AI, coach, anonymity](#rules-cheat-sheet-ai-coach-anonymity)
8. [Timeline and milestones](#timeline-and-milestones)
9. [Templates and toolkit](#templates-and-toolkit)
10. [Maintenance rules and conventions](#maintenance-rules-and-conventions)
11. [Known limitations and open questions](#known-limitations-and-open-questions)
12. [Sources and contacts](#sources-and-contacts)

---

## The competition in 60 seconds

Nine graduate teams of four compete over three days in **three case formats**, then a final round.
Everything runs **in English**, PowerPoint only, judged by ~50 industry practitioners.

| Round | Prep | Delivery | Weight |
|---|---|---|---|
| **Prepared case** | released ~2 weeks ahead, all resources incl. coach | 25 min presentation + 15 min Q&A; deck due as `.pptx` by e-mail before arrival (**late = bottom of pool**) | **25 %** |
| **Boardroom case** | 4 h on site, no coach contact | 3-min *protected* pitch from **one summary slide** + 22-min judge discussion; one-page b/w judge brief handed to judges in advance | **30 %** |
| **Traditional case** | 3 h on site, no coach contact | 20 min presentation + 10 min Q&A; unlimited slides | **45 %** |
| **Final** | top 3 by weighted score; **decks frozen** | 20 + 15 to a fresh panel | decides the winner |

Standing conditions: internet **and Generative AI allowed** during prep · one laptop per student, no
phones or smartwatches · prebuilt own templates permitted · every team member must speak in every round ·
yellow card at 5 min, red at 1 min · **naming your school to a judge = disqualification**.

Field and history: 2025 saw Asper, Beedie, DeGroote, HEC Montréal, Ivey, John Molson, Levene, Memorial,
Telfer. 2026 (fourth edition) included the first international team — Babeș-Bolyai, Romania — which **won
outright**, ahead of DeGroote and HEC Montréal. That is the precedent this team is following.

Full validated rule base: `01-competition/facts_and_rules.md` in the zip — **the single source of truth**
for every rule claim in every other document.

---

## What is in this directory

| File / folder | What it is |
|---|---|
| **`README.md`** | This file — the entry point |
| **`DOCUMENTATION.md`** | Full inventory of the structured repository: every file, what it is, when to use it, plus workflows and maintenance rules |
| **`asper-abcc-2027.zip`** (14 MB) | **The complete repository**, including its own `.git` history and the six official past-case PDFs. Slightly newer than the loose copies here |
| `abcc_overview.pdf` | The 25-frame kick-off briefing deck (Beamer, HSBI house style) — competition, week, all three rounds, deliverables, rubric, roles, roadmap |
| `coach_and_ai_rules.md` | One-pager: **may we use AI in competition?** (yes, officially) and **what may the coach do, round by round?** |
| `exercise_catalog.md` | The complete drill inventory — ~200 solved exercises mapped week by week onto the calendar |
| `team_template.pptx` | The general 14-slide skeleton, anonymity-proof (placeholder consulting name "Aurora Advisory") |
| `case-type-templates/` | Six type-specific slide skeletons, A–F (see [Templates and toolkit](#templates-and-toolkit)) |
| `case_financial_toolkit.xlsx` | Live-formula calculators: market sizing, unit economics & break-even, NPV & payback, CLV cohort |
| `judge_brief_template.docx` | The boardroom one-page black-and-white judge brief, ready to fill |

**Relationship between the two.** The loose files above are the documents and assets in day-to-day use;
they are byte-identical to their counterparts inside the zip, except `DOCUMENTATION.md` and
`abcc_overview.pdf`, where the zip holds the newer build. Everything else — rules, plan, cases, drills,
logistics — exists **only inside the zip**. To work with the whole thing:

```bash
unzip asper-abcc-2027.zip          # → ./asper-abcc-2027/ with full git history
cd asper-abcc-2027 && git log --oneline
```

---

## The full repository (inside the zip)

The eight numbered folders follow the lifecycle of the project:
*understand the competition → plan → form the team → train → practice → build assets → travel → brief.*

```
asper-abcc-2027/
├── README.md                  Entry point: quick facts + next actions
├── DOCUMENTATION.md           Full inventory, workflows, maintenance
├── 01-competition/            What the ABCC is: rules, history, judging, past cases
├── 02-plan/                   When we do what: concept, dated calendar, results log
├── 03-team/                   Who we are: charter, role playbooks (incl. GenAI SOP)
├── 04-training/               Skill building: presenting, Q&A, math, English, frameworks, exercises/
├── 05-practice-cases/         What we practice on: 3 full cases, 12 mini-cases, model answers
├── 06-templates/              What we build with: slide skeletons, toolkit, judge brief
├── 07-logistics/              Getting there: travel, registration, competition-day runbook
└── 08-briefing-slides/        The kick-off Beamer deck (LaTeX + PDF)
```

### 01-competition — know the game

| File | What it is |
|---|---|
| `facts_and_rules.md` | **Source of truth.** Validated rules, round formats, official rubric, schedule pattern, past-case links, open questions for the organizers |
| `handbook.md` | Narrative handbook: history 2023–2027, eligibility, event flow, forensic round detail, scoring, conduct, day-in-the-life, TBA tracker |
| `judging_scoresheet.md` | Printable official-rubric scoresheet (7 categories, ×2.5…×1.0, /105) with behavioural anchors, timing checklists, feedback template |
| `past_cases.md` | All editions and all ten past clients profiled, each with a **re-crack brief**; pattern analysis for 2027 |
| `past-case-pdfs/` | Six official case PDFs 2023–2025 (© University of Manitoba — internal use only, cases are confidential) |

### 02-plan — when we do what

| File | What it is |
|---|---|
| `preparation_plan.md` | The training **concept**: principles, roles, five phases, prepared-case sprint, risk register |
| `week_by_week_plan.md` | **The calendar — governs on conflicts.** Dated weeks Aug 3, 2026 → competition + debrief: sessions, materials, homework, admin milestones |
| `simulation_log.md` | Results log, pre-filled with all ten planned simulations; rubric scores + one goal per person per round |

### 03-team — who we are

| File | What it is |
|---|---|
| `team_charter.md` | Commitments, working rules, non-negotiables, escalation path, signature block |
| `role_playbooks.md` | Per-role missions, artifacts, prep minute-maps (3 h and 4 h), drills, failure modes; **GenAI standard operating procedure**; prep-room kit checklist |
| `coach_and_ai_rules.md` | The AI + coach one-pager (also loose in this directory) |

The four roles: **finance lead** · **innovation lead** · **CS & analytics lead** (also the designated
GenAI operator) · **general-business strategist**, all running against one shared team clock.

### 04-training — skills

| File | What it is |
|---|---|
| `presentation_and_storyline_guide.md` | Action titles, storyline skeleton, 3-h deck production workflow, boardroom technique, delivery for non-native speakers |
| `qa_drills.md` | Answer-first protocol, bridging, quarterback system; 60 hard questions with model answer patterns |
| `business_math_drills.md` | 40 drills with worked solutions; the weekly 30-minute routine |
| `english_phrasebook.md` | DE–EN terminology, phrase banks (presentation, Q&A, boardroom), numbers out loud, pronunciation traps |
| `vocab_flashcards.csv` | 87 flashcards (German, English, note) — import into Anki: File → Import, comma-separated, first row is header |
| `frameworks.md` | Framework toolkit (problem framing, strategy, marketing, finance, innovation, implementation) |
| `exercises/README.md` | **The exercise catalog** — inventory + week-by-week schedule (= `exercise_catalog.md` here) |
| `exercises/format_quiz.md` | 25-question format quiz with answer key; every member scores 25/25 by W3 |
| `exercises/workbook1_reading_and_structuring.md` | Timed speed-reads and ask-decomposition **on the real ABCC PDFs**, issue trees, case-type classification — with keys |
| `exercises/workbook2_quant_drills.md` | 12 sizing problems (DE + Manitoba), exhibit math on real cases, sensitivity one-pager, weekly arithmetic circuit — worked |
| `exercises/workbook3_storyline_and_slides.md` | Action-title rewrites, storyline sprints, ordering drills, implementation-plan drills (**the 2.5× muscle**), boardroom one-slider |
| `exercises/workbook4_delivery_drills.md` | 3-min pitch scenarios with model script, judge-brief writing + marking checklist, 24 number-attacks per case, choreography, dress-rehearsal protocol |

≈ **200 discrete solved exercises** — enough for two sessions a week from August to February without repetition.

### 05-practice-cases — material to train on

| File | What it is |
|---|---|
| `index.md` | Practice-material index and recommended order (real re-cracks first, original cases for graded sims) |
| `case1_traditional_sparkasse_youth.md` | Original full case, **traditional** format (3 h, 20+10): regional bank winning back under-30s. 8 exhibits + coach-only teaching note with solution, traps, 100-point rubric |
| `case2_boardroom_premium_brand.md` | Original full case, **boardroom** format (4 h, 3-min pitch + 22-min discussion): premium → luxury candle maker. 6 exhibits + teaching note with 10 judge questions |
| `case3_prepared_arts_festival.md` | Original full case, **prepared** format (14 days, 25+15): jazz festival needing one radical idea. 8 exhibits + teaching note with a 4-option solution space |
| `mini_cases.md` / `mini_cases_set2.md` | Twelve one-page cases for 30–45-min drills, each with a 90-second sizing warm-up and a boxed solution sketch; Set 2 is Canadian-leaning and quant-heavier |
| `model_answers.md` | Calibration: a full worked answer outline (Access CU 2026 re-crack) and a filled one-page judge brief (AROW 2025) |

### 06-templates — competition-legal assets

Prebuilt own templates are explicitly permitted (built outside prep time); third-party templates are **not**
allowed for the prepared case. See [Templates and toolkit](#templates-and-toolkit).

### 07-logistics — getting there and operating there

| File | What it is |
|---|---|
| `registration_email_draft.md` | Ready-to-send e-mail to `aspercasecomps@umanitoba.ca`: eligibility, dates, fees, hotel block, formalities |
| `travel_logistics.md` | eTA, flight routings and price bands, Delta Hotels Winnipeg, airport transfer, −30 °C clothing list, money/SIM, insurance (**GKV does not cover Canada**), 7-hour jet-lag plan, booking countdown |
| `competition_day_runbook.md` | Hour-by-hour sheets for all five days (2025 baseline, TBA-hedged) plus contingency plans |

### 08-briefing-slides — the kick-off deck

`abcc_overview.tex` / `abcc_overview.pdf` — 25 Beamer frames in HSBI house style. Rebuild with:

```bash
cd 08-briefing-slides && pdflatex abcc_overview.tex && pdflatex abcc_overview.tex   # twice, for navigation
```

(Or upload the `.tex` to Overleaf.)

---

## Quick start

**New team member — first 90 minutes.** Read `01-competition/handbook.md` → skim
`02-plan/week_by_week_plan.md` for the weeks ahead → read your section of `03-team/role_playbooks.md` →
sign `03-team/team_charter.md` → take `04-training/exercises/format_quiz.md` (target: 25/25 by W3).

**Coach.** `coach_and_ai_rules.md` (what you may and may not do, round by round) →
`01-competition/judging_scoresheet.md` (print one per simulation judge) →
`02-plan/week_by_week_plan.md` (run the calendar) → `02-plan/simulation_log.md` (log the same day).

**Immediate next actions.**

1. Send `07-logistics/registration_email_draft.md` to `aspercasecomps@umanitoba.ca` — register, confirm
   eligibility for the HSBI student mix, get on the 2027 mailing list.
2. Verify all five passports; apply for **eTAs** (CAD 7 each, official site only).
3. Hold the kick-off with `abcc_overview.pdf`, then follow `02-plan/week_by_week_plan.md`.
4. Book flights by early autumn; secure university funding; confirm the hotel block.

---

## Core workflows

**Kick-off (W1).** Present `abcc_overview.pdf` → everyone reads `01-competition/handbook.md` → sign
`03-team/team_charter.md` → assign roles per `03-team/role_playbooks.md` → send the registration e-mail →
start the admin track in `07-logistics/travel_logistics.md`.

**A normal training week (Phases 2–3).** One 3–5 h weekend block (simulation or workshop) per the calendar
→ one 60–90 min midweek debrief plus a skill session from `04-training/` → 30 min of individual drills
(math routine, flashcards). A mini-case opens the midweek session. If a week collapses, the priority order
is **simulation > mini-case > workbook item > individual drills** — protect the simulations above all.

**Running a simulation.** Pick the case from the week plan → coach prints
`01-competition/judging_scoresheet.md` → run under competition-identical conditions (timed, one laptop each,
internet + GenAI allowed, **no coach contact**, `.pptx` "USB" hand-in at the deadline, all four speak,
yellow/red cards) → score on the official rubric → 2 strengths / 2 gaps / 1 drill per person → enter results
in `02-plan/simulation_log.md` → goals carry into the next week.

**When a case lands (competition or graded sim).** Classify the type within 10 minutes using
`06-templates/case_type_playbook.md` → duplicate the matching skeleton from `case-type-templates/`, delete
its red briefing slide, rename to the round's file convention → storyline pass, **titles first** → parallel
build along the role minute-maps → every number through `case_financial_toolkit.xlsx` → for boardroom rounds
fill `judge_brief_template.docx`, wording mirroring the summary slide.

**Prepared-case sprint (on release, ~2 weeks).** Follow Phase 4 of `02-plan/preparation_plan.md` day by day.
Coach input **is** allowed in this round. Submit the `.pptx` by e-mail **at least 24 h before the deadline**,
file named `[Team Name] Prepared Case`.

**Competition week.** `07-logistics/competition_day_runbook.md` is the daily script; the standing rules at
its top apply all week.

**After.** Debrief in the week of Feb 23, write thank-yous, and hand the repository to the next team
(final section of the week plan).

---

## The rubric — and what it means for training

The official ABCC rubric (2025 Event Guide) applies to **all rounds**, 7 categories, max 105 points:

| Category | Weight | What judges ask |
|---|---|---|
| **Implementation & resources** | **2.5×** | Is there a clear path to follow, with resources, time, and financial considerations? |
| Analysis | 2.0× | Is the assessment substantiated by research, logic, quantitative and qualitative analysis? |
| Recommendation | 2.0× | Effective, clear, comprehensive, strategically fitting? |
| Communicating effectively | 1.0× | Clear, professional, compelling delivery and a readable deck? |
| Framing the problem | 1.0× | Are issues wrapped into a clear, solvable summary (primary + secondary)? |
| Impact | 1.0× | Quantitative and qualitative benefit to the organization? |
| Measurement, risks & mitigation | 1.0× | Progress measurement and realistic risk mitigation? |

**Training implication.** Implementation & Resources alone is worth more than any other category — 2.5× is
nearly a quarter of the sheet. Every mock presentation must end with a **concrete, resourced, costed
implementation plan with owners, timing, and KPIs**. Drill it explicitly in
`04-training/exercises/workbook3_storyline_and_slides.md`.

---

## Rules cheat sheet: AI, coach, anonymity

**AI is explicitly allowed.** The official rules permit internet use during timed prep, including
"any login-required website … filesharing websites, **and Generative AI**." That covers the 4-h boardroom
and 3-h traditional prep; in the prepared case all resources are allowed anyway.

Because every team has the same arsenal, the edge is a **drilled procedure**, not access
(`03-team/role_playbooks.md`, GenAI SOP): one designated operator (CS & analytics lead), narrow sanctioned
tasks (checking math, stress-testing the recommendation, generating counterarguments, polishing brief
wording, the 10-minute Q&A-anticipation routine), and the hard rule that **no unverified number reaches a
slide**. Framing, option choice, and the recommendation are never outsourced — borrowed logic collapses in
the 22-minute discussion. **Confidentiality caution:** competition cases are confidential documents, so do
not paste full case text into consumer AI tools; prefer university-licensed enterprise tools and work from
your own summaries. Re-check the 2027 guide for new AI clauses before travelling.

**The coach is in the game** for the prepared case (unrestricted — faculty input explicitly allowed), for
everything before the competition, and on site for presentations, feedback sessions, and the full social
program.

**The coach goes silent** from the moment a **boardroom** or **traditional** case is released until the team
has presented — no contact of any kind. Any communication between coach and team during a presentation or
Q&A, or any coach intervention in the question period, means **immediate disqualification**. Advisors of
finalist teams may not communicate with their team until after it has presented.

**Anonymity binds everyone, coach included.** Nothing said, worn, or shown may identify HSBI; teams compete
under neutral division letters drawn at registration. Identifying your school to a judge = disqualification.
This is why every template in this repository is deliberately clean of HSBI branding — **never commit the
HSBI name into a slide template or judge brief.**

---

## Timeline and milestones

| Date | Milestone |
|---|---|
| Aug 2026 | E-mail organizers: register interest, confirm eligibility, join the 2027 mailing list |
| Aug 2026 | All five passports verified; **eTAs applied for** |
| Sep–Oct 2026 | **Flights booked** (arrive Feb 16/17, return Feb 22/23); funding secured; hotel block confirmed |
| Nov 2026 | Travel health + cancellation insurance closed; **team `.pptx` template v1** built (anonymity-proof) |
| Dec 2026 | Winter gear complete; eSIMs ordered; template v2 frozen after use in three simulations |
| Late Jan 2027 | Taper begins; prepared-case sprint logistics ready |
| ~Feb 4, 2027 *(TBA)* | **Prepared case released** → 14-day sprint |
| ~Feb 17, 2027 *(TBA)* | **Prepared deck submitted** ≥24 h before the deadline |
| Feb 16/17, 2027 | Fly Bielefeld → Winnipeg |
| **Feb 18–22, 2027** | **ABCC 2027** |
| Week of Feb 23 | Debrief, thank-yous, handover to the next team |

Training phases: **Foundations** (W1–W5, Aug 3 – Sep 6) → **Skill building** (W6–W10, Sep 7 – Oct 11) →
**Simulations under competition rules** (W11–W20, Oct 12 – Dec 20) → *Christmas, light load* (W21–W22) →
**Peak** (W23–W26, Jan 4–31) → **Prepared-case sprint & travel** (W27–W29, Feb 1–17).

A typical competition week on the 2025 pattern: Wednesday arrival, registration and division draw ·
Thursday prepared-case presentations, museum social · Friday boardroom case, Festival du Voyageur ·
Saturday traditional case, finals, awards gala · Sunday departure.

---

## Templates and toolkit

| Asset | Notes |
|---|---|
| `team_template.pptx` | 14-slide general skeleton: title, exec summary, content patterns, financials, chart, roadmap, risks, the ask, appendix, **boardroom one-slide summary**. Placeholder consulting name "Aurora Advisory" — replace at the division draw |
| `case-type-templates/casetype_A_turnaround_nonprofit.pptx` | Turnaround / nonprofit sustainability |
| `case-type-templates/casetype_B_growth_market_entry.pptx` | Growth and market entry |
| `case-type-templates/casetype_C_brand_premiumization.pptx` | Brand premiumization |
| `case-type-templates/casetype_D_new_product_screen.pptx` | New-product screening |
| `case-type-templates/casetype_E_digital_customer_engagement.pptx` | Digital customer engagement |
| `case-type-templates/casetype_F_talent_and_change.pptx` | Talent and change |
| `case_financial_toolkit.xlsx` | Live formulas: market sizing (top-down / bottom-up + cross-check), unit economics & break-even with sensitivity grid, NPV & payback, CLV cohort. **Blue = inputs, yellow = key assumptions**; ships with a worked example |
| `judge_brief_template.docx` | Boardroom one-page b/w brief: recommendation, three pillars, numbers table, risks, 90-day ask |

Each case-type deck opens with a **red coach-briefing slide** — delete it before any round — and then a
full type-tuned storyline with coaching in the speaker notes. `06-templates/case_type_playbook.md` (in the
zip) explains how to recognise each type within 10 minutes, its core question, the decisive analyses, the
storyline, the judge attacks and counters, the traps, and the self-checks.

---

## Maintenance rules and conventions

- **Update `01-competition/facts_and_rules.md` first** whenever the organizers publish 2027 information
  (Competition Guide, deadlines, agenda, hotel), then sweep the repo for affected statements. The TBA
  tracker in `01-competition/handbook.md` §12 lists exactly what to confirm.
- **The calendar is authoritative.** Date conflicts resolve in favour of `02-plan/week_by_week_plan.md`.
- **Log every simulation the same day** in `02-plan/simulation_log.md`.
- **Never commit the HSBI name** into slide templates or judge briefs — anonymity is a disqualification rule
  and the assets here are deliberately clean.
- **Git.** The zip carries the full history; commits so far run one per work package
  (v1 initial → v2 validated expansion → v3 adversarial review + new material → v4 templates & toolkit →
  v5 restructure + documentation). To publish privately:

  ```bash
  gh repo create asper-abcc-2027 --private --source=. --push
  # or: git remote add origin git@github.com:<user>/asper-abcc-2027.git && git push -u origin main
  ```

**Provenance.** All competition facts were researched and validated (July–August 2026) against the official
Asper website, the official **ABCC 2025 Event Guide** (the fullest public rulebook), the official past-case
PDFs, and press coverage. The materials went through a multi-agent adversarial review: rule claims verified
against the fact base, all exhibit arithmetic recomputed, all official URLs link-checked. Every document
flags where 2027 specifics are still TBA.

---

## Known limitations and open questions

- The **2027 agenda, deadlines, fees, and field are TBA** until the organizers publish them. Everything
  schedule-shaped is a 2025/2026-baseline assumption, flagged as such in place.
- The three original practice cases and all worked model answers use **fictional, internally consistent
  data** (labelled as case data); teaching-note figures are calibration aids, not real-company facts.
- **Eligibility of the specific HSBI student mix needs written confirmation** from the organizers — the top
  open question in `facts_and_rules.md`.
- Six of nine past-case PDFs are mirrored locally; the remaining three (2024 cases 1 and 3, all 2026 cases)
  are linked by URL in `01-competition/past_cases.md`.

Open questions to put to the organizers after registration: 2027 agenda and prepared-case release/submission
dates · registration process and fee for an international (German) team and what it covers · eligibility
confirmation · roster, bio and photo requirements plus advisor registration · 2027 hotel block and booking
code · whether the 2027 rules package changes anything against the 2025 baseline.

---

## Sources and contacts

**Organizers:** `aspercasecomps@umanitoba.ca` — Judith Jayasuriya (Instructor & Lead, Experiential Learning),
Steven Harrison (Case Competition Coordinator, +1 204 396 9631) · Instagram **@Asper_BCC**
**Venue:** Drake Centre, Asper School of Business, 181 Freedman Crescent, Winnipeg (venues can vary by day)
**Hotel 2027:** Delta Hotels Winnipeg, downtown

- Official ABCC page (2027): <https://umanitoba.ca/asper/asper-business-case-competition>
- Case competitions hub (past cases): <https://umanitoba.ca/asper/student-experience/case-competitions>
- **ABCC 2025 Event Guide** (schedule, rules, rubric): <https://umanitoba.ca/asper/sites/asper/files/2025-01/abcc25-eventguide.pdf>
- 2026 recap (fourth edition, first international winner): <https://umtoday.ca/stories/forging-worldwide-relationships-2026-asper-business-case-competition>

> **Confidentiality.** The official case PDFs in `01-competition/past-case-pdfs/` are © University of
> Manitoba and are competition documents marked "no reproduction or transmission" — internal team use only.
> Do not redistribute them, and keep this repository private.
