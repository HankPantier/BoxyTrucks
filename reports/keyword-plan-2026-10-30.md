# BoxyTrucks keyword plan — 2026-10-30

Research only. No site files or data were changed. The evidence comes from 31 Google-style WebSearch result lists run on 2026-10-30, the built HTML in `site/`, and the data in `data/`. I have no search-volume numbers, so demand is rated strong, moderate or weak from what ranks: the number of pages written for that exact phrase, and whether big publishers or content farms bother with it. Autocomplete and "People also ask" boxes don't come back through the search tool, so the phrasing is taken from the ranking pages' titles and URLs (see "Unverified" at the end).

## 0. What the audit found (read first)

1. **Titles run long and put the brand where the words people search should be.** Of 107 generation-guide titles, 0 use "problems", "years to avoid", "reliability" or "buyer's guide". All 21 best-years titles run 58–88 characters, and only the Jeep one (58) is under 60. Ten of the 17 comparison titles are over 60. Repair titles run up to 110 characters and put the truck last.
2. **Our names for the trucks aren't the names people search.** People type "80 series land cruiser", "5th gen 4runner", "g wagon", "jeep xj", "gen 1 blazer", "square body". We print "Toyota Land Cruiser 80 Series", "Toyota 4Runner 5th Gen", "Mercedes-Benz G-Class W463", "Chevrolet K5 Blazer (1st generation)". The ranking pages for "g wagon years to avoid" (rerev.com, carscounsel.com) all say "G Wagon" in the title and URL. Our G-Class titles never use it.
3. **The page formats that win are "years to avoid" and "common problems" pages for each model.** rerev.com, carscounsel.com and carwhere.com publish one URL per model just for "years to avoid". SlashGear, RealTruck and CarGurus run "best and worst years" articles. Unsealed 4x4 ranks first for "80 series land cruiser problems" with a "common problems & solutions" list. Most of these pages are thin content-farm pages, and several result lists also contain spam domains, so sourced pages have a real chance.
4. **Comparison and classic-truck searches are won by forum threads.** "land cruiser 80 vs 100" returns almost nothing but IH8MUD and Expedition Portal threads. "k5 blazer buyers guide" returns ck5.com threads plus one shop blog. A clean comparison table or checklist page can outrank these.
5. **Tire-fitment searches are won by a page per generation.** trail4runner.com ranks with a "Largest Tire Size on 5th Gen 4Runner" article, followed by forum threads. Our `/tires/` is one URL for 99 trucks, so it can't rank for each truck's tire query.
6. **Meta descriptions are the opening of the verdict prose, cut off with "…".** They contain no years, no "problems" and no "best years".
7. **Most family-page H1s drop the make**: "Trooper", "Hummer", "Jeep", "4Runner".

## 1. Top 30 target queries

URLs are the live pretty URLs. "NEW" pages are described in section 3. Priority means expected payoff for the effort: H, M or L.

