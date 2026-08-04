# Workbook 2 — Quant Drills: Sizing, Exhibit Math, Sensitivity

Complements `04-training/business_math_drills.md` (the 40-drill base set). Everything here is done **without calculator first**, then verified. State every assumption aloud — that habit is scored in Winnipeg under Analysis (2.0×).

## Exercise 2.1 — Market-sizing ladder · 12 problems, 3–4 min each

German set: (1) Annual spend on premium candles in Germany. (2) Number of student bank accounts opened in NRW per year. (3) Annual ticket revenue of all jazz festivals in Germany. (4) Market for corporate team-event services in OWL. (5) Annual revenue of one Bielefeld Sparkasse branch. (6) German market for refillable home-fragrance products in 2030.
Canadian set (competition warm-up): (7) Annual museum admissions revenue in Manitoba. (8) Coffee sold on the University of Manitoba campus per year. (9) Manitoba market for youth banking accounts. (10) Winnipeg annual spend on live-music tickets. (11) Number of skilled aviation-maintenance roles in Manitoba. (12) Candles sold in Canada per year.

> **Worked answers (top-down; your structure matters more than the number).**
> **(1)** 84M Germans → ~40M households → ~30% buy candles regularly ≈ 12M → premium share ~15% ≈ 1.8M households → ~€60/yr ≈ **€110M** (sanity: Coal & Canary-type brands' DE revenues fit). **(9)** ~1.35M Manitobans → ~16% aged 13–25 ≈ 215k → banked ~90% ≈ 195k accounts; at $40–60 annual revenue each ≈ **$8–12M p.a.** — small pool, so the case for youth investment is lifetime value, not current revenue (exactly the Access CU logic). **(7)** ~300k Manitoba Museum visitors + ~500k other museums/galleries ≈ 800k visits → paying share ~60% at ~$15 ≈ **$7–8M** — one $500k blockbuster is a big bet against that base. Full worked set for the rest: build in pairs, cross-check top-down vs bottom-up within ±30%.

## Exercise 2.2 — Exhibit math on the real cases · 20 min, pairs

Using facts from the official cases (sources: `01-competition/past-case-pdfs/` and the profiles in `01-competition/past_cases.md`):

a) **Manitoba Museum:** a travelling show costs $500k upfront. At a $12 blockbuster surcharge and 62% of the museum's ~300k annual visitors passing through in a four-month run, does it break even? What attendance is required at $15?
b) **Museum, downside check:** Ultimate Dinosaurs drew 23,945 against 45,000 projected. At what shortfall does a $500k show at $15 lose $200k+?
c) **Access CU:** with ~208,000 members and the under-30 share at 11%, how many under-30 members exist; and if churn among them is 8%/yr while intake is 1,400/yr, what is the base in five years?
d) **IJL:** online revenue ~$370k with two-thirds from outside Winnipeg. If national e-commerce grows 35%/yr for three years while the ~$3.6M store base stays flat, what share of a $4M business is national online by year 3?

> **Answers.** a) Revenue 0.62 × 300k × (4/12) ≈ 62k visitors… careful: 62% *of the four-month visitor flow* = 0.62 × 100k = 62k × $12 ≈ $744k → breaks even with margin; at $15 need 500k/15 ≈ **33,400 visitors** (~⅓ of the four-month flow — plausible only with a strong title, which is the case's real lesson). b) Loss ≥ $200k when revenue ≤ $300k → **≤ 20,000 visitors at $15**. Ultimate Dinosaurs' actual 23,945 sits just above that line: 23,945 × $15 ≈ $359k, a **~$141k loss** on this hypothetical $500k/$15 show — the real 2022 show lost ~$300k because its economics were worse than this drill's. Either way the projection error, not the price, was fatal. c) ≈ 22,900 under-30s (*planning assumption — `05-practice-cases/model_answers.md` models a less conservative 15% share; state whichever you use*); five-year base ≈ 22,900 × 0.92⁵ + 1,400 × (0.92⁴+…+0.92⁰) ≈ 15.1k + 5.9k ≈ **21.0k — still shrinking**; intake must rise ~30% (to ~1,830/yr) just to hold. d) Online ≈ 370k × 1.35³ ≈ $910k; national share ⅔ ≈ $607k → **~15% of the $4M firm** — meaningful, not yet "national." State rounding aloud; judges accept clean approximations.

## Exercise 2.3 — Sensitivity one-pager · 15 min, solo

For the museum show (a): build the ±20% grid on price and attendance (nine cells, net result). Mark the loss region. Then write the one sentence you would say to a board about it.

> **Answer pattern.** Base $15 × 33.4k = break-even. Worst cell (−20/−20): $12 × 26.7k ≈ $320k → −$180k. Best (+20/+20): $18 × 40k = $720k → +$220k. Board sentence: "The show breaks even at a third of our four-month traffic; the realistic downside is a $180k loss, which sponsorship of $200k caps at zero — so we recommend proceeding only with the sponsor signed." (Note the shape: number → downside → the condition that caps it. That sentence is Implementation & Resources material.)

## Exercise 2.4 — Ten-minute arithmetic circuit · weekly, all four members

Rapid-fire, no calculator, 30 seconds each: (1) 17% of 2.4M (2) 340k/1.7% (3) CAGR if 80→140 in 5 yrs (4) payback: 1.2M invest, 350k/yr (5) break-even: fixed 850k, CM €23.40 (6) 6.8M × 1.04³ (7) margin if cost 10.90, price 32.77 (8) 3/7 as % (9) NPV factor yr 3 at 8% (10) €95 price, 62% margin → COGS?

> **Answers.** (1) ≈408k (2) 20M (3) ≈12% (4) ≈3.4 yrs (5) ≈36.3k units (6) ≈7.65M (7) ≈67% (8) ≈43% (9) ≈0.794 (10) ≈€36. Log times in `02-plan/simulation_log.md` notes; target: 10/10 in under 6 minutes by November.
