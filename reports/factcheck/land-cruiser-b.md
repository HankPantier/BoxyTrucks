# Fact-check report: land-cruiser-b

Models: 70 Series, 100 Series, 200 Series, 250 Series, 300 Series (family `land-cruiser`).
Files edited: `data/pages/land-cruiser/{70,100,200,250,300}-series.json` and `data/extra/land-cruiser/{70,100,200,250,300}-series.json`. Schema unchanged. All ten files parse as JSON.

## Method

- **Links:** I curled every URL in all ten files and fetched page titles for every part and mod link to catch soft 404s and wrong products.
  - Hard 403s were from bot-blocked suppliers only: Slee Off-Road, Amsoil, NHTSA recall pages, Roughtrax, Dobinsons, Superior Engineering, Toyota pressroom and Blackstone. Their URL formats are real. Amsoil, Roughtrax and the Toyota pressroom pages were also read through WebFetch.
  - RockAuto, Lexus Parts Now and TLCA returned 000 on the first pass and 200 on retry. Tundra Headquarters (526) and the Expedition Portal thread were read through WebFetch.
- **Sources:** I checked claims against Wikipedia wikitext for J70, the main Land Cruiser article (J100/J200/J300), Prado J250, Lexus LX and Grey import. I also used:
  - NHTSA's recall API (by vehicle and by campaign number) and the 25V767 Part 573 PDF
  - Toyota's 2021 Land Cruiser Warranty & Maintenance Guide PDF and the 2024 Land Cruiser Owner's Manual PDF (OM60U35U)
  - KBB spec pages for 1999, 2002, 2004–06, 2008, 2015, 2016, 2021 and 2024
  - Unsealed 4X4 (70 and 200 articles), CarExpert, Motor1, 4X4 Australia, Car and Driver (via Yahoo), Japanese Nostalgic Car, Auto Bild, Threepiece, Toyota.com, and the cited IH8MUD and LandCruiserForum threads
- **Photos:** I opened all 16 images, and checked Commons author and licence metadata where the API allowed.
- **Cross-links:** Every `[[family/slug|…]]` and `related` entry was checked against the families' `generations` lists. One was broken and is now fixed (see 250).
- **Social accounts:** I removed none. All YouTube channels resolve with matching names. Instagram @ih8mud and @cruisercorps were confirmed through the public profile API. The others (@cruiseroutfitters, @metaltech4x4, @dissentoffroad, @familycruiser250, @sleeoffroad) could not be checked because Instagram rate-limited the requests, so they are kept, per the coordinator rule. None of my group's handles appear in `social_manual.json` or `resources_manual.json`.

---

## 70 Series

**Corrections made**

- **2.8 L torque.** The page gave 332 lb-ft for the four-cylinder. That figure is the October 2024 five-speed *manual*; the automatic makes 369 lb-ft (500 Nm). Fixed in the story, the generations table and the "Is the V8 gone?" FAQ. Sources: Motor1, CarExpert (150 kW / 500 Nm).
- **Safety and frame update date.** The story said side airbags and the strengthened frame came "in 2022". The 4X4 Australia launch report dates them to the late-2016 update: curtain and knee airbags plus a thicker chassis with seven crossmembers on the single cab, for five ANCAP stars, alongside the DPF and piezo injectors. Rewritten in the story and the detail timeline. Source: 4X4 Australia (Oct 2016).
- **V8 end date.** The engineering cell, generations row and plate said "2007–2024". GXL V8 utes shipped until Q4 2025, so these now read 2007–2025, with the September 2024 wagon/troopy end kept (Motor1). Added a 2024 timeline entry.
- **Japan return.** "End of 2023" is now November 2023. Source: Toyota global newsroom, 29 Nov 2023.
- **Fuel tank on the plate.** The plate said "130 L (wagon and dual cab)", which contradicted the detail file (2024 76 wagon: 180 L total, CarExpert). The plate now reads "130 L (79 cab-chassis & dual cab); 180 L total (2024 76 wagon)".
- **Timing-belt kit name.** The kit fits to 08/2007, not 2020; corrected per the CruiserTeq page title.
- **Wording.** "The four-door 76 wagon came back" is now "was added to the range" (Wikipedia: added in 2007).
- **Tire FAQ attribution.** The 255/85R16 "with a lift" remark was misattributed. Reworded to match the IH8MUD thread.

