# Fact-check report: land-cruiser-a

Scope: 80 Series (flagship `data/land-cruiser.json` → `page` and `family`), FJ40, FJ45/FJ55, FJ60 and FJ62. Pages, detail files (`data/extra/land-cruiser/*.json`) and photo files were all checked.

Method:
- Wikipedia (raw wikitext of *Toyota Land Cruiser*, *J40*, *Lexus LX*, *F engine*, *FZ engine*).
- Slee Off-Road's 80 Series Newbie Guide, Hagerty (FJ80, FJ40, FJ55, wagon values), Toyota pressroom (via WebFetch) and Toyota UK Magazine.
- Corsetti Cruisers, Rough Trax 4x4 (via WebFetch), KBB 1997 specs, Truck Encyclopedia, Retro Rides (via WebFetch) and Silodrome.
- IH8MUD threads, including the Toyota-sourced lubricant tables (threads 50281, 50283 and 50284).
- The NHTSA recalls API (`recallsByVehicle` for 1969–1997, plus `campaignNumber`).
- Cruiser Corps product JSON (prices, SKUs, fitment) and CruiserTeq, Metal Tech and Slee page titles.

All 350 unique URLs in the ten files were requested with curl. 327 returned 200. The 403s are bot-walled real pages (Hagerty, NHTSA web, Toyota pressroom, Rough Trax, Retro Rides, JDMBuySell, Tapatalk); Hagerty, Toyota pressroom, Rough Trax and Retro Rides were then read with WebFetch. Three RockAuto timeouts returned 200 on retry. Instagram handles were confirmed through the supplier's own site link or a third-party article, and YouTube handles were resolved to channel IDs. All `[[family/slug|…]]` cross-links and `related` entries resolve to real generations.

---

## 80 Series (flagship page + family object + `extra/80-series.json`)

### Corrections made
- **Family › FJ60 summary** said "The first four-door wagon Land Cruiser for the US". That is wrong: the four-door FJ55 was sold in the US from 1967 (Wikipedia, Hagerty). Rewritten without the claim.
- **Story lead** repeated Hagerty's line that the 80 was "the last [Land Cruiser] with both a straight-six and a solid front axle". That is false globally: the non-US 105 Series had the 1FZ-FE and a solid front axle, and the 70 Series has both. Changed to "the last **US-market** Land Cruiser with…", with a note on Hagerty's overreach.
- **Wheelbase**: "112.2 in, every Land Cruiser has used since" is not true of the 70 or Prado. Now "the big wagons (100/200/300) kept the figure".
- **A343F automatic**: Slee confirms the A343F on most 1995–97 trucks, with some '95s keeping the A442F. The buying check, story and detail file now say A442F for 1993–94 and A343F for most 1995–97 (source: Slee).
- **Semi-float rear**: the engineering note said "1991–most '92". Slee says the full-floater with discs came with ABS from 1993, so non-ABS trucks after 1993 stayed semi-float. Now "1991–92 US trucks, and non-ABS trucks after that: C-clip semi-float with drums". The IH8MUD rear-seal thread confirms the C-clip design and that the bearings run in gear oil (added to the repair).
- **4WD note**: the HF2A/HF2AV and viscous-coupling description was aligned with Slee and Wikipedia (lockable in 4HI, auto-locked in 4LO, viscous coupling on ABS trucks).
- **1995 changes**: added the MAF meter and "voluntary OBD-II, full OBD-II 1996" (Slee).
- **1997 editions**: now the "40th Anniversary Limited Edition (4,744 sold)" and the Collector's Edition (Wikipedia).
- **Timeline 1993**: added larger brakes from October 1992 production, option code K294 and R134a from May 1993 (Wikipedia).
- **Timeline 1995/1997**: the aluminum radiator was listed under 1997. Slee lists it for 1995–97, so it was moved to 1995 together with the in-line catalytic converters.
- **Center-diff FAQ**: rewritten to follow Slee exactly. The switch was omitted from 1993 on full-floater trucks, and unplugging a transfer-case connector gives low-range control.
- **Reliability FAQ**: "Pre-1993 brakes notably weaker" is now tied to Wikipedia's "larger brakes from October 1992".
- **ATF capacity** (High): the FAQ quoted Rough Trax's 6.0 L for a drain-and-fill. The Toyota-sourced IH8MUD table gives 1.9 L for an A343F drain-and-refill. Both figures are now shown and marked `[CONFIRM IN MANUAL]`, in the FAQ and in `baseline_service`.
- **Lug torque**: the detail file had 116 lb-ft for steel wheels from Rough Trax alone. It now gives both sources (IH8MUD birf-repack: 76 alloy and 109 steel; Rough Trax: 103 and 157 N·m) and is marked `[CONFIRM IN MANUAL]`.
- **Starter repair tools**: changed to the spanner sizes actually given in the IH8MUD write-up (10, 12, 14, 17 and 19 mm). The "8 mm contact cover" claim was unsourced.
- **Generations table**: added diesel outputs from Wikipedia's engine table (1HZ 96 kW/271 N·m; 1HD-T 115 kW/357 N·m) and noted that 155 hp is the US 3F-E rating (Toyota quotes 112 kW elsewhere).
- **Plate › Production**: now "1990–1997 (Japan); Venezuela to 2007".
- **ARB Air Locker URL**: redirected, so updated to `https://store.arbusa.com/drivetrain/air-lockers/`.
- **IH8MUD starter thread URL**: updated to the current `/threads/…44393/` format.
- **KBB URL**: updated to the page it redirects to (the spec data is on that page).
- **PHH repair**: removed the Cruiser Corps "water bypass hose FJ62/FJ80 1988–92". It is a 3F-E part, and the PHH is a 1FZ-FE problem.
- **Frame repair part**: the Metal Tech scab plate is now labeled as a generic plate, not an 80-specific one.
- **Photo alt and captions**:
  - The hillside truck is a pre-1995 **diesel** (DIESEL badge on the grille).
  - The Algeria trucks are post-1995 with snorkels.
  - The mud truck is a cab-and-tray conversion. Its caption now names the event (Toperi Challenge), per Commons.

