# Fact-check report: nissan-patrol (Y60 flagship, Y61)

Scope: `data/nissan-patrol.json` (family object + Y60 page), `data/pages/nissan-patrol/y61.json`, `data/extra/nissan-patrol/y60.json`, `data/extra/nissan-patrol/y61.json`, and all 8 photos in `site/img/nissan-patrol/`.

Method: Wikipedia raw wikitext (Nissan Patrol, TD, ZD, TB and RD engine articles), 4X4 Australia (every-generation buyers guide, 1988 GQ project car, 2016 Legend Edition review, 70th-anniversary news), CarsGuide (GQ used review, GU used review, TD42 guide, ZD30 guide, problems Q&A, Legend Edition news; read through WebFetch because curl gets 403), GoAuto, Marque News, CarExpert spec pages, Curbside Classic, JDM Buy Sell Y60/Y61 guides, ExplorOz and NissanPatrol.com.au threads, Patrolapart/HD Automotive product pages, and Wikimedia Commons metadata for every photo.

Links: I curled all 179 original URLs. 144 returned 200. 34 returned 403 from bot-blocking sites (CarsGuide, NissanPatrol.com.au archive, patrol4x4.co.za, Curbside Classic, JDM Buy Sell, NHTSA, TJM, Fulcrum). All of these are in the sites' real URL formats, and I opened the key ones with WebFetch to confirm their content. koleso.ee timed out once and returned 200 on retry. I checked the titles of every 200 page: all are the right product or page, with no soft redirects to a home page. I then curled all 31 newly added URLs: 28 returned 200 and 3 returned 403 (CarsGuide and two Supercheap search URLs, which are Cloudflare rate limits on the real URL format). All Instagram handles exist: @gq_patrol is confirmed through Instagram's API, and @patrolapart_navarapart and @hulk_4x4 are linked from the suppliers' own websites. All YouTube channels return the right channel titles.

Cross-links: every `[[family/slug|…]]` and every `related` entry points to a real slug (land-cruiser/fj60, 70-series, 80-series, 100-series; land-rover/defender-90-110; nissan-patrol/y60, y61).

---

## Family object (`data/nissan-patrol.json` → `family`)

**Corrections made**
- Intro paragraph 1 said the 1962–69 Datsun-dealer Patrol was "the only time a Nissan-badged Patrol was offered here until the Infiniti QX56 and the Nissan Armada". That was muddled: the QX56 is Infiniti-badged, and the 2004–16 Armada wasn't Patrol-based. It now reads "the only time a Patrol was sold in North America until the Patrol-based Infiniti QX56 arrived for 2011 (and, from the 2017 model year, the Nissan Armada)" (Wikipedia, Nissan Patrol intro and Y62 section).
- Intro paragraph 2 said the Y61 "stayed in production until April 2024". Wikipedia's prose flags its 2024 end date as "citation needed". It now reads "was still being built for the Middle East in 2024" (JDM Buy Sell Y61: "Middle East production continued into 2024").

**Verified:** the 4W60 of 1951 (Jeep-like, Japan only); the 60 Series of October 1960 in 60/G60 form; US and Canadian sales from 1962 to 1969; the 160 Series as MQ and then MK from 1983, with the SD33; the Y62 of 2010, the QX56 for 2011 and the Armada for 2017; the Y63 unveiled in Abu Dhabi on 3 Sept 2024. All are from Wikipedia and 4X4 Australia.

**Still unverified / shortcomings**
- Low: forum notes ("busiest GQ board on the internet") are opinion, not fact. They're fine as voice.

---

## Y60 (GQ): page (`data/nissan-patrol.json` → `page`) + `data/extra/nissan-patrol/y60.json`