| # | Query | Page | Change needed | Pri | Demand note (from the results) |
|---|---|---|---|---|---|
| 1 | best year 4runner to buy / 4runner years to avoid | /models/4runner/best-years/ | Title: `4Runner Years to Avoid (and the Best Years to Buy)`. H1: `Toyota 4Runner years to avoid, and the best years to buy`. Add a summary table at the top (gen · best years · avoid · why). | H | Strong: RealTruck, SlashGear, AutoTrader, CarWhere and two rerev URLs all target it, plus many spam copies. |
| 2 | 4th gen 4runner years to avoid | NEW: /models/4runner/4th-gen/years/ | Page for one generation, built from the timeline flags and the years FAQ. 4th-gen has avoid flags. | H | Strong: SlashGear "years to never buy", rerev, CarWhere and mechanicbase rank. No enthusiast page. |
| 3 | 5th gen 4runner biggest tire without lift | NEW: /models/4runner/5th-gen/tires/ | Tire page for this generation from `fitment.max_tire` (Stock / 2 in / 3 in+ rows already exist). Link lift kits. | H | Strong: trail4runner ranks with two pages and comment pages, plus forum threads. Affiliate intent. |
| 4 | 80 series land cruiser problems | NEW: /models/land-cruiser/80-series/problems/ | Problems page from `buying_checks` + `repairs` (symptoms/cost) + recalls. For now, rename the gen-page H2 "What to check before you buy" to "80 Series problems and what to check". | H | Moderate–strong: Unsealed 4x4 (3 URLs) holds the top spots, then forums and au7o.io. Few US pages. |
| 5 | land cruiser 80 vs 100 | /compare/80-series-vs-100-series/ | Title: `Land Cruiser 80 vs 100 Series: Which to Buy?` (44). Add a spec table above the fold if it isn't there. | H | Moderate: the results are almost all IH8MUD and Expedition Portal threads. No editorial competitor, so it's winnable. |
| 6 | g wagon years to avoid | /models/g-class/best-years/ | Title: `G-Wagon Years to Avoid (and the Best Years to Buy)` (50). H1 should include "G-Wagon (G-Class)". Mention "G-Wagon" in the meta. | H | Strong: rerev (3 URLs), carscounsel (2) and Reddit r/AMG "G63 best year" all use "g wagon". |
| 7 | fj cruiser years to avoid | NEW: /models/land-cruiser/fj-cruiser/years/ | Page for one generation. fj-cruiser has avoid flags. | H | Strong: rerev, carscounsel, CarGurus buying guide, SlashGear and about 6 spam copies target it exactly. |
| 8 | fj cruiser lift tire size / fj cruiser biggest tire | NEW: /models/land-cruiser/fj-cruiser/tires/ | Tire page + the SUSPENSION entries from `mods` (lift-kit affiliate links). | H | Strong commercial demand: the results are ReadyLift, Zone and Tuff Country product pages. Buying intent, which suits affiliates. |
| 9 | jeep xj best years / jeep cherokee xj years to avoid | NEW: /models/jeep/cherokee-xj/years/ | Page for one generation. cherokee-xj has avoid flags. The Jeep family best-years page covers 17 generations and is too broad. | H | Moderate: NAXJA threads, a 4WD Mechanix forum ranking, Wikipedia and CarWhere. Weak editorial competition. |
| 10 | jeep wrangler jk years to avoid | NEW: /models/jeep/jk/years/ (cover JK and JK Unlimited, canonical from jk-unlimited) | Page for one generation. Both JK slugs have avoid flags. | H | Strong but crowded: jk-forum slideshow, SlashGear, rerev (2), RealTruck, CarWhere and 8020automotive. |
| 11 | hummer h1 / hummer h1 truck | /models/hummer/h1/ | Title: `Hummer H1 (1992–2006): Buyer's Guide, Prices & Problems` (55). H1 `AM General Hummer H1 (1992–2006)`. Add an H2 "H1 body styles: wagon, open top, pickup, slant-back" (already in the copy). | H | Search Console query. Moderate demand. The "years to avoid / buyers guide" results are spam PDFs, Reddit and KBB, so competition is weak. |
| 12 | gen 1 blazer / 1st gen k5 blazer | /models/chevrolet/k5-blazer-1st/ | Title: `1st Gen K5 Blazer & Jimmy (1969–72) Buyer's Guide` (49). H1 `First-gen Chevy K5 Blazer (1969–1972)`. Use "1st gen" and "Chevy" in the intro. | H | Search Console query. Mixed results (TrailBlazer, GM Authority poll, classic-car listings), so the intent is ambiguous but nobody owns it. |
| 13 | square body k5 blazer / k5 blazer buyers guide | /models/chevrolet/k5-blazer/ | Title: `Square Body K5 Blazer (1973–91) Buyer's Guide` (45). | H | Moderate: ck5.com threads fill the results, plus one Velocity Restorations blog post. Weak competition. |
| 14 | land cruiser years to avoid / best land cruiser year | /models/land-cruiser/best-years/ | Title: `Land Cruiser Years to Avoid (and the Best to Buy)` (49). Add a summary table at the top. | H | Strong: rerev has a vehicle page, and Land Cruiser buying is a heavy-traffic topic. |
| 15 | 100 series land cruiser problems | NEW: /models/land-cruiser/100-series/problems/ | Problems page. | M | Moderate: Carsguide used review, IH8MUD "common 100 problems", ExplorOz and au7o.io. Mostly Australian. |
| 16 | w463 g500 reliability / g500 problems | NEW: /models/g-class/w463/problems/ (titled "W463 G-Wagon Problems & Reliability") + link from /models/g-class/g500/ | Problems page. Add "reliability" to the H2 on the g500 page. | M | Moderate: Expedition Portal, MBWorld "how reliable" threads, euroautopro "common problems W463 G500" and rerev. Thin. |
| 17 | lx470 vs land cruiser 100 | /compare/lx470-vs-100-series/ | Title: `LX 470 vs Land Cruiser 100: Which to Buy?` (41). Add the FAQ "Is the LX 470 a Land Cruiser?" | M | Moderate: forums plus 5 kevinsautos "is the LX470 the same as a Land Cruiser" Q&A pages, which suggests a "People also ask" box. |
| 18 | gx460 vs 4runner | /compare/gx460-vs-4runner-5th-gen/ | Title: `Lexus GX 460 vs 5th Gen 4Runner: Which to Buy?` (46). | M | Moderate: iSeeCars compare, IH8MUD, PickupTruckTalk, MotorBiscuit and a dealer page. |
| 19 | gx470 vs 4runner 4th gen | /compare/gx470-vs-4runner-4th-gen/ | Title: `Lexus GX 470 vs 4th Gen 4Runner: Which to Buy?` (46). | M | Moderate: Expedition Portal threads and a Drivingline article. |
| 20 | 6th gen 4runner biggest tire no lift | NEW: /models/4runner/6th-gen/tires/ | Tire page. | M | Moderate and growing: only 4runner6g.com forum threads rank. No article competitor. |
| 21 | lr3 years to avoid / lr3 problems | NEW: /models/land-rover/lr3/years/ + /problems/ | Both new page types. lr3 has avoid flags. | M | Moderate: rerev (2), carscounsel, forcar, CarComplaints and landroverforums threads. |
| 22 | range rover p38 problems | NEW: /models/range-rover/p38/problems/ | Problems page. | M | Moderate: Classics World and Autocar buyer's guides, AULRO threads and mez.co.uk. UK-leaning. |
| 23 | isuzu trooper / isuzu trooper problems | /models/trooper/ + NEW: /models/trooper/trooper-2/problems/ | Family H1 `Isuzu Trooper` (currently "Trooper"). Title `Isuzu Trooper: Generations, Best Years & Problems` (49). Put the badge twins (Acura SLX, Opel Monterey, Holden Jackaroo) in the meta. | M | Search Console query. Results: RepairPal pages for each year, WhatCar, RAC and Edmunds forums. |
| 24 | k5 suburban / square body suburban | /models/chevrolet/suburban-square/ + /models/chevrolet/ | Title: `Square Body Suburban 4x4 (1973–91) Buyer's Guide` (48). Family title `Chevy K5 Blazer & Square Body Suburban Guide` (44). Add the FAQ "Is there a K5 Suburban?" The 4x4 Suburbans are K10/K20, later V1500/V2500, and the page already says so. | M | Search Console query. Wikipedia's K5 Blazer article and classified listings rank. The intent is mostly people looking up the name. |
| 25 | early bronco buyers guide | /models/bronco/early-bronco/ | Title: `Early Ford Bronco (1966–77) Buyer's Guide` (40). | M | Moderate: Velocity Restorations, LMR (for OBS), Broncozone and classicbroncos threads, and a podcast. Weak competition. |
| 26 | ineos grenadier problems / reliability | NEW: /models/grenadier/station-wagon/problems/ | Problems page + recalls (already in the data). | M | Moderate: vincheck, Carsguide, Edmunds consumer reviews, KBB recall news and fourwheelask. Thin, mostly reviews. |
| 27 | hummer h1 price / worth | /models/hummer/h1/ (an H2 "What a Hummer H1 is worth") → later NEW /price/ | Rename the "What they cost" H2 on every gen page to "{name} prices and values (checked {values.checked})". | M | Moderate: conceptcarz valuations for each year, The Classic Valuer, oldcarsdata (BaT data), Hagerty and spam PDFs. |
| 28 | boxy suv / boxy suvs | NEW: /best/boxy-suvs/ | Category hub listing every boxy SUV family with its years and price ranges, new ones included (Bronco, Defender, GX 550, 4Runner 6th gen, Grenadier, LC 250). | M | Strong but hard: Edmunds, Motor1, SlashGear (2), AutoGuide, Jalopnik and CarScoops. Long shot. Also covers "boxy suvs 2017" and "boxy jeep car" from Search Console. |
| 29 | 80 series biggest tire / 80 series 35s | NEW: /models/land-cruiser/80-series/tires/ | Tire page (the IH8MUD and Slee answers are already in the FAQ). | M | Not searched directly. Rated by analogy with #3 and #20 and the strong IH8MUD tire threads. |
| 30 | boxy trucks / box style trucks / boxy 4x4 | / (home) | Title: `BoxyTrucks: Buyer's Guides to Boxy 4x4s & SUVs` (46). See section 4. | L | Mismatched intent: "boxy trucks" returns commercial box trucks (Wikipedia "Box truck", TruckPaper listings). "best boxy 4x4 to buy used" returns UK "best used 4x4" lists. Weak demand for our meaning. |

