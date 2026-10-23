# Fact-check report — group `grenadier-scout`

Checked 2026-10-22. Files edited in place (schema unchanged, `json.dump(..., ensure_ascii=False, indent=1)`):

- `data/grenadier.json` (family + Station Wagon page), `data/extra/grenadier/station-wagon.json`
- `data/pages/grenadier/quartermaster.json`, `data/extra/grenadier/quartermaster.json`
- `data/scout.json` (family + Scout II page), `data/extra/scout/scout-ii.json`
- `data/pages/scout/scout-80-800.json`, `data/extra/scout/scout-80-800.json`
- `data/pages/scout/scout-motors.json` (the detail file `data/extra/scout/scout-motors.json` was checked but not edited)

How the checks were done:

- All 356 URLs across the 10 files were checked with curl (browser UA). 309 returned 200. The 403s are bot blocks on real URL formats: theineosforum.com, expeditionportal.com, gearjunkie, motorauthority, cars.com, nhtsa.gov/recalls, amsoil, ecstuning, edmunds and autonews. Key 403 pages were read with WebFetch instead.
- Page titles of the 200s were checked for soft-404s and redirects to home pages.
- NHTSA recalls API was queried for INEOS Grenadier MY2023–2026.
- Wikipedia raw wikitext was used for the Ineos Grenadier, Ineos Automotive, International Scout, Monteverdi Safari, Nissan SD engine and Scout Motors articles.
- Bring a Trailer model pages were scraped for value claims.
- Commons metadata and categories were read for every photo, and every photo was opened and looked at.
- Every `[[family/slug|…]]` cross-link and every `related` entry was checked and resolves.

---

## 1. Grenadier — Station Wagon (flagship: `data/grenadier.json` page + family, extra file)

### Corrections made
- **JLR approach.** The page said Ratcliffe "reportedly asked to buy the design… JLR declined, pointing at its own new Defender." It now says he approached JLR to buy the **tooling**, and JLR declined. The "pointing at its new Defender" part had no source. Source: Wikipedia (Autocar, Cropley, 1 Jul 2020).
- **Founding.** "Ineos Automotive was formed in 2017" is now "Ineos announced Ineos Automotive in February 2017." The codename is now spelled "Projekt Grenadier". Wikipedia's Ineos Automotive article gives the founding as 2016 and the announcement as 13 Feb 2017.
- **Spot welds.** "4,068 spot welds on the steel shell" is now "steel floor and shell" (AutoDaily factory tour).
- **Production numbers.** The 4,553 (2023) and ~8,000 (2024) figures are now attributed to Wikipedia's production table. The 2024 figure comes from an Automotive News sales-growth article, so it may be a sales figure rather than a build figure. "25,000 a year it planned" is now "the plant could build at full capacity" (FT via Wikipedia).
- **Tire FAQ.** It said owners run 35×11.5R17 without a lift and to "treat 35s as the outer limit." That contradicted the detail file, which says 35s need 2 in of lift. The FAQ now follows DVA Mechanics: 295/70R17 is "stock or 40 mm lift", 35s (315/70R17) are a 2-inch-lift job, and 285/75R17 is the practical stock limit. The 35s-without-lift reports are kept as forum anecdotes. The detail file's note "295/70 fits but tight at full lock" (unsourced) now uses the DVA wording.
- **Roof rack.** The claim that the Front Runner Slimline II "attaches to the grab-handle brackets" is not on Dometic's page and was removed. Dometic confirms "no drilling required" and 57.26 kg installed weight.
- **Transfer-case fill.** The page said "fill to spill isn't reliable." Owners quoting the workshop manual say it calls for **fill to spill**. The note now gives the manual method first, with the owner practice of measuring drained oil as an addition. Source: INEOS Forum fluid-levels thread, read via WebFetch.
- **Power-steering fluid.** Was "[CONFIRM IN MANUAL]" only. It now adds "Penrite LDAS (cited from an INEOS support document by an Australian owner)" and keeps the marker.
- **Values (detail file).**
  - "16 BaT sales… top result was an armored truck" was wrong. BaT shows **12 sold 2024 wagons** (Mar 2025–Sep 2026), $56,500–92,500, median $65,750. The armored 2024 was **bid to $95,000 and did not sell**.
  - The ranges were rewritten to match.