**Corrections made**
- **Story, petrol paragraph:** the page said 4X4 Australia's 1988 TB42 "drank about 20 L/100 km and boiled three times on one High Country climb". The article gives no L/100 km figure. It says the gauge "rocketed to boiling point" and then the truck "boil[ed] over three more times", so four times in all. I rewrote the sentence to match and quoted "the TB42 loves a drink" (4X4 Australia, 1988 GQ 4x4 shed).
- **FAQ "fuel economy":** I removed the unsupported "about 20 L/100 km (12 mpg)" figure for the TB42 project truck (same source).
- **FAQ "oils and capacities" + baseline engine-oil spec (High):** these were presented as "for a TD42 manual". The source thread (NissanPatrol.com.au t-3459) comes from a 1990 GQ DX 4.2 manual owner who never says whether his engine is a TD42 or a TB42. Gregory's grades are as quoted (20W-40 engine oil, 75W-90 GL-4 gearbox and transfer, 80W-90 GL-5 diffs). The capacities are the owner's own fills (8.2 / 3.9 / 2.2 / 5.4 / 3.0 L). I reworded both entries to say that and kept "confirm in manual".
- **FAQ "biggest tire":** "about -22 mm offset" became "negative-offset wheels (owners quote -22 to -24 mm)". t-30409 gives -22, t-8162 gives -24 on an 8-inch rim, and both threads were verified. The rub location (mud-flap bracket at full lock or flex) is now stated as in t-30409.
- **Generations table, RD28T row:** "Early 1990s–1997" became "1992 or 1995–1997 (Australia; sources differ)". CarsGuide's GQ review says it arrived with the 1992 update. 4X4 Australia's buyers guide and its 70th-anniversary piece both say 1995.
- **Generations table, Safari TD42T row:** "1991–1997" became "Early 1990s–1997". Wikipedia's Patrol article says 1991, its TD-engine article says 1993, and JDM Buy Sell lists it for the 1993–94 Kingsroad.
- **Extra timeline 1991:** the TD42T date conflict is now noted. **1992:** the RD28T EGR and oil cooler are marked as applying "in markets that had it". **1995:** now notes the RD28T date conflict and that Wikipedia lists the RX grade from 1994–95.
- **Extra production, Australian sales:** now attributed to "Nissan Australia figures as quoted by JDM Buy Sell" (verified on that page).

**Removed or softened**
- Extra `community`: I removed "Founded in 1976" because the club's site doesn't state it. The 94 ha near Windellama, the training and "all makes welcome" are all confirmed on nissanpatrolclub.org.

**Added (sourced)**
- Buying check "swivel hubs": CarsGuide's GQ review says rear diff-seal leaks are common.
- Buying check "4WD test": Wikipedia records fifth-gear bearing failures in high-mileage European five-speeds.
- RD28T timing-belt repair: Wikipedia's RD-engine article warns that the crank/balancer bolt can loosen, so use thread-locker.
- Sources: Wikipedia (Nissan RD engine) and JDM Buy Sell Y60.

**Verified, no change needed:** the coil-sprung 3-link/5-link layout; leaf-sprung utes to 1994; sway bars and power steering; LSD on most trucks and the vacuum/electric locker; the PTO winch; 24 V Safaris; engine outputs (TB42S 125/325, TB42E 135/320 per Wikipedia and 129 kW per CarsGuide/CarExpert, TD42 85/264, RB30 100/224, RD28T 92/255 per Wikipedia and 85/235 per 4X4 Australia); the RB30 arriving in 1990; FS5R50A and RE4R03A gearboxes; wheelbases and lengths; the 100 L tank (Wikipedia) and 95 L (CarExpert 1997 ST), both already noted; August 1993 TD42 lightening and Silvertop/Blacktop; TD42 manual-only in Australia, the gear-driven cam ("set-and-forget"), 12–14 L/100 km and "half-a-million-kilometre engine" (all CarsGuide TD42); overheating causes (CarsGuide); the 70–80 km/h shimmy and shim fix (CarsGuide GQ); petrol heads cracking on LPG with low coolant (CarsGuide GQ); the Series 2 contents (Wikipedia, 4X4 Australia); the 80 Series in 1990 and "essentially a GQ" GU at +230 kg (4X4 Australia); Ford Maverick body styles, trims, no Ti equivalent, badge-only changes, not built in Australia, and rural/fleet dealers (Curbside Classic); the 33-inch "but only just" quote (patrol4x4.co.za); 1997 ST towing 2,800/750 kg, 13.4 m turning circle, 2,100 kg and 265/70R16 (CarExpert); the JDM chassis codes, Kingsroad Aug 1993, 2,110 kg Granroad and 31x10.50R15 (JDM Buy Sell). All 25 supplier part links return 200 with matching product titles.

