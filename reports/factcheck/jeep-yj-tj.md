# Fact-check report: jeep-yj-tj

Scope: `data/pages/jeep/{yj,tj,tj-unlimited}.json`, `data/extra/jeep/{yj,tj,tj-unlimited}.json` and the 9 photos in `site/img/jeep/` that these pages reference.

Method: I checked every URL in the six files (236 unique) with curl, and fetched the titles of all product and reference pages to confirm each one is the right page. I re-read the main sources: Wikipedia YJ and TJ wikitext, Quadratec and ExtremeTerrain fluid charts, the ExtremeTerrain TJ torque table, the Quadratec 2005–06 Jeep spec sheet, the Quadratec buyer's guide PDF, the Skyjacker YJ instructions, the 4WD Mechanix articles, Drivingline, Off Road Xtreme, Jalopnik, Rockcrawler's 2004½ Unlimited spec sheet, Hagerty and the Jeep 2003 Rubicon press release. I also checked every recall against the NHTSA API, EPA ratings against the fueleconomy.gov web service, and VIN codes against NHTSA vPIC pattern decodes. I opened and looked at every photo.

**One finding affects all three models:** the Haynes "routine maintenance FAQ" URL now redirects to a Shopify page (us.haynes.com) that contains **only the service schedule**: 7,500 mi/12 mo oil and chassis grease, and 30,000 mi/24 mo for air/PCV, plugs, coolant, manual and automatic transmissions, transfer case and differentials. None of the torque values, fluid types or capacities attributed to "Haynes" across the YJ and TJ pages can be seen there any more, and the Wayback Machine is blocked from this sandbox. I kept the Haynes intervals, which are verified. Every Haynes-attributed spec was either re-sourced (ExtremeTerrain factory torque table, Quadratec or ExtremeTerrain charts) or marked `[CONFIRM IN MANUAL]`.

---

## Jeep Wrangler YJ (`yj`)

### Corrections made
- **Internal clutch slave years.** The page said "1987–92" in a buying check, a repair and an FAQ, while the detail file's timeline said 1994. The sources genuinely disagree:
  - 4WD Mechanix says 1987–92 internal, with an external slave from 1993.
  - Wikipedia says the slave moved outside the bellhousing for 1994.
  - The Advance Adapters internal-bearing kit (716130IR-93) is listed for 1987–93.

  All three places now say "early YJs" and give the conflicting sources. The timeline and identify entries were softened to match.
- **Rio Grande engine.** The generations table said "2.5 L I4 or 4.0 L I6". Wikipedia says the package was added to the base four-cylinder S, so it now reads "2.5 L I4 (base S)", which matches the detail file.
- **2.5 L four.** It was listed as fuel-injected TBI for the whole run. It is now "throttle-body injection (multi-point from 1991)". NHTSA vPIC decodes 1J4FY19E… (1990) as TBI and 1J4FY19P… (1995) as MPFI.
- **4.0 automatic.** It is now "A999 for 1991, then 32RH" (Wikipedia powertrain table).
- **VIN engine codes (detail file).** It said "E is the 2.5 L four" for 1989–95. It now says E = TBI 2.5 (1989–90), P = MPI 2.5 (1991–95) and S = 4.0, all confirmed with vPIC. Trim code 1 = base S was added.
- **Baseline service.** Every "Haynes" spec was re-sourced or marked:
  - Oil grade is now 10W-30 (Quadratec) or 10W-30/5W-30 (ExtremeTerrain). The old "5W-30 below 32°F" split had no source.
  - Capacities now come from the Quadratec chart: 2.5 L 4 qt oil and 9 qt coolant; six-cylinders 6 qt oil and 10.5 qt coolant.
  - Manual transmissions: GL-3/GL-4 75W-90 (ExtremeTerrain) replaces the unverifiable "Haynes GL-5", with `[CONFIRM IN MANUAL]`.
  - Transfer case: NP231 2.2 pints and NP207 4.4 pints (Quadratec chart) replace the unverifiable "Haynes 3 pints / 4.5 pints".
  - Automatic: the unsupported "≈4 qt pan drop / ATF+3 (Haynes)" was replaced with the total capacities from the chart and `[CONFIRM IN MANUAL]`.
  - Torque values (drain plug 25 ft-lb, transfer case plugs, cover bolts 30 ft-lb, 32RH filter screws 35 in-lb) now come from ExtremeTerrain's 1997–2006 TJ factory table. Each is marked `[CONFIRM IN MANUAL for YJ]`, because no YJ-specific table was verified.
  - Spark plug torque: the old year-split figures had no verifiable source. It is now `[CONFIRM IN MANUAL]`, with the TJ-era 27 ft-lb given as a reference.
  - Added Haynes' fuel-filter item (1987–95) and its cap/rotor/wires inspection item.
