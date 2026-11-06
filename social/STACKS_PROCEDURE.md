# Weekly spec stack (Tuesdays, 3:41 pm ET)

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
   Instagram @boxytrucks, X @boxytrucks, Pinterest boxytrucks (link = the compare page with utm_source=pinterest),
   TikTok @boxytrucks (photo post) and YouTube (Boxy Trucks channel) as a Community post if available, otherwise skip YouTube.
   Caption: the question in the title, one line per truck on who it suits (from the compare page verdict), "Which would
   you pick?", the link (or "link in bio" on Instagram), and photo credits.
3. Mark the row posted with the date and URLs, commit, push. Tell Hank only if something went wrong.

## Order
| # | Stack | Trucks | Source | Status |
|---|---|---|---|---|
| 1 | defender-vs-grenadier-vs-g-class | Defender, Grenadier, G-Class | compare page | ready (rendered Nov 6) |
| 2 | 80-series-vs-100-series | 80, 100 | compare page | ready (rendered Nov 6) |
| 3 | land-cruiser-250-vs-4runner-6th-gen + GX550 | LC 250, 4Runner, GX 550 | compare + gen data | todo |
| 4 | jk-vs-jl + Bronco | JK, JL, Bronco | compare pages | todo |
| 5 | gx470-vs-100-series + LX470 | GX 470, 100 Series, LX 470 | compare pages | todo |
| 6 | early-bronco-vs-fj40 + CJ-5 + Scout 800 | Early Bronco, FJ40, CJ-5, Scout | compare + gen data | todo |
| 7 | samurai-vs-jimny | Samurai, Jimny | compare page | todo |
| 8 | cherokee-xj-vs-wrangler-tj + ZJ | XJ, TJ, ZJ | compare pages | todo |
| 9 | fj-cruiser-vs-4runner-5th-gen + GX460 | FJ Cruiser, 4Runner, GX 460 | compare pages | todo |
| 10 | grenadier-vs-70-series | Grenadier, 70 Series | compare page | todo |
