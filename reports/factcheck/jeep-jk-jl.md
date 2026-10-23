# Fact-check report: jeep-jk-jl

Models: `jk`, `jk-unlimited`, `jl`, `jl-unlimited`. Files: `data/pages/jeep/<slug>.json` and `data/extra/jeep/<slug>.json`.

## Method

- **Wikipedia.** I read the raw wikitext of the Jeep Wrangler (JK), (JL) and Jeep Wrangler articles, including the US sales table.
- **Quadratec reference pages.** I checked the JK 2007, 2007–2011, 2012 and Unlimited spec sheets, the JL 2020 and 2021 specs, the TJ/JK/JL differences article, the used-Wrangler checklist, both oil-change guides, the farewell article and the death-wobble/damper blog.
- **ExtremeTerrain guides.** I checked the JK fluid chart, spark-plug guide, torque page and wheel-spec page.
- **Other spec and torque sources.** I checked the Northridge4x4 torque chart, the 2020 JL owner's-manual fluid sheet (sklepjeep reprint), the WAYALIFE axle and maintenance index threads, and the Stellantis blog and press releases (2018 Rubicon capability, Xtreme Recon, Xtreme 35).
- **Press.** I checked The Drive and Hagerty (via WebFetch) on the 2024 refresh. I checked KBB on the 392 and on the 4xe recall, AutoGuide (2012 head failure and the 4xe recall), Fox News (NHTSA investigation), AARP (26V-363) and TFLcar (clutch recall, via WebFetch). I also checked the Driving Line and Performance Plus tire articles, and Auto123 on the 2026 model year.
- **NHTSA.** I pulled the NHTSA recalls API for Wrangler and Wrangler 4xe for every model year 2007–2026. Every campaign number cited in the four detail files exists, and I checked the years and summaries against it. I also read the NHTSA-hosted bulletins: TSB 09-002-14, Warranty Bulletin D-14-12, TSB 02-001-16, CSN V41 and TSB 19-002-19.
- **EPA figures.** I got these from the fueleconomy.gov API (2012 JK; 2017 JKU; 2018/2020 JL; 2022 JLU incl. 4xe).
- **Links.** I curled all 330 URLs in the eight files.
  - All 102 Quadratec part pages return 200. Quadratec returns a real 404 for bad URLs, so a 200 is meaningful. Each page title names the stated part.
  - ExtremeTerrain category and guide pages all return 200.
  - Bot-walled sites (403/Cloudflare) are real URL formats and I left them: jk-forum, jlwranglerforums, cars.com, cjponyparts, jegs, pickuptrucktalk, gearpatrol, curbsideclassic, hagerty, nhtsa.gov/recalls, mopar.com.
- **Photos.** I opened all 15 photos. Two needed alt/caption fixes.
- **Cross-links.** Every `[[...]]` link points to a slug that exists in a family `generations` list.

---

## JK (2-door): `jk.json` and `extra/jk.json`

**Corrections made**
- **Pentastar head failures.** The pages said "cracked" left cylinder heads (story, generations table, FAQ, timeline). Chrysler TSB 09-002-14 describes *excessive cylinder leakage* that sets P0300/P0302/P0304/P0306, and AutoGuide says "faulty cylinder heads". I reworded all of these to "faulty heads / misfires". The FAQ now cites the TSB, the D-14-12 X56 10-year/150k extension and the redesign reported by AutoGuide.
- **Axles by trim (extra `identify`).** It said "X/Sport has a Dana 30 front and Dana 35 rear", which contradicted the page. Quadratec's own prose and its differences article say the Dana 44 rear was standard, and that fewer than a thousand early 2007s got a Dana 35. I fixed it to match.
- **Locker availability (extra).** It said "optional on X and Sahara for 2007 only". Per Wikipedia, it was 2007 X/Sahara, then select X models for 2008–09. Fixed.
- **Recall 16V-288 (extra).** The years said "2008–2016"; NHTSA says 2011–2016 RHD, built Feb 2010–May 2016. Fixed. The summary now cross-references 11V-528, 13V-176 (2008–12 RHD) and 24V-196 (2016 RHD), all verified in the NHTSA API.
- **Recall 16V-352.** The claim that owners were "told not to drive until repaired" is not in the NHTSA summary for the Wrangler. I removed it and replaced it with the hot/humid-state scope.
- **"Quadratec's trail boss calls…".** The quote is from a Quadratec blog with no trail-boss attribution, so it now reads "Quadratec calls".
- **Unit bearing year split.** The page said "2007–11 and 2011–18 parts differ". Mopar lists 2007–10 and 2011–18 hubs, so I changed it to match.
- **Spark plugs.** "Chrysler specifies 102,000 mi" is now attributed to ExtremeTerrain with `[CONFIRM IN MANUAL]`. The 3.8 plug torque of 12 lb-ft (ExtremeTerrain) also now carries `[CONFIRM IN MANUAL]`, in both the repair and `baseline_service` (see the High item below).
- **Photo alt (`jk-snow-forest-arizona.jpg`).** It showed a "snowy, muddy track"; the image is a wet, slushy road. Fixed, and the alt now notes the visible "JK" fender decal.