- **Photo captions.**
  - `station-wagon-trailmaster-overland.jpg` was labelled "Trailmaster Edition", but that is the Commons uploader's misspelling. The truck is a test vehicle. It is now captioned as a test truck, with Goodwood FoS 2024 in the alt text (Commons category confirms Goodwood FoS 2024).
  - The Greenwich photo caption now names the Greenwich Concours (per the Commons description).
- **Mods links.**
  - The Agile Offroad lift-kit category URL returned 404. It now points to the Agile Eibach Pro-Lift product page (200).
  - The Agile "bumper" link (`?p=51324`) actually went to Agile's home page and was removed. The ARMOR category gains the Agile complete skid-plate set (200).

### Verified as correct (selection)
- **NHTSA recalls 23V828/23V903/25V147:** components, model years and unit counts (727 / 61 / 7,022) all confirmed through the NHTSA API. The 25V147 build window (Jul 6 2023–Apr 19 2024) is confirmed by Motor1. No recalls are listed for MY2025 or MY2026.
- **Engines and driveline:**
  - B58 282 hp/332 lb-ft and B57 245 hp/406 lb-ft
  - ZF 8HP51/8HP76
  - Tremec 2.5:1 low range
  - Carraro axles, Eibach five-link
  - BMW deal March 2019, Magna Steyr December 2019, Bridgend plan September 2019, Hambach purchase December 2020
  - Flood during Australian testing, January 2022
  - Production from Oct 2022, deliveries December 2022
- **Specs:**
  - 264 mm clearance, 800 mm wading, 35.5/28.2/36.1° (4X4 Australia)
  - Roof load 150/420 kg (GoAuto)
  - 90 L tank, 13.5 m turning circle (Top Gear)
  - EPA 15/15/15 and Trialmaster 14 (fueleconomy.gov, 2024 and 2025)
- **Prices and launch:**
  - $71,500 US start; Rough Pack $2,850 on base and Fieldmaster, standard on Trialmaster (Motor1)
  - US trucks left the factory September 2023 (Carscoops)
  - Recaro-linked stop September 2024 to January 2025 (Expedition Portal via WebFetch)
- **2026 update:**
  - Steering revisions, 40+ changes, "big leap forward" (GearJunkie via WebFetch)
  - 2026 MSRPs $71,000 / $79,000 / $82,995, about $1,995 destination (Automotive Addicts)
- **Other:**
  - Wheel spec 6x130 / +55 / 84.1 mm / M14x1.5 (ThreePiece)
  - Leitner bracket: 1¾ in relocation, 37 in max tire, 25 mm offset limit, $239
  - Owl pump kit $2,150; Eibach springs $599, +2.5/+1.2 in
  - US service interval 12 months / 12,000 mi (ineosgrenadier.com)
  - Fluids thread: diffs 80W-90 2.1 L each, 31 Nm; transfer case Fuchs Sintopoid 75W-90 1.8 L / 2.64 L, 15 Nm; LC-18 = BMW 83195A42DF3 (HT-12); oil cap and drain 25 Nm
  - Agile diff-cover PDF: 12 mm hex drain, 23 ft-lb (≈31 Nm), 75W-140

### Removed or softened
- The "pointing at its own new Defender" line (removed), the grab-handle rack mount (removed), and the 35s-without-lift claim (now an anecdote).

### Added
- Sources: Wikipedia — Ineos Automotive; Automotive Addicts 2026 MSRP.