**Removed or softened**

- **Gearbox oil.** "The specified oil is GL-4 75W-90" is softened to "Unsealed says GL-4 75W-90". Roughtrax lists GL-4 or GL-5, and the 1HZ Toyota data says GL-4 or GL-5 SAE 90. The baseline gearbox spec now carries `[CONFIRM IN MANUAL]`.

**Added**

- Sources: 4X4 Australia 2016 update, Toyota 2023 Japan re-introduction, CarExpert 76 wagon.

**Verified (no change needed)**

- All Wikipedia history: the 1999 facelift, June 2004 Japan exit, the 2007 V8, 2009 1GR, 2012 double cab, the Canadian BJ70s and the automatic list.
- The Al-Thalab, Babcock and Technamm sidebar.
- All the Unsealed-attributed buying checks and repairs: A-pillar ~A$15k, 54 mm hub nut, ~A$500 a side, door seals fitting all 70s from 1985, 130–150 A alternator and 240 A Jaylec, Freezebrain, DPF run every 1,000–2,000 km, Black Duck seat covers about 20 mm, Superior coil conversion.
- CarExpert capability figures.
- The 70 Series Store wheel spec (5x150, 110.3 mm bore, M14x1.5, ET+5).
- The 1HZ fluid capacities (IH8MUD Toyota-publication thread) and the Roughtrax VDJ79 capacities.
- The Bring a Trailer values: the 17 sales and the $29k–42k Troopy range check out.
- Cruise Moab details.

**Still unverified / shortcomings**

- **High.** The Roughtrax VDJ79 lubricant table is headed "1KZT" although the article is about the 1VD-FTV, which the page already flags. Engine oil, transfer case and diff capacities for the V8 rest on that table alone and need a Toyota manual check.
- **Med.** The power-steering fluid for the V8 is still `[CONFIRM IN MANUAL]`.
- **Med.** There is no North American recall data, which is correct for gray imports. A human could add Australian (ACCC) recalls.
- **Low.** There are only 3 photos. The 76 river crossing and the 75 mud trial are good. The Egyptian troopies are parked on desert, which is acceptable.

---

## 100 Series

**Corrections made**

- **AHC on the Land Cruiser.** The page claimed AHC "finally became a Land Cruiser option near the end of the run" and called out "AHC-equipped 2006–07 Land Cruisers". No source supports specific years, and owners only report that AHC was optional on some UZJ100s. Softened in the story, the FAQ, the baseline intro and the AHC item name. The generations row (2005–07) dropped "AHC became a Land Cruiser option" and the unsourced "LED tail lamps (2006)".
- **Lug nut size.** "22 mm lug nuts" was unsourced and is removed from the engineering intro.
- **Part number typo.** BELTTKT021 is BELTTK021, per the CruiserTeq page.
- **OME kit name.** The CruiserTeq title calls it a stock/light-load replacement kit (listed as about 1.5 in). Name corrected.
- **Brake-bleed note.** "Cycle the ABS on dirt, then bleed again" was not in the cited thread. Replaced with the thread's actual procedure: key ON so the electric pump runs, the bleed order, and the factory manual's actuator steps.
- **Photo alt text.** The side-hill photo is a *white* 4500 EFI 100 in the UAE (Commons), not silver. The dune photo alt now notes the steel wheels and the 4500 EFI badge.
- **Source URLs.** Twelve legacy IH8MUD and KBB URLs were replaced with the canonical URLs they redirect to (page and detail TSB links).

**Added**

- Detail recalls: the 2005–07 FMVSS 110 load-label campaigns 09V223000 / 10V036000, found via the NHTSA API.
- Source: IH8MUD max-tire-size thread for the lifted fitment rows.

**Verified (no change needed)**

- Wikipedia J100 facts: 404T, Grand Cruiser, Kondo, Araco, 105 markets, 1HD-FTE in Australia from Oct 2000, the 4WD Monthly quote, Night View, 3.72 million, the two-pinion diff.
- KBB figures: 230/235/275 hp, 320/332 lb-ft, 5,500 and 6,500 lb towing, 12/15–16 mpg, 25.4 gal, 5,115–5,425 lb, 9.8 in, 192.5 in, payload, turning circle.
- IH8MUD 90k parts list (every part number), the transfer-case DIY (1.4 qt, 24 mm, 27 ft-lb, gasket 90430-18008), the front diff (1.8 qt, 10 mm Allen) and the rear diff (3.5 qt).
- Spark plug torque 13 ft-lb, the AHC 60k interval and fluid price, the heater-tee and starter-contact write-ups, and the ball-joint steps.
- Roughtrax capacities and the Amsoil 2005 lookup.
- Recall 16V065000.

