# Fact-check report: group `g-class-b`

Models: `europa`, `g55-amg`, `g550`, `4x4-squared`, `second-gen` (family `g-class`).
Files edited: `data/pages/g-class/<slug>.json` and `data/extra/g-class/<slug>.json` for those five slugs only. Backups of the pre-edit files are in the session scratchpad.

## How the checks were done

- **Specs and dates:** checked against the Wikipedia G-Class raw wikitext (engine table and update notes), the Wikipedia G500 4×4² and G 63 6x6 articles, and Mercedes' own 500 GE history page. I also used the MBUSA 2017 G550 press-release PDF (fetched and parsed), the MBUSA media spec pages for the 2017 4×4², 2018 G550 and 2019 G550, and the 2017 4×4² launch release.
- **Fuel economy:** EPA figures for every relevant model year came from the fueleconomy.gov web-services API.
- **Recalls:** all 25 recalls in the detail files were looked up through NHTSA's `recalls/campaignNumber` API.
- **Source pages:** checked with WebFetch. These included PeachParts, five Expedition Portal posts, the MBWorld locker thread, the 500eboard fluids thread, Hagerty, Ferraris Online, German Cars For Sale Blog (GCFSB), Jalopnik, Autoblog, VRP, Autocar, The Shop, SlashGear, TFLcar/TFLtruck, Motor Authority, Practical Motoring, CAR (SA), AMSOIL, Bolidenforum, autofiles, BaT listings, Eurowise and GwagenParts.
- **Links:** all 269 URLs in the 10 files were curled (Mozilla UA). The 100 parts-supplier URLs had their page titles checked, and 17 questionable FCP Euro parts had their G-Class fitment lists scraped.
- **Cross-links:** every `[[family/slug|…]]` and every `related` entry was validated against `family.generations` in all family files. All are valid.
- **Photos:** all 14 images were opened. The 4 Pexels images were re-downloaded by ID to confirm each file matches its `source_url`.

**Link status after fixes**

- **Bot-blocked but in the correct format (403/429):** NHTSA recall pages, MBWorld, AMSOIL, Autoblog, Carvana, Go-Parts, Toolsource, Hagerty, PeachParts, Pexels, Reddit, MBCA, Overland Expo, au7o and Motor Authority. Where it mattered, these were confirmed through WebFetch or the NHTSA API.
- **MBUSA media release URLs:** curl returns 404, but WebFetch loads them with full content, so they were kept.
- **Expedition Portal forum posts:** these send curl to a JavaScript challenge, but they load through WebFetch.

---

## Europa International Gs (`europa`)

### Corrections made
- **Gray-market history:** "tighter import rules in 1987 and the 1988 Act…" became "the Imported Vehicle Safety Compliance Act of 1988 largely ended that trade."
- **Mike Serpe quote removed:** the page used it as a warning about 1980s gray-market dealers. Hagerty actually quotes him about *today's* gray-market imports. (Hagerty)
- **Dave Holland:** the text now says this is from a Motor Trend feature quoted by GCFSB. GCFSB itself says the text is an excerpt. (GCFSB 2000 G500 Europa)
- **Small Volume Manufacturer status:** added that Ferraris Online dates it to 1999, against Wikipedia's 1998. (Ferraris Online)
- **"Europa G-Wagen LLC … title histories as late as 2013":** unsourced, so replaced with Jalopnik's statement that Europa is still in business, selling parts, service and modifications. (Jalopnik)
- **Engineering intro:** it said Europa trucks lack the smart key. Wrong: GCFSB says late Europa trucks (around 2000) already have EIS and a smart key. Rewritten. The buying check "Ignition and key system" was rewritten to match. The unsourced "one Europa G 320 needed a new ignition tumbler" was removed.
- **Diff-locks repair:** it was "usually the vacuum system." It now explains that the centre lock is vacuum-operated and the axle locks are hydraulic (MBWorld, 2005 G 500), and that the locker circuit uses brake fluid (500eboard, 1997 G 320). Fix steps now cover both circuits.
- **FAQ "Which Europa G should I buy?":** GCFSB doesn't "prefer" the 300 GE or G 500. It says the head gasket is the G 320's only drawback against them. Reworded, and the V6-vs-G 500 mpg claim is now attributed precisely. (Expedition Portal post 1015121)
- **FAQ on Europa vs MBUSA trucks:** "COMAND electronics that GCFSB blames…" became GCFSB's actual warning about electrical problems on 2002–2005 MBUSA trucks.
- **Head-gasket repair:** "A later Europa seller still recommended the G 300 or G 500" became the PeachParts owner's recommendation of a G 500.
- **Baseline intro:** called Europa trucks "grey-market imports," which contradicts the whole page. Fixed.
- **Jalopnik source URL was dead (404):** replaced with `https://www.jalopnik.com/at-32-000-is-this-2000-mercedes-g500-a-boxy-bargain-1851582344/`. The content was confirmed: 202,750 miles, $32,000, black bumpers, skid plate, steering stabiliser.
- **Photo 1:** the caption and alt now say plainly that it is a UK-registered European-market SWB, not a Europa truck.
- **Detail file:** the timeline wording about GCFSB was fixed. The note on the Eurowise 60 mm max-tire figure was corrected: the trimming remark applies to the King shock option, and Eurowise lists G 500/G 55/G 550/G 63 fitment.