### Still unverified / shortcomings
- **High:** B58 oil capacity (6.5 L), ATF capacity (≈10.6 L) and the M22×1.5 plug spec with part GRA-5000-021220 all come from owner posts. The INEOS workshop manual is not public. These are marked in the text but have not been checked against a manual.
- **High:** Diff oil conflict. Owners quoting the manual say 80W-90 GL-5, but Agile's cover instructions say 75W-140. Both are stated; an owner should follow the manual.
- **High:** The FCP Euro ZF 8HP pan kit and the B58 spark-plug kit are listed for BMW applications. Grenadier fitment is unconfirmed, and owners say the Grenadier pan has an extra pickup port. The B57 diesel oil capacity is unknown.
- **Med:** Length is 4,856 mm (Wikipedia/press kit) but Top Gear's spec sheet says 4,896 mm. The approach angle is 35.5° (4X4 Australia) in some sources and 36.2° (GoAuto, Ineos Quartermaster claim) in others.
- **Med:** The "toot" horn line has no fetched source.
- **Med:** INEOS Forum threads (about 15 cited) return 403 to curl. Only the fluids and fluid-levels threads were re-read via WebFetch.
- **Low:** None of the three photos is truly off-road. Two were taken at Goodwood FoS 2024 on event grass and one on a concours lawn. `station-wagon-showroom.jpg` is in the img folder but not referenced.
- **Low:** LR4x4 and AULRO forum links are bot-blocked (403), but the URLs are real. Social is empty.

---

## 2. Grenadier — Quartermaster (`data/pages/grenadier/quartermaster.json`, extra file)

### Corrections made
- **"80% of Australian sales" claim.** "Ineos said it expected 80% of its Australian Grenadier sales to be Quartermasters or cab-chassis" was not found in any source, including a targeted search, and was removed. The story now notes Australia as a key market with a Norweld partnership.
- **Australian deliveries.** "As wagon deliveries were only just starting in markets like Australia" was unsourced and removed.
- **Production start.** "Late 2023" is now November 2023 (BMWBlog).
- **Cab-chassis.** "Scheduled for later in 2024" is now "added in Australia and NZ".
- **Expedition Portal claims (checked via WebFetch):**
  - The page said the "optioned Trialmaster had about 1,400 lb left." The article actually says the test Trialmaster *has* a 1,400 lb payload, so this was corrected in both the buying check and the FAQ.
  - "Towed a 5,000 lb trailer" is now "a 5,000-plus-pound Xplore overland trailer".
- **Parts score.** Caravan World's 7/10 is for "accessibility of spare parts". It isn't a head-to-head score against the LandCruiser.
- **Fuel FAQ.** "Caravan World saw the high 20s in L/100 km from both engines" was wrong. That figure was the B57 diesel Grenadier towing a big van. The ADR figures are now attributed to 4X4 Australia's spec table, and the Edmunds 14 mpg combined is pinned to MY2026 (confirmed via WebFetch).
- **"US base trim dropped".** This is now "no base trim on US 2026 price lists". No official announcement was found; the Automotive Addicts trim list shows only Fieldmaster, Trialmaster, Black and Trialmaster X.
- **Transfer-case and power-steering fluid notes.** Same corrections as the wagon.
- **Detail-file values.** "Only BaT Quartermaster… bid to $81,000 in August 2025 without selling" was wrong. BaT shows the 2025 Quartermaster Trialmaster **sold for $76,000 on July 31, 2025**. The $81k bid was a 2024 Fieldmaster wagon.
- **Sources.** The dead Yahoo Autos first-drive source (404) was removed. Its fact (first ship arrived March 2025) is confirmed by the Automotive News Europe article already cited. The FAQ source label was updated.
- **Social.** @expeditionportal (Instagram) was dropped because it couldn't be confirmed. The other Instagram handles are linked from the brands' own websites.

### Verified as correct (selection)
- **Launch and prices:**
  - Goodwood debut July 2023
  - US orders April 2024 at $86,900 / $94,900, 1,675 lb payload, 7,700 lb towing (Motor Authority via WebFetch)
  - Tariffs: total 50%, +11%, $85,500 to $94,500 including shipping, up to 20% of US volume, Raptor and R1T as named rivals, first ship March 2025 (Automotive News Europe)