### Removed or softened
- PHH OEM part number "99556-30100, cut-to-fit 16 mm hose" could not be found in the cited thread and was removed. Kept the sourced "owners use Gates heater hose instead of a $45 bypass kit".
- LX 450 "center-console subwoofer" was unsourced and removed. Replaced with Wikipedia's grille, wheels, cladding and extra insulation.
- Locker switch part number "84725-60020" could not be verified and was removed.
- The rust check (footwells and rear windows) is now attributed to buyers' guides. Its source, Flexmotor, returned 503.

### Added
- IH8MUD birf-repack torque values (flange nuts 26 ft-lb, caliper 90 ft-lb) to the knuckle repair.
- Battery-tray corrosion check (Slee).
- Sources: Rhino-Rack article confirming @blackhillsbuilds and its 80 Series; Wikimedia Commons (Toperi); IH8MUD birf-repack (detail file).

### Verified as correct (selected)
- 1FZ-FE 212 hp @ 4,600 / 275 lb-ft @ 3,200; 1FZ-F 188 hp / 268 lb-ft; LX 450 215 hp (Wikipedia).
- KBB 1997 figures: 4,751 lb, 189.8 in, 10.8 in, 5,000 lb, 25.1 gal, 40.4 ft, GVWR 6,470, payload 1,719, 12/14 mpg.
- Hagerty $141,000 / 1,005-mile 1994, "993 of Land Cruisers", nearly triple the $58k #1 value, ~300k-mile trucks above $20k.
- Slee 6,640 lb (3,200 front / 3,480 rear) weigh-in, LSPV 38 mm / 600 mm / 4.8 mm, 4.11 gears with 4.56/4.88/5.29 options, 2" OME with 35s.
- IH8MUD tire answers ("35s fit, but rub like mad"; 285, 295 and 305 fit stock) and tow manual (3,000 normal, 5,000 with package).
- Toyota lubricant table on IH8MUD; Timmy the Toolman part numbers and torques; FA9097 at $125.
- NHTSA: only 93E023000 (Reese hitch) for 1991–93 and none for 1994–97.
- LX 450: production November 1995, US sale January 1996, 9,000+ in 1997, two-month wait list.
- Venezuela build to 2007 (Cumaná); Blue Marlin (500 built).
- Family object: Umehara June 1954; Toyota's US exit announced December 2020 (Autoblog, 24 Dec 2020); BaT and AutoTempest links all 200.