- **Axle FAQ.** It was re-sourced to the Quadratec and ExtremeTerrain charts and now carries a "fill to the hole" caveat.
- **Peugeot FAQ.** The AX-15 change is now worded exactly as Wikipedia gives it (behind the 4.2 from 1989).
- **Photos.**
  - The Devil's Canyon photo caption and credit were corrected: Commons says the photo is by John Johnson, BLM, Devil's Canyon, El Centro FO.
  - The Mounds caption is now Mt. Morris, Michigan, per Commons.
  - The Crystal Mountain alt text was corrected. The truck is grey-tan with Colorado plates.
- **Values note (detail file).** It claimed a window of "January 2025 to October 2026" but cited a September 2024 sale. The sale is now flagged as falling just before the window.
- **Haynes source URL** was updated to the live us.haynes.com URL and relabeled as a maintenance *schedule*.

### Removed or softened
- The Haynes-attributed oil-viscosity temperature split, the spark plug torque split, coolant "2000-and-earlier spec", ATF+3, the transfer case capacities and the plug torques were removed or marked `[CONFIRM IN MANUAL]`, as above.
- The rear main seal "torque the cap to spec" step now says `[CONFIRM IN MANUAL]`.

### Added
- Recall **NHTSA 86V058000** (1987: lug nuts and steering-shaft clamp bolts not properly tightened), confirmed via the NHTSA API.
- Sources: the ExtremeTerrain TJ torque table (as a cross-reference), the ExtremeTerrain fluid capacities chart and NHTSA vPIC pattern decodes. A 4WD Mechanix and a Wikipedia entry were also added to the detail-file sources.

### Verified as correct (highlights)
- **Dates and production:** unveiling (February 1986) and on-sale date (May 13, 1986); Brampton closure on April 23, 1992; 632,231 / 685,071 built; no 1996 model.
- **Mechanical specs:** 117 hp (2.5) and 112 hp / 210 lb-ft (4.2); NP207 1987 only; Dana 30 vacuum disconnect; 1995 297x/1330 U-joints.
- **Renegade:** $4,266, $923 hardtop and $164 defroster, and its colors (Wikipedia).
- **Hagerty:** $8,100 vs $9,900, HVR 86, "180 hp", the Islander's 11 percent premium and Gen X interest (re-fetched).
- **Fitment and capability:**
  - Four Wheel Trends' 30-inch / 31x10.50 YJ answer.
  - Skyjacker's 90 ft-lb U-bolts, small spring eye to the rear and retorque at 50 and 100 miles.
  - Towing 2,000 / 1,000 lb, payload 800 lb, 8.2 in ground clearance and 15/20 gal tank (Quadratec 1990 and 1995 spec pages).
  - EPA 15/20 (1991 4.0 manual) and 14/17 (1995), confirmed via the fueleconomy.gov API.
- **Recalls:** all 7 listed recalls exist with the stated years and remedies.
- **Social:** Civilian Jeeps ("1987 Wrangler YJ Interview – Save the Squares!") and Jerod's Garage ("CHEAP JEEP? – 89 Wrangler YJ" series) both have real YJ content.

