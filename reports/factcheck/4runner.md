# Fact-check report — group `4runner`

Scope: `data/4runner.json` (family object + 3rd gen flagship page), `data/pages/4runner/{1st,2nd,4th,5th,6th}-gen.json`, and all six `data/extra/4runner/*.json` files. I opened all 17 referenced photos.

Method: I checked all 461 unique URLs with curl (bot UA first, then `Mozilla/5.0` on failures). I pulled every recall ID from the NHTSA recalls API (1988–2026 model years). I read the Toyota-Club owner's-manual capacity tables (180u/210u/280u/500u), the Wikipedia 4Runner article (text, infoboxes and sales table) and the Wikipedia UZ, VZ and KDSS articles. I also read the CarComplaints V06 dealer packet, both Hagerty articles, The Autopian, the Car and Driver history (AOL), the C&D 2022 TRD Pro test, the C&D 2025/2026 first drive, test and buyer's-guide pages, the MotorWeek/JNC 1996 review, The Auto Channel 2002 spec sheet, the AdventureTaco LBJ, timing-belt, axle-bearing and rack-bushing guides, the Trail4R driveline-fluid and torque-spec pages, the 4Runner6G wheel-spec, torque-list and brake-TSB threads, and the ShockWarehouse X-REAS kit listing. I checked every ToyotaPartsDeal part number against the part description on its page (all 48 match a real part of the stated type), and checked page titles for all LC Engineering and Total Chaos links.

Cross-links: every `[[family/slug|…]]` and every `related` entry in all six pages resolves to a real generation. The **family object** (intro, verdict, years, generations, summaries, forums) checked out against Wikipedia, and I made no changes to it.

---

## 3rd Gen (flagship, `data/4runner.json` → `page`; `data/extra/4runner/3rd-gen.json`)

**Corrections made**
- **2001–02 drivetrain:** the page said "push-button Multi-Mode". Changed to: "Multi-Mode (with lockable centre diff) standard on 4WD, VSC standard, plus brake-based traction control". The edit covers the story, the engineering 4WD cell and the generations table. Source: Wikipedia; HotCars says the centre-diff locker came with traction control from 2001.
- **Manual gearbox:** the story implied it was dropped for 2001. It was actually dropped for 2000 (Wikipedia). I fixed the story, the 3RZ generations-table row ("dropped for 2000") and the plate ("5-spd manual (to 1999)").
- **Facelift paragraph:** removed the unsourced forum claims (the cupholders and the "'99 sits an inch taller"). Replaced them with Wikipedia's 1999 changes: fat-lip bumper and crush zone, multi-parabola lamps, digital-odometer cluster, and colour-keyed Limited/Highlander (later Sport Edition) trim.
- **Land Cruiser locker:** the page said Toyota had been "fitting electric lockers for years". Changed to "offered on the US Land Cruiser since 1993" (Wikipedia).
- **Replacement date:** the page said "replaced it in August 2002". Changed to: production ended in August 2002 and the 4th gen reached showrooms in October 2002 (Wikipedia).
- **Ball-joint campaign:** "Special Service Campaign 50J" is actually **safety recall 50J = NHTSA 05V-225** (NHTSA API). Fixed in the buying check and the source name.
- **"Safety Recall 20A for rear springs and bump stops"** is NHTSA **02V-021 (Toyota SSC 20A)**, under which dealers replaced rear suspension parts on 1996–98 trucks. I rewrote the check accordingly and added the NHTSA API URLs to the sources.
- **Plate curb weight:** the plate said 4,245 lb; Wikipedia and the extra file say 3,616–3,902 lb. The plate now shows the Wikipedia range and notes the Auto Channel figure. The Auto Channel 4,245 lb is confirmed, but it is an outlier.
- **Hilux Surf row:** added the intercooled 1KZ-TE (≈140 hp from July 1996), per Wikipedia.
- **Extra file, production:** "best-selling 4Runner until the 4th gen" was wrong; the 4th gen never outsold it. Changed to: the 1997 total of 128,496 stood as the record until 2018 (5th gen). Source: Wikipedia sales table.
- **Extra file, sales note:** the 2002 calendar-year figure includes early 4th gen sales; I added a note saying so.

**Removed or softened**
- "Owners grumble about the early VSC and the late automatic" became "some owners prefer the simpler earlier drivetrain".
- Lug torque (81 lb-ft / 110 N·m, Limitless Tire aggregator) now carries `[CONFIRM IN MANUAL]`.