**Still unverified / shortcomings**

- **Med.** Claims attributed to the Slee Off-Road 100 Series Newbie Guide could not be re-read. The site and the archive.org copy are bot-blocked from this sandbox. They include:
  - HF2A with no viscous coupling; 9.5 in / 32-spline semi-float rear; 4.30 to 4.10 gears in 2003
  - stronger U-joints and 17 in wheels in 2003; the 2004 switch to ATF WS and pink SLLC
  - coolant intervals; the throttle-sensor faults; the hitch/crossmember change; the snorkel antenna note; variable-ratio steering from 2003
  
  They are plausible and consistent with KBB and Roughtrax, but a human should confirm them against the Slee page.
- **Med.** The AHC fluid quantity (≈4.5 L) is a forum estimate, as Roughtrax itself says.
- **Low.** Photos are all desert or steppe and fit the off-road rule. The two 4500 EFI trucks may be 105s rather than IFS 100s; the captions say only "100 Series".

---

## 200 Series

**Corrections made**

- **Transfer-case anecdote.** The baseline service item claimed "One IH8MUD owner got a center-diff error after filling with 75W-90… first change at 60,000 mi came out almost black". The cited thread (1375042) is a **300 Series / LX 600** thread and says nothing of the kind. Removed, and the source dropped from the 200 page. The transfer-case spec is now marked owner-reported plus `[CONFIRM IN MANUAL]`, because Amsoil lists no transfer-case spec. The interval now follows Toyota's guide ("special operating conditions").
- **Heritage Edition count.** "Slee counts 1,202 built for 2020" did not match the detail file's 1,200. Both now use Wikipedia's 1,200, in the story and the FAQ.
- **Tire FAQ.** It had quoted one optimistic post. It now also notes that other owners in the same thread say 285/70R18 needs heat-gunning and trimming, and names 285/65R18 as the no-work size.
- **Fuel FAQ.** "Regular unleaded, not premium" is now sourced to Toyota's 2013 press release (87 AKI). The 2021 combined figure is 14 mpg.
- **Koyari quote.** Now attributed to Unsealed 4X4, which is where the quote appears.
- **Broken part link.** The Air Lift 25804 Summit search redirected to a tire category. It now points to Air Lift's own search.
- **Fuel-pump recall.** Expanded to 20V012000 / 20V682000.
- **Photo alt text.** The Gobi truck is black. The dune truck is a facelifted Dubai safari 200.

**Added**

- Detail recalls: the FMVSS 110 label and accessory campaigns (10V035000, 10V036000, 13V123000, 14V828000, 16V236000, 19V244000) from the NHTSA API.
- 2013 timeline entry: Off-Road Turn Assist, Multi-Terrain Monitor and Trailer Sway Control.
- Source: Toyota pressroom 2013 Land Cruiser.

**Verified (no change needed)**

- Wikipedia J200: development, Roraima, 2UZ/1UR/1VD outputs, the five-speed manual only on the 1GR, the 3.90 to 3.30 axle ratio, the Dakar T2 titles 2014–22, the Road & Track exit.
- KBB towing (8,500 / 8,200 / 8,100 lb), mpg, 24.6 gal, curb weights, clearance and payload.
- Amsoil 2020 capacities (7.9 qt, 30 ft-lb, ATF 10.7 qt, diffs 4 / 8.9 pt, coolant 17.1 qt).
- The Toyota 2021 maintenance guide schedule.
- Unsealed claims: 90% diesel, the 2015 DPF and piezo injectors, injectors ~A$4,000 DIY, the airbox, U-joints every six months.
- Expedition Portal water pump, IH8MUD P2438, the KDSS 5 mm valves, the Venza cap 15620-31060, the towing air-bag thread (Firestone 4164, Air Lift 25804 / 21838, 35 psi, under $250).
- Tundra HQ air-injection warranty: Tundra and Sequoia only.

