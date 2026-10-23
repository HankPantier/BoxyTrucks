# Fact-check report: land-rover group

Models checked: `defender-90-110` (flagship page and family object in `data/land-rover.json`, plus `data/extra/land-rover/defender-90-110.json`), `series`, `defender-l663` and `discovery-1` (pages in `data/pages/land-rover/` and detail files in `data/extra/land-rover/`).

**Method.** I extracted all 382 unique URLs and checked each one with curl. 275 returned 200. 97 returned 403 and 7 returned 401. Those were bot walls (Cloudflare or Akamai): NHTSA web pages, Rovers North, AULRO, ECD, Hagerty, CarsGuide, BolidenForum, GearJunkie and the Unsplash and Pexels photo pages. For the 200s I checked page titles, and for parts I checked the fitment text. I verified the main claims against:

- Wikipedia: Land Rover Defender, Land Rover series, Land Rover Defender (L663), Land Rover Discovery and Camel Trophy.
- The NHTSA recalls API, by vehicle and by campaign number.
- Land Rover USA's spec pages and the 21MY Defender 90 technical-data PDF.
- FuelEconomy.gov.
- RM Sotheby's lot pages.
- ECD, Atlantic British, Motor Authority and Hagerty, all fetched through WebFetch.
- Defender2.net and LandyZone threads, PistonHeads, GoAuto and BolidenForum.

I opened all 14 photos. Cross-links (`[[...]]` and `related`) all resolve.

**Site-wide issue (outside my scope, not touched).** `https://www.oldmanemu.com/` is a parked domain that GoDaddy is selling. It is still linked from `data/affiliates.json`, `range-rover.json`, `land-cruiser.json`, `nissan-patrol.json` and several Jeep and Land Cruiser pages. In my files I replaced it with `https://arbusa.com/old-man-emu`. The owners of those other files should do the same.

---

## Defender 90 / 110 (flagship) + family object

### Corrections made
- **LT230 note (engineering).** The note said the LT230 was "used in pre-Td5 Defenders…", which wrongly implies the Td5 and Puma trucks used something else. It now reads: "used through the Defender run (early V8 One Tens had the LT95), plus Discovery 1 and Range Rover Classic." Source: Wikipedia Defender (LT95 on early V8s).
- **300Tdi timing-belt torque (repair, High).** The page said "tensioner bolt torque reduced from 14 Nm to 11 Nm". The AULRO thread actually describes the torque used *to tension the belt*, applied to the tensioner before its bolt is tightened. It is not the bolt's clamping torque. I rewrote the step and added `[CONFIRM IN MANUAL]`. Source: AULRO thread 42103 (via WebFetch).
- **Swivel preload repair.** The 1.16–1.46 kg figure checks out against the workshop-manual text quoted on Defender2 topic8607. I added the bolt torques from that same text (bearing housing to axle 73 Nm, lower pin 25 Nm, top pin 65 Nm, sealant STC50552) and a `[CONFIRM IN MANUAL]` marker.
- **Rear axle capacity note.** The note said "Defender2 members found the 1.7 L book figure close". The thread says the opposite: an owner got nearly 2 L into the axle on level ground. The note now tells owners to fill to the level plug.
- **Swivel lubricant (High).** I added that a 1997 NAS D90 data set (BolidenForum) still lists 0.35 L of EP oil, while Lucky8 lists one-shot grease for 1994–97 NAS 90s. Owners are told to check what is in theirs before topping up.
- **Chassis repair cost.** "Galvanised chassis about £2,000 supplied" was not in PistonHeads. It now reads "supplied and fitted for under £5,000 (UK), per PistonHeads". Outriggers at about £30 each is confirmed.
- **2014 DHS seizure story.** "Dozens… many came back" became: more than two dozen Defenders seized from one North Carolina importer's group, found correctly imported and ordered returned in 2015 after a pro bono challenge (Motor Authority). The separate Hagerty case is now attributed correctly. I also tightened the detail file's import paragraph.
- **NAS 90 body styles and final run.** The story now says the 90 came first as a soft-top, then with a removable fibreglass roof panel or a full hard-top (Wikipedia). The "tops cracked" claim is now attributed to ECD. The final run is now described as the 300-unit **Limited Edition station wagon** in Willow Green with a white roof and a numbered placard (Wikipedia, ECD). The callout's "Colors later included…" became "across the run", because Arles Blue was a 1994-only colour (RM Sotheby's).
- **Fuel economy.** The ECD figures are now labelled ECD's *estimates* (method not stated) rather than "real-world" figures. Changed in both the FAQ and the capability row.
- **Family intro.** Added that the Amsterdam launch was in April 1948 (Wikipedia).
- **Part labels.** STC8651 now carries its "Defender 110 to VIN WA159806" limit (Lucky8). The Britpart link was a broken search URL (`?q=` returned "No results for ''"). It is now `?Query=footwell`, which returns 31 results, relabelled "confirm fitment".
- **Old Man Emu link.** Replaced the parked domain with ARB USA's Old Man Emu page.
- **Wheel torque (detail file, High).** "96 lb-ft (130 N·m)" is confirmed by BolidenForum, but its 1997 D90 page also lists 170 N·m. The field now shows both, with `[CONFIRM IN MANUAL]`.
- **Stock tyre sizes.** The detail file's stock line now attributes the 235/80 and 265/75 sizes to 1998 data from Limitless Tire.
- **Photo alt.** The hero alt text now describes the light bar and roof tent that are actually in the shot.

