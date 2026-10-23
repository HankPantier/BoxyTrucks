# Fact-check report: Lexus group (GX 470, GX 460, GX 550, LX 450, LX 470, LX 570, LX 600)

**Files checked:** `data/lexus.json` (family object plus the GX 470 flagship page), `data/pages/lexus/{gx460,gx550,lx450,lx470,lx570,lx600}.json`, `data/extra/lexus/*.json` (7 files), and the 21 photos referenced in `photos`.

**Primary sources used to check claims:**
- Wikipedia wikitext for *Lexus GX*, *Lexus LX* and *Toyota Land Cruiser*.
- Lexus-hosted owner's manuals: GX 460 OM60G24U, LX 570 OM60P32U (a 2016-or-later edition) and LX 600 OM60V34U.
- The 2005 GX 470 factory repair manual (RM1164U, posted on GXOR).
- Lexus maintenance guides for the 2008 GX 470, 2016 GX 460, 2023 LX 600 and 2024 GX 550.
- Lexus Canada spec PDFs (2009 GX 470, 2002 LX 470).
- NHTSA's recalls API (by vehicle and by campaign) and the 25V-767 Part 573 report and dealer letter.
- fueleconomy.gov, Lexus Pressroom, Expedition Portal, CarSpec, IH8MUD, Slee Off-Road, AMSOIL, Auto123, KBB and Cars.com.

**Link check:** I curled all 489 unique URLs in these files.
- **423 returned 200.**
- **54 returned 403**, all from bot-blocking sites with real URL formats: NHTSA recall pages, ClubLexus, AMSOIL, wheel-size.com, Expedition Portal, Cars.com, Motor1, Engine Builder, Gear Patrol, Autosphere, Pexels and Low Range Off-Road. I opened several through WebFetch to confirm their content.
- **12 timed out.** All were RockAuto, and all returned 200 on retry.
- I pulled page titles for 345 non-RockAuto URLs and 12 sampled RockAuto URLs to confirm each points to the right vehicle and part. Two product links pointed to the wrong part (fixed below). No olathetoyotaparts.com links were found.

**Cross-links:** All `[[family/slug|…]]` links and `related` entries resolve to real generations.

**Recalls:** Every recall in the detail files matches NHTSA's campaign records, both the campaign number and the model years.

---

## Family object (`data/lexus.json` → `family`)

**Corrections made**
- LX 450 summary said "215-hp". Changed to **212 hp**, the period spec (Auto123 1997 LX 450 spec sheet: 212 hp @ 4,600 rpm). The LX 450 page already used 212 hp, so the family summary contradicted it. Wikipedia gives 215 hp.

**Verified:** years, chassis codes, the 409-hp V35A-FTS, the 349-hp GX 550, the 301-hp GX 460, the 2010 Consumer Reports episode, the forum URLs, the AutoTempest and BaT URLs (titles checked), and the hero photo.

**Still unverified / shortcomings**
- **Low:** The GX generations all point to the same BaT page (`/lexus/gx/`). That page is real, but it isn't specific to each generation.

---

## GX 470 (flagship, `data/lexus.json` → `page`, `data/extra/lexus/gx470.json`)

**Corrections made**
- **Rear suspension:** The page called it a "five-link solid rear axle" in the story lead, the engineering intro, the engineering cell and the plate. Lexus Canada's 2009 GX 470 spec sheet calls it a **4-link**. I changed all four to "four-link solid rear axle with a lateral rod" / "4-link".
- **Wheelbase:** The plate said "109 in". Changed to **109.8 in (2,790 mm)**, per Lexus Canada and Wikipedia. The capability table already said 109.8. The "109-inch" in the story is a correct direct quote from Expedition Portal, so it stays.
- **Fluid FAQ:** The FAQ (oil "6.6 qt", rear diff "6.6 pints") disagreed with the baseline-service table. I rewrote it from the 2005 factory repair manual:
  - Oil: 5W-30, 6.5 qt (6.2 L) with filter.
  - ATF WS: 3.2 qt drain-and-fill, 11.0 qt dry.
  - Transfer case: 1.5 qt, GL-5 75W-90.
  - Diffs: front 1.48 qt and rear 3.22 qt, GL-5 SAE 90.
  - Coolant: 13.6 qt.
  - The FAQ source label is now the repair manual.
