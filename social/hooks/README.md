# Hook-style Shorts test (Nov 17, 2026)

Why: YouTube Studio Research → "Outliers in my niche" (Shorts, last 90 days, ≥2x outlier score) showed small channels hitting
400K–3.6M views with one surprising fact per Short and a curiosity title. YouTube's own title-pattern summary (100 videos, 71M views):
1. exact price contrast, 2. obscure engineering quirk, 3. disbelief / design-debate question. Almost all are real footage with a voice.
Ours (spec-answer titles over stills, e.g. "K5 Blazer tire size: the biggest tire with no lift (33x12.50R15)") sit at 60–290 views;
Hank's own G 500 footage did best (456).

Test: one Short per pattern, voice B (AI, disclosed on the end card and in captions), facts only from site data or Hank's own statements.

| File | Pattern | YouTube title | Facts from |
|---|---|---|---|
| g500-three-lockers.mp4 | engineering quirk | Hank's G 500 has three locking diffs. Here's the catch. | data/g-class.json (three lockers; lockers "never used" often don't work; vacuum leak + bleed hydraulic lines); Hank: "I'm still working through the lockers on mine" |
| l322-timing-guides.mp4 | price contrast | The $1,850 job hiding in a 2003–05 Range Rover | data/pages/range-rover/l322.json M62 guides entry (AULRO owners; Atlantic British TCKL322 $1,849.95; ~26 h) |
| lr3-2005-complaints.mp4 | question | Why do 2005 LR3s get 12x the complaints of a 2008? | data/extra/land-rover/lr3.json (96 vs 8 NHTSA complaints, five recalls, ReRev 2008–09) |

Measure: views, average view duration and % viewed vs swiped at 48 h, against the tire/years Shorts' usual 100–200 views.
If they clearly win, switch the daily Shorts to this format (same data underneath; keep the tire/years facts in the description).

Build: `VOICE=<en_US-joe-medium.onnx> python3 social/hooks/build_hook.py social/hooks/<name>.json social/hooks/<name>.mp4`
(then re-encode real-footage videos at -b:v 3500k).

## Results (Nov 22, 2026)

YouTube Studio, lifetime numbers read on Nov 22 at about 3 pm ET. Ages differ (the hook Shorts are 2–4 days old, the comparisons 1–8 days), so this is a direction, not a clean A/B. "Stayed" is Studio's "Stayed to watch" (the rest swiped away).

| Short | Type | Posted | Views | Stayed to watch | Watch time (h) |
|---|---|---|---|---|---|
| Hank's G 500 has three locking diffs | hook: engineering quirk | Nov 18 | 145 | 52.5% | 0.3 |
| The $1,850 job hiding in a 2003–05 Range Rover | hook: price contrast | Nov 19 | 181 | 30.9% | 0.3 |
| Why do 2005 LR3s get 12x the complaints of a 2008? | hook: question | Nov 20 | 62 | 45.8% | 0.1 |
| Land Rover LR3 / Discovery 3 years to avoid | years | Nov 16 | 482 | 64.5% | 1.9 |
| Suzuki SJ / Samurai tire size | tire | Nov 17 | 608 | 25.3% | 0.6 |
| Pajero / Montero (3rd gen) tire size | tire | Nov 19 | 292 | 26.3% | 1.7 |
| Hummer H1 tire size | tire | Nov 18 | 123 | 15.9% | 0.1 |
| Hank's G 500 on a fall back road | Hank's footage | Nov 14 | 465 | 31.3% | 0.6 |

Other tire/years Shorts Nov 14–21 (views only): Delica L300 239, Pinzgauer 710/712 143, Y62 years 354, K5 1st gen tires 291, Scout II tires 120, Bronco 6G years 87, Patrol 60 tires 225, JK years 350; median of the tire/years Shorts is about 265.

What it says:
- No hook style beat the usual views. All three landed at 62–181, below the tire/years median (~265).
- Hooks hold people better than tire Shorts: 31–53% stayed vs 16–26% for tire Shorts. They just get shown less. Tire and years titles match what people search for, which is where most of their views come from.
- The best performer on both counts is the "years to avoid" format (LR3: 482 views, 64.5% stayed), followed by Hank's own footage.
- Instagram Reel plays and Pinterest impressions weren't compared this round.

Next: keep the searchable "years to avoid" / tire titles, make more years-to-avoid Shorts, and borrow the hook as the first on-screen line (a surprising fact in the first second) rather than as the title. Keep Hank's own footage weekly.
