# Fact-check report: jeep-classic

Group: `jeep-classic`. Models in scope: CJ-7 (flagship: `data/jeep.json` → `page` and `family`), CJ-5, CJ-8 Scrambler, Grand Wagoneer (SJ), Cherokee XJ, plus each model's `data/extra/jeep/<slug>.json`.

## Method

- I extracted all 487 unique URLs from the 10 files and checked each with curl (`-L`, `Mozilla/5.0`). Every Quadratec, Team Grand Wagoneer, ExtremeTerrain, BaT and AutoTempest link was also title-checked, and each part name was matched against the product page title (about 230 part and mod links in total).
- I checked recall lists against NHTSA's API (`recallsByVehicle` and `campaignNumber`), including unit counts.
- I re-read the main sources as text: Wikipedia (Jeep CJ, YJ, Wagoneer SJ, Cherokee XJ, AMC V8, AMC straight-6, AMC, Kaiser Jeep, Buick V6, Willys Hurricane, Land Rover Series, Land Cruiser, Dukes of Hazzard, Iron Duke), Offroaders.com engine, axle, gearbox, transfer-case and VIN pages, Novak, the ExtremeTerrain CJ and XJ fluid guides, the JeepCJ.com buyer's guide and forum threads, both Hagerty pieces, Hagerty UK, 4WDrive, SlashGear, eBay Motors, RealTruck, KEYT, DrivingLine, OffroadXtreme, NAXJA threads, Wagoneer World and jeep.com.
- I opened all 16 photos with Read and checked their Commons licence and author metadata.
- All 61 `[[family/slug]]` cross-links and every `related` entry resolve to real generations.
- 403s, 202s and 503s from NHTSA, naxja.org, hagerty.com, cherokeeforum.com, bjsoffroad forum, roughcountry.com, AMSOIL and morris4x4center.com are bot walls on real URLs. NAXJA, Hagerty, Faxon and AMSOIL pages were confirmed through WebFetch.

---

## CJ-7 (flagship page + family object)

### Corrections made
- **Family intro.** It said the CJ line "ran from the CJ-2A to the CJ-5". Changed to: the CJ-2A of 1945, then the CJ-5 for the 1955 model year after Kaiser had bought Willys. Added "from 1972" for AMC's own engines. Sources: Wikipedia Jeep CJ, Offroaders AMC 258/304.
- **AMC's price for Kaiser Jeep.** The page said "about $75 million". Now gives both figures: $70 million (Wikipedia, AMC and Jeep articles) and about $75 million (jeep.com history).
- **Missing engine.** The page left out the AMC 232 six, which was the CJ-7's standard engine for 1976–78; the 258 became the base six for 1979. Added it to the story, the engineering cell, generations-table row 1 (100 hp / 185 lb-ft) and a new 1979 timeline entry in the extra file. Sources: Offroaders AMC 232, restore-an-old-car.
- **Quadra-Trac.** "Introduced in the full-size Wagoneer in 1972" now reads "early 1970s (the 1973 model year, by Wikipedia's dating)". Jeep.com says 1972. Also added the optional low range's 2.57:1 ratio. Source: Offroaders BW 13-39.
- **Golden Eagle.** "Levi's soft top and bigger tires" was unsourced. Replaced with the tachometer, clock and decals (Wikipedia), noted the package was tied to the 304, and identified Dixie as Daisy Duke's white 1980 CJ-7 Golden Eagle. Source: Wikipedia Dukes of Hazzard.
- **Export diesel.** Removed "lowest gearing of any CJ-7", which was unsupported (Offroaders lists 4.10 codes for gas AMC 20s). Now reads Dana 300 (some reportedly Dana 20), typically narrow-track axles with 4.10s. Source: Wikipedia.
- **Generations table.** Row 2 output now includes the 258 (110 hp / 195 lb-ft). Row 3 now dates the 151 to '82–'83 and the AMC 150 to '84–'86. Row 6 gives Offroaders' serial-number range for the change to the Dana 44. Sources: Offroaders 151/150/Dana 44.
- **Front wheel bearings (High).** The page said "back off 1/6 turn … no end play". The manual figures quoted in the source thread are 50 ft-lb to seat the bearings, then 0.001–0.005 in end play; the 1/6-turn back-off is one owner's method. Rewritten that way in the repair and the service item, and the outer-nut torque is now marked [CONFIRM IN MANUAL]. Source: Off-Road.com thread.
- **Axle-ratio FAQ.** It presented Offroaders' 3.54 / 2.73 ratios as fact, but Wikipedia gives 3.73 / 3.55. Both are now shown, with advice to read the code. The extra file's capability note says the same.
- **Coolant capacities.** Filled in the 258 (10.5 qt) and split the 2.5 four into the 151 (7.8 qt) and the AMC 150 (11 qt). Source: ExtremeTerrain.
- **Automatic-transmission fluid.** ExtremeTerrain lists ATF+4 for the TH400, but the TH400 is a GM unit, so I added [CONFIRM IN MANUAL].
- **Extra file.** "Mid-1986 trucks get a Dana 44" is now "some late trucks". The Axles item now also mentions the Quadra-Trac offset Dana 44 (Offroaders). "Only numbered AMC Jeep" is now attributed to Wikipedia.
- **Broken mod link.** `rancho.com` is a parked domain that redirects to `/lander`. Replaced with `https://www.gorancho.com/`, Rancho's store.
- **Photo alt text.** The rock-ledge photo's alt said "one front wheel in the air", but both front tires are on boulders. Fixed.