**Verified unchanged:** 150 hp/177 lb-ft and 183 hp/217 lb-ft; the 105.3 in wheelbase; towing 3,500→5,000 lb; MotorWeek's prices ($19,908 / $25,568), 0–60 in 9.5 s and EPA 17/19; Auto Channel's 2002 figures (16/19/17, 18.5 gal, 183.3 in); all Toyota-Club capacities; the E-locker years (1996–2000); every AdventureTaco part number and torque (LBJ 43340-39465 / 43330-39585, bolts 37/59 ft-lb, castle nuts 103/67, crank bolt 217 ft-lb, rack 123/123/141, axle-bearing numbers, backing-plate nuts 48 ft-lb); and the sales figures.

**Added:** two NHTSA API sources (1997 and 2001).

**Still unverified / shortcomings**
- **Med:** the spark plug spec (Denso K16TR11, 1.1 mm gap) rests only on the Toyota-Club plug table. Confirm it in the manual.
- **Med:** engine-oil viscosity is still marked `[CONFIRM IN MANUAL]`.
- **Low:** Wikipedia's "2.3 in longer wheelbase" is internally inconsistent: its infoboxes give 103.3 → 105.3 in, which is 2.0 in. It is quoted with attribution.
- **Low:** the Yahoo Autos, HotCars, JNC and Auto Channel URLs fail with curl (404 or 000) but render through WebFetch. They are probably geo- or bot-blocked; recheck from a browser.
- **Low:** all `toyota-4runner.org` thread URLs return 403 to bots. That looks like Cloudflare, and the URL format is real, but I couldn't read the threads, so the forum-attributed claims (locker on Base/SR5/Limited, the 265/75R16 consensus, rust spots) are unverified by me.
- **Low:** ovrmag.com returns 405 to curl.
- Photos: all 4 are 3rd gens and off-road; captions match.

---

## 1st Gen (`data/pages/4runner/1st-gen.json`; `data/extra/4runner/1st-gen.json`)

