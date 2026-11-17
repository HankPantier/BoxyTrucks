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