## 2. Title and H1 templates for each page type

**Add one optional data field: `search_name`** on each generation entry in `data/<fam>.json`. Every template below starts from it and falls back to `mlabel(maker, page.title)`. It's needed because only about 40 of 107 current names fit a useful title under 60 characters. Suggested values for the families we already get impressions for:

`80 Series Land Cruiser`, `100 Series Land Cruiser`, `FJ Cruiser`, `5th Gen 4Runner` (likewise for 1st–6th), `W463 G-Wagon`, `G500 G-Wagon`, `G63 AMG`, `Jeep XJ` (Cherokee XJ), `Jeep JK`, `Jeep TJ`, `1st Gen K5 Blazer`, `Square Body K5 Blazer`, `Square Body Suburban`, `Hummer H1`, `Hummer H2`, `2nd Gen Isuzu Trooper`, `Range Rover P38`, `Land Rover LR3`, `Defender 90/110`, `Early Bronco`, `Bronco II`, `Lexus GX 470`, `Patrol Y61 (GU)`, `Montero 2nd Gen` (US) / `Pajero 2nd Gen`.

Other fields used: `{years}` = `g.years` shortened to `1990–97`. For an open range it becomes `2025–present` or is dropped. `{n}` = `len(buying_checks)`. `{family}` = `fam.name` (with "G-Wagon" for g-class and "Chevy" for chevrolet).