### Still unverified / shortcomings
- **High:** No YJ-specific torque table was verified for the drain plug, spark plugs, diff covers or transfer case plugs. The figures shown are TJ-era factory values, and all are flagged. A YJ factory service manual check is needed.
- **High:** Automatic transmission fluid type and service-fill quantity for the TF999/32RH/30RH are flagged only. Fluid type matters (ATF+3 vs Dexron-era specs).
- **Med:** AX-5/AX-15 lubricant. ExtremeTerrain says GL-3/GL-4 75W-90. Many owners and the factory manual may differ, so this is flagged.
- **Med:** Lug-nut torque is still unconfirmed for the YJ; the fitment note already says so.
- **Med:** BaT value ranges (71 sales, median ≈$9,800) could not be re-verified, because BaT results load through JavaScript.
- **Low:** Only 3 photos. The Crystal Mountain photo's Commons metadata is thin ("my jeep went wheeling", date "0007"), so a human should confirm its license.
- **Low:** The 1987–88 AMC-style VIN decode ("2BC…") comes from the original author's decodes and was not re-run.
- **Low:** JK-Forum, WranglerForum and JeepForum return 403 or 202 bot walls. These are real, known URLs. The 4WD Mechanix forum fails through curl here (proxy 502) but loads through WebFetch.

---

## Jeep Wrangler TJ (`tj`)

### Corrections made
- **Curb weight on the plate.** It said "3,092–3,857 lb (incl. Unlimited)". Wikipedia's range is for the TJ, and the LJ detail file lists an Unlimited Rubicon at 3,977 lb. It now reads "(short wheelbase)".
- **Towing.** It said 2,000 lb flat in the FAQ, plate and capability. Jeep's 2005–06 spec sheet (via Quadratec) rates the 2.4 **and the 4.0 automatic with the base 3.73 axle** at 1,000 lb. The FAQ, plate and capability now say so.
- **Rubicon lockers.** "Engaged at 5 psi in low range below 10 mph" was rephrased to match the press release. The 5 psi is the pneumatic pump pressure; the 10 mph low-range limit is the engagement rule. The press-release URL was fixed from the unreachable `www2020.theautochannel.com` to `www.theautochannel.com`, which returns 200 and shows the same text.
- **Rubicon gearing.** "4.10" is now "4.10 (Jeep spec sheets also list 4.11)", in the table, FAQ and plate.
- **OPDA.** The callout, FAQ and repair said the factory upper bushing is *steel*, citing Dorman. Dorman does say steel, but Crown's listing (Quadratec and ExtremeTerrain) describes two **bronze** bushings with a seal. Both accounts are now shown. "Stopping the oil pump" was not in the Dorman text that could be fetched, so it now reads "seize and destroy the cam bearing" (Dorman) plus "can damage the engine" (Quadratec).
- **Biggest-tire FAQ.** "Usually allows full articulation" overstated the source. Four Wheel Trends says 31x10.50 keeps full function but may rub at full flex, and that a steering-stop washer fixes it.
- **Baseline service and FAQs.** Haynes specs were re-sourced:
  - Drain plug: 25 ft-lb for the 4.0 and 2.5, and **20 ft-lb for the 2.4** (ExtremeTerrain).
  - Transfer case plugs: **15–25 ft-lb**. The old "20 ft-lb (Haynes)" could not be seen.
  - Verified against the ExtremeTerrain factory table: 42RLE filter screws 45 in-lb, 30/32RH 35 in-lb, cover bolts 30 ft-lb.
  - **Spark plug torque conflict:** ExtremeTerrain's engine tables give 27 ft-lb (4.0, 2.5) and 250 in-lb (2.4), but its ignition table says 30 ft-lb for all engines. The page's "2.4: 132 in-lb (Haynes)" could not be verified. All of this is now marked `[CONFIRM IN MANUAL]`.
  - Coolant type (the HOAT changeover around 2001) and the 30/32RH ATF type are now `[CONFIRM IN MANUAL]`.
  - The AX-5/AX-15 lube spec is now ExtremeTerrain's GL-3/GL-4.