- **Specs:**
  - Bed 1,564 × 1,619 mm, 1,337 mm between the arches
  - 907/832 kg payload, 3,550 kg GVM, 7,000 kg GCM, 350 kg towball
  - 36.2/26.2/22.6°
  - 14.5 m turning circle with the "genuinely appalling" quote (Top Gear)
  - 225 kg tailgate and the "more of a 4×4 with an open load area" quote (AutoDaily)
  - 15 L box in the spare (Driven)
- **Australian costs:** Caravan World's A$5,800 GVM upgrade, A$7,000 tray contribution, Norweld trays from A$18,990 and canopies from A$19,205.
- **Kaiju:** every detail was confirmed (4X4 Australia, 19 Dec 2024).
- **Aftermarket:** Dirtbox camper $11,499 and air bags $765/$795; Leitner rack 375/200 lb, bolts to the roll cage.
- **2026 changes:** about 5% tighter turning circle, ISA chime shortcut, Black Edition (Professional Pickup via WebFetch).

### Added
- Detail-file capability: Quartermaster roof load **120 kg dynamic / 375 kg static**, from the Caravan World spec table. It is lower than the wagon's 150/420 kg.
- Sources: Caravan World spec table, BaT result, Automotive Addicts, DVA Mechanics.

### Still unverified / shortcomings
- **High:** Same owner-sourced fluid capacities and fitment caveats as the wagon. The baseline service is copied from the wagon.
- **Med:** "0–100 km/h in 8.8 s" in the generations table is a wagon figure from Top Gear and isn't confirmed for the Quartermaster. The Drive quotes 1,653 lb payload against Motor Authority's 1,675 lb.
- **Med:** Owner anecdotes ("jitter", the B57 heat-shield bolt, bed rails and L-track) come from INEOS Forum threads that are 403 to curl and were not re-read.
- **Low:** Only 2 photos, both at Goodwood on grass, both of the same truck (LG24 SLZ). `quartermaster-boblingen.jpg` is in the img folder but not referenced.

---

## 3. Scout — Scout II (flagship: `data/scout.json` page + family, extra file)

### Corrections made
- **Baja 1000.** "'72 Scout II Cabtop" is now "'72 Scout II". Octane Press doesn't name the body style.
- **End of the line.** "IH had plans for Scout-based coupes, minivans, campers…" now lists the experiments Wikipedia gives: minivans, station wagons, dune buggies, Hurst editions and a small motorhome, plus the 1979 Scout III **SSV** concept.
- **Monteverdi Sahara.** "Only about 30 were made" is now "an estimated 30" (Wikipedia/BaT wording).
- **4WD Mechanix bedliner story.** Softened to "reportedly", because the 4WD Mechanix forum is unreachable (the proxy returns 502).
- **Baseline service.** Capacities sourced only to the AMSOIL lookup (403, unverifiable) now carry `[CONFIRM IN MANUAL]`: coolant ~20 qt, A727 5 qt, transfer case 3.4 pt, diffs 4.2/3 pt and power-steering fluid. The transfer-case entry now also gives the IHPA guidance against GL-5.
- **Wolford photo.** It shows a heavily modified open-top rock crawler, and the caption and alt now say so. The credit "Vanessa Lacayo, BLM · CC BY 2.0" is correct per the Commons file page.
- **Social.** @ihscoutswest and @internationalscoutii were dropped because they couldn't be confirmed. @anythingscout and @superscoutparts are linked from the suppliers' own sites.
- **Detail-file timeline.**
  - The 1971 entry listed the 345 V8 at launch. It now says the truck launched with the 196, 232 and 304, with the 258 and 345 "added soon after" (Hagerty).
  - The 6,200 lb GVWR/XLC change moved from 1976 to 1975, per Super Scout Specialists ("Scout XLC… 6200 GVW in 1975"). Wikipedia says 1976, so the capability note gives both.
- **Detail-file stock-tire row.** It said "31x10.50R15 stock" with an odd "drawn around a 33-in tire" note, which contradicted the page FAQ that says 31s are marginal. It now reads "30–31 in (31s marginal)" with the IHPA guidance.
- **Detail-file values.** The claims of "about 110 BaT sales", a "$158,000 L92 1979" and a "$96,000 1980 345" couldn't be reproduced, because the BaT page only shows recent results. The note is rewritten from the 18 most recent Scout II sales (Jul–Oct 2026: $10.5k–87.5k, median ~$25k, top a 4.8 Vortec 1978 at $87.5k) plus Hagerty's #2 values. The ranges were adjusted.

