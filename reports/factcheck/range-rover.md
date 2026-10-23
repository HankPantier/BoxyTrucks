# Fact-check report: range-rover group

Scope: Classic (flagship page and family object in `data/range-rover.json`, plus `data/extra/range-rover/classic.json`), P38A, L322, L405 and L460 (pages in `data/pages/range-rover/` and detail files in `data/extra/range-rover/`). I opened all 17 photos.

How I checked:
- **Links.** All 500 unique URLs were curled. 376 returned 200. 109 returned 403 from sites that block bots (Rovers North, AULRO, nhtsa.gov, BolidenForum, Pexels, Top Gear, roverparts.com and others). Those URLs are in each supplier's real format. 6 returned 404, and those are dealt with below.
- **Product pages.** About 120 product URLs were checked by title. More than 40 Lucky8 products were also checked for fitment through Shopify `.json`.
- **Recalls.** Every NHTSA campaign number cited was checked against `api.nhtsa.gov`, by vehicle and by campaign.
- **Fuel economy.** Every EPA figure was checked against the fueleconomy.gov web service.
- **History and specs.** Checked against Wikipedia's raw wikitext for all five generations, plus Land Rover, Range Rover USA, Hagerty UK, Atlantic British Roverlog, the Dunsfold Collection, Motor1 and Australian Car Reviews.
- **Cross-links.** All `[[family/slug]]` and `related` entries resolve to real generations.
- **Files.** All edited files are valid JSON with the schema unchanged. A backup of the pre-edit data is in the scratchpad.

---

## Range Rover Classic (flagship and family)

**Corrections made**
- **Louvre.** The page said the Classic was "the first car exhibited at the Louvre". Range Rover's own heritage page says that in 1971 a **quarter-scale model** took a leading role in the "Idea and Form" exhibition at the Musée des Arts Décoratifs, in the Louvre's Pavillon de Marsan. The text now says that, and notes that Land Rover bills it as the first vehicle displayed at the Louvre. Sources: rangerover.com "Range Rover at the Louvre"; Automotive World (LR 45-year release).
- **Velar name.** The etymology is now attributed: Latin *velare*, "to veil or cover", per Land Rover (landrover.in Velar launch release).
- **Paris–Dakar.** The page said the Classic "won the 4WD class". It now says Range Rovers won the first Paris–Dakar in 1979 and won again in 1981. Source: LR 45-year release. Wikipedia's "4WD class" wording understates this.
- **3.9 V8 timing.** "3.9 litres for 1989–90" is now "for the 1989 model year" (Wikipedia, Engines).
- **Soft dash.** The page said the soft dash "borrowed its steering wheel from the Discovery". Wikipedia says the dashboard itself was derived from the facelifted Discovery's, with Rover 800 switches. Corrected.
- **US launch order.** The truck was officially introduced at the LA Auto Show in January 1987, and imports began on 16 March 1987. The old sentence put these in the wrong order.
- **Hagerty prices.** "Tenfold in the decade to 2020" is now "almost tenfold over a decade", which is what Hagerty UK actually says. The article is undated.
- **Darién Gap sidebar.** Now reads: "Darién transit took 96 days; mud-packed swamp tyres broke three differentials; development engineer Geof Miller flew out". Sources: Atlantic British Roverlog; Dunsfold Collection.
- **Dead link.** The Dunsfold URL returned 404. It is replaced with `dunsfoldcollection.co.uk/collection/trans-americas-expedition/`, which confirms VXC 765K, the 18,000-mile route and the diff failures.
- **ABS dating.** The baseline brake note said "ABS trucks (late soft-dash)", which contradicted the engineering cell ("ABS around 1990"). It now says "from about 1990".
- **Photo alt text.** The In Guezzam photo no longer claims the truck is a "Turbo D". That can't be confirmed from the image or the file name.