**Removed or softened**
- Verdict: "they're probably worn" became "JK ones wear quickly", which is what Quadratec says.
- "Broke every Wrangler sales record" became "went on to set new Wrangler sales records". US sales fell in 2016–17, so "every" overstated it.
- The FAQ claim that adding Rubicon hardware to a Sport "costs more than the price gap" was unsourced. It is now a qualitative statement.
- The extra max-tire note credited "4.75 in backspacing" and "bang the bump stops" to JEGS/Driving Line. Driving Line's test was actually a 2017 JK **Unlimited** Sport on 4.75 in-backspacing wheels with the splash guard removed, and it concluded that aftermarket or heavily trimmed flares are needed. Rewritten to say that.
- Lug torque: "100 lb-ft (136 N·m)" is now "100 lb-ft (Northridge4x4); ET 85–125 range" plus `[CONFIRM IN MANUAL]`.

**Added**
- Death-wobble repair: Northridge4x4 torque figures (track-bar bolts 125 ft-lb, tie-rod nuts 63 ft-lb).
- Ball-joint nuts: 75 ft-lb.
- Unit bearing: hub bolts 75 ft-lb, axle nut 100 ft-lb.
- Clockspring repair: a pointer to recall 16V-290 for 2007–10 trucks.
- New sources: Northridge chart, fueleconomy.gov 2012 page (EPA 17/21 confirmed), NHTSA API, TSB 09-002-14, Quadratec differences article.