- **Exhaust manifold part.** The OMIX 17622.12 kit is listed for 1991–99. The label now says 1997–99 TJs only and to check fitment for 2000–06.
- **Radiator buying check.** The "≈100,000 miles" figure is now attributed to Quadratec, which is where it comes from.
- **Detail file:**
  - Stock max-tire note: the unsourced "at least 4.5 in backspacing" was removed.
  - Lift notes: the "Quadratec suggests 4.10 or 4.88" regear wasn't in the PDF and was removed. The 31 in (2 in spacer), 33 in and 35 in (long-arm) figures are now attributed to the Quadratec buyer's guide PDF.
  - Curb weight top end: now 3,857 lb (Rubicon automatic).
  - VIN identify items: trim code 3 = X and engine code 1 = 2.4 were added (vPIC). The 7th-character SWB/Unlimited rule is softened, because vPIC decodes 1J4FA49S as "Sport/Unlimited".
- **Photos.** The Shotgun Creek credit was corrected: Commons says the photo is by Carlos Velez of the Salem Jeepers, posted by BLM. The Cow Mountain alt text now mentions the trailer. The Paragon photo is now captioned as "TJ" and its alt text says the photographer describes it as a Rubicon.

### Removed or softened
- The old Haynes coolant and ATF changeover years in the baseline intro were replaced with "check the manual or labels".
- "Quadratec suggests 4.10 or 4.88" was removed. "At least 4.5 in backspacing" was removed.

### Added
- Recalls **98V023000** (1998 brake booster vacuum diaphragm) and **99V117000** (1999 instrument-panel ground screws), both confirmed via the NHTSA API.
- Sources: the ExtremeTerrain TJ torque table, the Quadratec 2005–06 Jeep spec sheet, the Crown OPDA listing and fueleconomy.gov.

### Verified as correct (highlights)
- **History (Wikipedia):** development under Sheaves/Winn, the $260M budget, Santoro's design frozen in May 1993, the January 2, 1996 debut, April 1996 showrooms and production from January 1996 to July 2006.
- **Special editions:** the 60th Anniversary count of 4,067 (1,862/2,205), Tomb Raider 1,001, Willys about 1,000 in 2004, 65th Anniversary about 1,600, and the Golden Eagle and Columbia years.
- **Powertrain:** outputs (181/222 and 190/235; 120/140; 147/165); the transmission years table; the Rubicon spec and the 65.92 crawl ratio (Rockcrawler). fueleconomy.gov lists the 2.4 L six-speed for 2006, which confirms the 2.4 ran through 2006.
- **Drivingline and Off Road Xtreme claims:** "junk" Dana 35, a track bar for a little over $50, a radiator for about $150, manifold cracks most common on 1997–2000, the cowl leak, the lower track-bar bolt and the 30–50 mph test.
- **Quadratec:** the inspection checklist, the Rotondo frame article (1998 TJ with 190k miles, 1 in overlap, "do NOT cut the body mount") and the death-wobble and alignment pages.
- **Fluid service details:** 4x4xplor's NV3550 fluid service (17 mm Allen, about 2 bottles).
- **EPA and recalls:** 15/18 (1997) and 13/17 (2005–06) EPA figures; all 9 originally listed recalls.
- **Social:** Kubicon, Trail Expedition ("DIY: Jeep Wrangler TJ Floor Pan and Torque Box Repair!") and Muddy Beards ("Build your own Track Bar and Steering!") were confirmed.