### Removed or softened
- The Hagerty-owner line now uses "apparently lost". The "galvanised chassis £2,000" figure is removed.

### Added (with sources)
- Swivel bolt torques (Defender2 manual quote), a towing cross-check (GoAuto 2009 D90: 3,500/750 kg) and the LT77 capacity of 2.67 L for the 1993 NAS 110 (BolidenForum).
- New sources: GoAuto, both BolidenForum pages, the Britpart search and ARB USA.

### Verified as correct (selected)
- One Ten 1983, Ninety 1984 and One Two Seven 1985. Renamed Defender for the 1991 model year.
- 2.5 D at 68 hp. Diesel Turbo in 1986 at 85 hp. V8 at 134 hp in 1986.
- 200Tdi at 107 hp / 195 lb-ft; 300Tdi at 111 bhp / 195 lb-ft; Td5 at 122 hp; Puma at 122 hp / 265 lb-ft (2.2 from 2012).
- Production ended 29 January 2016, the 2,016,933rd Defender.
- 1993 NAS 110: 525 built (500 US, 25 Canada), Alpine White, 3.9 V8, five-speed, external cage (Wikipedia and Atlantic British).
- 1997 NAS 90: 4.0 V8 and ZF automatic (RM Sotheby's). US sales ended because of the 1998 airbag and side-impact rules.
- SV90: 90 built. 50th Anniversary: 1,071 built, 385 for the UK. Defender Black: 92 and 144. Works V8: 150 built.
- South Africa 2.8i: 1,395 (656 + 739).
- NHTSA recalls 95V099000 (155 units) and 96V108000 (4,254 units).
- Fluids from BolidenForum's 1997 D90 page: oil 6.7 L, coolant 12.8 L, ATF Dexron IID 9.1 L, transfer box 2.3 L, front axle 1.7 L, PAS 2.8 L.
- Fuel tank 79.5 L (1993 110). GoAuto's 47°/47° angles and 500 mm wading for the 2009 90.
- Part pages: all Lucky8 and LR Direct product pages resolve to the named part.

### Still unverified / shortcomings
- **High:** Defender wheel-nut torque is 130 or 170 N·m depending on the source. It needs the workshop manual.
- **High:** The Td5 and Puma oil grade and capacity, the V8 EFI fuel filter and the Salisbury rear axle capacity are still `[CONFIRM IN MANUAL]`.
- **High:** The Comma Oil data (300Tdi 6.65 L oil, 11.1 L coolant, intervals, R380 oil) could not be checked. The egress proxy blocks app.commaoil.com.
- **Med:** All the AULRO tyre-fitment threads (255/85, 285/75, 315/75) and the 35s thread sit behind Cloudflare. I couldn't re-read them, so the tyre FAQ rests on the original research.
- **Med:** The CarsGuide 2004 towing page returns 403. GoAuto backs up the figure.
- **Med:** All Rovers North links (`/search?q=`, parts pages, forums, the blog) return Cloudflare 403. The search URL format is the project standard (`data/suppliers.json`), but I couldn't confirm it works.
- **Med:** The "≈7,059 NAS total" figure comes only from ECD, a commercial builder.
- **Low:** Defender Source forum links return 202 with a JS challenge.
- **Low:** Photos: all four are genuine classic Defenders off-road. The location tags ("Danish dunes", Vejers Strand) come from the Unsplash listings and can't be checked from the image itself. `defender-110-dirt-road.jpg` shows power lines and houses on the horizon.

---

## Series I–III

### Corrections made
- **Hagerty claims.** The US-rarity comparison named the FJ40, but Hagerty says "a comparable Jeep or Land Cruiser". The text now matches, and the link is kept. The $39,000 median and the 6% and 2% premiums are now dated to Hagerty's 2019 analysis. That was done in the story, the FAQ and the detail file's value intro. The horsepower figures (77 and 94 hp) were confirmed against Hagerty.
- **Freewheel 4WD date.** "Around 1950" became "during 1950–51". Wikipedia gives mid-1951 in one place and "during 1950" in another. The timeline was updated to match, and the 2.0 petrol date is marked as differing between sources.
- **Tyre FAQ and repair.** Rewritten to what the Rovers North thread actually says:
  - 235/85 is "close to but a little wider than" 7.50x16.
  - 215/85 is "also close"; it was previously called "safer".
  - 265/75 rubbed by ½–¾ in for one owner, and another found it too wide on a 109.
  - The "rims at least 5.5 in" rule wasn't in the thread, so I removed it and replaced it with the tube-type rim warning.
- **STC3945 brake shoes (fitment, High).** LR Direct lists this part for Series LWB six-cylinder and V8 trucks and the 101 FC only. It was labelled as a generic Series part. The label is now corrected.

### Removed or softened
- **Instagram handles removed:** @lrsoclub, @lrseries2club, @lr_series_i_ii_iii_club and @series1landrover. I couldn't confirm they exist: Instagram serves a login wall, and a web search found nothing. @series3.restoration is kept because its page title confirms it. The YouTube channels are kept because all four resolve to the named channels.

### Verified as correct (selected)
- Wilks, Anglesey and the Jeep. Centre steer, Birmabright and the cockpit-green paint.
- Amsterdam launch. The 80-inch truck with the 1.6 at about 50 bhp.
- Tickford: fewer than 700 sold.
- Wheelbases 86/107 (1954), then 88/109 (1956). 2.0 diesel in 1957.
- Series II: about 1,500 early trucks kept the 2.0. The 12-seater counted as a bus for tax.
- 811 NADA trucks. Headlamps moved into the wings in February 1969.
- Just under 600,000 built by February 1968, more than 70% exported. Sales over 60,000 a year in 1969–70.
- Series III changes: all-synchro gearbox, compression raised from 7:1 to 8:1, Salisbury axle on LWB.
- Factory sales to North America ended in 1974. The millionth Land Rover was built in 1976.
- Five-bearing engine in 1980. 24-spline shafts in 1982. County trim in April 1982.
- Stage 1 V8 at 91 hp, 24 of them built as 88s. About 440,000 Series IIIs built.
- One Ton 109 (1968–77): 170 and 238 built.
- Pink Panther conversions by Marshall's. Dutch and Danish Lightweights had diesels.
- LR Direct part pages all match their labels.
- Photos: all four are correct Series trucks off-road, and the captions match the Wikimedia and Unsplash titles.

### Still unverified / shortcomings
- **High:** Engine oil capacity, gearbox and axle capacities, coolant and brake-fluid grade are all `[CONFIRM IN MANUAL]`. That is honest, but it's a gap for owners.
- **Med:** Every Rovers North forum source (swivel, half-shaft, clutch, cruising speed, California registration) returns 403. Only the tyre thread could be re-read, through WebFetch.
- **Med:** The swivel preload range is deliberately left to "the workshop manual"; there is no Series figure.
- **Low:** The AULRO fuel-economy thread couldn't be re-read. The Series I 80" photo is hard to confirm as an 80" from the image alone, so I trust the Commons title.

---

## Defender (L663)

### Corrections made
- **Wading depth (safety, High).** The page gave 900 mm everywhere. Land Rover's 21MY Defender 90 tech data rates coil-sprung 90s at **850 mm**. The figure is now corrected in the story, the engineering note, the FAQ, the buying check and the detail file's identify item.
- **Coil ground clearance.** The tech data gives 225 mm (226 mm at the off-road setting). The page and detail file are now consistent.
- **Dakar claim.** "Says it won on its 2026 debut" was misleading. The D7X-R won the **Stock category**, not the rally outright (Land Rover media release, January 2026). Corrected and sourced.
- **275/60R20 fitment.** The page said the owner had fitted these to "a coil-sprung 110". That contradicts the page's own "every 110 is on air" line, and the thread doesn't identify the body. It now says "a coil-sprung truck" on both the page and the detail file.
- **Fuel-economy FAQ.** The NEDC figures for the P400 (9.9) and P525 (12.1) couldn't be traced. They are replaced with EPA 2026 figures:
  - 3.0 six: 18 city / 22–23 highway.
  - V8: 14–15 city / 18–19 highway.
  - OCTA: 15 / 19.
  - The diesel figure (7.6 L/100 km NEDC-equivalent) comes from the 21MY tech sheet. The owner's 40 mpg report is kept.
- **US engine FAQ and identify item.** Added that EPA still lists 2026 2.0 and V8 trucks, and that EPA shows the 2026 130 P300 as a 3.0 six.
- **Oil filter part.** A search link that returned oil-filter *housings* is replaced with LR133455, the 3.0 Ingenium oil filter element. LR Direct's fitment lists New Defender 3.0 AJ20D6 and AJ20P6.
- **Searches.** The Defender 90 AutoTempest link now starts at 2021, matching its label; the US 90 arrived for the 2021 model year.

### Removed or softened
- P400e: removed the unverified 640 Nm and "27 miles (43 km)" figures. The row now reads "404 PS system, 110 only, not sold in US".
- D350 "from 2024" became "added later". The model year couldn't be confirmed. Changed in the table and the timeline.

### Added (with sources)
- **Recalls (NHTSA API):**
  - 26V263000 (2026 fuel tank walls too thin, fire risk).
  - 22V523000 (front belt pretensioners).
  - 23V789000 (TReK-modified 130 calipers could detach; relevant to the TReK identify item).
- All existing recall entries checked out against the API, including their Land Rover numbers N598, N763, N908, N964 and D120. 26V599000 expands 26V248000.
- Sources added: Land Rover Dakar release, the 21MY tech PDF, FuelEconomy.gov, LR Direct LR133455 and the three NHTSA recall pages.

### Verified as correct (selected)
- Frankfurt reveal on 10 September 2019. Nitra plant opened 25 October 2018. Shares no components with the old Defender.
- Lockable centre diff and locking rear diff. ZF 8-speed. 50/50 bevel centre diff.
- 4,536 kg winch rating. Every 110 on air. Up to 291 mm clearance.
- US towing 8,200 lb and UK 3,500 kg.
- Roof loads 370 / 260 / 661 lb, V8 has no dynamic rating, OCTA mode is 0 (Land Rover USA).
- Bond Edition: 300 built, 22-inch wheels, blue calipers, £105,000.
- 30th Anniversary Edition: 500 Fuji White 110 P300s, all with the same 1/500 badge.
- Lego set: 2,573 pieces.
- OCTA: 635 PS / 626 hp, 750 Nm, 0–60 in 3.8 s, 323 mm clearance, 1 m wading, 33-inch tyres, 6D suspension, Faroe Green Edition One.
- 26MY update revealed 28 May 2025. Wolf Series II, September 2026 (Wikipedia).
- E005 build window 1 March 2024 to 18 April 2026 (Defender2 thread).
- Owners' oil refills of 8.5–8.8 L.
- Wheel spec: 5x120, 72.6 mm bore, M14x1.5, 140 Nm.
- Photos: all three are genuine L663s on dirt, sand or forest tracks.

### Still unverified / shortcomings
- **High:** Petrol oil grade, ZF 8HP fluid capacity, transfer-case and diff fluids, coolant and brake-fluid grade are still `[CONFIRM IN MANUAL]`. The 8HP service-kit fitment needs checking.
- **Med:** The "Gerry McGovern styled it" claim isn't in the Wikipedia text I checked, though it is widely reported.
- **Med:** Track-rod-end and exhaust-pressure-sensor links are generic searches. The steering-joint and PM-sensor links are LR Direct part searches that resolve to the named part.
- **Low:** In `l663-dust.jpg` the road has power poles. The Pexels slug calls the car white, while the alt text says silver; the photo looks silver or white.

---

## Discovery Series I

### Corrections made
- **Horse and Hound edition.** The callout said 1998; Wikipedia and the detail file say **1997**. Fixed.
- **Sunroof buying check.** "A 1998 Anniversary model, specified without sunroofs" is now attributed to a LandyZone member, and I added the verified fact that the US XD was built without sunroofs (Wikipedia).
- **Old Man Emu link** replaced, as for the flagship. **Photo alt text** for `disco1-200tdi-offroad.jpg` corrected: it is a pre-facelift truck in a concrete-sided trench, not "cross-axled with rock sliders".
- **Wheel torque** now carries `[CONFIRM IN MANUAL]`.

### Removed or softened
- **DiscoWeb community link and source removed.** Every page on discoweb.org now shows "Oops! We ran into some problems." The archived thread used on the flagship (`/oldsite/…`) still works.

### Verified as correct (selected)
- Project Jay. Frankfurt 1989, UK sales from October. Three-door first, five-door in 1990. 64 G-WAC press cars.
- Conran interior, which won a British Design Award in 1989. Sonar Blue trim. Parts-bin sources: Maestro and Montego, Rover 800 vents, Freight Rover headlamps, Maestro van tail lights, Marina door handles.
- Engines: 3.5 V8 on SU carburettors, then 14CUX injection from 1990. 2.0 Mpi petrol for UK and Italian tax reasons.
- 1992: automatic 200Tdi, beige trim and the SE pack. 1994: 300Tdi, 3.9 V8, R380 gearbox and the new dashboard.
- US: 1994–98 model years, V8 only. The 1996+ "4.0" is the same 3,946 cc, changed to GEMS for OBD-II. XD: 250 built.
- Camel Trophy: 200Tdi from 1990 (Siberia, three-door) to 1994 (Argentina, Paraguay and Chile), then 300Tdi from 1995 to 1997 (Mongolia).
- Honda Crossroad. Special editions: Country Life (50), Orienteer (75), Goodwood (500 planned, 1 badged), Safari (1,100).
- Australian-spec outputs.
- Recalls 98V040000 (54,488), 04V203000 (45,267), 96V247000 (20,889), 95V099000 and 12E010000 (TVF100010 couplings made April–November 2011).
- LandyZone claims: tyres (245/75 stock maximum; 35s need a 4.1 to 4.37 ratio), rust list and three-doors being worse.
- Photos: both are genuine Disco 1s (one facelift, one pre-facelift) off-road or in a ford.

### Still unverified / shortcomings
- **High:** Engine oil grade and capacity, R380 oil, swivel lubricant, coolant type, brake-fluid grade and intervals are all `[CONFIRM IN MANUAL]`. The baseline service section is the thinnest in the group on hard numbers.
- **Med:** Only two photos. A third off-road shot, ideally a US V8 truck, would help.
- **Low:** BaT lists a "1996 Discovery XD 5-Speed", but Wikipedia says the XD was a 1997 automatic-only special. Someone should check this before relying on the XD's year or gearbox.
- **Low:** The AULRO Discovery forum link returns 403.

---

## Top 5 remaining problems (land-rover group)
1. **Fluid specs and capacities are mostly `[CONFIRM IN MANUAL]` across all four models (High).** The Series, Disco 1 and L663 baseline service sections lack sourced oil grades and capacities. The flagship's 300Tdi numbers rest on a Comma Oil page that the proxy blocks.
2. **Classic Defender swivel lubricant and wheel-nut torque conflict between sources (High).** Swivels: one-shot grease or 0.35 L EP oil on 1994–97 trucks. Wheel nuts: 130 or 170 N·m. Both are now flagged, but the workshop manual should settle them.
3. **The site-wide `oldmanemu.com` link is a parked domain for sale (Med).** It is fixed in my files but still used by other families and in `affiliates.json`.
4. **Many forum sources couldn't be re-read (Med).** These are Rovers North, AULRO and the CarsGuide towing page, all behind Cloudflare. That includes the classic Defender tyre-fitment consensus and most Series repair guidance. The Rovers North `search?q=` URL format is also unconfirmed.
5. **The 300Tdi timing-belt tension figure (11 vs 14 Nm) is a forum-reported factory change (High).** The text is now accurate about what the figure is, but a Land Rover service bulletin or the RAVE manual should confirm the procedure before owners rely on it.