- **Lug torque** (detail file): 83 → **82 lb-ft (112 N·m)**, per the 2005 repair manual's wheel nut spec.
- **Expedition Portal callout:** I re-read the article.
  - Removed "with the tires touching the fenders", which isn't in the article. It now says the truck couldn't be driven out and needed a tow.
  - Changed "voids the warranty" to "may void ARB's warranty", which is how the editor's note words it.

**Removed or softened**
- "Cracked driver's-side exhaust manifolds" became "cracked exhaust manifolds (often the driver's side)" in the story, the buying check and the repair title. CarSpec's example was a driver's-side crack on a Sequoia, but it doesn't say the driver's side is the rule.

**Added**
- Lexus Canada 2009 GX 470 spec PDF added to page sources.

**Verified (no change needed)**
- Launch and sales: NAIAS January 2002 debut, sales from November 2002.
- Output: 235 hp/320 lb-ft, then 270 hp (2005 VVT-i), then 263 hp (2006 SAE restatement).
- Towing: 5,000 lb, then 6,500 lb from mid-2004.
- 2004 changes: sealed transmission, TPMS and curtain airbags. KDSS arrived late in the 2004 model year. The Sport model came in 2005.
- Awards: Four Wheeler of the Year 2003/2004.
- US sales: 35,420 in 2004 and 6,235 in 2009. The 2002–09 total sums to 174,473 (≈174,500).
- Expedition Portal quotes: "pinnacle", "most reliable engines", Air Lift 52420, BP-51, Warn Zeon 10-S, 255/80R17, built on the same Tahara line.
- Every baseline-service figure, checked against the RM1164U and the 2008 Lexus schedule:
  - Intervals: 90k-mile/108-month timing belt, 120k-mile plugs (Denso SK20R11, gap 1.0–1.1 mm).
  - Capacities: ATF 3.2/11.0 qt, transfer case 1.5 qt, diffs 1.48/3.22 qt, PS fluid Dexron II/III 1.0 qt, coolant 13.6 qt.
- Lexus Canada capability figures: 31°/25° angles, 8.3 in clearance, 4,740 lb curb weight, 6,150 lb GVWR, 87 L tank, 38.4 ft turning circle.
- EPA: 14/18/15 mpg (2007).
- Recalls 03V-031, 03V-088, 09V-234 and 16V-065: years confirmed on NHTSA.

**Still unverified / shortcomings**
- **Med:** All three photos are street or parking shots: a driveway, a kerb and a car park. They show the correct generation and match their captions and alt text, but they break the brief's off-road-only rule. Four off-road Prado 120 photos (`prado120-*.jpg`) sit unused in `site/img/lexus/`. Commit 0644921 deliberately switched to Lexus-badged photos only, and those files have no credit data, so I didn't reinstate them.
- **Med:** The front differential support part number 52380-60021 (stamped 52391-60021), and the claim that the early support "can fail catastrophically", come only from GXOR. A human should confirm them against Toyota EPC or a TSB.
- **Med:** CruiserTeq's oil filter link is titled "Fits 3/1969–5/2005 … 2UZ". Its fit on 2005½–2009 VVT-i trucks should be confirmed. The exhaust manifold gasket link already carries a "confirm for VVT-i trucks" note.
- **Low:** I couldn't open the ClubLexus repair-cost quotes ($950–1,770 timing belt, $1,900 rack) because the site returns 403. They are presented as owner reports.
- **Low:** The Expedition Portal forum `goto/post` links resolve to a bot-challenge page, so I couldn't check what they say.

---

## GX 460 (`data/pages/lexus/gx460.json`, `data/extra/lexus/gx460.json`)