### Still unverified / shortcomings
- **High:** Coolant type by year (conventional vs HOAT) and 30RH/32RH ATF type are flagged only. These are the specs most likely to mislead an owner.
- **High:** Spark plug torque for all three engines conflicts within the ExtremeTerrain table (27 vs 30 ft-lb; 2.4 at 250 in-lb) and is flagged.
- **Med:** Retailer charts disagree on differential capacities. ExtremeTerrain's oils page gives TJ Dana 30/35 as 1.7 qt; the Quadratec chart gives Dana 30 2.5 pt and Dana 35 3.5 pt. The page now leans on "fill to the hole".
- **Med:** The OPDA replacement procedure in the repair is generic ("follow the FSM sync procedure"). A human expert should add the actual indexing steps, such as the slot alignment at #1 TDC and the scan-tool sync, from a factory manual.
- **Med:** BaT values (256 sales, median ≈$15,500) were not re-verified.
- **Low:** The Paragon photo's Commons date (January 30, 2001) predates the 2003 Rubicon, so either the camera date or the "Rubicon" label is wrong. The caption has been neutralized. The Shotgun Creek photo is by a club member but tagged public domain as a BLM work, so its license should be checked.
- **Low:** Dorman/NAPA, Jeepz.com, Jeepfan and wranglertjforum return 403/406 to bots. They are real URL formats; the Dorman text was confirmed through WebFetch.

---

## Jeep Wrangler Unlimited / LJ (`tj-unlimited`)

### Corrections made
- **"When the 4.0 became standard across the Wrangler line" (2006) was removed.** fueleconomy.gov lists a 2006 Wrangler 2.4 L six-speed, and Jeep and Quadratec spec sheets list the 2.4 for the 2005–06 SE. Wikipedia's 2006 section contradicts its own trim list.
- **"The LJ was also the end of the AMC straight six in a Wrangler"** is now "the TJ and LJ were the last Wranglers with the AMC-derived 4.0". Both ended in 2006.
- **"By mid-2017, Autotrader found three-quarters of new Wranglers… were four-doors" was removed.** No source for it was given or found.
- **CJ-6 wheelbase claim.** "103.5 inches of the CJ-8 and CJ-6" was cut to the CJ-8 only. The CJ-6's 101/104 in wheelbases don't match.
- **"Rubicons get monotube shocks" was removed** as unsourced. The suspension note now follows Jeep's 2004½ spec sheet: leading and trailing arms, track bars, stabilizer bars and gas-charged shocks.
- **"Fully boxed frame"** is now attributed to the Jeep engineer quoted in Jalopnik.
- **Biggest-tire FAQ.** The page's own "we couldn't open a forum thread" admission and a RealTruck quote were removed. The quote does not appear on the RealTruck page, and that source was dropped. The FAQ now cites Four Wheel Trends (31x10.50, may rub at full flex) and the Quadratec buyer's guide (33s need about a 3-inch lift).
- **Fuel-economy FAQ.** It gave only Jeep's original 16/20 figures. EPA's revised 13/16 (automatic) and 13/17 (six-speed) were added from fueleconomy.gov, and the 19-gal tank is now sourced to Jeep's 2004½ spec sheet rather than a forum post.
- **Production.** The page said ≈47,000 (Jalopnik) and the detail file said "a little over 46,000" (Driving Line). Both figures are now shown in both places, along with Driving Line's "fewer than 13,000 Rubicons".
- **2004½ transmissions.** "Jeep's 2004½ spec sheet lists the 42RLE automatic" was added as the attribution (Rockcrawler).
- **Detail file:**
  - Max-tire notes: "4.5 in backspacing" removed; lift figures attributed to the Quadratec PDF.
  - VIN identify item softened: vPIC doesn't separate Unlimited from short wheelbase.
  - The Quadratec 2006 specs page is now labeled as containing errors. It lists a Dana 35 rear for the Unlimited, which contradicts Wikipedia and Jalopnik.

### Removed or softened
- The Autotrader statistic, monotube shocks, the CJ-6 comparison, the RealTruck quote and the "4.0 standard in 2006" claim, all as above.

### Added
- Sources: Four Wheel Trends, the Rockcrawler 2004½ spec sheet, the Driving Line LJ feature and the Quadratec buyer's guide on the page; Jalopnik and Four Wheel Trends in the detail file; fueleconomy.gov.