**Brand suffix rule:** add ` | BoxyTrucks` only when the result is 60 characters or less. Otherwise leave it off, because Google shows the site name separately. Put the truck name first in every title.

**Meta description template (all model pages):** `{search_name} ({years}): best years, problems to check, what they sell for ({values.ranges[1].range}), specs and tire sizes. Sourced from owners and specialists.` This replaces the cut-off verdict prose.

### 2.1 Generation guide — /models/{fam}/{gen}/
- Title: `{search_name} ({years}) Buyer's Guide`, plus ` & Problems` if it still fits (move to ` & Specs` once the /problems/ page exists, so the two pages don't compete).
- H1: `{mlabel} ({years}): buyer's guide, history and specs`
- Rename H2s: "What to check before you buy" → `{search_name} problems to check before you buy`. "What they cost" → `{search_name} prices and values`. "Wheels & tires" → `{search_name} tire sizes and the biggest tire that fits`.
- Examples:
  - `80 Series Land Cruiser (1990–97) Buyer's Guide` (46) / H1 `Toyota Land Cruiser 80 Series (1990–1997): buyer's guide, history and specs`
  - `Hummer H1 (1992–2006): Buyer's Guide, Prices & Problems` (55)
  - `1st Gen K5 Blazer & Jimmy (1969–72) Buyer's Guide` (49)

### 2.2 Family page — /models/{fam}/
- Title: `{maker short} {family}: Generations, Best Years & Problems`. If that's over 60, use `{family}: Every Generation & Best Years`.
- H1: `{maker} {family}`. It must include the make. Fix "Trooper", "Hummer", "Jeep" and "4Runner".
- Examples: `Isuzu Trooper: Generations, Best Years & Problems` (49) · `Toyota Land Cruiser: Generations, Best Years & Problems` (55) · `Mercedes G-Wagon: Generations, Best Years & Problems` (51)

### 2.3 Best-years page for a family — /models/{fam}/best-years/
- Title: `{family} Years to Avoid (and the Best Years to Buy)`, shortened to `(and the Best to Buy)` if needed.
- H1: `{maker} {family} years to avoid, and the best years to buy`
- Examples: `4Runner Years to Avoid (and the Best Years to Buy)` (50) · `G-Wagon Years to Avoid (and the Best Years to Buy)` (50) · `Land Cruiser Years to Avoid (and the Best to Buy)` (49)
- Jeep: `Jeep Years to Avoid: Wrangler, XJ, CJ, Grand Cherokee` (52). Then link prominently to the new pages for each generation.

### 2.4 Specs page — /models/{fam}/{gen}/specs/
- Title: `{search_name} Specs, Fluid Capacities & Oil Type`
- H1: keep the current `{mlabel} specs, fluids and service intervals`.
- Examples: `5th Gen 4Runner Specs, Fluid Capacities & Oil Type` (50) · `80 Series Specs, Fluid Capacities & Oil Type` (44) · `Jeep XJ Specs, Fluid Capacities & Oil Type` (42)

### 2.5 Comparison — /compare/{slug}/
- Title: `{A search_name} vs {B search_name}: Which to Buy?`. If too long, drop the shared family word from A ("Land Cruiser 80 vs 100 Series").
- H1: `{A} vs {B}: differences, best years and which to buy`
- Examples: `Land Cruiser 80 vs 100 Series: Which to Buy?` (44) · `Jeep JK vs JL: Differences & Which to Buy` (40) · `Defender vs Grenadier vs G-Wagon: Which to Buy?` (46)

### 2.6 Repair guide — /repairs/{fam}/{gen}/{slug}/
- Title: `{search_name} {repair.short or repair.title}: DIY Guide`, cut at a word boundary to 60 or less. The truck goes first. Today it comes last and the titles reach 110 characters.
- H1: `{repair.title} on the {mlabel}`
- Examples: `80 Series Birfield Rebuild: DIY Guide & Parts` (44) · `5th Gen 4Runner Transmission Drain and Fill: DIY Guide` (53) · `80 Series Heater Hose (PHH) Replacement: DIY Guide` (49)
- A `repair.short` field (optional, about 30 characters) would be needed for clean titles. Otherwise use the cut-down repair title.

### 2.7 Buyer's guide — /best/{slug}/
- Title: `Best Boxy 4x4s {qualifier}: {n} Picks with Best Years`
- Examples: `Best Boxy SUVs Under $15,000: 4x4s Worth Buying Used` (51) · `Best Boxy 4x4s for Overlanding: Picks & Best Years` (50) · `Best First 4x4: Boxy SUVs That Are Easy to Own` (45)

### 2.8 Engine swap — /engine-swaps/{slug}/ (demand not checked, so the template is only for length)
- Title: `{engine} Swap {target}: Kits, Cost & What It Takes`
- Examples: `Coyote Swap Early Bronco: Kits, Cost & What It Takes` (51) · `LS Swap Land Cruiser & Jeep: Kits, Costs, Guide` (47; check which trucks the page covers) · `Cummins 4BT & R2.8 Swaps: Kits, Costs & Fitment` (47)

### 2.9 Tools
- /tires/: `Biggest Tire Without a Lift: Every Boxy 4x4 Listed` (50)
- /which-4x4/: `Which 4x4 Should I Buy? 5-Question Boxy SUV Quiz` (48)

## 3. New page types to generate from data we already have

All five can be built in `build.py` from the fields named below. The counts are generations that have enough data, computed today from `data/`.

1. **Problems: /models/{fam}/{gen}/problems/** (106 of 107 have at least 5 buying checks and 5 repairs)
   - Title `{search_name} Problems: {n} Common Issues to Check`. Example: `80 Series Land Cruiser Problems: 8 Things to Check` (50).
   - Fields: `page.buying_checks[].head/body` (the list), `page.repairs[].title/symptoms/cost/diff/time` (cards that link to the /repairs/ pages), `extra.recalls.items`, `extra.timeline` rows with `flag=avoid|recall`, FAQ questions about problems. Add FAQPage schema.
   - Format to match: Unsealed 4x4's "common problems & solutions" list. Our version adds sourcing, costs, links to repair guides, and parts/affiliate links.

2. **Years to avoid for one generation: /models/{fam}/{gen}/years/** (76 have a years FAQ answer or buy/avoid flags; build only those)
   - Title `{search_name} Years to Avoid & Best Years to Buy`. Example: `4th Gen 4Runner Years to Avoid & Best Years to Buy` (50).
   - Fields: the years FAQ answer (`BEST_Q` regex already in build.py), `extra.timeline` (all rows as a table by year, with the buy/avoid/recall flags shown), `page.generations_table`, `extra.recalls`, `extra.values.ranges` and `page.searches` (AutoTempest/BaT links to the best years).
   - Format to match: rerev/carwhere/carscounsel pages for one model. Those pages are thin, and ours would be sourced.
   - The family best-years page becomes the hub that links to these.

3. **Tire fitment for one generation: /models/{fam}/{gen}/tires/** (99 have `fitment.max_tire`)
   - Title `{search_name} Biggest Tire Size: Stock & Lifted`. Example: `5th Gen 4Runner Biggest Tire Size: Stock & Lifted` (49).
   - Fields: `extra.fitment.stock`, `extra.fitment.wheel` (bolt pattern, center bore, lug thread/torque), `extra.fitment.max_tire[]` (lift → size → note), the tire FAQ answer (present on all 107), and `page.mods` where `cat` = SUSPENSION/WHEELS/TIRES (affiliate links). Link to `/tires/?t={fam}/{gen}`.
   - Format to match: trail4runner's per-gen "largest tire size" article.

4. **Price / value guide: /models/{fam}/{gen}/price/** (105 have `values`). Lower priority than 1–3.
   - Title `{search_name} Price Guide: What They Sell For ({values.checked year})`. Example: `Hummer H1 Price Guide: What They Sell For (2026)` (47).
   - Fields: `extra.values.checked/intro/ranges/note`, `page.searches[]` (AutoTempest/BaT links for each sub-range, which are affiliate or outbound), `extra.production.editions` (which editions sell for more), and timeline buy flags.
   - Demand checked only for the Hummer H1 (conceptcarz, Classic Valuer and oldcarsdata rank). Make these pages only if the values data is refreshed regularly, or they go stale.

5. **Category hub: /best/boxy-suvs/** (one page)
   - Title `Boxy SUVs: Every Boxy 4x4 You Can Buy, New & Used` (49).
   - Fields: each family's `name/maker/years/verdict`, each generation's `years`, and `values.ranges` for the price column. The current generations (Bronco sixth-gen, Defender L663, GX 550, 4Runner 6th gen, LC 250, Grenadier, Jimny JB74, Wrangler JL) answer "new boxy SUV". The quiz data (`data/quiz_axles.json`) supplies the solid-axle column.
   - This answers the "boxy suv(s)" category terms plus "boxy suvs 2017" and "boxy jeep car" from Search Console. Competition is strong (Edmunds, Motor1), so expect this to rank on long-tail terms first.

Don't build these from the current data: per-year pages ("2003 4runner problems"). RepairPal and CarComplaints own that format, and our data isn't organized by year.

## 4. Quick wins on the Search Console queries

| Query | Page now | Change |
|---|---|---|
| boxy truck(s), box style trucks | Home: title `BoxyTrucks — For the love of right angles`, H1 `For the love of right angles.` | The results for this query are for commercial **box trucks**, so the impressions won't convert. Don't chase it. Spend the home title on the category instead: `BoxyTrucks: Buyer's Guides to Boxy 4x4s & SUVs` (46). Keep the tagline as visual text, and make the H1 (or a visible H2 under it) `Boxy 4x4s and SUVs: buyer's guides, years to avoid, repairs`. Rewrite the meta to name the trucks people search: "Land Cruiser, 4Runner, G-Wagon, Defender, K5 Blazer, Bronco, Jeep XJ…". |
| k5 suburban | /models/chevrolet/ (title `Chevrolet K5 Blazer & Suburban — BoxyTrucks`, H1 `K5 Blazer & Suburban`) | Title `Chevy K5 Blazer & Square Body Suburban Guide` (44). H1 `Chevy K5 Blazer & Square Body Suburban`. Add the FAQ "Is there a K5 Suburban?": K5 is the Blazer code, the 4x4 Suburbans are K10/K20, later V1500/V2500, and the suburban-square page already states this. Retitle /models/chevrolet/suburban-square/ as `Square Body Suburban 4x4 (1973–91) Buyer's Guide` (the current title is 83 characters with the suffix). |
| isuzu trooper | /models/trooper/ (H1 `Trooper`) | H1 `Isuzu Trooper`. Title `Isuzu Trooper: Generations, Best Years & Problems`. Meta: "Isuzu Trooper (1981–2002), also sold as the Acura SLX, Opel Monterey and Holden Jackaroo: best years, problems, prices." Generation titles: `1st Gen Isuzu Trooper (1981–91) Buyer's Guide`, `2nd Gen Isuzu Trooper (1991–2002) Buyer's Guide`. trooper-2 has avoid flags, so it's a good first problems/years page. |
| gen 1 blazer | /models/chevrolet/k5-blazer-1st/ (title `Chevrolet K5 Blazer (1st generation) — BoxyTrucks`) | Title `1st Gen K5 Blazer & Jimmy (1969–72) Buyer's Guide`. H1 `First-gen Chevy K5 Blazer (1969–1972)`. Put "1st gen / gen 1 / '69–'72" in the first paragraph. Make the meta lead with the years, not the prose. |
| hummer h1 truck | /models/hummer/h1/ (title `AM General Hummer H1 — BoxyTrucks`) and /models/hummer/ (H1 `Hummer`) | Generation title `Hummer H1 (1992–2006): Buyer's Guide, Prices & Problems`. Add an H2 for body styles (the page already covers wagon, open top, 2- and 4-door pickup, slant-back), since "truck" in the query points to the pickup. Family H1 `Hummer H1 & H2`, title `Hummer H1 & H2: Generations, Best Years & Problems` (49). Retitle the best-years page `Hummer H1 & H2 Years to Avoid (and the Best to Buy)` (51), because the "h1 years to avoid" results are spam and Reddit. |

Other Search Console terms: "boxy suvs 2017" and "boxy jeep car" go to /best/boxy-suvs/ (section 3.5), which should also link to /models/jeep/cherokee-xj/.

## Unverified / limits

- **No volumes.** Every demand rating comes from the makeup of the search results, not from Keyword Planner or Search Console volume.
- **No autocomplete or "People also ask" data.** The WebSearch tool doesn't return them. Wording such as "years to avoid", "g wagon", "biggest tire … without lift" and "is the LX470 a Land Cruiser" is taken from the titles and URLs of ranking pages.
- **US-only results.** The Australian and UK angles (80/100 Series, P38, Patrol, Trooper as Jackaroo) are probably undercounted.
- Not searched: engine-swap queries, specs/fluid queries, repair queries (e.g. "80 series birfield rebuild"), the Defender/Discovery 1–2 years, the Patrol, Scout, Delica, Unimog, Pinzgauer and Niva. Their templates are based on title length only.
- Some result lists contained spam or hijacked domains. That's a sign of weak, easily manipulated competition, but it isn't a reliable read of where actual results rank.
- The new paths (`/years/`, `/problems/`, `/tires/`, `/price/`) are suggestions. I didn't check build.py's link checker or sitemap logic for conflicts.
