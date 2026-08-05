# Asper Business Case Competition 2027 — HSBI Preparation

Everything the HSBI team needs to **prepare for, travel to, and compete at** the
**Asper Business Case Competition (ABCC) 2027** — fifth annual edition,
**February 18–22, 2027**, I. H. Asper School of Business, University of Manitoba, Winnipeg.

**Team:** four Masters students (finance · innovation · computer science · general business administration)
**Coach / faculty advisor:** Prof. Dr. Christoph Weisser

Reference map of every file: [`DOCUMENTATION.md`](DOCUMENTATION.md) ·
change history: [`CHANGELOG.md`](CHANGELOG.md) · *documentation verified 2026-08-05*

---

## Where we are right now

**Week 1 of 29 — Aug 3–9, 2026. Kick-off week.** The calendar in
[`02-plan/week_by_week_plan.md`](02-plan/week_by_week_plan.md) starts here; this week's job is to get the
team formed and the admin clock running.

- [ ] Kick-off meeting with [`08-briefing-slides/abcc_overview.pdf`](08-briefing-slides/abcc_overview.pdf);
      everyone reads [`01-competition/handbook.md`](01-competition/handbook.md) afterwards
- [ ] Charter signed ([`03-team/team_charter.md`](03-team/team_charter.md)), roles assigned
      ([`03-team/role_playbooks.md`](03-team/role_playbooks.md))
- [ ] Coach briefs the team on [`03-team/coach_and_ai_rules.md`](03-team/coach_and_ai_rules.md) — AI is
      allowed, coach contact is not
- [ ] **Registration e-mail sent** to `aspercasecomps@umanitoba.ca`
      ([`07-logistics/registration_email_draft.md`](07-logistics/registration_email_draft.md))
- [ ] All five passports checked (eTA applications follow in W2)
- [ ] Homework: [`01-competition/past_cases.md`](01-competition/past_cases.md) Part I; first pass at
      [`04-training/exercises/format_quiz.md`](04-training/exercises/format_quiz.md)

Then: Foundations to Sep 6 → skill building to Oct 11 → simulations under competition rules to Dec 20 →
peak in January → prepared-case sprint and travel in February.

---

## Contents