### Verified as correct (highlights)
- **Wikipedia:** April 2004 launch, 18-year hiatus, 10 in / 15 in stretch, 2 in more legroom, 13 in more cargo space, 3,500 vs 2,000 lb towing, Dana 44 3.73 LSD rear and NV231.
- **Rubicon Unlimited:** the specs, and the Sahara Edition (1,000 numbered, Light Khaki, manual and automatic).
- **Storm II:** 2,931 mm wheelbase, described as the "first five-door Wrangler derivative".
- **Jalopnik:** $24,995 price, 27.7° and 21.4° angles, 47,000 at about 20 percent, the JK Unlimited about 350 lb heavier.
- **Rockcrawler 2004½ spec sheet:** 190 hp at 4,600 and 235 lb-ft at 3,200, 6 qt oil, 10.5 qt coolant, 3,721 lb, 43.1° approach angle, 28.5 cu ft cargo and the 36 ft turning circle.
- **Hagerty quote:** "especially the Unlimited Rubicon, have been the priciest TJ" (confirmed via hagerty.com/media/?p=287024).
- **Quadratec how-tos:** TPS (P0122, T25 and the listed tools), U-joint and hub (36 mm axle nut, three 13 mm bolts), driveway alignment (1/16 in toe-in, no more than 1/8 in; 13 and 15 mm) and SYE (strongly recommended above 2 in, required at 4 in or more).
- **Recalls:** all 3 listed recalls.

### Still unverified / shortcomings
- **High:** The 2005–06 Rubicon Unlimited curb weight (3,977 lb) has no verified source. The detail file now carries a `[CONFIRM]` note.
- **Med:** Whether 2004½ LJs were offered with a manual. Jeep's 2004½ sheet and Jalopnik list only the 42RLE, but this wasn't confirmed against a 2004 order guide.
- **Med:** The OPDA indexing procedure is generic. It needs factory-manual steps, as on the TJ page.
- **Med:** Only 2 photos. Both are genuine LJ Rubicons: the badges "RUBICON" and "UNLIMITED" are visible. The Hell's Revenge hero is a parked group shot with a Can-Am and a Polaris in frame, not an action shot. The Antler Mine photo shows a readable California plate.
- **Med:** BaT values (55 sales, median ≈$20,500) were not re-verified.
- **Low:** The Instagram handles (@quadratec, @extremeterrain) load only a login wall, so they couldn't be confirmed beyond their brand websites. The YouTube channels resolve.
- **Low:** There are only two forums (WranglerTJForum, JeepForum) and no LJ-specific board.

---

## Top 5 remaining problems for this group
1. **Torque specs on the YJ (High).** No YJ-era factory torque source is verified for spark plugs, drain plug, diff covers or transfer case plugs. TJ-era values are shown and flagged. Someone with a 1987–95 factory service manual needs to fill these in.
2. **Fluid *types* by year across YJ and TJ (High).** These need factory-manual confirmation: coolant (conventional vs HOAT changeover), automatic fluid (TF999/30RH/32RH, ATF+3 vs ATF+4) and manual gear lube (AX-5/AX-15 GL-3/4 vs GL-5). Every Haynes spec the pages relied on is no longer visible at the cited URL.
3. **TJ spark plug torque conflict (High).** ExtremeTerrain's own factory table gives 27 ft-lb in its engine sections and 30 ft-lb in its ignition section, and 250 in-lb for the 2.4. It is flagged, but should be resolved against the factory manual.
4. **OPDA replacement procedure on the TJ and LJ (Med).** The steps are generic. The cam-sensor indexing and sync check is where DIYers go wrong, and it needs factory-manual steps and a source.
5. **Values and thin photo coverage (Med).** None of the three BaT-derived value tables could be re-verified, because BaT results load through JavaScript. The LJ has only 2 photos and the YJ 3, and the licenses of the Paragon and Shotgun Creek photos need a human look.