### Removed or softened
- **Differential spec "MB 235.0, 85W-90":** unsourced. Replaced with the owner's Red Line 75W-90 GL-5 plus `[CONFIRM IN MANUAL]`. The capacities (1.4 L front, 1.8 L rear) are confirmed by the 500eboard thread and AMSOIL.
- **Transfer case "some later W463 cases take ATF":** now carries `[CONFIRM IN MANUAL]`.
- **Vacuum hose 000 158 14 35:** labelled as a generic bulk hose. FCP Euro lists it for many Mercedes models, not specifically the G.
- **Club G-Wagen forum:** dropped. clubgwagen.com resets the connection or returns 503.
- **Instagram @gzilla500:** dropped. I couldn't confirm it exists or is tied to G-Class content.

### Added
- MBWorld locker thread added to `sources`.

### Verified (no change needed)
- **Ferraris Online:** five-year, $500,000 programme finished October 1993; nearly two years and more than $1 million for Small Volume Manufacturer status; fewer than ten SWB Cabriolets certified.
- **Hagerty:** up to $135,000; trucks later built to DOT standards; 30% premium for originality.
- **PeachParts:** 40,000-mile repack interval, a necessity by 75,000 miles, $1,500–2,000; right-rear M104 head-gasket seep at about $2,000; 1998 changeover year.
- **Scott Brady's 1996 Europa truck:** lockers, ABS, airbags, Labrador trip, 10–15 years. (Expedition Portal)
- **Neiman Marcus edition:** 1999, $160,000, six sold, birch trim.
- **Engine outputs vs Wikipedia:** 300 GE 125 kW / 190 Nm; G 320 I6 155 kW / 300 Nm; V6 160 kW; G 500 218 kW / 456 Nm.
- **Recalls:** all four NHTSA recalls, with the stated populations.
- **Fluids (500eboard):** transfer case GL-4 about 3 qt; 60 Nm drain plugs; 14 mm hex.

### Still unverified / shortcomings
- **High:** diff-lock actuation on **1990s** Europa trucks isn't documented directly; the evidence is from 1997 and 2005 trucks. The transfer-case fluid for 1998–2001 trucks is unconfirmed, as are the M103/M104 oil, air-filter and spark-plug specs (all marked `[CONFIRM IN MANUAL]`).
- **High:** several part links are FCP Euro pages listed for **2002-on** W463s (front bearing, wheel seal, axle seal, steering damper, drag link). They say "confirm fit by VIN", but nobody has confirmed that they fit 1993–2001 trucks.
- **Med:** the hero photo is a UK-market truck at a show, and the second is a Europa truck in a parking lot. There is no off-road photo of an actual Europa G. Both break the off-road-only photo rule.
- **Med:** the M104 head gasket part numbers (104 016 28 20, 104 010 37 20) are not listed by FCP Euro for the G 320. They are labelled "confirm vs engine no."
- **Med:** Eurowise OME springs list 2002–2014 fitment only, yet the page recommends them in the mods section for 1990s trucks.
- **Low:** the engineering cell doesn't say which gearbox the V6 G 320 uses. The 722.6 is likely, but no source confirms it.

---

## G 55 AMG (`g55-amg`)