### Verified as correct (selection)
- **Production:**
  - April 1971 start; last Scout October 21, 1980; 532,674 Scouts in total
  - Yearly output: 1973 34,117 through 1980 13,106; about 4,000 SSIIs
  - Diesels 1,602 / 1,038 / 1,045 / 537 / 571 / 5,389 = 10,182 (Super Scout Specialists)
- **Engines and diesels:**
  - SD33 95 PS, SD33T 110 PS, T-19 with the SD33T (Wikipedia, Nissan SD engine)
  - "First domestically built diesel SUV" (Jim Allen, Octane)
- **Axles and brakes:** Dana 30/44 until 1974, Dana 44/44 after; ratios 2.72–4.54; late-1974 disc brakes; Dana 300 in 1980 only, 2.62:1 (4Low, SSS code TC-146).
- **Grilles:** dating by grille, the 15-bar 1976 grille and the 1980 ABS grille.
- **Racing and models:** 1977 Baja (Boone, ~2 h ahead of a CJ-7); four sponsored race teams; the Traveler replacing the Travelall.
- **Hagerty:** ≈260,000 Scout IIs; Gen X 46%; median #2 values $42,200 (Scout II) and $64,750 (SSII); >90% V8 4WD; 1979 test car 168 hp, 288 lb-ft, 3,800 lb.
- **Motor Sport 1978:** 163 bhp / 292 lb-ft, 10 mpg (14 possible), brakes that "pull and twitch".
- **Monteverdi Safari:** facts match Wikipedia.
- **Line tickets:** locations and codes, plus serial prefixes CGD–KGD (SSS code reference).
- **Parts:** all IH Parts America and Anything Scout part links resolve to the named parts.

### Still unverified / shortcomings
- **High:** No factory fluid capacities or specs. Engine oil (7 qt, IHPA moderator), diffs, transfer case, coolant and A727 all rely on forum or AMSOIL figures and are now marked. The manual-transmission oil spec is unknown.
- **Med:** The Scout II page cites forums.4wdmechanix.com (Moses Ludel quotes), which couldn't be reached (proxy 502). Those quotes are unverified.
- **Med:** The detail file's stock fitment entry (10-15LT on 15×7 rally wheels) comes from Spirit of 76 line-ticket codes. It isn't a general stock size.
- **Low:** Photos are good. Two are off-road (Wolford, Lake Pleasant). The 1976 farm photo is on gravel by a barn.

---

## 4. Scout — Scout 80 / 800 (`data/pages/scout/scout-80-800.json`, extra file)

### Corrections made
- **Clay model.** "First clay model made in June 1959" (Silodrome) is now Ornas's own account: a full-size clay model started in late July 1959 and approved that November. Sources: Ornas quote on Wikipedia and Super Scout Specialists.
- **100,000th Scout.** "By 1964 IH had built more than 100,000 Scouts" has no year source. It is now "IH marked its 100,000th Scout with the Red Carpet edition". The detail file's Red Carpet "1964" date is now "Scout 80 era". The Scout 800 arrived "in 1965", not "for 1965".
- **Autotrader Classics date.** The article was published Nov 5, 2024 (via WebFetch), so "mid-2024" is now "late 2024" in the story and FAQ. Its other figures were confirmed: about 28,000 first-year sales, Dana 44 and Dana 20 dated to 1967, no reproduction fenders, the hub test, 75 mph, $40k/$25k/$15k and the $114,900 800A.
- **Ride quote.** "IH Parts America calls the ride… 'a bit choppy'" isn't on the cited pages. It is now CPT's own claim that its reverse-shackle kit "significantly" improves ride quality.
- **Length.** "154 in long overall" had no source. It was removed from engineering, and the plate LENGTH row was dropped (12 rows remain).
- **152 four torque.** 135 lb-ft is now 137 lb-ft, per Silodrome, the cited source.
- **Four-speeds.** "Silodrome says… four-speeds came later" isn't in Silodrome. It now says "many later 800s have four-speeds", which is supported by BaT listings of 4-speed 800s.
- **Photo.** The `scout800a-autumn-woods.jpg` Commons description says "Scout 800", the file is in the "Scout 800" category, and the file name says 800A. The caption is now "SCOUT 800-SERIES". Iowa is confirmed by the Commons geotag (41.99, −93.88), and the alt text now says the lane is paved.
- **Detail-file values.**
  - "$87,000 304-powered 1967 800" was wrong: BaT shows a **345-powered** 1967 (a non-original engine).
  - "$68,000 304-powered 1961 80" was wrong: the $68,000 truck was a 1964 Scout 80 4×4.
  - The 800 median is about $33.75k, not $25k.
  - The note and ranges were rewritten from the current BaT data, and the unverifiable $21,101 Red Carpet sale was dropped.