**Corrections made**
- Removed a Car and Driver quote ("smaller, more civilized, more comfortable, but still rugged") that doesn't appear in the cited C&D/AOL article.
- **3VZ-E output:** the page said "145 hp rising to 150 hp for 1989" without a source. Changed to "145–150 hp depending on the source" (Wikipedia VZ article; Hagerty quotes 150).
- **Head-gasket buying check:** clarified that the 1996 policy adjustment covered 1988–94 V6 trucks and that V06 only covered 1/90–10/94 builds, so 1988–89 1st gens fall outside V06 (CarComplaints V06 packet).
- **Fuel-economy FAQ:** Trail4R's 19/23 mpg has no EPA backing. The answer now leads with Wikipedia's EPA 17 mpg city for the 22R-TE turbo and 14.5 mpg observed in period testing.
- **Hagerty lead claim:** "had to add to its price guide" became "says can't be ignored" (that is Hagerty's own headline).
- **1989 sales:** the 36,927 figure is calendar 1989, which includes the first 2nd gens. Noted on the plate, in the story and in the extra file.
- **LCE 3VZ water pump:** LCE titles it 1989–92, but the page said 1988–92. The part name now says to confirm fit on 1988 trucks.

**Removed or softened**
- **Sunroof drains:** "Blocked factory sunroof drains have rusted out A-pillars on these trucks" is now an owner report, limited to sunroof-equipped trucks. I found no source confirming a factory sunroof on N60 4Runners, and the IH8MUD buying guide doesn't mention it.

**Verified unchanged:** the Hagerty details (14-bolt roof, roll bar, retracting rear glass, altimeter/inclinometer, no rear shoulder belts, "months to weeks to about 12 seconds", values $8,400/$13,700/$21,100, BaT $19,250/$17,500, the preference for the 22R-E over the V6, no reproduction seats or floors); the Wikipedia history (May 1984 launch, 96→116 hp, 22R-TE 135 hp 1986–87, IFS and +3 in track for 1986, 1988 V6, no US diesel); the Trekker numbers (≈1,200–1,500); NHTSA 88V-019 and 05V-389; the Autopian quote; and the sales figures.

**Still unverified / shortcomings**
- **High:** the baseline service section has no sourced fluid capacities or grades. They are correctly marked `[CONFIRM IN MANUAL]`; a human should add owner's-manual figures.
- **Med:** the sunroof-drain repair card is weakly sourced. Consider replacing it with a sourced job such as front wheel-bearing repack or hub service.
- **Med:** only 2 photos. The Rogue campsite shot is on a paved campground loop, which is borderline for the off-road rule.
- **Low:** the Hagerty, Curbside Classic and Expedition Portal URLs return 403 to bots; the Hagerty pages are confirmed readable via WebFetch.
- **Low:** the extra file has no `docs` section.

---

## 2nd Gen (`data/pages/4runner/2nd-gen.json`; `data/extra/4runner/2nd-gen.json`)

**Corrections made**
- **Sales in the lead:** "more than 75,000 a year by the end of the run" relied on calendar 1995, which includes early 3rd gens. Changed to "passed 74,000 in calendar 1994". The plate peak is now annotated, and the extra-file sales note explains the calendar-year overlap.
- **1KZ-TE torque:** "213 lb-ft" was unsourced and is removed. The output is now "≈130 hp" (Wikipedia).
- **V06 door-hinge label:** this claim comes only from a forum thread (403, unread) and is now attributed as a forum report in both the buying check and the FAQ.

**Verified unchanged:** the V06 scope (1/90–10/94 builds, the October 1996 policy adjustment on 1988–94 trucks, expiry 24 September 2018); C&D's "four-door was the volume seller" and 0–60 in 15.7 s; the Wikipedia facts (two-door to May 1993, US two-door sales ended August 1992, chicken tax, 4-link plus Panhard, chain case on V6 and gear case on I4, rear ABS on SR5 V6, door beams for 1994–95, 1–2 star frontal rating, EPA 15 city); Zhuhai, China assembly (Wikipedia infobox); curb weight 3,760 lb; towing 3,500 lb; LCE prices (OME coils $240.42, guides $64.09, MLS set $115.90); and NHTSA 05V-389.

**Removed:** the `@toyteclifts` Instagram handle, which I couldn't confirm exists.

**Still unverified / shortcomings**
- **High:** baseline fluids are all `[CONFIRM IN MANUAL]` with no sourced capacities.
- **Low:** the 22R-E torque is 139 lb-ft here but 140 lb-ft on the 1st gen plate, and neither figure is sourced. A human should pick one from a Toyota spec sheet.
- **Low:** the 2nd gen claim that ADD with locked hubs was used rests on a 4Runners.com thread.
- **Photos (all 4 checked):** Asiago and Veneto show the same 1992–95 facelift N130 (rectangular modular headlamps); it is fine, but could be a Euro 4Runner or Hilux Surf.
  - **Low:** the "Irkutsk" caption doesn't match the Russian plate's region code 25 (Primorsky Krai). Consider "Russia".
  - **Low:** the Ashford meadow truck has a "FOR SALE" sign in the window.

---

## 4th Gen (`data/pages/4runner/4th-gen.json`; `data/extra/4runner/4th-gen.json`)

**Corrections made**
- **VVT-i V8 output:** this is quoted variously. Wikipedia's 4Runner article says 268 hp/315 lb-ft, its UZ article says 271/315, and the C&D history says 270 hp. Changed to "≈270 hp / 315 lb-ft" with the discrepancy explained in the story. Updated in the story, engineering, generations table, plate, FAQ and extra timeline.
- **"Sibling of the LC100's engine":** changed to "the same engine family". It is the same 2UZ-FE.
- **Gear oil grade (High):** the diff/transfer-case repair and FAQ said 75W-90 everywhere. Toyota-Club's owner's-manual table says GL-5 75W-90 for the front diff and transfer case but **80W-90 for the rear**. The repair, its tools line and the FAQ now give the manual grades and Toyota-Club capacities (front 1.5 L V6 / 1.4 L V8, transfer case 1.4 L, rear 3.05 L).
- Lug torque (Limitless Tire, 110 N·m) is now marked `[CONFIRM IN MANUAL]`.

**Verified unchanged:** C&D's "biggest, heaviest, most luxurious… most powerful" and 0–60 in 7.2 s for a 2005 V8; launch in October 2002 and production August 2002 to August 2009; V6 245/282; V8 235/320; the 4AT/5AT split; full-time V8 and Multi-Mode V6; X-REAS fitment; HAC/DAC; towing 5,000/7,300/7,000 lb; EPA 17/20 and 15/19; the third row from 2004; the 2009 Trail Edition locker; IIHS ratings; sales; NHTSA 03V-146, 02V-339, 11V-113 and 16V-065; the ShockWarehouse kit contents (24-324359, 33-313146, SM5640, ≈$652); and the LCE 2UZ belt kit at $144.94.

**Still unverified / shortcomings**
- **Med:** the V6 output may have been re-rated under SAE J2723 for 2006-on. I haven't verified this; the page only quotes 245 hp.
- **Med:** the V8 air-injection failure costs ($2,000–4,000) come from CarComplaints owner reports.
- **Med:** only 2 photos. Vilano Beach is beach sand, which is fine. The forest camp shot is an unpaved campsite and fine.
- **Low:** wheel-size.com returns 403. The stock sizes and offsets are cross-checked with Limitless Tire (265/70R16, 265/65R17; +30 mm), but the 18 in +25 mm offset is unverified.
- **Low:** the extra file has no `import` section. The Hilux Surf is mentioned only in the generations table.

---

## 5th Gen (`data/pages/4runner/5th-gen.json`; `data/extra/4runner/5th-gen.json`)

**Corrections made**
- **Fuel-pump recalls (High, safety):** the page said 20V-012 and 20V-682 both covered 2018–19. Per the NHTSA API, **20V-012 now covers 2014–2015 4Runners** (Toyota moved 2018–19 out of it) and **20V-682 covers 2018–2019**. Fixed in the buying check, the FAQ and the extra recall list.
- **Takata wording:** "19V-005 for 2014–2016" was too narrow; the recall text covers 2011–2016 (2014–16 in Zone A). The buying check now names 19V-005 and 19V-741 across 2010–2016.
- **KDSS:** it was presented as standard on the Trail. Wikipedia lists it on the Trail and TRD Off-Road, and C&D calls it optional; the story, table and engineering cell now say "optional". Removed the unsourced "valves open below about 12 mph" claim; Wikipedia describes KDSS as fully mechanical.
- **TRD Pro shocks:** the page said Bilstein throughout. The C&D 2022 test truck had Fox dampers, so the text now says Bilstein at launch and Fox on later trucks. Updated in the story, table, extra identify/timeline and editions.
- **Rear diff capacity (High):** Trail4R (2.9 qt with locker / 2.8 qt without) contradicts Toyota-Club (2.70 L without / 2.65 L with), and the page used both. The repair and baseline now show both with `[CONFIRM IN MANUAL]`.
- **Lug torque (High):** the repair said 85 ft-lb (Trail4R). A Trail4R reader quoting the repair manual gives 76 ft-lb for alloy and 83 ft-lb for steel wheels, and the extra file had 76–83. The repair now shows the spread with `[CONFIRM IN MANUAL]`, and the extra lug torque is marked too.

**Removed:** the `@expo_t4r` and `@4xploration` Instagram handles, which I couldn't confirm. `@trail4r`, `@runnin4tacos`, `@4runnermods` and `@4runnerlifestyle` confirmed, and all YouTube channels resolve with matching titles.

**Added:** the Wikipedia KDSS article as a source in the extra file.

**Verified unchanged:** C&D 2022 TRD Pro (0–60 7.7 s, 15 mpg observed, 17 mpg / 390 mi at 75 mph, 9.6 in clearance, 4,800 lb, body-roll quote); "bronze and granite" (C&D Trailhunter test); 92,156 sales in 2024 (C&D); the sales table; the Wikipedia infobox (109.8 in, 189.9–191.3 in, 4,400–4,805 lb, August 2009 to August 2024, LHD only); TRD Pro colours; the Toyota-Club capacities (oil 6.2 L, ATF 10.7 L, front 1.55/1.40 L, transfer case 1.00/1.40 L, coolant 10.5 L); and the Trail4R fluid figures and torques (front 48/29, rear 36, transfer case 27).

**Still unverified / shortcomings**
- **Med:** the "Fox from 2017" switch year is not confirmed; the page only says "later".
- **Low:** the TrueCar URL returns 403 to bots.
- **Low:** the +15 mm stock offset in the extra file isn't confirmed (Limitless gives a −6 to +20 range).
- Photos: all 3 are 5th gens and off-road; captions are fine.

---

## 6th Gen (`data/pages/4runner/6th-gen.json`; `data/extra/4runner/6th-gen.json`)

**Corrections made**
- **Battery type:** "NiMH pack" was unsourced. Replaced with C&D's estimated ≈0.9 kWh battery under the cargo floor.
- **Roll-down window FAQ:** it was attributed to Motor1, which isn't in the sources. It is now attributed to Wikipedia, which supports it.
- **Cabin filter:** the repair's tools line said 87139-60030 while its parts list said 87139-0C010. Changed the tools line to 87139-0C010 to match the dealer-confirmed thread and the parts list.
- **Ground clearance:** the extra file gave a single 9.2 in; it now gives the trim-dependent 8.1–10.1 in, consistent with the C&D first drive and the story.
- **Third row:** "hybrids are expected to lose the third row" is now stated as fact per C&D.
- **Trailhunter photo alt:** it said "snorkel"; C&D says it is not a snorkel, so the alt now says "high-mounted air intake".
- Lug torque (97 lb-ft, from the 4Runner6G owners' torque list) is marked `[CONFIRM IN MANUAL]`.

**Verified unchanged:** the C&D first drive (TNGA-F, "SUV version of the Tacoma", nine trims, 278/317 and 326/465, peak torque at 1,700 rpm, full-time 4WD only on Platinum and hybrid Limited, LSD on the others, locker on TRD Off-Road/TRD Pro/Trailhunter, 6,000 lb towing, EPA 21/22/23, 8.1/10.1 in clearance, Fox QS3 vs OME, the $2,800 hybrid option, prices $42,220 / $50,640, third row only on SR5 and non-hybrid Limited). Also verified: the C&D Trailhunter test (6.7 s, 17 mpg, $68,350, 323 hp with the intake, "flirting with the red zone", production compressor); the C&D 2025/2026 pages (7.5 s, 18 mpg, 21 mpg highway, no major 2026 changes, MSRP ranges); the Wikipedia infobox (112.2 in, 194.9 in, 4,456–5,454 lb, December 2024 start); the Toyota-Club 500u capacities (oil 5.6 L, front 1.3/1.2 L, rear 5.6/6.5 L, transfer case 1.1/1.4 L, ATF 11.5/12.5 L, 72 L tank); the brake TSB parts and labor (04465-34040, 04945-0C060, 04947-0C030, BR2503, 0.9 h, SST 09719-77020/-77050); the wheel spec (M14×1.5, 95.1 mm); NHTSA 25V-595, 26V-282 and 26V-571; and the 2025 sales of 98,805.

**Still unverified / shortcomings**
- **Med:** neither photo meets the off-road rule. `gen6-mucubaji.jpg` shows paved mountain road with a bus and pedestrians; `gen6-trailhunter-sonoma.jpg` is a static display on tarmac at Sonoma Raceway. Both should be replaced with dirt or trail shots.
- **Med:** the oil-filter fitment on hybrids, the spark plug (90919-01303, listed for the NX350) and the 5.9 qt oil figure are forum-sourced; they are flagged as such on the page.
- **Low:** the steering-clunk and liftgate-water items rest on single forum threads.

---

## Links summary
- **All 461 URLs checked.** Dead or failing for curl:
  - `autos.yahoo.com` (404), `aol.com` C&D history (404) and `hotcars.com` return errors to curl, but all three load through WebFetch, so they are probably blocked by region or bot filtering rather than gone.
  - `japanesenostalgiccar.com` and `www2020.theautochannel.com` time out with curl (000) but also load through WebFetch.
  - `ovrmag.com` returns 405.
- **Bot-blocked but real URL formats (403/401):** `toyota-4runner.org` (17 URLs), Pexels/Unsplash photo pages, Hagerty, Curbside Classic, `wheel-size.com`, TrueCar, YotaTech, Expedition Portal classifieds, and the NHTSA `/recalls?nhtsaId=` pages. All recall IDs are confirmed via the API.
- **Parts links:** all 48 ToyotaPartsDeal URLs return the matching Toyota part. LCE and Total Chaos page titles all match the described part. RockAuto, Coastal Offroad, Metal Tech, 4Runner Lifestyle and Mudify links resolve. No olathetoyotaparts.com links.

## Top 5 remaining problems (group `4runner`)
1. **High — 5th gen rear diff capacity and 5th gen lug torque conflict between sources.** Trail4R and Toyota-Club disagree on which version (locker or no locker) holds more; lug torque is quoted as 76, 83 or 85 ft-lb. Both are now flagged `[CONFIRM IN MANUAL]`, but an owner's-manual check should settle them.
2. **High — 1st and 2nd gen baseline service has no sourced fluid grades or capacities** (all `[CONFIRM IN MANUAL]`). It needs a pass with an owner's or factory service manual.
3. **Med/High — lug-nut torques on 3rd, 4th and 6th gen come from aggregators or forums** (Limitless Tire 110 N·m; 4Runner6G 97 lb-ft). They are now flagged; confirm them against Toyota documentation.
4. **Med — photos.** 6th gen has no off-road photo (paved road and a raceway display). 1st and 4th gen have only 2 photos each. The 1st gen campsite photo is on pavement, and the 2nd gen "Irkutsk" caption conflicts with the plate's region.
5. **Med — forum-only claims I couldn't read because toyota-4runner.org returns 403.** These include the 3rd gen tire consensus, locker trim availability, the V06 label location and the 1st gen sunroof-drain rust story. A human with browser access should spot-check them.