**Removed or softened**
- The upper tailgate "replacement runs around $800 or more" claim was removed because no source supports it.
- The baseline oil note now cites Hagerty's specialist (about 7 L of 20W-50 every 6,000 miles or 12 months). It sits alongside the BolidenForum 10W-40/50 figure, so the FAQ and the baseline no longer seem to contradict each other.
- The detail file's wheel thread (M16x1.5) is now marked as coming from wheel-spec databases [CONFIRM ON YOUR STUDS].

**Added**
- Sources: Range Rover "at the Louvre"; Land Rover India's Velar release; Automotive World's LR 45-year release.

**Verified as correct**
- Production of 326,070 (Wikipedia; Land Rover's release says 317,615, and the detail file already notes the discrepancy).
- Four-door from July 1981; two-door made to January 1994, mainly for France.
- 135 hp at launch; power steering from 1973.
- VM 2.4 (1986) and 2.5 (1989); 200Tdi (1992) and 300Tdi (end of 1994).
- Towing of 3.5 tons (launch claim).
- The LT95 / LT77 + LT230 (1983) / Borg Warner viscous-coupling story.
- Air suspension from late 1992 on 1993 model-year trucks.
- 16 March 1987 imports; Playboy "Best 4x4" (1988).
- All 6 NHTSA recalls, with years matching the API.
- EPA 11/15/13 (1990 3.9) and 11/15/12 (1995 County LWB).
- Lucky8 fitments: LR059968 swivel seal; STC3435 grease ('87–'95); STC483 pump; STC3135 heater core; ETC4765; TF1003.
- Photos: all four show Classics and are off-road.

**Still unverified / shortcomings**
- **High.** Fluid capacities come from BolidenForum (a 1991–92 data sheet, behind a 403) rather than a factory manual. The swivel fill (0.33 L), PAS (2.8 L) and ATF (9.5 L) figures should be checked against the RRC workshop manual.
- **High.** Lug torque of 130 N·m and the M16x1.5 thread are not confirmed from a factory source.
- **Med.** The viscous-coupling test procedure and the "RTC6044 same on Classic and P38A" claim rely on Ashcroft and LandRoverWorld. Ashcroft's page title loaded but I couldn't read its contents.
- **Med.** Many repair part links are Rovers North and Atlantic British *search* URLs, not product pages. Rovers North returns 403 to bots.
- **Low.** The forum archive links on forums.roversnorth.com are 403 to bots and couldn't be confirmed live. The tflcar.com source returns a 307 redirect loop.

---

## Range Rover P38A

**Corrections made**
- **BECM location.** "Under the passenger seat" is now "under the right-hand front seat (the passenger seat on US trucks)", in both the story and the buying check. Atlantic British's coil-conversion instructions say the BECM is behind the right front seat's lower surround. On UK right-hand-drive trucks that is the driver's seat.
- **Designer.** "George Thomson is credited with the 1990 design" is now "styling director George Thomson's in-house design was chosen over a Bertone proposal" (Motor1). No source gave a 1990 design date.
- **Traction control.** The page said four-wheel traction control came on all V8s from mid-1999. Wikipedia only says "later versions" got it. The story, the engineering cell, the generations table and the detail-file timeline now say "later trucks".
- **Diesel EGR timing.** "From 1997" is now "post-1998 engines" (Wikipedia).
- **Gearbox fluid.** The baseline item listed only the ZF 4HP24. It now says 4HP22 (4.0 and diesel) / 4HP24 (4.6), and the 11 L fill is attributed to the 4HP24, with 4HP22 marked [CONFIRM IN MANUAL].
- **Coolant figures.** The page gave 11.3 L in the buying check, 11.4 L in the baseline and "3.5 gallons" (13 L) in the repair. These are now consistent at about 11.4 L, with a drain of about 11–12 L.
- **Photo alt text.** The Rejvíz photo was described as on a "mountain track". It is actually parked on wet tarmac, so the alt text now says so. "Winched aboard" is now "lifted aboard" in the ferry alt text, because the image shows crane slings.

**Added**
- Sources: Motor1 P38 history; Atlantic British coil-conversion instructions.

**Verified as correct**
- Pegasus / Discovery / Block 38A naming; the LP code.
- V12 M73 prototypes (Wikipedia).
- 4.0 at 190 hp and 4.6 at 230 hp (GEMS); 188/218 hp (Bosch).
- M51 at 136 hp / 270 Nm.
- 4.6 automatic only (4HP24), with a 4-pin rear diff.
- BorgWarner 4462 with electric shift.
- Five EAS heights.
- Production of 167,259 (Wikipedia figure, marked "citation needed"; the page already says "uncited").
- 6 of 7 NHTSA recalls confirmed directly. 00V-142 (idler pulley) is filed as 00V142001 and covers 1999–2000 Range Rovers; the URL already uses that ID.
- EPA 12/16/13 (2000 4.0) and 11/14/12 (2000 4.6).
- Lucky8 fitments: REB101740, LR030219, ERR3340, TF223, ANR3902, STC3261, STC3259G, the P38 hose kit and the thermostat.

**Still unverified / shortcomings**
- **High.** The lug torque in the detail file (80 lb-ft vs 130 N·m) is still contradictory, and the page says so. It needs the handbook figure.
- **High.** Engine oil spec (5W-40/5W-50, ACEA A2) and the transfer box (Dexron III, 2.0 L) come from BolidenForum (403) and forum posts. The differential grade is already marked [CONFIRM].
- **Med.** **Photos are weak.** The hero (Rejvíz) is on tarmac. The ferry shot is not off-road. The harvest-field shot is only 640 px wide. A better off-road P38 hero is needed.
- **Med.** About 15 parts links are Rovers North search URLs (403 to bots).
- **Low.** "Coil conversions are becoming less popular" and the £-figures come from Classics World (403 to bots), so I couldn't re-read them.

---

## Range Rover L322

**Corrections made**
- **Wrong fluid product.** The transfer-fluid part link "Rock Oil TF 0753-type IYK500010" pointed to Lucky8's **TF-0870** product page. It now points to Lucky8's IYK500010 set, which lists 2006–12 L322 fitment.
- **Transfer box dating.** The DD295 "(2006 onward)" date is now qualified with Lucky8's fitment and [CONFIRM BY VIN] for 2006 MY. The engineering section says "Torsen until 2006", so the exact model-year changeover is ambiguous.
- **Recall years.** 17V-015 years changed from 2009–2012 to 2007–2012, per the NHTSA API.

**Verified as correct**
- L30 codename; BMW FIZ, then Solihull.
- Production of 293,494; wheelbase 2,880 mm.
- Engine outputs: M62 286 PS / 440 Nm; Jaguar 305/400 PS; 5.0 375/510 PS; Td6 177 PS / 390 Nm; 3.6 TDV8 272 PS / 640 Nm; 4.4 TDV8 313 PS / 700 Nm; ZF 8HP70 for 2011.
- Terrain Response 2007, with an e-diff on Supercharged models.
- 20th Anniversary edition (40 cars) and the Holland & Holland / Overfinch edition.
- Torsen T-2 with 50:50 split, up to 65% (Australian Car Reviews).
- All 7 NHTSA recalls; 08V-635 covers 19,168 trucks.
- EPA figures: 2004 at 11/15/12; 2008 at 12/18/14; 2011 5.0 at 12/19/15 and 12/18/14.
- Lucky8 fitments: WFL000021, PHE000050, PHE500021, LR031439, LR005253, LR032080 set, IGH500010, 2006–12 shift motor, LR020627/LR020626, RQH100030 set, LR064185, LR051050 belt set, LR134696 pads.

**Still unverified / shortcomings**
- **High.** Fluid capacities (front diff 0.75 L, rear 1.14/1.55 L, transfer 1.0/1.5 L) come from TOPIx owner-guide PDFs and FullFatRR. TOPIx needs a login and its PDFs couldn't be fetched. The FullFatRR wiki "Recommended Lubricants" page returns HTTP 500.
- **Med.** The exact model year the DD295 transfer box arrived (2006 vs 2007).
- **Med.** **Photos.** The "hill road" shot is on tarmac. The G4 shot is at a show ground. The moorland and autumn shots are on gravel but next to roads. There is no true trail photo.
- **Low.** The callout details (35th Anniversary: 30 Claret cars; 40th Anniversary Autobiography Black: 700; Ultimate Edition: 500; Armoured Vogue B6) rely on Wikipedia text I didn't re-read line by line.

---

## Range Rover L405

**Corrections made / removed**
- **Unsourced claim removed.** "Benchmarked against a Rolls-Royce Ghost" is gone. I couldn't find a source, and the Driven to Write profile doesn't mention it.
- **Dead source removed (ACM Technik, 404).** It backed the claim that "aftermarket nylon couplers are listed for 2010–2013". That clause is now a generic "check fitment for your build year".
- **Dead source removed (4x4 Sint Annaland, 404).**
- **Dead PDF replaced (autoteile-store.at, 404).** The Arnott strut install manual is replaced by the Shock Warehouse ASE-3756 product page.

**Verified as correct**
- Paris Motor Show 2012; 39% lighter body and a 420 kg weight saving.
- Wheelbase 2,922 mm (LWB 3,122 mm); LWB shown at LA 2013.
- Engine outputs: 5.0 SC at 510 then 525 PS; SVAutobiography Dynamic at 550 then 565 PS; V6 SC at 340/380 PS; SDV6 Hybrid at 340 PS / 700 Nm with a 35 kW motor.
- P400e: 404 PS, 13.1 kWh, 85 kW.
- SV Coupé cancelled January 2019; DD295 with 50/50 split.
- EPA figures (2016): V8 SC 14/19/16; V6 17/23/19; Td6 22/28/24.
- All 10 NHTSA recalls plus the cross-referenced 24V-840, 26V-527, 20V-387 and 19V-350, with years matching.
- Lucky8 fitments: LR072469/71 arms; BWI strut; LR079515; LR011593; LR036369; Proud Rhino rods, sliders, bash plate and A-bar.
- Photos: all four are genuine L405s (two facelift, two pre-facelift) on dirt, sand or a river.

**Still unverified / shortcomings**
- **High.** Fluid capacities are much smaller than the L322's (front diff 0.54 L, rear 0.85/1.25 L, coolant 6.83–8.93 L). They are sourced to TOPIx owner-guide PDFs, which need a login and couldn't be fetched. They need a manual check.
- **Med.** WheelWorld Reviews (source for 303 mm / 900 mm / 34.7° / 29.6°) returned 503 during the check.
- **Med.** The TDV6 crank bulletin (SSM71816) is cited only through an AULRO thread, which is 403 to bots.
- **Low.** The beach photo's caption "BLACK SANDS BEACH, WALES" can't be verified from the image, and the sand is light.

---

## Range Rover L460

**Corrections made**
- **Wheelbase growth.** "Wheelbase 22 mm longer at 2,997 mm" was wrong. The L405 SWB is 2,922 mm and the L460 is 2,997 mm, so the growth is **75 mm**. Source: both Wikipedia infoboxes. Wikipedia's own "22 mm" contradicts its infoboxes.
- **P550e output.** "560 PS" is now **550 PS** (800 Nm). Source: Wikipedia powertrain table.
- **PHEV motor.** The page applied the 105 kW motor to every PHEV. Range Rover USA says the **P550e uses a 160 kW motor**; 105 kW applies to the P440e/P510e. Fixed in the story, the FAQ and the generations table.
- **DC-DC converter recalls.** The text cited only 26V248000. Both campaigns were checked through the NHTSA campaign API, and follow-up 26V599000 (interim letters due 13 November 2026) has been added to the story, the buying checks, the repair and the baseline.
- **Cam-carrier recall.** Years changed from "2020–2023 trucks" to 2022–2023 L460s, noting that the campaign also covers 2020–21 L405s.
- **Wheel sizes.** The FAQ said "Factory wheels run from 21 to 23 inches", which contradicted the detail file and the identify section (20–23 in). It now says 20–23 in.
- **Oil filter fitment.** The LR133455 oil filter link is now flagged "confirm L460 by VIN". Lucky8's listing names the Ingenium 3.0 Defender/RR but not the L460 explicitly.

**Added**
- Sources: NHTSA campaign API entries for 26V248000 and 26V599000.

**Verified as correct**
- Revealed 26 October 2021 at the Royal Opera House; MLA-Flex.
- 53/63/35 mm larger than the L405; 50,000 Nm/deg (+50%); 24% noise reduction.
- Turning circle 10.95/11.54 m.
- Front-axle disconnect at 35–160 km/h, cutting drag losses by 30%.
- 38.2 kWh battery (31.8 kWh usable).
- N63 for 2022–23, S68 for 2024 on; P550e replaced the P440e for 2024.
- Range Rover Electric: unveiled 2 September 2026; 2027 MY in the US; twin 260 kW motors; **660 lb-ft** (Range Rover USA; Wikipedia's 627 lb-ft is outdated); 344 NMC cells; 35-in wading; 5,511 lb towing; 333-mile range; Müller and Dino test films.
- Towing: 7,716 lb (P400 and V8s) and 6,614 lb (PHEV).
- All 13 NHTSA recalls.
- EPA figures: P400 18/26/21; V8 16/21/18; P440e 51 MPGe and 21 mpg.
- Lucky8 fitments: VPLYT0295; L460 hitch; wheel bolts; LR153550 rotor.

**Still unverified / shortcomings**
- **High.** Most fluid specs are [CONFIRM] or owner reports: diesel oil 0W-30 at about 9 L, the transfer fluid, and the e-diff / front-disconnect fluid. There is no factory capacity table, and the TOPIx owner guide wasn't accessible.
- **Med.** **Only 2 photos**, both of the same dealer-plated car on a single shoot. More off-road L460 imagery is needed.
- **Med.** The mods section is thin (4 categories). There is no sourced lift, armour or roof-rack supplier yet, which matches the forum finding that none exist.
- **Low.** The Range Rover Electric's 333 miles is "EPA" per Wikipedia, but Range Rover USA calls it "estimated real-world range". The FCP Euro search links return HTTP 404 to curl but render a search page in a browser.

---

## Group-wide notes
- **Low.** The Mid-Atlantic Rally and ANARC Rovers North blog links return 403 to bots; the URL format looks legitimate.
- **Low.** Instagram handles (@atlanticbritish, @paddockspares, @blackbox_nanocom) redirect to the login page, so they couldn't be confirmed. They are the suppliers' plausible official accounts but are not verified.

## Top 5 remaining problems (range-rover group)
1. **High: fluid capacities and specs on all five pages rest mostly on BolidenForum, TOPIx PDFs (login-only) and forum posts.** The L405 and L322 diff and coolant volumes and the P38 and Classic transfer, PAS and swivel fills need checking against factory manuals.
2. **High: wheel-nut torque and thread are unconfirmed.** The P38 detail file holds two contradictory torque figures (80 lb-ft vs 130 N·m). The Classic's M16x1.5 thread and 130 N·m come from wheel-spec databases.
3. **Med: photos.** The P38 hero is on tarmac and its other two photos are a ferry deck and a 640 px shot. The L322 has no genuine trail shot. The L460 has only two images of one dealer car.
4. **Med: L322 transfer-box changeover year.** It isn't settled whether the NV225/Torsen box gave way to the DD295 for MY2006 or MY2007. That decides which fluid (BOT 26 vs TF 0753) an owner buys.
5. **Med: many repair "parts" links are supplier search URLs, not specific part numbers.** This is mainly Rovers North (403 to bots) and Atlantic British, especially on the Classic and P38 pages. Specific product URLs would be more useful and verifiable.