### Verified as correct (selection)
- **Origins:** Ornas "replace the horse" quote; Scout 80 in late 1960 as a 1961 model.
- **Engines:** 152 is half a 304 at 93 hp; 196 is half a 392 at 111 hp (August 1966); 266 V8 from spring 1967.
- **Driveline:** Dana 27 axles with offset diffs and a Dana 18 transfer case; T-90A three-speed; 800A from November 1968; 800B August 1970 to March 1971.
- **Sources quoted in the text:** SCM ($800 in 2003, the $33,000 Barrett-Jackson sale in 2014, the TravelTop being in most demand, data plate on the cowl) and Hagerty's 800B article (beat the Bronco, tractor-durable driveline).
- **Camper sidebar:** "Pato", the drive from Denver to Patagonia, sold in Santiago (Commons description in full). Camper prices $960 / $1,850 (Wikipedia).
- **Transfer-case oil:** SAE 90 GL-1 or straight 50-weight, no GL-5, about 2.5–3 qt (IHPA moderator threads).
- **Scout Motors coordinates:** the 41°03′36″N 85°04′33″W on scoutmotors.com do point at Fort Wayne.

### Still unverified / shortcomings
- **High:** No factory capacities or specs for engine oil, coolant, gearbox, diffs or brake fluid. All are marked `[CONFIRM IN MANUAL]` and the page says so.
- **Med:** The kingpin preload figure isn't sourced; the page already tells readers to use the shop manual.
- **Low:** The detail file has no `fitment` or `capability` sections, because no sourced wheel or tire data was found. `scout80-riverbank.jpg` is only 640 px wide and `scout80-camper-panamerican.jpg` only 931 px.

---

## 5. Scout — Scout Motors (`data/pages/scout/scout-motors.json`; detail file checked only)

The brief allows only officially announced, dated facts here. The page was rewritten to remove the following third-party reports:
- **Der Spiegel** (production slipping to summer 2028).
- **AutoForecast Solutions** (Traveler September 2028, Terra March 2030), reported by Jalopnik and Motor Illustrated. Scout disputed it, saying "initial production is targeted to begin in 2027."
- **Jalopnik's unnamed-source claims** that the EREV generator causes engineering problems and that towing could be about halved.
- **The 87% EREV share.** Electrive's attribution to the CEO is ambiguous.
- **"The range-extender version will now come first".** No official source.
- **"In February 2024 Scout was talking about 2026".** No source.
- **"About 1,100 acres".** No source.
- **The NADA lawsuit of February 3, 2025.** Not supported. It was replaced with the dated suits Wikipedia documents: Florida VW/Audi dealers (February 2025) and the California New Car Dealers Association, whose case a judge allowed to proceed on March 30, 2026.