### Corrections made
- **Verdict:** "507 horsepower" became "507 PS (500 hp)". The engine makes 373 kW. (Wikipedia, Autoblog)
- **"AMG turned some of the 446 500 GEs into 6.0-litre specials for individual customers":** became "13 of the 446 500 GEs got AMG's 6.0-litre upgrade kit." (Wikipedia; Mercedes' 500 GE page)
- **"Mercedes treated it as a regular series model rather than a limited edition":** removed. Mercedes' page doesn't say this.
- **Year labels:** engineering "ENGINE (2001–03)" and generations table "1999/2001–2003" both became **1999–2004**. That matches the story (introduced 1999) and the Kompressor's arrival in 2004.
- **Fuel-economy FAQ:** it quoted a dealer listing's 12/14 mpg for a 2005 Kompressor. The EPA figures are **11/13/12** for 2005–2011 Kompressors and **12/14/13** for the 2003 naturally aspirated truck. (fueleconomy.gov API)
- **"Owners say the windshield behaves like a consumable":** now attributed to the single GCFSB commenter who said it.
- **Buying check "Is it really an AMG?":** the autoevolution "G 55 given a G 63 nose" claim was removed. It isn't in the article.
- **VRP source URL:** updated to the canonical `/the-complete-e55-bible/` and relabelled. Its claims were confirmed: high failure rate of the original intercooler pump, updated Bosch pump, fluid-filled mounts that leak and collapse, better-insulated wires, and the 13-pin connector and conductor plate.
- **Detail timeline (2007):** removed the unsourced "C-Class-style cluster" and "COMAND APS". HID, camera and TPMS are confirmed by Wikipedia.
- **Detail max-tire:** the trimming note is now tied to Eurowise's King shock option.

### Removed or softened
- **Differential spec "MB 235.0, 85W-90":** removed. The page now gives GL-5 75W-90 with AMSOIL capacities and `[CONFIRM IN MANUAL]`.
- **Club G-Wagen forum:** dropped (dead).

### Added
- Sources: EPA fueleconomy.gov and the AMSOIL 2006 G500 capacities page.

### Verified (no change needed)
- **Outputs and performance (Wikipedia table):** 354 PS / 525 Nm; 476 → 500 → 507 PS, 700 Nm; 0–100 km/h 7.4 s → 5.6 s → 5.5 s; 210 km/h; US Kompressor from MY2005.
- **2009 update (Autoblog and Wikipedia):** three-bar grille, KOMPRESSOR lettering, 9.5×19 wheels with 275/55R19 tires, Alcantara headliner, designo leather, COMAND APS, ESP with hill-start assist.
- **GCFSB:** 7,000 lb towing; about 400 lb-ft on the naturally aspirated truck; mounts and coastal-rust comments.
- **MBWorld locker thread:** centre lock vacuum, axle locks hydraulic, split Y-connector.
- **Fluids:** oil 8.5 L (9 qt) and coolant 12.7 L (Bolidenforum, 2011); 722.6 9 qt (AMSOIL).
- **Recalls:** all three in NHTSA.
- **autoevolution prices:** $72,500 and $94,000 for 2011s; Deep Black and Fire Opal Red.
- **FCP Euro fitment:** confirmed the G 55 is listed for the engine mount, transmission mount, intercooler pump, axle seal and wheel bearing.

### Still unverified / shortcomings
- **High:** transfer-case fluid type and capacity, and differential viscosity and MB sheet, remain `[CONFIRM IN MANUAL]`.
- **High:** whether brake fluid feeds the axle-lock hydraulics on the G 55 isn't confirmed (marked `[CONFIRM IN MANUAL]`).
- **Med:** two of the three photos are street shots (one of them on aftermarket wheels), which breaks the off-road rule. The Schöckl photo's lead truck has aftermarket-looking bodywork. It is identified as a G 55 only by its Commons filename.
- **Med:** the claim that autoevolution's average Kompressor price was about $60,000 in 2021–22 wasn't re-verified.
- **Low:** the Carvana source returns 403, but the 2012 US line-up is confirmed by EPA data.

---

## G 550 (`g550`)

### Corrections made
- **Seven-speed gearbox:** "had already replaced the five-speed on the 2007 US G 500" became "Mercedes had begun phasing the 722.9 into the US G 500 during 2007." (Wikipedia: "start to phase out" the 722.6)
- **Engineering note:** "until it was addressed" was dropped. The owner never said the ESP issue was fixed. (Expedition Portal post 2232303)
- **Buying check:** "sagging headliner means water (usually blocked sunroof drains)" became Autocar's actual wording, plus a check of the drains and seals.
- **Diff-locks repair:** now notes that the axle locks may be hydraulic (MBWorld) and adds `[CONFIRM IN MANUAL]`.
- **Idler-gear FAQ codes:** "P0272–P0276" became "P0272, P0275 or P0276", the codes FCP Euro actually lists.
- **Photo 2:** it is not a G 550 that can be confirmed. It's a pre-2013 V8 W463 with no LED running lamps. Alt and caption corrected.
- **Detail recalls:** 19V787 years corrected from 2013–2017 to **2013–2016** for the G 550 and G 63. (NHTSA API)
- **Detail sources:** the "2014 G 550 on 275/70R18" source pointed to post 2136416 (HeliNomad's 2017 thread). Corrected to **post 2232303**, the 2014 G550 build thread that actually has the KO2s, flex and ESP comments.
- **Detail timeline (2007):** removed the unsourced "new cluster and COMAND APS". COMAND was revised in the 2008 update.
- **Detail editions:** Edition Select is now dated 2011 per Wikipedia (it said 2011–2012), with clearer wording.
- **Detail max-tire:** the Eurowise trimming note is now tied to the King shock option.

### Removed or softened
- **Detail timeline "2009–2010: no factory trailer hitch … avoid them if you plan to tow"** (flagged "avoid"), and the matching capability note: removed. No source found.
- Instagram @gzilla500 dropped, and the Club G-Wagen forum dropped.

### Added
- Sources: MBWorld locker thread and EPA fueleconomy.gov.

### Verified (no change needed)
- **MBUSA 2017 press PDF:** 416 hp / 450 lb-ft; 0–60 mph 5.8 s; 130 mph; 5,724 lb; $119,900; 9.3 in clearance; 23.6 in wading; 30°/30°/24°; 76.9 × 80.9 × 187.56 in; 112.2 in wheelbase.
- **M273 (Wikipedia):** 285 kW / 530 Nm (382 hp / 391 lb-ft).
- **EPA:** 2010 G 550 11/15/13; 2012–2015 12/15/13; 2016–2018 13/14/13. So "13 combined 2010–2018" holds.
- **FCP Euro M272/M273 guide:** thermostat 15.2 Ω ± 1.5 Ω and replacement at 60,000 mi; P0597–P0599; swirl-flap codes P2004–P2006 with whole-manifold replacement; tensioners and idlers at 60,000 mi; cam-magnet pigtails; two air filters.
- **autofiles:** 7,000 lb towing, 25.4 gal tank, and the tire list.
- **MBUSA 2018 spec page:** 8.1 in clearance at maximum load, 1,334 lb payload, 44.6 ft turning circle, 28.4° tilt.
- **Autocar:** cracked coil springs at £120 per corner.
- **Expedition Portal:** sinkhole story, Gobi rack, mpg drop, 265/65R18 = 31.6 in, stock tires 30.5 in.
- **Other facts:** Japan-only Night Edition (100 built); the 2012 update with the ML-derived dash.
- **Recalls:** all eight checked in NHTSA.
- **FCP Euro fitment:** confirmed the G 550 is listed for the upper hose, rear coil spring, battery, cabin filter, vacuum hose and ignition coil.

### Still unverified / shortcomings
- **High:** transfer-case and differential fluid types and capacities, and the oil capacity, are all `[CONFIRM IN MANUAL]`.
- **High:** whether the lock actuation is vacuum or hydraulic on 2009–2018 trucks is unconfirmed.
- **Med:** both photos are street shots (Miami; a kerbside V8 W463). There is no off-road G 550 photo.
- **Low:** Front Runner's URL now redirects to the Dometic home page. It works, but the destination is generic.

---

## G 500 4×4² (`4x4-squared`)

### Corrections made
- **"Went on sale in Europe in late 2015":** unsourced. Changed to "Mercedes put it into production in 2015." (Wikipedia)
- **"Two coil-over struts":** became "two spring struts in parallel," matching Expedition Portal's description. BaT also calls them coilovers.
- **Callout:** "Everything that changed is below the axle line" was false, because flares, roof lights and track width also changed. It now reads "Almost everything that changed is in the running gear."
- **Tire FAQ:** "re-code the tire size" contradicted MBUSA's launch release, which says larger tires don't need a speedometer recalibration because it reads from the axles. Replaced with MBUSA's statement. "The Geneva show car wore 37s" became "concept photos showed 37s on beadlocks." Same fix in the mods "Wheels & tires" text and the detail-file max-tire note.
- **G 63 6×6:** the unsourced "never sold in the US" was removed (generations table and detail editions). Production is now given as 2013–2015, just over 100 built, last delivery May 2015. (Wikipedia 6x6 article)
- **Rust repair part:** the link was a Rovers North (Land Rover supplier) search page, which returned 403. Replaced with the Eastwood Internal Frame Coating page, which was verified.
- **Photo 1:** the caption said "GRASS FIELD". It's a car-show field, and the truck has an aftermarket Warn bumper and non-factory tires. Alt and caption corrected.

### Removed or softened
- Instagram @gzilla500 and the Club G-Wagen forum were dropped.

### Added
- Sources:
  - Wikipedia G500 4×4²
  - Eastwood
  - Wikipedia G 63 6x6
  - mbpassion (G 650 Landaulet €749,700)
  - Motor Authority (Landaulet limited to 99 units)

### Verified (no change needed)
- **MBUSA spec page:** 177.1 in long; 86.2 in wide with mirrors; 88.0 in tall; 69.3/70 in track; 6,694 lb; 17.24 in clearance; 51.6°/43.8°/44.6°; 39.4 in fording; 46.92 ft turning circle; 11/11/11 mpg; 25.4 gal; towing "TBA"; $225,000 + $925.
- **MBUSA launch release:** 47.4° breakover; front track more than 9 in wider and rear more than 10 in; two stabilizer bars; geometry, steering links and driveshafts unchanged; "most capable G-Class ever."
- **Practical Motoring:** concept shown at Geneva in March 2015 with production depending on the reaction; 450 mm; 1,000 mm; 299 mm wider track; 325/55R22; optional 37×12.5×18 tires; 310 kW.
- **Expedition Portal:** 15 ms damper switching; "straight out of the park."
- **CAR (SA):** €231,693; orders close at the end of October.
- **Wikipedia:** KW suspension; shortened 6×6 chassis; G 63 4×4² June 2022, 585 hp, $350,050, 13.8 in clearance, 35.8 in wading, 6,315 lb (379 lb lighter).
- **BaT listings:** the 39k-mile truck (Pirelli Scorpion ATRs, plugs, coil, transmission service, roof scratches) and the Banyan Motors LeTech conversion.
- **EPA:** lists both 2017 and 2018 "G550 4x4" at 11 mpg.
- **Recalls:** all three in NHTSA (17V817 432 units; 22V937 278; 23V851 590).

### Still unverified / shortcomings
- **High:** portal-hub oil, axle oil, transfer-case and power-steering fluids are all `[CONFIRM IN MANUAL]`, with nothing sourced. This is the biggest service gap in the group.
- **Med:** Practical Motoring says production depended on the reaction to the show car, but I couldn't confirm when the truck actually went on sale in Europe.
- **Med:** none of the three photos is off-road (car-show field, plaza, parking lot).
- **Med:** the repairs section is thin: 6 jobs, with the sunroof-drain job lacking parts and the diff-lock job pointing to a generic FCP category page. No sourced portal-specific repair (hub seals, damper replacement) was found.
- **Low:** the eyebrow says 2015–2018 and the plate says 2015–2017. Both are defensible, since some US trucks were titled as 2018 models.

---

## Second-generation G (`second-gen`)

### Corrections made
- **G 580 weight:** "about 7,716 lb" (TFL's figure, which equals 3,500 kg and looks like a gross rating) became "more than three tonnes (Wikipedia quotes 3,085 kg)". Added the EPA range of 239 miles next to WLTP's 294. (Wikipedia, EPA API)
- **"AMG Offroad Package Pro that swaps anti-roll bars for hydraulic roll stabilization":** unverified, so removed.
- **Lift kit:** the GwagenParts kit is **2.5-inch**, not 2-inch (the page body and the redirect slug both say 2.5-inch; it's Eurowise's kit). Corrected in the repair, the FAQ, mods and sources. Eurowise's own page was added as the primary supplier. Its warnings above 33 in were confirmed: wheel-speed-sensor faults, active brake assist, blind-spot and cruise warnings. It works with AMG Ride Control.
- **G 580 FAQ:** "hold 35° side slopes" removed. The 35° figure is The Shop's number for the combustion G, not the G 580.
- **Photos:** the alt text and captions on three of the four Pexels images were swapped between files. All four were re-matched; the `source_url` values were already correct. All four show a **Mercedes-AMG G 63**, so the captions and alts now say so.
- **Detail file:** the 2019 launch price "$149,900 (G 550) / $188,050 (G 63)" came from Wikipedia and contradicts MBUSA's 2019 spec sheet ($124,500 + $995). The MBUSA figure is now used in the timeline and values note, and the G 63 price was dropped.

### Removed or softened
- Instagram @gzilla500 and the Club G-Wagen forum were dropped.

### Added
- Sources: Eurowise W463A lift kit and EPA fueleconomy.gov. The GwagenParts source was relabelled and repointed to its canonical URL.

### Verified (no change needed)
- **Launch:** Detroit on 14 January 2018; 121 mm wider, 53 mm longer, about 170 kg lighter. (Wikipedia, SlashGear)
- **The Shop:** frame-mounted IFS with no subframe; four links plus Panhard rod; 9.5 in clearance; 27.6 in wading; 31°/30°/26°; low range 2.93 (vs 2.1), engaged up to 25 mph and back to high up to 43 mph; G-Mode; Schöckl 60%; 40:60 split.
- **SlashGear:** 10.6 in clearance under the front axle.
- **Wikipedia:** 400,000th G on 4 December 2020; 500,000th in April 2023 (agave green tribute); G 63 577 hp / 627 lb-ft; G 350 d / G 400 d outputs; G 63 4×4² figures; Final Edition 1,500 units; G 580 sales 1,450 vs about 9,000.
- **TFL:** 2025 G 550 443 hp / 413 lb-ft; Cd 0.55 → 0.48; twin 12.3-inch screens.
- **TFL and Motor Authority:** G 580 579 hp, 116 kWh, 200 kW charging, 9.8 in clearance, 33.5 in wading, 2:1 low range, G-Turn, G-Steering, US Edition One only.
- **EPA:** 2019–2020 14 mpg combined; 2025–2026 18 combined; G 580 62 MPGe.
- **Recalls:** all ten in NHTSA, including MBUSA campaign 2023030005 for 23V097.
- **MBUSA 2019 spec page:** 7,700 lb towing, GVWR, 26.4 gal, 5,551 lb, 44.6 ft, 275/55R19.

### Still unverified / shortcomings
- **High:** transfer-case, differential and battery specs are all `[CONFIRM IN MANUAL]`. The 9G-TRONIC oil pan with filter (725 270 31 14) is listed by FCP Euro for the **G 63 only**, not the G 550; the label says so, but owners could still order it for a G 550.
- **High:** the biggest-tire-without-a-lift FAQ is still marked `[TO VERIFY FOR 2019+]`. I found no owner consensus for unlifted 2019-on trucks.
- **Med:** "transfer-case output-seal leaks on 2013–2023 trucks", door-hinge sag and infotainment faults rest on au7o owner-report summaries. au7o rate-limits bots (429), so these weren't re-read.
- **Med:** the hinge, infotainment and recall repairs have no parts. There are 6 repairs and 7 buying checks, at the low end of the target.
- **Low:** the photos show an AMG G 63, not a G 550; there's no off-road photo of a non-AMG second-generation truck.

---

## Top 5 remaining problems for g-class-b

1. **Driveline fluids are unsourced across all five models (High).** Transfer-case fluid type and capacity, differential oil spec and, on the 4×4², portal-hub oil are still `[CONFIRM IN MANUAL]`. The 4×4² has no sourced driveline or portal-hub figures at all. A Mercedes WIS or STAR TekInfo lookup is needed.
2. **Diff-lock actuation by year (High).** Only a 2005 G 500 (centre lock vacuum, axle locks hydraulic) and a 1997 G 320 (brake-fluid locker circuit) are documented. Owners of 1990s Europa trucks and 2009–2018 G 550s are working from inference.
3. **Part fitment on Europa trucks (High).** Bearings, seals, damper and drag link are linked to FCP Euro pages listed only for 2002-on W463s, and the M104 head-gasket parts aren't listed for the G 320. All need confirming against VIN or EPC for 1993–2001 trucks.
4. **Photos break the off-road rule (Med).** Only the G 55 Schöckl shot and the four second-gen Pexels shots (all AMG G 63s) are off-road. The Europa, G 550 and 4×4² pages have only street, show or parking-lot photos, and Europa's hero isn't a Europa truck.
5. **Second-gen biggest tire without a lift (Med).** The FAQ still has no owner consensus for unlifted 2019-on trucks. Also, Wikipedia's $149,900 launch price conflicts with MBUSA's $124,500; the page now follows MBUSA, but the conflict should be flagged for other pages in the family that may use Wikipedia's figure.