**Corrections made**
- **Fuel-economy FAQ:** It said "Wikipedia lists the EPA estimate at 17 mpg combined", but Wikipedia says no such thing. Replaced with fueleconomy.gov: **15/20/17 (2010)** and **15/19/16 (2023)**, premium fuel.
- **Turning circle:** The page and detail file said it "grows from 38.1 to 41.4 ft" for 2014. The only source for 41.4 ft is a ClubLexus thread, and **KBB's 2014 GX specs list 38.1 ft**. I removed it as a buy/avoid factor in the generations table, the FAQ and the timeline. The plate and capability table now say "38.1 ft (some spec sheets list 41.4 ft for '14+)". Both sources were added.
- **YouTube:** The C4 Fabrication link pointed to `@C4Fabrication`, a different channel from the one c4fabrication.com links to. Changed to the official **`@c4_fabrication`**.

**Removed or softened**
- The secondary air pump coverage "for 10 years from first service" couldn't be verified. It now says Lexus extended coverage (program ZLH) and tells the reader to confirm the terms with a dealer. CarSpec confirms the extended warranty but not its length.

**Added**
- Recall **16V-340** (2010–2011 Takata passenger inflator, zone-based) added to the detail file, verified on NHTSA.
- Sources added: fueleconomy.gov (2010 and 2023), ClubLexus turning-radius thread, KBB 2014 specs.

**Verified:**
- Every baseline-service figure, checked against owner's manual OM60G24U:
  - Oil: 0W-20, 8.2 qt with filter.
  - Coolant: 16.3/14.5 qt.
  - Plugs: Denso SK20HR11, gap 1.1 mm.
  - Diffs: LT 75W-85, front 1.48 qt and rear 2.85 qt.
  - ATF WS: 11.6/11.8 qt.
  - Lug torque: 83 lb-ft.
- The Consumer Reports timeline (April 13 → 16 → 19 → 29 → May 7).
- Torsen split: 40:60, 30:70 and 50:50.
- GX 400: 271 hp.
- Sales: 32,509 in 2021 and 31,910 in 2023. The 2010–23 total sums to about 325,600 ("300,000+").
- The $4,750 price cut in 2014.
- Recalls 10V-159, 19V-005, 19V-741, 20V-012, 20V-682 and 17V-831.

**Still unverified / shortcomings**
- **Med:** The owner-reported repair prices (timing cover $2,600–3,500; transmission $7–8k) come from ClubLexus and IH8MUD threads that I couldn't fully read.
- **Med:** Photos: two are street or driveway shots and one is a show stand. Only the snow photo is outdoors and off pavement. All show the correct generation and match their captions.
- **Low:** I didn't decode the VIN pattern "JTJ…7FX" against a real VIN.
- **Low:** Wikipedia's sales table gives an identical 28,519 for both 2020 and 2022, which looks like a copy error. The page doesn't use either year's figure.

---

## GX 550 (`data/pages/lexus/gx550.json`, `data/extra/lexus/gx550.json`)

**Corrections made**
- **Engine recall 25V-767:** The story, the repair and the FAQ said the remedy was "still being developed". NHTSA's campaign record now gives the remedy: **dealers inspect the No. 1 main bearing using inspection software and drive data, replace the engine if necessary, and mailed owner letters on August 28, 2026**. All three were updated, and the NHTSA record was added as a source. The 3,717-GX population, the 126,691 total and the build dates (May 31, 2023 – April 10, 2024) are confirmed from the Part 573 report.
- **Sales line:** "30,914 in 2024 and 37,180 in 2025, more than any year of the GX 460" was wrong for 2024, because 30,914 is below the GX 460's 32,509. It now reads "…the best year the GX has ever had in the US".
- **YouTube:** C4 Fabrication changed to the official `@c4_fabrication`, as on the GX 460.

**Verified:**
- From Lexus Pressroom: the June 8, 2023 reveal, the 50:50 Torsen center diff, 26°/24°/21° angles, MTS modes, five-speed Crawl Control, E-KDSS, the Overtrail rear locker, Tahara assembly, the 4.52 in/3.74 in width increases and the hybrid-later statement.
- Specs: 349 hp/479 lb-ft and an EPA rating of 15/21/17 (fueleconomy.gov, 2025).
- Towing: 8,000 lb at launch (the December 2023 pricing release), and 7,601 lb for the Luxury+ (Cars.com 2026 specs, source added).
- Seating: seven seats on the non-Overtrail grades.
- Recalls 25V-744, 26V-341 and 26V-179.