### Still unverified / shortcomings
- **Med**: FZJ80 A343F drain-and-refill quantity (1.9 L vs 6.0 L) is still unresolved. It is marked, but needs a human with the FSM.
- **Med**: Bring a Trailer value statistics (250 sales, $25.5k median, ICON $124,500, HDJ80 $75k) could not be re-pulled; BaT's listings API refused requests. Spot-checked recent sales look consistent.
- **Low**: Flexmotor (source for seat-belt, dash and window wear) was down (503) during the check.
- **Low**: Aus80 Tapatalk forum returns 403 to bots, so it could not be confirmed live.
- **Low**: The family object says the 250 has "center and rear lockers standard". The Drive says yes, but also contradicts itself (limited-slip), and Toyota's pressroom doesn't break it down by grade. This belongs to another group's page but sits in the shared family object.
- **Low**: Only 3 photos, all OK for generation; the hero shows a diesel, which US readers may not realise.

---

## FJ40 (`pages/land-cruiser/fj40.json` + `extra/fj40.json`)

### Corrections made
- **US arrival date**: the story set Hagerty's 1963 against "Toyota's history: 1960" without detail. Toyota's US pressroom actually says the FJ40 came to the US in 1960 (after a single Land Cruiser in 1958). The story, timeline and production row now give both dates with their sources.
- **F engine lineage**: Hagerty's "reverse-engineered Chevrolet 235 Stovebolt" is now flagged as folklore. Wikipedia says the bottom end is loosely based on GMC's 236.
- **H diesel date**: was 1972. Wikipedia's two articles disagree (1972 vs 1973), so it now reads "1972 or 1973 (sources differ)".
- **2F output**: "135 PS / 210 lb-ft" corrected to **135 hp** (Wikipedia: 101 kW, 135 hp). Torque is now "200–210 lb-ft", since Wikipedia says 200 and Corsetti says 210.
- **Power steering**: "optional on F-engine trucks" was misleading, because US 1979 trucks had the 2F. Now "petrol trucks" (Wikipedia: "only F models", meaning petrol).
- **Valve cover gasket cost**: was "about $35"; actual price $17–22 (Cruiser Corps 551-122/124).
- **H55F swap**: added Cruiser Corps' requirement for a split transfer case built 10/1982 or later (5th-gear oiler provision).
- **Recalls** (detail file):
  - 91V110000 now carries NHTSA's actual consequence and remedy text and the 38,500 count.
  - Added **81V117000** (1981 tie rod, 855 vehicles; NHTSA doesn't name the body, Corsetti calls it FJ60).
  - Added **69V027000** (1968–69 wiring, 263 vehicles, no defect text in the NHTSA record).
- **Photos**:
  - Deosai truck: may be a medium-wheelbase 40, so now captioned "40 SERIES". Its square bezels are noted.
  - Wadi Rum truck: a converted safari truck that may be long-wheelbase, now captioned "40 SERIES SAFARI TRUCK".
- **IH8MUD valve-adjustment URL**: updated to the current format.

### Removed or softened
- The baseline valve-lash note attributed periodic valve adjustment to Hagerty's FJ40 article, which doesn't say it. The attribution was removed.

### Added
- Keyster kit link (by carb number), floor pan 605-111L ($195, verified) and urethane bushing kit A216 as repair parts.
- Cruiser Corps H55F source.

### Verified as correct
- Wikipedia J40 timeline: 1974 roll bar, 1975 barn doors, 1976 discs, 1977 vent windows, 1979 bezels, PS/AC and 4.11→3.70.
- About 300 1983 US imports; BJ42 Canada 1984 at about CA$14,000; Bandeirante dates and engines.
- Dimensions and weights (151.2 in; 3,263 / 3,427 lb).
- Hagerty $47,375 / −7.6% / 1968 $49,100 / 1975 $44,800 and the SBC V8 swaps.
- Retro Rides values ($4,400 → $33,000; AU$30–50k) and freewheeling hubs standard from 1982.
- IH8MUD tire threads (31x10.50 "tried and true"; 33x9.50 rubbing, fixed with bump-stop spacers and steering stops).
- Cruiser Corps prices and SKUs: 514-108/109 at $159.95, A151 $699.95, ARB-103 $2,349.70, 520-139 $91, 524-117 $899.47, Keyster $34.99.
- 40/55 lubricant table; OEM wheel 15x5.5, 3.25 in backspace, H78-15.

### Still unverified / shortcomings
- **Med**: Neither photo is a definite FJ40. The Deosai truck may be a 43, and the Wadi Rum truck is a safari conversion. A clean off-road FJ40 photo is needed.
- **Low**: "1980-and-later bodies rust more readily" and "$2–3k 2F rebuild" come from IH8MUD buyer threads I couldn't locate in the pages fetched; attributed as member opinion.
- **Low**: GoAuto (2021 GR Heritage Parts for the 40) returns 200 but wasn't read in full.
- **Low**: BaT value statistics not re-pulled (same API limit as above).

---

## FJ45 / FJ55 (`pages/land-cruiser/fj45-fj55.json` + `extra/fj45-fj55.json`)

### Corrections made
- **Iron Pig origin**: Hagerty actually says the **two-tone paint** made the front look like a pig's snout. The lead, callout and FAQ previously credited the "headlamps set in the grille opening".
- **FJ45 wagon count**: "none known to survive" was unsourced and removed. "About 60 built" is now attributed to Truck Encyclopedia.
- **80 mph**: Toyota UK describes 80 mph cruising as the **design brief**, not a demonstrated ability. Reworded.
- **Body panels**: the FAQ and story said panels "generally don't exist", but Cruiser Corps sells FJ55 outer rockers ($179.50) and lower-fender patch panels with the inner brace ($229.95). Now "complete panels generally don't exist; repair sections do".
- **Gen X share**: "well over half" replaced with Hagerty's exact 58.5 percent.
- **OME kit cost**: was "about $2,700"; Cruiser Corps lists $2,300–2,700 (ARB-120 $2,713.75; ARB-164 $2,314.80).
- **Valve cover cost**: now $17–22.
- **Baseline steering**: "power steering (1979–84)" was copied from the FJ40. Now "where fitted".
- **Recall 69V027000**: the detail file stated a door-scuff-plate harness defect. NHTSA's record has no defect text; it shows 1968–69, 263 vehicles and no body named. Softened, with the earlier description kept as unverified.
- **Photos**:
  - Yemen: the second truck is a 60 Series, not a second FJ55.
  - Broghil: a long-wheelbase 40 **hardtop**, not an "FJ45 wagon", so engine and code are unknown. Captions now read "40 SERIES LWB".

### Removed or softened
- The H diesel date is now "1972 or 1973 (sources differ)".

### Added
- Cruiser Corps FJ55 rocker panel source.
- "Domed hood is the easy tell" in the best-years FAQ (Hagerty).

### Verified as correct
- Hagerty FJ55 guide: first Land Cruiser designed as a wagon; August 1967 to July 1980; Suburban/Wagoneer rivals; tailgate window by dash switch or key; $34,500 / $46,300 / +65.8%; rust list; drums adequate; F/2F valve adjustments; non-synchro first gear; domed hood.
- Wikipedia: 2,700 mm wheelbase, fully boxed frame, FJ56 in Japan, 1975 front discs, Moose.
- Toyota UK: 11 percent of Land Cruiser sales.
- Irish Army: 77 FJ45s in 1977.
- IH8MUD J45 production chart: 412,383 / 39,593 / 9,488; Venezuela to 8/85; body-code dates.
- FJ55 VIN thread: July 1977 frames 76441–77572; the leading zero is a title error.

### Still unverified / shortcomings
- **Med**: The biggest-tire FAQ honestly says there is no FJ55- or FJ45-specific consensus and borrows the FJ40 answer. Needs an owner-sourced figure.
- **Med**: Only 6 repairs, the minimum.
- **Low**: The FJ45 long-wheelbase photos can't be confirmed as FJ (petrol) rather than BJ or HJ.
- **Low**: The Hagerty wagon-values piece is undated (around 2020).

---

## FJ60 (`pages/land-cruiser/fj60.json` + `extra/fj60.json`)

### Corrections made
- **High Altitude Compensation** (story, FAQ, repair): described as "adjusts the mixture". Corsetti, the cited source, says it **advances ignition timing** above 3,930 ft. Corrected.
- **Export engine code**: the 3F export truck was labeled "FJ60 (export) 1984–87". Wikipedia gives it as the **FJ61 (1984–88)**. Corrected in the table and story.
- **BJ60 years**: were 1980–1990; Wikipedia says 1980–1986. Corrected. The HJ60 note now mentions the infobox's 1982 date.
- **Five-speed date**: the story said 1982 and the FAQ said "around 1983". Now consistent: Wikipedia 1982, Toyota UK 1983.
- **US gearbox**: now "H41F/H42F (US-only)" (Wikipedia), not H42 alone. Baseline intro wrongly said "H55F five-speed from 1985" for US trucks; corrected to "never fitted at the factory to US trucks". Manual-transmission capacity is now 3.5 L for the H41, with the H42 marked `[CONFIRM IN MANUAL]`.
- **H42 spacer story**: in April 1985 Toyota added a spacer in place of fifth gear (Off-Road.com). Reworded from "made the H42 the same length".
- **Tire FAQ**:
  - The 33x9.50 example was on a stock **FJ62**, not a stock 60.
  - The 33x12.50 example rubbed at **full stuff on a 2.5" BDS lift**, not at full lock.
  - The "6-inch-wide stock wheel" claim was unsourced and was replaced with the Corsetti and Cruiser Corps rim-width guidance.
- **End of production**: Toyota UK's December 1989 is now paired with Wikipedia's 1990 and Venezuela to 1992.
- **Hagerty valuation**: the $18,500 median covers FJ60s and FJ62s together, the piece is dated about 2020, and "appears to be overtaking" is Hagerty's hedge.
- **Recall summaries**: 91V110000 now uses NHTSA's own consequence and remedy text.
- **Engineering › Brakes** note referred to A/C and the rear heater. Fixed.
- **Social**: @tomahawk.cruiser was dropped; no web reference to it could be found.
- **Photos**: the Ingeegoodbee truck is a **diesel** (badge), so the alt was updated. The White Desert photo is watermarked "Johan Holmdahl 2011" while Commons credits Ysjyd; the credit now shows both.

### Removed or softened
- Flexmotor's "first Land Cruiser sold in trim levels (STD, GX, VX)" is softened to "named trim levels… and, later, VX". Flexmotor was down, so it couldn't be verified.

### Added
- Sources: Corsetti tire-sizes page and Cruiser Corps OEM rim.

### Verified as correct
- Corsetti specs: 135 hp @ 3,600, 210 lb-ft @ 1,800, 65 mph top speed, about 300k-mile life, 184 × 70.9 × 69.5 in, 4,246 lb, 23.8 gal, 3,500 lb towing, 11/18 mpg, compression benchmarks, $300 carb, $200–600 knuckles, $112 damper.
- Off-Road.com H55F article: 3,250 → 2,750 rpm, 0.84 fifth, 32 and 36 mm sockets, $30 flywheel resurface, crossbar plug.
- IH8MUD 60/70 lubricant table; Wikipedia J60 timeline.
- Silodrome HJ61 figures: 3,980 cc, 18.6:1, 7 psi, 134 bhp, 315 lb-ft.
- Cruiser Corps SKUs and prices: 595-102 $119.95, 595-101, 520-127 $229.95, OMESD24 $104.95, ARB-108/111 $2,411.75.

### Still unverified / shortcomings
- **Med**: The HJ60 start year (1980 vs 1982) is inconsistent within Wikipedia itself.
- **Low**: BaT value statistics not re-pulled.

---

## FJ62 (`pages/land-cruiser/fj62.json` + `extra/fj62.json`)

### Corrections made
- **"First automatic in a Japanese 4x4"** was attributed to Wikipedia. It is Toyota UK's claim, and it refers to the 60 Series automatic of **1984**. Re-attributed and re-dated.
- **Push-button electro-pneumatic 4WD (August 1986)**: this comes from Toyota UK and isn't clearly applicable to US FJ62s. Softened in the story and engineering note to "check whatever your truck has engages cleanly". A human should confirm what US FJ62s actually have (see top 5).
- **3F-E "used only in FJ62 and 1991–92 FJ80"**: this holds only for US trucks. Now "in US trucks" (IH8MUD 3FE list text).
- **Tire FAQ**: the "stock 15x6 wheel shops won't mount on" claim was unsourced and was replaced with Corsetti and Cruiser Corps rim-width guidance.
- **Hagerty valuation**: the wording now matches the article ($18,500 for FJ60s and FJ62s, around 2020).
- **Recall summary 91V110000**: now uses NHTSA's text.
- **Social**: @tomahawk.cruiser was dropped (unverifiable). @cruiserpartsllc was kept; it is confirmed from cruiserparts.net.
- **Tremalzo photo**: the caption no longer says "HJ60", since a turbo HJ61 can't be ruled out. Now "60 SERIES DIESEL, LATE-STYLE FRONT".

### Removed or softened
- See above. Nothing else was removed.

### Added
- Sources: Corsetti tire-sizes page and Cruiser Corps OEM rim.

### Verified as correct
- Corsetti: 155 hp @ 4,000, 220 lb-ft @ 3,000, 4,480 lb, 68.9 in height, 12/19 mpg, 3,500 lb towing.
- Wikipedia: FJ62G VX in 1987 and the last carbureted 3F FJ62 from Cumaná in 1992.
- IH8MUD "Opinion on a FJ62": pan-bolt and rear-main advice, "any '88 Cruiser is going to leak some oil", 159k is "nothing", a $986 transfer-case rebuild at 74k, vacuum-leak idle.
- 60/70 lubricant table: A440F 5 L / 15 L, transfer case 2.1 L.
- NHTSA 89V155000 covers 1982–88, so 1988 is the only FJ62 year.
- All CruiserTeq part URLs resolve to the FJ62/3F-E parts named.

### Still unverified / shortcomings
- **Med**: The `fj62-grey.jpg` photo shows a 1990 FJ62 **parked on a city street**, which breaks the site's off-road-only photo rule. It is the only true FJ62 photo; the other shows a diesel 60 with a late-style front. I searched the Commons J60 category for an off-road FJ62 and found none. One candidate there ("Mountain of Ghosts – Algeria") is actually a Nissan Patrol miscategorized as J60. A replacement photo is needed.
- **Med**: Only 6 repairs and 13 baseline items. Within targets but thin.
- **Low**: The FJ62 3F-E oil viscosity is still `[CONFIRM IN MANUAL]`.

---

## Top 5 remaining problems (land-cruiser-a)

1. **FZJ80 automatic fluid capacity (High, owner-facing):** Rough Trax says 6.0 L for a drain-and-fill, while the Toyota-sourced IH8MUD table says 1.9 L for an A343F drain-and-refill. Both are now marked `[CONFIRM IN MANUAL]`. Someone with the FSM, ideally year-specific since the A442F and A343F differ, should settle it.
2. **80 Series steel-wheel lug torque (High):** sources disagree (109 vs 116 lb-ft; IH8MUD vs Rough Trax). Now shown as a range with `[CONFIRM IN MANUAL]`, and needs the owner's manual figure.
3. **FJ62 photo set (Med):** the only real FJ62 photo is street-parked, which breaks the off-road rule, and there is no off-road FJ62 on Commons. The FJ40 photos also can't be confirmed as short-wheelbase FJ40s.
4. **US FJ62 4WD engagement and 60 Series details (Med):** Toyota UK's "push-button electro-pneumatic from Aug 1986" (and its diff-lock lever claim) may not describe US trucks. An FJ62 owner or the FSM should confirm what US FJ62s have, and the HJ60 start year (1980 vs 1982) also needs settling.
5. **Bring a Trailer value statistics across all five detail files (Med):** sample sizes, medians and top sales could not be re-pulled because the listings API refused requests. Recent sales spot-checked are consistent, but the numbers are unverified. The FJ45/FJ55 "biggest tire without a lift" FAQ also still has no model-specific consensus.
