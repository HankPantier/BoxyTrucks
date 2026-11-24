# Weekly spec stack (Tuesdays, 3:41 pm ET)

> **Nov 24, 2026 mix change (weekly planning, from the Nov 23 scoreboard): Instagram gets Reels only.** Spec sheets, spec stacks and single-image posts go to Pinterest only, not Instagram, because 15 singles averaged 44 IG views and 17 carousels 58, against 2,227 for the 2 reader-rig Reels, 884 for the 3 data-hook Reels, 141 for 9 years Reels and 117 for 17 tire Reels. Targets per week: 3 reader-rig Reels (when owners submit), 2 data-hook Reels ("By the numbers #NN": one surprising, sourced number from our pages, voice B), and years-to-avoid Reels. Carousels stay only for Hank's own trucks. For this format: post to Pinterest (and YouTube Community if the procedure says so); skip Instagram, and log ig_status "skipped (Reels only, Nov 24)".


Hank, Nov 6, 2026: work comparison graphics in occasionally, a spec stack about weekly. Use 3–4 trucks when the data
allows, not just 2. Inspired by the "1993 Bronco / K5 / Ramcharger / Yukon" spec-sheet posts, done our way.

## Rules
- Facts only from the site's own data: `data/compare/<slug>.json` → `table`, or, for a 3–4 truck stack built across
  pages, each generation's page/extra data (`data/extra/<family>/<gen>.json`, specs on the gen page). Shorten wording,
  never change a number.
- Photos only from the site's licensed page photos (off-road, no wrecks), credited on the image. Blur any readable number
  plate with the spec's `blur` boxes. No brand logos or wordmarks, no press photos, no AI-looking studio side profiles.
- Footer always points to boxytrucks.com/compare; the caption links the specific compare page (or the family's
  best-years page when there's no compare page).

## Each week
1. `git pull`. Take the next row in the list below whose status isn't `posted`; write its spec in `social/stacks/` if
   it doesn't exist and render: `node social/stacks/make_stack.js social/stacks/<slug>.json`. Look at the image.
2. Post the JPG to all five platforms, verifying the account before each (stop on a wrong account, never switch):
   Instagram @boxytrucks, Pinterest boxytrucks (not X: weekly round-up only since Nov 14, 2026) (link = the compare page with utm_source=pinterest),
   TikTok @boxytrucks (photo post) and YouTube (Boxy Trucks channel) as a Community post if available, otherwise skip YouTube.
   Caption: the question in the title, one line per truck on who it suits (from the compare page verdict), "Which would
   you pick?", the link (or "link in bio" on Instagram), and photo credits.
3. Mark the row posted with the date and URLs, commit, push. Tell Hank only if something went wrong.

## Order
| # | Stack | Trucks | Source | Status |
|---|---|---|---|---|
| 1 | defender-vs-grenadier-vs-g-class | Defender, Grenadier, G-Class | compare page | posted 2026-11-10: IG https://www.instagram.com/boxytrucks/p/DfkyzeTAeiu/ · X https://x.com/boxytrucks/status/2120256658249064752 (link reply https://x.com/boxytrucks/status/2120256823873634677) · Pinterest https://www.pinterest.com/pin/1128292512945945077/ · YouTube https://www.youtube.com/post/UgkxMptah-3MAxW0EphDl3CpMhpbdHwt8Q3g · TikTok not posted: two photo-post attempts redirected to Studio but never appeared (check for late duplicates) |
| 2 | 80-series-vs-100-series | 80, 100 | compare page | posted 2026-11-17: IG https://www.instagram.com/boxytrucks/p/Df20ZWBG9uS/ · Pinterest https://www.pinterest.com/pin/1128292512946493809/ · YouTube https://www.youtube.com/post/Ugkxx83v323-oKnflzaDUNAxYZgs8iyq4U0z · X not posted (Friday round-up only) · TikTok tt_status skipped (paused, Hank Nov 17) |
| 3 | land-cruiser-250-vs-4runner-6th-gen + GX550 | LC 250, 4Runner, GX 550 | compare + gen data | posted 2026-11-24: YouTube https://www.youtube.com/post/Ugkx0TLUdDUWuCgVD9JoYATu9-KPLThJcM6u · Pinterest https://www.pinterest.com/pin/1128292512947052191/ (draft published Nov 24 by the session) · IG ig_status skipped (Reels only, Nov 24) · X not posted (Friday round-up only) · TikTok not posted (video only) |
| 4 | jk-vs-jl + Bronco | JK, JL, Bronco | compare pages | todo |
| 5 | gx470-vs-100-series + LX470 | GX 470, 100 Series, LX 470 | compare pages | todo |
| 6 | early-bronco-vs-fj40 + CJ-5 + Scout 800 | Early Bronco, FJ40, CJ-5, Scout | compare + gen data | todo |
| 7 | samurai-vs-jimny | Samurai, Jimny | compare page | todo |
| 8 | cherokee-xj-vs-wrangler-tj + ZJ | XJ, TJ, ZJ | compare pages | todo |
| 9 | fj-cruiser-vs-4runner-5th-gen + GX460 | FJ Cruiser, 4Runner, GX 460 | compare pages | todo |
| 10 | grenadier-vs-70-series | Grenadier, 70 Series | compare page | todo |