**Still unverified / shortcomings**

- **High.** The 200 transfer-case oil spec (Toyota LF 75W) and its capacity have no primary source. They are marked `[CONFIRM IN MANUAL]`.
- **Med.** Slee-attributed items (US spec list, no factory axle lockers, the no-2012-model-year explanation) could not be re-read because the site is bot-blocked. The 2012 gap is well established.
- **Med.** The AB60F (2008–15) ATF capacity is still `[CONFIRM IN MANUAL]`.
- **Low.** Wikipedia's "production ended March 2021" is debatable, since non-US production ran later in 2021. Kept, as Wikipedia states it.

---

## 250 Series

**Corrections made**

- **Broken cross-link.** `[[land-cruiser/60-series|…]]` and `related.gen: "60-series"` pointed to a slug that doesn't exist. Both are now `fj60`.
- **Rear locker on the 1958 grade.** The detail file's "identify" note suggested the 1958 might lack the rear locker (from Wikipedia). Toyota.com lists "Rear and center locking differentials" on the 1958. Corrected, so the page and the detail file now agree.
- **1958 wheel width.** The buying check said 18x7.5. The owner's manual gives 18x7J for 245/70R18. Fixed.
- **2027 pricing.** The detail file said "$57,880 / $62,725 (Land Cruiser grade drops)", from CarScoops, which contradicted the page. Aligned to Toyota.com base MSRP ($58,180 / $64,255) plus $1,495 destination, with the CarScoops launch figure noted.
- **2024 destination charge.** "$1,395 dealer fee" is a destination charge. Car and Driver: $55,950 + $1,395 = $57,345.
- **Tire FAQ.** "Threepiece puts the no-modification limit at 31.5 / 32.6 in" misread the source: those are the factory tire diameters. Rewritten. The repair's "zero-offset wheels didn't fit" was not in the guide; replaced with the guide's actual offset note.
- **Fuel-tube recall.** It was labelled an "interim notice (26TA23)". Corrected to safety recall 26TA23 (interim 26TB23), NHTSA 26V673000, filed 14 Oct 2026, covering 2024–27.
- **Load-label recall.** Described as "certain 2024–2025 hybrids". It is NHTSA 24V548000, Gulf States Toyota, 2024 trucks. Fixed in the story and buying check, and added to the detail recalls.
- **Pikes Peak anecdote.** The 575°F reading was taken by a ranger at the brake check, not by the owner. Fixed.
- **Styling claim.** "Pushed A-pillars back and lowered the beltline" is softened to Toyota's own "optimized A-pillar position".
- **Battery cooling-fan warnings.** "Several trucks … that dealers cleared" is softened to what the thread shows.

**Removed or softened**

- Dead AOL source (404) removed; the Car and Driver test via Yahoo covers the same figures.

**Added**

- Combination-meter recall summary with Toyota's ~82,000 vehicles (May 2026).
- Sources: Toyota.com 2027 Land Cruiser, NHTSA 26V673000 campaign lookup, Toyota pressroom recall.

**Verified (no change needed)**

- Owner's manual: 0W-20 5.9 qt, NGK DILZKAR8E7H at 0.7 mm, coolant 12.2 / 14.3 / 2.5 qt, diffs 1.29 / 5.94 qt LT 75W-85, 91 octane, 17.9 gal, 6,000 / 1,650 lb towing, payload 1,100–1,300 lb, wheel nut torque 97 ft-lb, tire and wheel sizes, the 36 kW (48 hp) motor and the 288 V NiMH battery.
- Wikipedia J250: platform, rigidity claims, EPS, angles, 221 mm clearance, Torsen 40/60, engine table, First Edition 5,000, US sales 29,113 / 43,946.
- KBB 22/25/23 mpg and 5,037 lb.
- Car and Driver: 7.7 s, 20 mpg, sheet-metal complaint.
- Motor1: $980 intake, not watertight.
- NHTSA 26V341000, 25V744000 and 25V767000. The US 250 is not on the V35A recalls; the GX 550 is.
- LandCruiserForum TSB T-SB-0006-26 / 0046-25 and the anti-rattle springs, battery vent location, 12 V drain.

**Still unverified / shortcomings**