### Corrections made
- **Trademark date.** "VW came to own the trademark in early 2021" is now "in 2021", when Traton completed the Navistar purchase.
- **Company dates.** Added May 11, 2022 (VW approval), May 24, 2022 (founding) and September 1, 2022 (Keogh becomes CEO), per Wikipedia.
- **Reveal specs.** "Launch coverage reported" is now "Scout announced/projected". KBB attributes the towing, payload, 35-inch tires, ground clearance, fording, sway-bar disconnect, 800 V and 350 kW figures to Scout. Scout's own model pages confirm body-on-frame, solid rear axle, front and rear mechanical lockers, 4WD, 240 V, a 5.5 ft bed, 350 mi BEV / 500+ mi EREV, under $60,000, 2027 "subject to change", 16 metros growing to about 100 stores by 2032, and engineering in Detroit. InsideEVs confirms $50,000/$51,500 with incentives and the $100 refundable reservation.
- **Timing is now limited to dated official statements:**
  - Keogh in March 2026, "I see that sometime in 2028", with about 160,000 reservations, about three-quarters Traveler. He shared these figures himself (Electrive, via WebFetch).
  - Scout spokesperson on April 13, 2026: "We expect customers will begin taking delivery… in 2028."
  - The July 2026 first validation body weld, with Keogh's quote (EVWire).
- **Reservation figures.** January 2025: more than 50,000, about 70% Traveler, more than half Harvester (Keogh, Motor Authority via Wikipedia).
- **Generations table.** The AutoForecast Solutions-based rows were removed.
- **Sidebar, FAQ and plate.** Rewritten to match.

### Still unverified / shortcomings
- **Med:** Scout's newsroom pages render client-side, and WebFetch isn't allowed for scoutmotors.com, so I couldn't re-read the press releases directly. These detail-file items are unverified and were not edited:
  - Oct 24, 2024 release: 0–60 in 3.5 s, about 1,000 lb-ft (KBB confirms 3.5 s only)
  - Nov 18, 2025 LA release
  - **Sept 2, 2026 release:** validation builds in 2026 continuing into 2027, the Mountainside and trail-ready concepts, Jazz Aspen Snowmass Sept 4–6
- **Low:** No photos (by design: `hero_note`). No mods, repairs or service, which is correct for a vehicle not yet delivered.

---

## Family objects
- **Grenadier family.** Intro, verdict, years, generation codes and summaries (2,922/3,227 mm, 305 mm stretch, 760 kg, Euro pallet) and the forums were all checked. No changes were needed. `has_page: false` on the Quartermaster is overwritten by `build.py` (line 169), so it was left alone.
- **Scout family.** Intro facts were confirmed: Ornas quote, late 1960 as a 1961 model, Fort Wayne, October 21, 1980, 532,674 built, the October 2024 reveal. The Binder Planet and IHPA forum links all resolve. No changes were needed.

---

## Top 5 remaining problems for this group
1. **High: Grenadier fluid capacities and torques rely on owner posts.** This covers 6.5 L oil, ≈10.6 L ATF, the plug part numbers, and the diff oil (80W-90 per owners quoting the manual vs 75W-140 per Agile). A human with INEOS workshop-manual access should confirm. The service tables are duplicated across the wagon and Quartermaster pages, so fix both.
2. **High: No factory fluid specs or capacities for any IH Scout.** The Scout II numbers come from an AMSOIL lookup that can't be verified (403) and from forum posts. The Scout 80/800 has none at all. An IH shop manual (CTS-2304/2313 or MT-series) is needed.
3. **High: Part fitment for the Grenadier is unconfirmed.** The FCP Euro ZF pan kit (Grenadier pans reportedly differ), the B58 spark-plug kit (listed for the 340i) and the Mahle LX3985/1 air filter are all owner-reported matches. Check them against the INEOS parts catalogue.
4. **Med: Scout Motors detail file cites official releases that couldn't be re-read** (the Sept 2, 2026 release and the Mountainside concept, among others). The scoutmotors.com newsroom renders client-side. Someone with a browser should confirm or trim these.
5. **Med: Weak photos.** All 5 Grenadier and Quartermaster images are event-lawn shots, not off-road, and the Quartermaster has only two, of one truck. Scout Motors has none. The Scout 80 shots are low-resolution. A photo pass is needed: off-road Grenadier and Quartermaster images, plus higher-resolution Scout 80s.