1. [The competition in 60 seconds](#the-competition-in-60-seconds)
2. [The repository](#the-repository)
3. [Quick start](#quick-start)
4. [Core workflows](#core-workflows)
5. [The rubric — and what it means for training](#the-rubric--and-what-it-means-for-training)
6. [Rules cheat sheet: AI, coach, anonymity](#rules-cheat-sheet-ai-coach-anonymity)
7. [Timeline and milestones](#timeline-and-milestones)
8. [Known limitations and open questions](#known-limitations-and-open-questions)
9. [Sources and contacts](#sources-and-contacts)

---

## The competition in 60 seconds

Nine graduate teams of four compete over three days in **three case formats**, then a final round.
Everything runs **in English**, PowerPoint only, judged by ~50 industry practitioners.

| Round | Prep | Delivery | Weight |
| --- | --- | --- | --- |
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

> **Watch the weekday question.** Feb 18–22, 2027 falls **Thursday–Monday**, but every edition in the
> current format has started on a **Wednesday** (2024, 2025, 2026 — three in a row), so 2027 as published
> would break the pattern. Either the window is exact, or the real week is Wed Feb 17 – Sun Feb 21. Every
> day-sheet here assumes the published window with the 2025 round order and says so in place; our flight
> envelope (arrive Feb 16/17, return Feb 22/23) covers both readings. Details:
> [`01-competition/facts_and_rules.md`](01-competition/facts_and_rules.md).

Full validated rule base: [`01-competition/facts_and_rules.md`](01-competition/facts_and_rules.md) —
**the single source of truth** for every rule claim in every other document.

---

## The repository

Eight numbered folders follow the lifecycle of the project:
*understand the competition → plan → form the team → train → practice → build assets → travel → brief.*
**62 files**, of which **42 markdown documents, ≈84,000 words**. **Every folder opens with its own
`README.md`** — what is inside, in what order to use it, and the hard rules that apply — so you can navigate
by clicking rather than by searching.

| Folder | Contents |
| --- | --- |
| [`01-competition/`](01-competition/) | Rules & facts (**source of truth**), handbook, official judging scoresheet + external-judge briefing, past-case dossier with ten re-crack briefs, and six official case PDFs |
| [`02-plan/`](02-plan/) | Preparation concept, dated week-by-week calendar (**governs on date conflicts**), simulation log |
| [`03-team/`](03-team/) | Team charter, role playbooks incl. the GenAI operating procedure, coach & AI rules one-pager |
| [`04-training/`](04-training/) | The core skills trio — presentation & storyline guide, Q&A drills (60 questions), business math (40 drills) — plus the framework selector, English phrasebook + 87 flashcards, and the **exercise program** in [`04-training/exercises/`](04-training/exercises/): 25-question format quiz, four solved workbooks, week-mapped catalog, ≈200 items |
| [`05-practice-cases/`](05-practice-cases/) | Three original full cases (traditional / boardroom / prepared, with teaching notes), mini-cases 1–12, model answers |
| [`06-templates/`](06-templates/) | The 14-slide team skeleton, six case-type skeletons (A–F), case-type playbook, financial toolkit (xlsx), judge-brief template (docx) |
| [`07-logistics/`](07-logistics/) | Registration e-mail draft, travel logistics Germany→Winnipeg, competition-day runbook |
| [`08-briefing-slides/`](08-briefing-slides/) | Kick-off Beamer deck — LaTeX source + the 25-page PDF |

**What each individual file is, and when to use it:** [`DOCUMENTATION.md`](DOCUMENTATION.md) §2. Every file
has one canonical location, every path in every document is relative to this root, and the sixteen longest
documents carry their own table of contents.

The eight commits of this material's earlier life as a nested repository (v1–v8, before it was flattened into
one) are preserved on the **`archive-history`** branch: `git log archive-history`.

---

## Quick start

**New team member — first 90 minutes.** Read [`01-competition/handbook.md`](01-competition/handbook.md) →
skim [`02-plan/week_by_week_plan.md`](02-plan/week_by_week_plan.md) for the weeks ahead → read your section
of [`03-team/role_playbooks.md`](03-team/role_playbooks.md) → sign
[`03-team/team_charter.md`](03-team/team_charter.md) → take
[`04-training/exercises/format_quiz.md`](04-training/exercises/format_quiz.md) (target: 25/25 by W3).

**Coach.** [`03-team/coach_and_ai_rules.md`](03-team/coach_and_ai_rules.md) (what you may and may not do,
round by round) → [`01-competition/judging_scoresheet.md`](01-competition/judging_scoresheet.md) (print one
per simulation judge) → [`02-plan/week_by_week_plan.md`](02-plan/week_by_week_plan.md) (run the calendar) →
[`02-plan/simulation_log.md`](02-plan/simulation_log.md) (log the same day).

**Anyone maintaining the material.** [`DOCUMENTATION.md`](DOCUMENTATION.md) — §2 for the file inventory,
§5 for the maintenance rules and the propagation order when the 2027 guide lands, §7 for what has been
verified and how. Then [`CHANGELOG.md`](CHANGELOG.md).

**Next actions beyond this week** (this week's checklist is at the top):

1. **W2:** apply for **eTAs** — CAD 7 each, official Government of Canada site only, all five travellers.
2. **W3–W6:** flight price alerts on, then **book flights** (arrive Feb 16/17, return Feb 22/23); submit the
   university funding application.
3. **W9:** confirm the hotel block with the organizers (Delta Hotels Winnipeg per the 2027 site).
4. **From W11:** the simulation cadence starts — ten simulations under competition rules, logged in
   [`02-plan/simulation_log.md`](02-plan/simulation_log.md). Download the five non-mirrored official cases
   before the sessions that use them (W14, W25).
5. **Watch for the 2027 Competition Guide** — the sponsor page and @Asper_BCC from autumn; case writing
   starts around October. When it lands, follow the propagation order in
   [`DOCUMENTATION.md`](DOCUMENTATION.md) §5.

---

## Core workflows

**Kick-off (W1).** Present the briefing deck → everyone reads the handbook → sign the charter → assign roles
→ send the registration e-mail → start the admin track in
[`07-logistics/travel_logistics.md`](07-logistics/travel_logistics.md).

**A normal training week (Phases 2–3).** One 3–5 h weekend block (simulation or workshop) per the calendar
→ one 60–90 min midweek debrief plus a skill session from [`04-training/`](04-training/) → 30 min of
individual drills (math routine, flashcards). A mini-case opens the midweek session. If a week collapses, the
priority order is **simulation > mini-case > workbook item > individual drills** — protect the simulations
above all.

**Running a simulation.** Pick the case from the week plan → coach prints
[`01-competition/judging_scoresheet.md`](01-competition/judging_scoresheet.md) → run under
competition-identical conditions (timed, one laptop each, internet + GenAI allowed, **no coach contact**,
`.pptx` "USB" hand-in at the deadline, all four speak, yellow/red cards) → score on the official rubric →
2 strengths / 2 gaps / 1 drill per person → enter results in
[`02-plan/simulation_log.md`](02-plan/simulation_log.md) → goals carry into the next week.

**When a case lands (competition or graded sim).** Classify the type within 10 minutes using
[`06-templates/case_type_playbook.md`](06-templates/case_type_playbook.md) → duplicate the matching skeleton
from [`06-templates/case-type-templates/`](06-templates/case-type-templates/), **delete its red briefing
slide**, rename to the round's file convention → storyline pass, **titles first** → parallel build along the
role minute-maps → every number through
[`06-templates/case_financial_toolkit.xlsx`](06-templates/case_financial_toolkit.xlsx) → for boardroom rounds
fill [`06-templates/judge_brief_template.docx`](06-templates/judge_brief_template.docx), wording mirroring
the summary slide.

**Prepared-case sprint (on release, ~2 weeks).** Follow Phase 4 of
[`02-plan/preparation_plan.md`](02-plan/preparation_plan.md) day by day. Coach input **is** allowed in this
round. Submit the `.pptx` by e-mail **at least 24 h before the deadline**, file named
`[Team Name] Prepared Case`.

**Competition week.** [`07-logistics/competition_day_runbook.md`](07-logistics/competition_day_runbook.md)
is the daily script; the standing rules at its top apply all week.

**After.** Debrief in the week of Feb 23, write thank-yous, and hand the repository to the next team
(final section of the week plan).

Step-by-step detail for each of these: [`DOCUMENTATION.md`](DOCUMENTATION.md) §4.

---

## The rubric — and what it means for training

The official ABCC rubric (2025 Event Guide) applies to **all rounds**, 7 categories, max 105 points:

| Category | Weight | What judges ask |
| --- | --- | --- |
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
[`04-training/exercises/workbook3_storyline_and_slides.md`](04-training/exercises/workbook3_storyline_and_slides.md).

---

## Rules cheat sheet: AI, coach, anonymity

**AI is explicitly allowed.** The official rules permit internet use during timed prep, including
"any login-required website … filesharing websites, **and Generative AI**." That covers the 4-h boardroom
and 3-h traditional prep; in the prepared case all resources are allowed anyway.

Because every team has the same arsenal, the edge is a **drilled procedure**, not access
([`03-team/role_playbooks.md`](03-team/role_playbooks.md), GenAI SOP): one designated operator (CS &
analytics lead), narrow sanctioned tasks (checking math, stress-testing the recommendation, generating
counterarguments, polishing brief wording, the 10-minute Q&A-anticipation routine), and the hard rule that
**no unverified number reaches a slide**. Framing, option choice, and the recommendation are never
outsourced — borrowed logic collapses in the 22-minute discussion. **Confidentiality caution:** competition
cases are confidential documents, so do not paste full case text into consumer AI tools; prefer
university-licensed enterprise tools and work from your own summaries. Re-check the 2027 guide for new AI
clauses before travelling.

**The coach is in the game** for the prepared case (unrestricted — faculty input explicitly allowed), for
everything before the competition, and on site for presentations, feedback sessions, and the full social
program.

**The coach goes silent** from the moment a **boardroom** or **traditional** case is released until the team
has presented — no contact of any kind. Any communication between coach and team during a presentation or
Q&A, or any coach intervention in the question period, means **immediate disqualification**. Advisors of
finalist teams may not communicate with their team until after it has presented.

**Anonymity binds everyone, coach included.** Nothing said, worn, or shown may identify HSBI. The team
competes under **a fictional consulting name it chooses itself** and registers with the organizers before the
event, plus a **division letter A–I drawn at on-site registration** that sets the week's presentation slots —
the name is ours, the letter is theirs. Identifying your school to a judge = disqualification. This is why
every template here is deliberately clean of HSBI branding — **never commit the HSBI name into a slide
template or judge brief.**

---

## Timeline and milestones

| Date | Milestone |
| --- | --- |
| **Aug 3–9, 2026 (now)** | **W1 kick-off:** deck presented, charter signed, roles assigned; **registration e-mail sent**; passports checked |
| Aug 2026 | **eTAs applied for** (W2), all five travellers |
| Sep–Oct 2026 | **Flights booked** (arrive Feb 16/17, return Feb 22/23); funding secured; hotel block confirmed |
| Nov 2026 | Travel health + cancellation insurance closed; **team `.pptx` template v1** built (anonymity-proof) |
| Dec 2026 | Winter gear complete; eSIMs ordered; template v2 frozen after use in three simulations |
| Late Jan 2027 | Taper begins; prepared-case sprint logistics ready |
| ~Feb 4, 2027 *(TBA)* | **Prepared case released** → 14-day sprint |
| ~Feb 17, 2027 *(TBA)* | **Prepared deck submitted** ≥24 h before the deadline |
| Feb 16/17, 2027 | Fly Bielefeld → Winnipeg |
| **Thu Feb 18 – Mon Feb 22, 2027** | **ABCC 2027** |
| Week of Feb 23 | Debrief, thank-yous, handover to the next team |

Training phases: **Foundations** (W1–W5, Aug 3 – Sep 6) → **Skill building** (W6–W10, Sep 7 – Oct 11) →
**Simulations under competition rules** (W11–W20, Oct 12 – Dec 20) → *Christmas, light load* (W21–W22) →
**Peak** (W23–W26, Jan 4–31) → **Prepared-case sprint & travel** (W27–W29, Feb 1–17).

**The competition week, and the caveat.** The 2025 pattern ran Wednesday arrival with registration and the
division draw · Thursday prepared-case presentations and the museum social · Friday boardroom case and
Festival du Voyageur · Saturday traditional case, finals and awards gala · Sunday departure. 2026 ran the
same shape, also from a Wednesday. The published 2027 window (**Thu Feb 18 – Mon Feb 22**) would break that
pattern, so the day-sheets in
[`07-logistics/competition_day_runbook.md`](07-logistics/competition_day_runbook.md) and the week-plan table
map the 2025 order onto the published dates and mark every weekday *expected*. What the team drills is the
*shape* of each day; the dates are a one-line edit when the agenda lands. First thing to reconcile then:
which date carries which round.

---

## Known limitations and open questions

- The **2027 agenda, deadlines, fees, and field are TBA** until the organizers publish them. Everything
  schedule-shaped is a 2025/2026-baseline assumption, flagged as such in place — and because 2027 runs
  Thursday–Monday against 2025's Wednesday–Sunday, the day-sheets will need re-mapping, not just re-dating.
- The three original practice cases and all worked model answers use **fictional, internally consistent
  data** (labelled as case data); teaching-note figures are calibration aids, not real-company facts.
- **Eligibility of the specific HSBI student mix needs written confirmation** from the organizers — the top
  open question in [`01-competition/facts_and_rules.md`](01-competition/facts_and_rules.md).
- Eleven official past cases exist across ten clients (2023 ran both rounds on Manitoba Hydro). **Six PDFs
  are mirrored** in [`01-competition/past-case-pdfs/`](01-competition/past-case-pdfs/); the remaining five
  (2024 cases 1 and 3, all three 2026 cases) are linked by URL in `facts_and_rules.md` and
  [`01-competition/past_cases.md`](01-competition/past_cases.md) — download them before the sessions that
  need them (W14, W25).

Open questions to put to the organizers after registration — all seven are covered by
[`07-logistics/registration_email_draft.md`](07-logistics/registration_email_draft.md): 2027 agenda and
prepared-case release/submission dates · registration process and fee for an international (German) team and
what it covers · eligibility confirmation · roster, bio and photo requirements plus advisor registration ·
2027 hotel block and booking code · whether the 2027 rules package changes anything against the 2025
baseline, **specifically any new generative-AI clauses** · a **formal letter of invitation** naming all five
travellers and the dates, for the Canadian border and for university travel funding.

**Provenance.** All competition facts were researched and validated (July–August 2026) against the official
Asper website, the official **ABCC 2025 Event Guide** (the fullest public rulebook), the official past-case
PDFs, and press coverage. The materials went through a multi-agent adversarial review: rule claims verified
against the fact base, all exhibit arithmetic recomputed, all official URLs link-checked. Every document
flags where 2027 specifics are still TBA. The documentation itself — structure, inventory, counts,
cross-references — was re-verified on **2026-08-04**; see [`DOCUMENTATION.md`](DOCUMENTATION.md) §7 for what
was and was not checked. No official URL was re-fetched on that date, so all competition facts still carry
their July–August 2026 validation.

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

**Publishing.** To put this on a private remote:

```bash
gh repo create asper-abcc-2027 --private --source=. --push
# or: git remote add origin git@github.com:<user>/asper-abcc-2027.git && git push -u origin main
```

> **Confidentiality.** The official case PDFs in
> [`01-competition/past-case-pdfs/`](01-competition/past-case-pdfs/) are © University of Manitoba and are
> competition documents marked "no reproduction or transmission" — internal team use only. Do not
> redistribute them, and keep this repository **private**.