### Removed or softened
- The "magnet won't find rot" line, which wasn't in the cited guide.
- "Emergency Drive switch in the glovebox": the location wasn't sourced.
- The NAPA BK1 "$15 a side" price, which isn't in the cited thread.
- The closing rivals paragraph, rewritten so it doesn't state "cheapest to fix" as fact.
- The BaT values note: removed "1980 Laredo five-speed $58,000" (the factory T-5 only arrived in 1982) and marked the statistics as a compilation to recheck.

### Added (with sources)
- Sources: Wikipedia AMC, Wagoneer SJ and Dukes of Hazzard pages; Offroaders AMC 232, GM 151, AMC 150 and Dana 44 pages.
- A 1979 timeline entry.

### Verified and left as is
Production of 379,299 and the 93.5 in wheelbase; the AMC 20 specs (8⅞ in ring gear, 29 splines, 50.5 in and 54.5 in track widths); 258/304 outputs by year; T-18A 6.32:1 first and T-176 ratios; low range of 2.03:1 (Dana 20) and 2.62:1 (Dana 300); SR-4, T-4 and T-5 casting numbers; Novak quotes; the Limited (2,500) and Jamboree (630) figures; the Canadian Army trucks (195, ECC 121526); YJ dates (green-lit 1982, unveiled February 1986, on sale 13 May 1986); the 60 Minutes segment; every ExtremeTerrain fluid figure; all nine NHTSA recalls with their unit counts; VIN codes and plate locations; Easter Jeep Safari 2027 dates; all four YouTube channels; and all three Instagram handles (each linked from the company's own site).

### Still unverified / shortcomings
- **Med.** CJ-7 wheelbase: Wikipedia's infobox says 93.3 in, while Quadratec and jeep.com say 93.5 in. Left at 93.5.
- **Med.** The automatic-transmission fluid specs (TH400, TF999) come only from ExtremeTerrain's generic "ATF+4". I've marked them [CONFIRM IN MANUAL], but a factory fluid chart would be better.
- **Low.** BaT value ranges and medians can't be re-derived from BaT's public page.
- **Low.** Photos: only 3. The hero (Turkish-plated CJ-7 with a full-length aftermarket-style hardtop) is plausible but its model year can't be confirmed.
- **Low.** The Morris 4x4 steering-brace link is a search URL that returned 503 to curl.

---

## CJ-5

### Corrections made
- **1979–83 258 output.** The page said "≈ 98 hp (1979 rating)", which has no source. Corrected to 110 hp / 195 lb-ft for 1979–81 and 115 hp / 210 lb-ft from 1982. Source: Offroaders AMC 258.
- **Hub bolt pattern.** The page said 1980–83 trucks have five-bolt hubs. Offroaders says 1981 and Wikipedia says 1980, so the service note and timeline now give both and tell owners to count the bolts.
- **CJ-6 wheelbase (extra file).** Was "103 in for 1972–75". Now "103.5 in (Wikipedia; Quadratec says 103 in)".
- **Dauntless V6 FAQ.** "Later bought the tooling" is now "GM sold Kaiser-Jeep the design and tooling in 1967". Source: Wikipedia Buick V6.
- **Lead paragraph.** The M38A1 component list is now attributed to Hagerty. "CJ-2A, first mass-produced civilian 4WD" (unsourced) became "first production civilian Jeep". The Hurricane's ratings are now marked as gross.
- **Prices.** The RT23007 kit was listed at "about $450 MSRP"; it is $407.69 at Quadratec, so the page now says about $410.
- **Golden Eagle edition (extra file).** It listed a 304, power steering and disc brakes as definite contents. Now: tachometer, clock and decals per Wikipedia, with the other items marked as period claims to check against the build sheet.

### Removed or softened
- The tire FAQ now says the Jeep-CJ.com thread was about a stock CJ (the question concerned a CJ-7; the respondent runs a '79 CJ-5).
- The BITOG "1955 manual calls for GL-4" claim: the thread starter only summarizes the manual, so it's softened and marked [CONFIRM IN MANUAL].
- The BaT values note now reads as a compilation to recheck.

### Added
- Sources: Offroaders AMC 258 and Dana 30.
- Alt text now says the vehicle is Brazilian-registered and that all three photos show the same truck.

### Verified and left as is
Production start in October 1954, 603,303 built and 29 years (Hagerty, Wikipedia); the Perkins diesel (62 hp / 143 lb-ft); the Dauntless (155 hp, about 75% take-up by 1968, $81 power steering); the 1972 changes (2.5 in stretch, 5 in longer nose, Dana 30 saving 25 lb and 6 ft of turning circle); the 1976–77 frame changes; the 60 Minutes test (8 rollovers in 435 runs); the Land Rover and Land Cruiser origin claims; Brazil and Ford production; the Renegade I and II details; the Silver Anniversary (1,000 built); all 11 recalls with unit counts; RockCrawler torque figures (65 / 55 ft-lb); HEI write-up details (0.045 in gap, 1-5-3-6-2-4 firing order, 8° BTDC); Hagerty quotes and prices; and part-to-title matches for every Quadratec and RockAuto link.

### Still unverified / shortcomings
- **Med.** Photos: all three show the same heavily HDR-processed, Brazilian-registered Jeep. It's probably a Brazilian Willys/Ford "Universal" (CJ-5-based), not a US CJ-5. A US CJ-5 photo would be better.
- **Med.** No sourced fluid capacities for the F134, the Dauntless V6, the T-90/T-14 or the Dana 18 (marked [CONFIRM]).
- **Low.** NHTSA campaign 76V-025 (no summary; 1972–76 CJ-5/6/7) isn't listed.
- **Low.** BaT statistics are not re-derivable.

---

## CJ-8 Scrambler

### Corrections made
- **T-5 dates (Med).** The page said "For 1985 and 1986 the T-5 arrived". Offroaders says the T-4 and T-5 were in CJs from 1982 to 1986. The story, engineering cell, plate, generations row and FAQ now give 1982 per Offroaders and note that SlashGear says 1985–86. The fifth-gear ratio now shows 0.76 (SlashGear) and 0.8 (Offroaders).
- **Engine years.** The GM 151 was dated "1981–82", leaving a gap in 1983. Corrected to 1981–83, with the AMC 150 from 1984. The paragraph that leaned on RockAuto's catalog was replaced. Sources: Offroaders GM 151, Wikipedia Iron Duke.
- **Hubs.** "Five-bolt hub pattern from 1980" (and "1980–86 CJs") now reads that every Scrambler has five-bolt hubs.
- **Tops.** "Hard half-cab standard, full tops optional" is now attributed to SlashGear. 4WDrive describes a "removable soft or hard cab", and the 1983 Reagan photo shows a soft half cab.
- **Bed length.** "Bed is two feet longer than a CJ-7's rear tub" is now attributed as 4WDrive's description of the stretch.
- **Reagan photo date.** Now cites the National Archives / Commons date, 2 April 1983. The second photo is dated 6 April 1988.
- **eBay example.** The "2,100-mile" truck has a five-digit odometer; now worded that way. Source: eBay Motors via WebFetch.
- **Axle-kit price.** The J8133885-1 kit (driver side only; the passenger side is a separate kit) is $215 at Quadratec. The cost line now says this.

### Removed or softened
- The BaT values note no longer gives specific dollar figures for one-off builds.

### Added
- Sources: Offroaders T-5 and GM 151; the Commons/NARA photo record.

### Verified and left as is
Production by year (8,355 / 7,759 / 5,405 / 4,130 / 2,015 / 128, total 27,792); the March 1981 launch, payload of 636 kg and prices of $7,288, $6,765 and $8,392 (4WDrive); the Alaska World Cab (230 built) and the Overlander; the Comanche replacement (Wikipedia); Reagan's Scrambler (RealTruck, KEYT, Conejo Valley Guide); recall 88V-009 (230 units); and all part links.

### Still unverified / shortcomings
- **Med.** Only 2 photos. Both are Reagan ranch images and neither shows trail use. No action photo of a CJ-8 off-road.
- **Low.** The tire-fitment FAQ is borrowed from a general CJ thread; there's no Scrambler-specific source.
- **Low.** T-176 capacity is marked [CONFIRM]; ExtremeTerrain's figure contradicts itself.

---

## Grand Wagoneer (SJ)

### Corrections made
- **360 V8 output (Med).** The page said "Wikipedia's AMC V8 entry gives 160 hp for 1978–91". The Wikipedia table actually gives 144 hp / 280 lb-ft for the 1991 two-barrel, matching Offroaders. Fixed in the engineering note, the FAQ and the generations table, which now reads 140–144 hp.
- **Chrysler purchase.** "Chrysler bought AMC on March 2, 1987" is now "agreed to buy AMC on March 9, 1987" (Wikipedia AMC). The extra-file timeline matches.
- **Best years.** "Wikipedia and Hagerty both point to 1989–91": Hagerty doesn't, so only Wikipedia is cited.
- **Hagerty values.** "For nearly a decade" isn't in the Hagerty piece; removed. The pandemic "most sought-after" claim is now attributed to Hagerty via Wikipedia.
- **Motorcraft 2150.** Kept, now sourced to Team Grand Wagoneer's carb kit. Removed "rather than fitting its own fuel-injected V8", which was interpretive.
- **Fluids (gap filled).** Added AMSOIL's 1989 capacity lookup, still marked [CONFIRM IN MANUAL]: engine oil 5 qt with filter, coolant 13.7 qt, A727 about 4 qt (8.6 qt total), NP208/229 5.9 pt, front differential 2.7 pt, rear 3 pt. Corrected the Team Grand Wagoneer service intervals to what the product pages say: ATF every 30,000 mi or 3 years with conventional fluid; transfer case every 50,000 mi severe use, 100,000 mi normal use.
- **Extra file.** The 1984 entry ("258 standard") is now attributed to Hagerty. The Haynes manual name now matches Quadratec's listing (1984–91 Wagoneer and Grand Wagoneer).

### Removed or softened
- BaT top-sale specifics are folded into a range, marked to recheck.

### Added
- Sources: AMSOIL lookup, Wikipedia AMC, Team Grand Wagoneer filter-kit listing.

### Verified and left as is
The November 1962 introduction, 29 years and longest-running claim; the $20 million development cost and the Tornado engine; Super Wagoneer output and production (270 hp, 3,989); 1978 Limited ($10,500, 28,871 built); production by year (20,019 / 17,814 / 17,254 / 14,265 / 14,117, and 4,253 Final Edition); 6,449 in 1990; the 27 February and 21 June 1991 dates; 6,378 ZJ Grand Wagoneers; the VAM 282 engine, Alpina and Ambassador (10–30 built); hunter green as a 1991-only colour; every Wagoneer World spec (108.7 in, 186.4 in, 10.1 in, 20.3 gal, 2.6:1, 2.73, 5,000 / 3,500 lb towing, 16:1–13:1, 37.7 ft); the Hagerty and Kerr quotes; DrivingLine figures; NP208 use on some trucks to 1988 (Offroaders); 4 recalls; and 60+ Team Grand Wagoneer part titles.

### Still unverified / shortcomings
- **High.** Fluid capacities rest on a lubricant vendor's lookup (AMSOIL), not a factory chart. AMSOIL also lists 75W-140 for the rear axle and a Command-Trac note that doesn't apply. Rear main-cap torque and head-bolt specs are absent ([CONFIRM]).
- **Med.** The tire FAQ admits there's no sourced consensus for maximum tire size, and the extra file has no `max_tire` entry.
- **Med.** Photos: the two Webster, NC shots (hero and side view) show a parked truck on a roadside gravel pull-off with traffic behind. That breaks the off-road-only rule. The other two photos are honestly captioned non-Grand-Wagoneer SJs.
- **Low.** "Hagerty says a 4.2 six was standard 1984–86" contradicts most accounts of a V8-standard Grand Wagoneer. It's attributed, but an expert should check it.

---

## Cherokee XJ

### Corrections made
- **Fluid attribution (High).** The FAQ and service intro said the figures were "Per the 2001 owner's manual as quoted on NAXJA". The thread is actually a member's capacity summary that doesn't say which year each figure applies to. Now attributed correctly. Also flagged the conflicts with ExtremeTerrain, all marked [CONFIRM IN MANUAL]:
  - AW4 fluid: Dexron III vs ATF+4.
  - Coolant: 10.5 qt vs 12 qt.
  - NP231: 2.2 pt vs 1.6 qt.
  - AX-15 and AX-5: GL-3/4 vs GL-5.
- **0331 head (High).** The repair recommended the Crown 53010334 head, but the listing doesn't state its casting. The part name now says to confirm it isn't an 0331. Added Wikipedia's caveat that even "TUPY" heads occasionally crack (FAQ and repair).
- **Rough Country link.** `rough-country.com` is a parked, for-sale domain. Replaced with `https://www.roughcountry.com/`.
- **Tire FAQ / extra fitment.** "NAXJA consensus" is now described as what members said in one 2005 thread. The rear-fender rub is now correctly tied to the 255/70R16, not the 30x9.50. "1997–2001 trucks have less room" is now attributed to one member (NAXJA max-tire-98 thread).
- **Up Country package.** "Skid plates and tow hooks" was unsourced. Replaced with: an inch of lift and no rear anti-roll bar (Wikipedia).
- **Coil rail.** The claim was reworded to match what the NAXJA post actually says.

### Removed or softened
- The BaT values note is marked as a compilation to recheck.

### Verified and left as is
Unibody "first", the 1,200 lb / 31 in / 90% interior-volume comparisons, about 3,200 welds and about 3 million built; Renault's 22% stake, the $250 million budget and the Teague, Lunn and Castaing roles; engine outputs (173, 177, 190, 193 hp); rear-axle years and spline counts; the low-pinion Dana 30 for 2000–01; Beijing Jeep and the BAW Qishi; trim editions; Cumberford and Kiplinger quotes; OffroadXtreme cooling and buying claims; NAXJA crash-course claims; 1987–90 VIN codes (Offroaders); all 13 recalls plus the RHD import campaigns 08V-056 and 11V-279; and all part titles.

### Still unverified / shortcomings
- **High.** Fluid specs conflict across sources as listed above, and no factory owner's manual was available to settle them.
- **Med.** Rear main-cap torque relies on one member's "80 ft-lb for a 1999" ([CONFIRM]). No factory head-bolt torque or sequence is given.
- **Low.** The engineering intro's claim that every transfer case is chain-driven in an aluminum housing isn't directly sourced.
- **Low.** Photos are good (all four show XJs off-road). Two show the same maroon truck.

---

## Top 5 remaining problems (jeep-classic)

1. **XJ fluid specs conflict (High).** NAXJA and ExtremeTerrain disagree on AW4 fluid, coolant capacity, NP231 fill and AX-15 gear-oil grade (GL-4 vs GL-5). An expert or a factory manual needs to settle these, because the wrong gear oil can damage a synchro box.
2. **Grand Wagoneer fluids and torques (High).** The capacities come from a vendor's lookup (AMSOIL), and there are no torque specs for the rear main cap or head bolts. It needs a factory service-manual table.
3. **XJ replacement-head guidance (High).** The page warns never to fit another 0331, but whether the recommended Crown 53010334 is a non-0331 casting is unknown. Confirm with Crown or remove the part.
4. **CJ automatic-transmission fluids and wheel-bearing procedure (Med–High).** The ATF+4 listing for a GM TH400 and the missing outer-nut torque are marked [CONFIRM], but a factory figure should replace the placeholders.
5. **Photo set (Med).**
   - CJ-5: three frames of one Brazilian-built Jeep.
   - CJ-8: no off-road photo.
   - Grand Wagoneer: hero and side shots are a roadside lot, not off-road.

   All three models need replacement trail photos of the correct US models.