**Still unverified / shortcomings**
- **High (thin content):** Only **2 repairs** against the 6–8 target, plus 4 mods and 6 buying checks. I added no repairs, because sourced DIY content for a two-year-old truck is still scarce.
- **Med:** Six baseline-service items still carry `[CONFIRM IN MANUAL]`: oil capacity, plug type, ATF, transfer case, diffs and brake fluid. I couldn't find the GX 550 owner's manual on Lexus's server. The spark-plug interval (40k miles) is marked with footnote "2" in the 2024 schedule, and I couldn't extract that footnote's conditions.
- **Med:** The 2027 towing figures of 9,063 lb (Premium), 9,041 lb (Premium+) and 7,844 lb (Luxury) aren't independently confirmed. The 9,063 and 9,096 lb figures appear in the current pressroom release.
- **Med:** All three photos are street or car-park shots of the correct model.

---

## LX 450 (`data/pages/lexus/lx450.json`, `data/extra/lexus/lx450.json`)

**Corrections made**
- Baseline service: replaced the `[CONFIRM]` placeholders.
  - ATF: **Dexron III-type ATF** (AMSOIL lists AF3 for the A343F).
  - Brake fluid: **DOT 3** (AMSOIL).
- A mod supplier was labelled "Cruiser Outfitters / CruiserTeq", but they're separate businesses. Renamed to "CruiserTeq".

**Verified:**
- From Wikipedia:
  - Production November 1995 – December 1997 and the US launch in January 1996.
  - The $47,995 / $40,678 / $46,968 pricing.
  - Sales of 5,000+ and 9,000+.
  - The tariff backstory and J.D. Power result.
  - The three factory options.
- From the ClubLexus article (fetched): the "everything a Lexus is" ad line and the Range Rover/Discovery positioning.
- From the AMSOIL lookup (fetched): all fluid capacities (7.8 qt oil, 11.6 qt ATF, 3.6 pt transfer case, 5.5/5.9 pt front, 7 pt rear, 14.8/15.9 qt coolant).
- From Auto123: 212 hp, 2,255 kg, 2,268 kg towing, 95 L and P275/70R16.
- The knuckle torque and preload figures (43 ft-lb, 3 ft-lb, 47 ft-lb, 6–12 lb, 26 ft-lb, 90 ft-lb), from the IH8MUD birf-repack page.
- EPA: 12/14/13.
- Photos: `lx450-dirt-mound.jpg` looks like a 100 Series at first glance, but on inspection it is an 80-body LX 450, so the caption is correct.

**Still unverified / shortcomings**
- **Med:** Four `[CONFIRM]` markers remain: the oil interval, plug gap, coolant interval and fuel filter/PCV interval.
- **Low:** The 4.11 axle ratio and the "viscous-coupled center diff" come from Slee and forum sources, not a Toyota document.
- **Low:** One photo is a street shot.

---

## LX 470 (`data/pages/lexus/lx470.json`, `data/extra/lexus/lx470.json`)

**Corrections made**
- **Wrong part link:** The baseline "Serpentine drive belt, UZJ100/LX470" went to a Cruiser Corps page that sells a **200 Series/LX 570 belt**, despite its URL slug. Replaced with RockAuto's 2005 LX 470 belt catalog (title verified).
- **Spark plug torque:** "Toyota's spec is 13 ft-lb" was half right. The Toyota 2UZ-FE repair manual lists **13 ft-lb (17.5 N·m) in the engine section and 15 ft-lb (20 N·m) in the ignition section**. The repair and the baseline item now give both.
- **Spark plugs:** The baseline spec gave part "90080-91180", which I couldn't verify. Replaced with the repair-manual plugs (Denso SK20R11 / NGK IFR6A11, gap 1.0–1.1 mm).
- **Instagram:** Dropped `@cruiseroutfitters`. The Cruiser Outfitters site links no Instagram account, and I couldn't confirm the handle exists.