**Photos** (all opened and checked against their Commons metadata)
- `y60-budapest-bamako-sahara.jpg`: a white Y60 wagon on dunes, Norwegian team, Budapest–Bamako 2014. Matches the caption. OK.
- `y60-tibet-everest-ford.jpg`: a dark green-grey Y60 ("Fuel Injection" decal) fording a creek on the Tingri–Everest trail in 2007. A silver non-Nissan SUV is also in the frame. OK.
- `y60-swat-snow.jpg`: a pre-facelift high-roof Y60 in snow at Kalam, from the Islamabad Jeep Club snow rally in 2013. OK.
- `y60-dakar-1998.jpg`: a red Patrol GR Y60 (préparation Dessoude, Motorsport Lora Lamia) on the Smara–Zouerat stage of the 1998 rally. One front wheel is lifted, so "airborne" is a slight stretch. OK.

**Still unverified / shortcomings**
- **High:** fluid capacities and grades are owner figures, not factory data (engine ≈8.2 L, gearbox 3.9 L, transfer 2.2 L, front 5.4 L, rear 2.5–3.0 L). Rear-diff oil weight differs between sources (Gregory's 80W-90 GL-5, owners 85W-140 LS). A factory service manual figure per engine is needed. All entries carry [CONFIRM IN MANUAL] or a "confirm" note.
- **High:** TD42 tappet clearance (0.35 mm from one forum member) and the 20,000 km interval are single-owner figures. Already flagged [CONFIRM IN MANUAL].
- **Med:** RD28T timing-belt interval (≈100,000 km, from an ExplorOz owner) is not a factory figure.
- **Med:** forum-only claims I couldn't open (NissanPatrol.com.au returns 403 to curl): GQ automatic rebuilds at about A$3,000, the 54 mm hub-nut socket, the front-bearing procedure in t-28142, and door-hinge and rust checks. They're plausible and attributed to forum members.
- **Med:** the extra `values` band (17 BaT sales, $5k–$41.5k) wasn't re-verified sale by sale.
- **Low:** the Y60's GQ/GR code split. Wikipedia oddly ties the codes to RHD/LHD, while the page uses the common Australia/Europe usage. Left as is.
- **Low:** "Team Nissan France Dessoude racing Y60 GRs in 1998" rests on the Commons photo caption only.

---

## Y61 (GU): `data/pages/nissan-patrol/y61.json` + `data/extra/nissan-patrol/y61.json`

**Corrections made**
- **Fabricated quote removed (High for credibility):** the story said "CarsGuide's David Morley writes that it was remembered 'neither for those attributes nor remotely fondly'". Neither the CarsGuide GU review nor the ZD30 guide contains that line. I replaced it with a verified CarsGuide quote: "has a history of breaking pistons due to poor engine management and boost spikes".
- **ZD30 oil spec (High):** "Nissan Australia specifies 10W-40 ACEA B3 at no more than 10,000 km or 6 months" wasn't in any cited CarsGuide page. ExplorOz owners quote Nissan service bulletin MA-04-001 (30 Sept 2004): ACEA B3 or JASO DH-1, 10W-40 strongly recommended, retrospective to all ZD30s. I corrected the story, the buying check, the FAQ, the baseline engine-oil item and the extra TSB list to that wording. The "6 months" interval is gone and the interval is marked [CONFIRM IN MANUAL]. Added the bulletin as a TSB entry in the extra file.
- **Rear diff oil (High):** the rear-axle repair, manual-gearbox item and diff item all linked "LSD gear oil 80W-90". An owner quoting the Nissan workshop manual and Gregory's on ExplorOz (t-42218) gives API GL-5 SAE 140 plus LSD friction modifier, and owners use 85W-140 LSD. I changed the specs and part links to 85W-140 LSD with [CONFIRM IN MANUAL]. The manual-gearbox link is now a 75W-90 gear-oil search, not LSD diff oil.
- **"Series IV/V" (Med):** GoAuto confirms there was no GU V; the series after IV is GU VI (Sept 2007). I fixed the table row and the FAQ, and the story now says so.
- **Panhard-rod fitment (Med):** the page said "Series 4 and later panhard rods differ". Patrolapart's listings split fitment at the **Series 2 wagon** (GU2-on vs GQ/GU1). I corrected the engineering note and the caster repair.
- **Legend Edition low range "2.02:1":** no source found, so I removed it. The Legend Edition contents are now verified: 300 units, rear diff lock, steel bar with Warn winch, snorkel, roof rack, tow bar, and 3,200/2,500 kg towing (4X4 Australia Legend review; CarsGuide Legend news).
- **TD42 discontinuation:** "In 2007 … because it couldn't meet Euro IV" now notes that 4X4 Australia and Marque News say 2006, while Wikipedia (ZD engine article) gives MY2007 and Euro IV. I updated the table and the extra timeline the same way.
- **Wheelbase:** the page gave only 2,970 mm. Wikipedia lists a 2,400 mm SWB three-door, so I updated the engineering cell, the plate and the story.
- **Series IV facelift:** I removed "Nissan Australia described it as a major facelift with no mechanical changes" because there was no source. It now reads "October 2004… new interior, 17-in alloys on ST and Ti" (4X4 Australia, GoAuto).
- **Series III table note:** I removed "TD42Ti offered on every variant except the Ti" (unverified). Added TD42Ti 114 kW / 360 Nm from 2003 (4X4 Australia).
- **2006 TB48:** "Euro III and auto-only" became "revised 180 kW / 400 Nm from February 2006 (GoAuto)".
- **FAQ "biggest tire":** I removed the unsourced "50 mm larger than placard" Australian rule. ExplorOz owners quoted state limits of 15–25 mm in the 2000s, so the rule wasn't safe to state. Owners are now told to check their state's current limit, and the FAQ notes that Nissan sold a 265/75R16 replacement placard (ExplorOz t-3667). The stock-height advice now leads with the verified 265/75R16.
- **FAQ "Why does front drive drop out":** I removed the unsourced "engage with the truck stationary and in neutral" instruction, which could be wrong for this box. It now gives the verified CarsGuide quote and tells owners to follow the manual procedure.
- **FAQ "Which engine":** I tightened it to CarsGuide's verbatim verdict ("very leery of any RD28 or ZD30…").
- **Overheating repair:** I removed the unsourced "ease off at around 450–500 °C" rule and replaced it with the owner-reported 300–450 °C cruise and about 600 °C climb (ExplorOz t-42467).
- **Lead and plate:** the AU sales figures are now attributed to JDM Buy Sell (verified there). "Production finally ended in 2024" became "reportedly", and "Dec 1997" on the plate became "Oct 1997", per Nissan Japan via JDM Buy Sell and the Wikipedia infobox.
- **Extra timeline:** 2000 now says the NA TD42 left wagons "reportedly"; 2006 and 2007 are rewritten as above. The 2007 "CarsGuide still reports piston failures on 2008–09 ZD30s" claim is now worded as Q&A questions from owners.
- **Extra community:** removed the unverified "Founded in 1976".

**Part links (High for usefulness).** The Y61 page relied on generic Supercheap Auto searches, including non-vehicle-specific ones like "coolant long life" and "brake fluid dot 4" against a spec that said [CONFIRM]. I replaced them with GU-specific product pages, each curled to a 200 with a matching title:
- **Patrolapart:** ZD30, TD42 (large thread), TB45/TB48 and RD28 oil filters; GU diesel air filter; ZD30 common-rail and VP44 fuel filters; TD42, ZD30 VP44, ZD30 common-rail and RD28Ti glow plugs; RD28 timing-belt kit; TD42 76.5° and ZD30 VP44/common-rail thermostats; GU TD42 manual radiator; TD42 viscous hub; H233 rear axle seal and inner bearing; diff gasket; front hub bearing seal; GU hub-nut socket; GU auto hub; HULK and genuine manual hubs; Pedders caster bushes; Roadsafe GU2+ panhard rod; ARB front Air Locker; VDO EGT kit.
- **HD Automotive:** GU front wheel-bearing kit and GU front pads.
- The TJM panhard rod was confirmed by WebFetch as "to suit the front of Nissan Patrol GU raised vehicles".
- Generic consumables (boost gauge, catch can, ATF, coolant, 85W-140 LSD oil, 75W-90 gear oil, brake fluid) stay as clearly labelled searches.

**Added (sourced)**
- The Sept 2004 oil-spec bulletin (ExplorOz t-32377) and the Nissan rep's 9 L advice (ExplorOz t-33801), in the repair and FAQ.
- Gregory's front-bearing torque procedure (167–196 Nm, back off, 3–5 Nm, 0–18.6 N preload) added to the baseline item with [CONFIRM IN MANUAL]. Verified in ExplorOz t-43679, which also notes that a Lonard's procedure differs.
- The CarsGuide petrol economy (15+ highway, 20+ town) and the CarExpert 2012 ST at 10.9 L/100 km in the fuel FAQ.
- The intercooler-leak check (NissanPatrol.com.au t-37496 via WebFetch) and the dash-blister warranty extension (JDM Buy Sell) in the buying checks.
- RD balancer-bolt thread-locker note in the timing item (Wikipedia RD engine).
- 12 new sources in `sources`, and 2 new sources in the extra file.

**Verified, no change needed:** the Dec/Oct 1997 launch; larger CVs, fewer synchros and wider housings on H233/H260 (Wikipedia); the Australian launch engines and outputs (TB45E 145 kW, RD28ETi 95 kW, TD42 91/272, TD42T 114/330 from 1999, ZD30 116 kW in 2000, TB48 185/420 in 2001) per 4X4 Australia; the timing belt/chain/gears split (CarsGuide GU); ZD30 failures on #3/#4 pistons, holed crowns and ring lands, the EGR/MAF/vent/boost-spike suspects, and 6 L → 8.3 L with recalibrated dipsticks (CarsGuide ZD30 and Q&A); the common-rail ZD30 at 118 kW / 380 Nm manual and 354 Nm auto (Wikipedia ZD); dual airbags standard from 2007 (CarsGuide); towing by engine (CarsGuide GU); GU II April 2000, GU III Oct 2001, ST-L in 2003, GU IV Oct 2004, GU VI Sept 2007, GU VII 2010, and petrol replaced by the Y62 in Feb 2013 (GoAuto); the Gulf Super Safari brochure (280 hp SAE gross, rear lock, VDC, winch, tan leather), the 245 PS Granroad Limited of Nov 2002, and the rear LSD from Sept 1999 (JDM Buy Sell); the TB48 tuning scene and the UN and military use (Wikipedia); the GU cab-chassis crack reports (ExplorOz t-75800); 2003 and 2012 ST specs (CarExpert); lug torque 118–147 Nm (owner's manual quoted in ExplorOz t-72073); the 2010 DX cab-chassis economy and LSD (nissanpatrol.com.au/gu.html); and the GU wagon handbook capacities of gearbox 3.8 L, transfer 1.9 L, front 5.4 L and rear 2.1 L (ExplorOz t-42218).

**Photos**
- `y61-oman-dune.jpg`: a silver Y61 wagon climbing a dune in Oman (2008). The "facelifted" claim is plausible from the larger tail lamp, but the front isn't visible. OK.
- `y61-barred-creek-camp.jpg`: a 2001 GU with an ARB Simpson rooftop tent near Broome. Matches the Commons description. **Only 800×600**, which is low resolution for a hero or gallery image.
- `y61-iceland-snow.jpg`: two Y61s (pre-facelift fronts) recovering in deep snow between Laugarvatn and Þingvellir in 2003. OK.
- `y61-cab-chassis-bush.jpg`: a GU ST cab-chassis with a service body (Audley, NSW, 2009). It's parked on grass, not driving off-road, and it's mostly a tradie service body, so it's weak against the "off-road only" photo rule.

**Still unverified / shortcomings**
- **High:** non-ZD30 engine oil specs and capacities, ATF type, transfer-case fluid (one owner quotes Dexron III, 1.9 L), coolant type and brake-fluid DOT rating are all [CONFIRM IN MANUAL]. A GU workshop-manual capacities table per engine would close this.
- **High:** the front-bearing preload figures come from one Gregory's quote, and a Lonard's procedure differs. Flagged in-page.
- **Med:** the RD28 timing-belt interval isn't given anywhere.
- **Med:** forum-only GU repair steps I couldn't open (403): the six 8 mm Allen bolts and 22 mm caliper bolts (t-15316), the A/C cut-out from the radiator sensor (t-51998), fifth-gear spline and 2nd–3rd synchro wear, and rear-door window cracks. All are plausible and attributed to owners.
- **Med:** the Y61 page has no `social` entries. No GU-specific accounts were verified.
- **Med:** the approach/departure angles (37°/31°) and 210 mm clearance in the extra capability section are only partly verified. CarExpert confirms the 210 mm clearance; the angles weren't checked.
- **Med:** the extra `values` (BaT sales) weren't re-verified sale by sale.
- **Low:** the TB48DE output is quoted variously as 184 kW (GoAuto) and 185 kW (4X4 Australia, CarExpert). Left at 185 kW (Australia).
- **Low:** the Barred Creek photo is low resolution, and the cab-chassis photo isn't an off-road scene. Consider replacing both.

---

## Top 5 remaining problems for nissan-patrol

1. **High: factory fluid capacities and grades are still missing for both models.** Every capacity is an owner or Gregory's-quoted figure. The GQ rear-diff grade conflicts between sources (80W-90 GL-5 vs 85W-140 LSD), and GU engine-oil capacities for non-ZD30 engines, ATF, transfer fluid and coolant are unconfirmed. A factory service manual check per engine is the biggest remaining gap.
2. **High: torque and adjustment specs come from single forum sources:** the GU front-bearing preload (two procedures disagree), the TD42 tappet clearance (0.35 mm, intake/exhaust not split), and the RD28/RD28T belt interval.
3. **Med: much repair detail cites NissanPatrol.com.au archive threads that return 403 to scripted checks.** The ones I could WebFetch held up, but about 10 GQ/GU forum-sourced claims weren't individually re-read.
4. **Med: dates for the RD28T (GQ, 1992 vs 1995), the TD42T (Japan, 1991 vs 1993) and the end of the TD42 (GU, 2006 vs 2007) conflict between reputable sources.** The pages now show both dates, but a Nissan Australia or Japan press source would settle them.
5. **Low/Med: photos and social.** The Y61 Barred Creek image is 800×600, and the Y61 cab-chassis image is a parked service-body ute rather than an off-road scene. The Y61 page has no verified social accounts, and neither model's BaT `values` bands were re-verified sale by sale.