- **Med.** Slee AT37 "Walrus" details (travel figures, 29-gal tank, 4.56 gears, R53/AT dampers) and the Slee bumper/TSS claim could not be checked; the site is bot-blocked.
- **Med.** All three photos fail the off-road rule: a display on grass, a gravel car park in Brittany and a city street in the Philippines. The captions are honest. A Commons search turned up nothing usable. **Needs real off-road 250 photos.**
- **Low.** The 1958 "TOYOTA heritage grille" and "first light-duty Land Cruiser with EPS" rest on Wikipedia, which is fine. Flexmotor (503) was not re-read.

---

## 300 Series

**Corrections made**

- **Japan hybrid tense.** "Hybrid due there on 1 October 2026" is in the past as of today. It now says it went on sale then, per Wikipedia. Fixed in the story and the generations note.
- **Transmission recall.** Now identified precisely: NHTSA 26V094000 / Lexus 26LA01, 4,374 2025–26 LX 600s, a solenoid-failure ECU communication fault, with a free software update.
- **V35A buying check.** Made precise with the 25V767 Part 573 figures: 9,895 LX built 26 Feb 2022 – 2 Apr 2024, with 24V381 covering earlier engines.
- **Photos.** The dirt-event alt now says black and Philippines. The SA Ambulance caption now flags "(ON STREET)", since the photo was taken at a city intersection.

**Added**

- Sources: NHTSA campaign lookups for 26V094000 and 24V381000; Wikipedia Lexus LX (detail file).

**Verified (no change needed)**

- Wikipedia J300: 9 June 2021, Yokoo, 200 kg, 32° / 26.5°, 230 mm, GR Sport lockers and 5 mm shorter, the engine table, ANCAP 89/88/81/77, UAE and Kuwait sale dates, no US sale and the reason.
- Japanese Nostalgic Car quotes and the Australia trip, Miura, laser welding.
- Auto Bild: four-year wait and the G-Klasse comparison; J150 Prado only in Germany.
- Lexus LX: unveiled 13 Oct 2021, 700h at 457 hp, Overtrail 10 Oct 2024, US sales ~6,800–7,500 a year.
- Amsoil LX 600: 7.7 qt, 30 ft-lb, ATF 12.2 qt, coolant 11.7 qt, front diff 2.5 pt, rear LSD 11.1 pt.
- IH8MUD service-data posts (1.89 / 1.23 / 5.55 qt and the plug torques), the early diff change and Tundra swarf, the hatch pinch sensor, the PCS clunk workaround.

**Still unverified / shortcomings**

- **High.** Baseline service is built on the US LX 600. Diesel (F33A-FTV), 1GR and hybrid capacities and intervals are absent and marked `[CONFIRM IN MANUAL]`. Overseas 300 owners need their own market's manual. Whether non-US V35A engines are covered by the bearing campaigns is still unknown.
- **Med.** Two of the three photos are not off-road (an ambulance on the street, a GR Sport parked on a street); only the dirt-lot shot is near the brief. **Needs off-road 300 photos.**
- **Med.** The Dissent "35s on +40 offset with minimal trimming" claim is relayed second-hand from a forum. Slee links are bot-blocked.
- **Low.** The detail recalls are "lookup: none". LX recalls live on the Lexus pages, which is reasonable.

---

## Top 5 remaining problems (group)

1. **High: V8 fluid capacities on the 70.** The 70 Series V8 (VDJ7x) capacities come only from a Roughtrax table mislabeled "1KZT". Engine oil, transfer and diff capacities need a Toyota manual check before owners rely on them.
2. **High: transfer-case oil on the 200.** The URJ200 transfer-case oil spec (LF 75W) and its capacity are unsourced. I removed a fabricated anecdote that had been citing a 300 Series thread; spec and capacity are now marked `[CONFIRM IN MANUAL]`.
3. **High: 300 service specs are US LX 600 only.** Diesel, 1GR and hybrid service specs are missing, and V35A recall coverage for non-US engines is unknown.
4. **Med: Slee claims unchecked.** Slee Off-Road content behind the 100, 200 and 250 claims (100 axle and gear specs, ATF and coolant changeover, the 250 AT37 build) could not be re-read because the site is bot-blocked. A human should spot-check it in a browser.
5. **Med: non-off-road photos.** The 250 (all 3) and 300 (2 of 3) photos break the off-road rule. Off-road replacements need to be sourced.