**Added**
- Sources: Auto123 "LX 470 gets power boost for 2006" (275 hp/332 lb-ft) and the 2UZ-FE repair manual.

**Verified:**
- History: the LA show debut in December 1997, sales from Q2 1998, and output of 230 hp, then 235 hp (2003), then 275 hp (2006, Auto123). The 2007 Limited Edition ×400.
- Hardware: the 2000 changes to the 4-pinion front diff, VSC and A-TRAC; the 2003 A750F and VGRS; the 2004 sealed transmission and WS fluid; the 9.5-in rear and HF2A with no viscous coupler. All per Slee's 100 Series guide.
- Lexus Canada 2002 specs: 30°/23° (normal) and 32°/27° (high) angles, 8.66 in clearance, 5,401 lb, 6,856 lb GVWR, 96 L and 39.7 ft.
- Recall 10V-346: 39,159 trucks, July 2010.
- Recalls 04V-434, 16V-065 and 17V-548.
- Sales total: 68,940.

**Still unverified / shortcomings**
- **Med:** For 2006–07 output, Wikipedia's infobox says 268 hp while Auto123 and Wikipedia's body text say 275 hp. The page keeps 275 hp. A Lexus spec sheet would settle it.
- **Med:** Six `[CONFIRM]` markers remain: oil grade and interval, A343F ATF type, brake fluid, fuel filter/PCV interval and the 1998–99 rear LSD.
- **Med:** The timing-belt part number 13568-09070 and the serpentine belt 90916-02586 come only from an IH8MUD 90k list.
- **Low:** Photos: a parking-lot build, a sand shot and a verge shot. All are LX 470s.

---

## LX 570 (`data/pages/lexus/lx570.json`, `data/extra/lexus/lx570.json`)

**Corrections made**
- **Towing (High):** The page said "8,500 lb" across the story, plate, FAQ and detail file. The Lexus-hosted 2016-on owner's manual (OM60P32U) lists **7,000 lb with trailer brakes** for the facelifted truck. All four now give 8,500 lb at launch and 7,000 lb for 2016+.
- **Baseline service, filled in from owner's manual OM60P32U** (noted as a 2016+ edition):
  - Oil: 0W-20 GF-5, 7.9 qt.
  - Coolant: SLLC, 17.1 qt.
  - Plugs: Denso SK20HR11, 1.1 mm.
  - ATF: WS, 10.7 qt.
  - Transfer case: LF 75W, 1.53 qt.
  - Diffs: LT 75W-85, front 2.01 qt and rear 4.44 qt.
  - Brake fluid: DOT 3.
  - AHC fluid type.
  - These replace five `[CONFIRM IN MANUAL]` markers.
- **Wrong part link:** The CruiserTeq radiator link's URL says URJ200, but the page is titled "Fits 08/1992–12/1997 FZJ80 & LX540" and mixes the two SKUs. Removed. The RockAuto LX 570 radiator catalog link stays.
- **Instagram:** Dropped `@crossroadsoverland`. I couldn't confirm the account exists. `@budbuilt` and `@sleeoffroad` are confirmed by links on the companies' own sites.

**Verified:**
- From Wikipedia: the April 4, 2007 NYIAS debut; 383 hp/403 lb-ft; the AB60F and AE80F; ±3/2 in AHC; 102 mm longer; 9 in front travel; the 240,000 test km; 450 hp/521 lb-ft supercharged and LX 450d figures; production ending in October 2021.
- The Car and Driver "most desirable SUV" quote and the 6.7-second 0–60 time, from the ClubLexus article (fetched).
- EPA: 12/18/14 (2008) and 12/16/14 (2020).
- Sales total: ≈65,500.
- Recalls 18V-887, 17V-548, 11V-113, 20V-012 and 20V-682.
- Lug torque 97 lb-ft and the 285/50R20 and 275/50R21 tire sizes, from the manual.

**Still unverified / shortcomings**
- **Med:** Fluid capacities come from a 2016+ manual. Confirm 2008–2015 figures, especially ATF (AB60F vs AE80F).
- **Med:** The oil-change interval is still `[CONFIRM IN MANUAL]`. I had no LX 570 maintenance schedule.
- **Low:** Photos are all LX 570s: red dirt, a mountain pass and snow.