**Verified as stated** (selection)
- 3.8 EGH 202 hp/237 lb-ft; Pentastar 285/260; W5A580; NSG370/42RLE.
- Track +3.4 in, wheelbase +2 in, 2.5 in shorter than the TJ.
- 44.3°/40.4°/25.4° angles on 32s; 61.9 in track; 73.7 in width; 18.6 gal tank.
- 2,000 lb tow; 1,000 lb payload.
- LaSorda's window stunt; Moushegian design; design freeze Jan 2004.
- Call of Duty, Moab (2.72 case), 10th Anniversary millionth JK on May 17, 2013, Rubicon X, Willys Wheeler/Hard Rock, Golden Eagle (beige top).
- Last JK on Apr 27, 2018; Mopar's 250+ accessories.
- Every figure in the ET fluid chart (6 qt 5W-20, HOAT/OAT split, 42RLE/NAG1 fills, NSG370 1.6 qt, NV241 2.1 qt, axle pints, 4 oz LSD additive).
- Plug gaps and 3.6 torque; Quadratec oil-interval and 2014 filter-change notes.
- US sales 2007–2017 of 1,560,169 (sum of Wikipedia's table).
- All the other extra recalls (09V-436, 10V-236, 11V-145, 13V-234, 14V-631, 16V-290, 16V-734, 18V-021, 19V-018) and both TSBs.

**Still unverified / shortcomings**
- **High:** 3.8 spark-plug torque. ET says 12 lb-ft, which looks low for a 14 mm gasket-seat plug in aluminum heads. It needs the factory service manual. It is flagged in both places.
- **High:** JK lug-nut torque. Northridge says 100 ft-lb and ET gives an 85–125 range. I couldn't see the owner's manual, so it is flagged.
- **Med:** The JEGS 33 in / 37 in fitment figures are bot-walled and I couldn't read them.
- **Med:** I couldn't read the JK-Forum threads behind the 285/75R17 tire FAQ (403). They are cited as owner reports.
- **Low:** Two of the photos are not off-road in the strict sense (a wet road; a paved campsite loop at Lake Mead). Both are the correct generation.
- **Low:** BaT/AutoTempest value ranges were not re-derived.

## JK Unlimited: `jk-unlimited.json` and `extra/jk-unlimited.json`

**Corrections made**
- **Coolant spec (`baseline_service`).** It listed "Mopar 10-yr/150k OAT … 3.8: about 13 qt", which implies OAT in the 3.8. Per the ET chart, the 3.8 and 2012 3.6 use **HOAT** 5-yr/100k (≈13 qt) and 2013–18 3.6s use OAT (10.5 qt). Fixed, and the mixing warning now says HOAT vs OAT. *Wrong-fluid risk, now corrected.*
- **Pentastar head extension.** It said "some 2011–2013 engines" in a Wrangler context, but the Wrangler is only covered for 2012–13 (D-14-12). Fixed in the story, the buying check and the FAQ, with the misfire/cylinder-leakage wording.
- **Recall 16V-288 (extra).** The years said 2009–2016; corrected to 2011–2016 RHD with the build dates. 16V-352 was corrected as for the JK.
- **Locker FAQ.** It said "optional on some X and Sahara trucks in 2007–2009". Corrected to the Wikipedia wording (2007 X/Sahara, then select X for 2008–09, the 2015 Wrangler X and the 2016 75th Anniversary).
- **Fuel economy (extra).** It said "EPA 17/19, 2007 3.8", which matches neither EPA's current ratings nor the 2007 Wrangler 4WD rating of 15/18. I replaced it with the EPA 2017 Unlimited 3.6 figures: 16/20 automatic, 16/21 manual. The FAQ now cites EPA alongside KBB.
- **Payload (extra).** It said "1,000 lb". Quadratec's two 2007–11 sheets disagree (1,000 vs 1,150), so it now shows the range and says so.
- **Axles by trim (extra)** was fixed as for the JK.
- **Photo `jku-rubicon-emery-dugway.jpg`.** The alt claimed "a black JK Unlimited Rubicon … with a white JK behind". The image shows one white JK, head-on and far away, and neither 4-door nor Rubicon can be confirmed. I rewrote the alt and changed the caption to "JK WRANGLER · EMERY COUNTY, UTAH".
- **Dead or mislabeled part link.** "Mopar 68218657AB axle lube" returns 404 on Quadratec, and per the 2020 manual sheet that part number is actually 75W-140 *synthetic*. I removed it from the front and rear axle items and replaced it with Yukon 80W-90 and a gear-oil search.

**Removed or softened**
- The verdict line "three in four buyers never looked back" was really a statistic about listings. It now reads "by 2017 three in four new Wranglers for sale were four-doors".
- J8 callout: "It was built in Egypt" became "It was to be built in Egypt" (Wikipedia: "will be produced").

**Added**
- Northridge torque figures in the ball-joint and hub repairs.
- New sources: ET fluid chart, fueleconomy.gov 2017, TSB 09-002-14, AutoGuide 2012.

**Verified as stated**
- NY show reveal on Apr 12, 2006; $21,000; +20.6 in wheelbase; 14 in longer than the LJ.
- 4x2 until 2010; only four-door convertible until the Bronco (July 2021).
- Every Driving Line claim (2013+ for daily use, Dana 30 good to about 35 in, bendable tubes/Cs, Dynatrac/Currie/EVO, 3.8 oil burning/intake gasket/manifold, rings and bearings around 100k, NSG370 grind, aluminum t-case housings, "mechanically virtually identical").
- 2012 four-door payload 1,067–1,301 lb (Quadratec).
- Unlimited spec sheet: 44.4/40.5/20.8°, 41.2 ft turning circle, 4,075–4,340 lb.
- Brute 139 in (Defender 130-inspired); JK-8 kit; RHD postal Unlimited from 2009; J8 payload 1,339 kg and 30 in wading; 19V-680 (RHD seat belt, 2011–18).

**Still unverified / shortcomings**
- **Med:** Cars.com (2017 Rubicon tongue weight 350 lb, payload 1,178 lb, GVWR) is bot-walled.
- **Med:** Expedition Portal payload thread is behind a browser check.
- **Med:** I can't confirm from the image that the Emery photo is a four-door. Consider swapping it for a clearly four-door JK.
- **Low:** The NSG370 plug torque of 22 ft-lb comes from the JK-Forum lube chart, which returns 403.
- **Low:** 3.8 spark plugs are still `[CONFIRM IN MANUAL]`.

## JL (2-door): `jl.json` and `extra/jl.json`

**Corrections made**
- **Coolant capacities.** "3.6 engine loop ≈10.6–10.7 qt" mixed up litres and quarts. The 2020 manual sheet gives **11.2 qt (10.6 L)**, plus 1.9 qt for the MGU and 2.5 qt for the battery loop on eTorque trucks. The 2.0T is 10.3 qt (9.7 L) plus a 3.2–3.5 qt intercooler loop. Fixed.
- **Rear axle.** I added the exact figures from the manual sheet: M220 1.45 L (1.36 L with Trac-Lok), M200 1.15 L of 75W-140 synthetic, and 70 ml (2.37 oz) of limited-slip additive. I removed the 404/mislabeled Mopar 68218657AB link and replaced it with a 75W-85 search (front and rear).
- **Spark-plug gaps** added from the manual sheet: 3.6 is 0.043 in, 2.0T is 0.024–0.025 in.
- **Fuel-economy FAQ.** It quoted "Quadratec: 2.0T 23/25 vs 3.6 17/21". EPA (2018 two-door) gives 2.0T 23/25, 3.6 automatic 18/23 and 3.6 manual 17/25. Fixed, and the extra capability note now matches.
- **Recall buying check.** "Early 8-speed park and cruise-control software" became the actual campaigns: 18V-280 (park-lock rod, a hardware fix, not software) and 18V-332 (cruise control). I added 18V-675 and 23V-116.
- **Clutch repair.** I added 23V-116 (2018–23) and 24V-572. TFLcar confirms 29,818 Wranglers and the Aug 23, 2017–Feb 13, 2020 build window.
- **Damper.** It said "Its CTO said…". This is now attributed to FCA's engineers per the Quadratec/FCA quote, with the CSN V41 scope (about 192,000 2018–19 JLs).
- **Steering box.** "Replaced with steel under a TSB" became "Jeep moved to cast-iron boxes" (Quadratec). TSB 08-074-20 is now attributed to owners.
- **Xtreme 35 package (extra).** It was missing that the package is for the Rubicon **and Willys** two-door, **2.0T only**, $4,495, with a reinforced swing gate, and is standard on the 2.0T Rubicon X (Stellantis blog). Fixed in fitment, identify and editions.
- **Real Rubicon identify (extra).** Now uses the M186/M200/M210/M220 designations, with Selec-Trac as a Sahara option.
- **Recall summaries (extra).** The 21V-028 "stop-sale" claim was unsourced and is removed. The 23V-116 "recall 19A, software" detail was rewritten to the NHTSA wording.
- **Wheel offset (extra).** "+37 mm Rubicon / +44 mm Sport-Sahara" had no source; it is now `[CONFIRM IN MANUAL]`. Spare lug torque "59 lb-ft" had no source; also `[CONFIRM IN MANUAL]`.
- **Dead source.** I removed the AOL/Car and Driver link (404). The 4xe drop is now attributed to Wikipedia in the 2025 and 2026 timeline entries.
- **Photo `jl-johnson-valley-wash.jpg`.** The alt said "descending toward the camera"; the truck is seen from behind. Fixed. The caption no longer claims Rubicon, because no badge is visible.
- **Plate ground clearance** now notes both 10.8 in (Quadratec 2020) and 10.9 in (Jeep at launch).

**Verified as stated**
- LA show on Nov 29, 2017; about 90 kg lighter; raked seven-slot grille.
- 2.0T eTorque dropped for 2020; Quadratec 2020/21 specs (96.8 in wheelbase, 166.3 in length, 2,000 lb tow, 1,000 lb payload, 3,970/4,160 lb, D478 manual, 850RE).
- WAYALIFE axles (M186 7.32 in ring gear, Rubicon axles 1.5 in wider).
- 18V-675; NHTSA probe of about 270,000 JLs (Fox News); Four Wheeler and Motor Trend 2019 awards; Goldblum's silver two-door Rubicon at Super Bowl LII.
- Every Hagerty and The Drive claim about the 2024 refresh (12.3 in screen, curtains, antenna, 8,000 lb Warn, sealed power seats with 34 in wading, Dana 44 HD full-float, 33s plus locker on the Willys, Rubicon X with 35s and full-time Rock-Trac).
- Euro NCAP 1 star; the IIHS results.
- JL oil: 5 qt 0W-20, MO-349, cap 18 ft-lb, drain plug 20 ft-lb.
- 2.0T 5W-30 SN PLUS warning; 8HP50 9 L; AL6 2.25 L ATF+4; transfer cases 1.6/1.76 L; front axles 0.86/1.03 L; electric steering pump fluid.
- 130 ft-lb lugs; WAYALIFE maintenance intervals (2.0T plugs at 30k).
- 2018 Rubicon capability (44/37/27.8°, 84.2:1, 30 in wading); 2019–2025 US sales of 1,290,426.

**Still unverified / shortcomings**
- **Med:** I couldn't read the TSB 08-074-20 text, and the $1,500 steering-box dealer quotes come from a 403 forum.
- **Med:** The 34.5 ft turning circle (extra) is unsourced and now flagged.
- **Med:** I couldn't access the Pickup Truck + SUV Talk known-problems article (eTorque battery, turbo coolant-line TSB). Those claims stand as attributed but unverified.
- **Low:** JL length is 166.3 in per Quadratec and 166.8 in per Wikipedia; the page uses Quadratec.
- **Low:** The 2024 5,000-lb towing figure may also apply to two-door Rubicons with the HD axle; the page still says 2,000 lb for every two-door. Needs a 2024 spec sheet.

## JL Unlimited: `jl-unlimited.json` and `extra/jl-unlimited.json`

**Corrections made**
- The story's "grew 3.5 inches … to a 118.4-inch wheelbase" implied a 3.5 in wheelbase gain. The 3.5 in is overall length (Wikipedia); the wheelbase gained 2.4 in. Reworded.
- Coolant, rear axle, spark-plug gap, recall check, damper, steering box, clutch and front-axle part fixes were applied as for the JL. The coolant spec adds the EcoDiesel's 12 qt (11.4 L).
- The buying check now lists both EcoDiesel pump recalls (22V-767 and 23V-263).
- **Rubicon 392 tires.** The FAQ and extra said it "rides on LT315/70R17s from the factory". This is now attributed to Performance Plus, with a caution that the 35s were also part of the optional Xtreme Recon package.
- **Selec-Trac identify (extra).** It said Rubicons use Rock-Trac, but the 392 uses Selec-Trac (Quadratec 2021). Fixed. I removed the unsourced claim that the Willys 4xe has a 2.72:1 Selec-Trac.
- **Fuel economy (extra).** "21 mpg combined (2.0T)" became EPA 22 mpg combined (2022 2.0T). The 4xe is 49 MPGe and 20 mpg, with 21 miles of electric range at launch and 22 for 2022.
- **4xe callout.** "AutoGuide counted 13 fires of parked, switched-off vehicles" went beyond the source. It now reads "an internal review … turned up 13 fire incidents".
- **Oil FAQ / baseline.** It claimed "2.0T and 4xe" share the 5W-30 spec. The 2020 sheet predates the 4xe, so 4xe oil is now `[CONFIRM IN MANUAL]`.
- **AEV DualSport XP kit.** Quadratec lists it for the **Rubicon 392**. The name is now labelled with "check fitment".
- **Max tire (extra).** "Rubicon 4xe sits about 2 in lower" became Performance Plus's actual claim: about 2.1 in less running clearance, because of the added weight.
- Removed the dead AOL source; the 4xe and 392 timeline is now attributed to Wikipedia and KBB.

**Verified as stated**
- Four-door production from November 2017; 118.4/188.4 in.
- EcoDiesel 260 hp/600 Nm (443 lb-ft), dropped for 2024.
- 4xe 375 hp/470 lb-ft, 17 kWh, 21 mi, 49 MPGe; Sport S 4xe and four-outlet Power Box (The Drive); E-Save about 50% (Hagerty).
- 392: 470/470, Selec-Trac MP3022, ZF 8HP75, 1,351 lb payload, $101,990 (KBB), Broderdorf quote (KBB, Aug 2025).
- Quadratec 2020 payloads (Sport 1,190 / Sahara 880 / Rubicon 892 lb) and weights (4,201/4,439/5,103 lb); 21.5 gal tank.
- 5,000 lb tow with the 2024 HD axle and the automatic, non-4xe (Hagerty).
- IIHS 2020 and 2022 Marginal ratings.
- KBB 4xe recall: 154,032 vehicles, park outside, don't charge.
- All 4xe and EcoDiesel recall IDs and years (23V-787, 24V-720, 25V-741, 22V-768, 22V-865, 25V-710, 25V-766, 22V-767, 23V-263, 18V-786).
- 26V-363 (AARP: about 1,077,000 vehicles, 51 fires, park outside).
- Xtreme Recon (2021: 35s, 4.56, 1.5 in lift, 47.4/26.7/40.4°, 12.9 in, 33.6 in wading; 4.88 gears optional on the Rubicon).
- EcoDiesel oil (9 qt 5W-40, MS-12991) and B5/B7 biodiesel rules; 4xe dropped from the US in 2025; 2026 Moab 392 and door hinges (Auto123).

**Still unverified / shortcomings**
- **High:** 392 oil and 4xe oil specs are not given (`[CONFIRM IN MANUAL]`). Owners of these trucks get no fluid figure here.
- **Med:** The 4xe 17.2 gal tank and the 255/55R20 Sahara 4xe tire come from Pickup Truck + SUV Talk (403). Flagged.
- **Med:** The 25V-741 vehicle count (320,068) isn't in the NHTSA API summary, so I couldn't confirm it.
- **Med:** EcoDiesel fuel-filter part: the page only links a RockAuto catalog. No specific filter part number is sourced.
- **Low:** The extra's 2021 turning circle (39.4 ft) and 4xe wading depth (31.5 in) are unverified.

---

## Top 5 remaining problems (group)

1. **High: JK 3.8 spark-plug torque.** ExtremeTerrain's 12 lb-ft is the only source and looks low for this plug; it needs the Chrysler service manual. It is flagged `[CONFIRM IN MANUAL]` on the JK page; the JKU page has no 3.8 plug spec.
2. **High: JK lug-nut torque.** The 100 lb-ft figure (Northridge) and the 85–125 range (ET) haven't been checked against the owner's manual. It is a wheel-safety number and is flagged in both JK detail files.
3. **High: no oil specs for the JL Unlimited 4xe and Rubicon 392.** They are marked `[CONFIRM IN MANUAL]`; a 2021+ owner's-manual fluid page would close this.
4. **Med: unreadable sources.** Several forum-sourced repair claims rest on bot-walled pages I couldn't read: the steering-box TSB 08-074-20 and its $1,500 quotes, the JK-Forum tire threads, the NSG370 plug torque, and the Pickup Truck + SUV Talk issue list. They are attributed but not independently verified.
5. **Med: photos.** The JKU Emery County photo can't be confirmed as a four-door (the caption is now generic). The JK set includes a wet-road shot and a paved campsite shot rather than trail use. A clearly four-door JK on dirt would strengthen `jk-unlimited`.