---

## LX 600 (`data/pages/lexus/lx600.json`, `data/extra/lexus/lx600.json`)

**Corrections made**
- **Engine recall 25V-767:** Updated the story, repair and FAQ with NHTSA's current remedy, as on the GX 550: a No. 1 main-bearing inspection, engine replacement if needed, and owner letters on August 28, 2026.
- **EPA:** The page attributed 17/22/19 to "2027". Confirmed on fueleconomy.gov for the **2025** LX 600, so the label and FAQ source now say 2025. The 2027 grade list (Premium, F Sport Handling, Luxury) is confirmed by KBB.
- **Plate:** The duplicate "weight vs LX 570" row (already in the engineering cells) became **TOWING 8,000 lb**.

**Added**
- FAQ "How much can it tow?": 8,000 lb braked and 1,650 lb unbraked, from owner's manual OM60V34U. KBB gives the same 8,000 lb for 2027.
- Towing row added to the detail file's capability table.
- Sources added: fueleconomy.gov, KBB 2027, the NHTSA record and the manual.

**Verified:**
- From Lexus Pressroom: 441 lb lighter, 20% more rigid, 100/145 mm travel, +20 mm rear rebound, Normal/Hi1/Hi2/Low heights, 45° climb and 44° stable inclination, 700 mm wading, five grades, the F Sport Torsen rear, 500,000+ LXs and 50+ countries.
- Recall 24V-381: 102,092 total and 3,524 LXs built July 30, 2021 – November 25, 2022 (Motor1 and NHTSA).
- Recall 25V-767: 9,895 LXs plus 10 service-engine trucks (Part 573 and the dealer letter).
- Every baseline-service figure, checked against OM60V34U:
  - Oil: 0W-20 GF-6A, 7.7 qt.
  - Coolant: 15.5 + 4.0 qt.
  - Plugs: Denso EC22HPR-D7, 0.7 mm.
  - ATF WS: 12.13 qt.
  - Transfer case: 1.89 qt.
  - Diffs: front 1.23 qt; rear 5.76 qt, or 5.55 qt LX-type oil with the LSD.
  - Brake fluid: DOT 3/4.
- LX 700h: 457 hp and 583 lb-ft. The Overtrail reveal date was October 10, 2024.
- Recalls 24V-125, 26V-180, 26V-094, 25V-744 and 22V-239.

**Still unverified / shortcomings**
- **Med (thin content):** 5 repairs and 4 mods, against the 6–8 and 5–7 targets.
- **Med:** The 25°/23°/20° angles come from Yahoo Autos. The pressroom release only says they match the previous model.
- **Low:** Photos: a dealer lot, a show stand and an event tent. None is off-road.

---

## Top 5 remaining problems for the Lexus group

1. **GX 550 content is thin.** It has 2 repairs (target 6–8) and 4 mods, and six baseline fluid specs still read `[CONFIRM IN MANUAL]` because the GX 550 owner's manual wasn't on Lexus's server. An owner could pick the wrong transfer-case or diff oil. (High)
2. **LX 570 capacities come from a 2016+ manual.** Earlier trucks (2008–2015, AB60F six-speed) may differ, and the oil-change interval is still unconfirmed. Someone should check a 2008–2015 manual. (Med–High)
3. **Off-road photo rule.** About two-thirds of the Lexus photos are street, car-park or show-stand shots, including all of the GX 470, GX 550 and LX 600 photos. The generations are correct, but these pages break the brief's off-road-only photo rule. (Med)
4. **Part numbers resting only on forum or GXOR posts.** These are the GX 470 front-diff support 52380-60021, the LX 470 timing belt 13568-09070 and serpentine belt 90916-02586, and the fit of the CruiserTeq 2UZ oil filter on 2005½–2009 VVT-i GX 470s. They should be checked against Toyota EPC. (Med)
5. **LX 470 2006–07 output (275 vs 268 hp)** and the **GX 550's 2027 Premium and Luxury towing figures** need a Lexus spec sheet to settle them. (Low–Med)
