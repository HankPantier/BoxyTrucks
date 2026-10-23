# Fact-check report: group `g-class-a`

Models: **G 500** (flagship page + `family` object in `data/g-class.json`, plus `data/extra/g-class/g500.json`), **W460**, **W461**, **W463** and **500 GE** (`data/pages/g-class/<slug>.json` + `data/extra/g-class/<slug>.json`).

## Method
- Checked every URL in the 10 files: 311 unique URLs, curled with the BoxyTrucksBot UA. All FCP Euro, Expedition Imports, Eurowise and GwagenParts product links return 200 on their real product URL. Fake slugs on FCP and EI return 404, so a 200 means the page is real. Page titles and part numbers matched; FCP "Fits these cars" lists were checked for G500 fitment on 18 part pages.
- Some sites block bots: MBWorld, Hagerty, NHTSA recall pages, Toolsource, AMSOIL, Motor1, WhichCar and B2B Connect return 403, au7o returns 429, and Expedition Portal and Club G-Wagen show bot walls. These are real URL formats. Where a claim depended on one of them, I read it with WebFetch.
- Primary references used:
  - Wikipedia G-Class article, including its raw wikitext engine tables
  - Mercedes-Benz "Milestones of development" (ggb.mercedes-benz.com)
  - Mercedes' own 500 GE 30th-anniversary story
  - Mercedes-Benz USA 2015 G-Class operator's manual (PDF, parsed)
  - NHTSA recalls API and the vPIC VIN decoder
  - Hagerty, Autocar, Classic & Sports Car, Auto Bild and Handsome Motors
  - RM Sotheby's lot pages, AMSOIL and Toolsource
  - 4X4 Australia, WhichCar and Expedition Motor Company
  - Owner threads on Expedition Portal, MBWorld, IH8MUD and 500eboard
- Opened all 14 photos in scope (resized copies) and compared each with its caption and alt text.
- Cross-links: every `[[family/slug|…]]` and every `related` entry resolves to a real generation, with 0 bad links.
- Social: all YouTube channels and the G-luxe Travel video IDs were confirmed through YouTube titles and oEmbed. Instagram accounts were confirmed through links on the owners' own sites: @nothingbutgs, @expeditionmotorcompany, @eurowise_performance, @gluxetravel_g500 (on the G-luxe YouTube about page) and @jackwagonoverlanding. @gzilla500, @Gluxetravel, @Littlehandegan and @Nothing-but-Gs are owner-supplied (resources_manual.json) and were kept. No social entries were removed.

---

## G 500 (flagship page + family object + extra)

**Corrections made**
- **Seven-speed automatic.** The story and the FAQ implied the 7-speed arrived with the 2009 G 550. Wikipedia says US G 500s moved from the 722.6 five-speed to the 722.9 seven-speed during 2007, and the extra file's own timeline already said so. Story, FAQ and generations-table note now say this.
- **Garage FAQ.** It gave unsourced, implausible heights (1.84 m for 2002–03 and 1.98 m for 2004–08). Replaced with KBB's 2002 length of 185.6 in and 112 in wheelbase, plus the 2015 MB-USA manual height of 76.8 in (1,951 mm). The answer also notes that the manual says the roof isn't rated for loads.
- **Harmonic balancer repair.** Removed the unverified MB counter-hold tool number "112 589 00 40 00" and the "torque-to-yield" claim. The torque (200 Nm + 90°) and the bolt 112 031 00 71 (M16×1.5) are now sourced to MercedesMedic's M112/M113 DIY, with a "confirm in WIS" note. The tool is now "e.g. CTA 7270", which is the FCP-linked part.
- **Coolant capacity.** "≈12.7 L" was wrong because AMSOIL gives **12.7 US quarts**. Changed to "≈12.7 US qt (≈12 L) per AMSOIL [CONFIRM IN MANUAL]".
- **Diff and ATF capacities.** Attributed to AMSOIL (front 3 pt, rear 3.8 pt, ATF 9 qt), and the diffs now carry [CONFIRM IN MANUAL]. Added to the ATF item: 2007–08 US trucks have the 722.9, so its fluid and procedure differ.
- **Europa callout.** The W210 wheel and cluster, the lack of radio controls and the absence of a tip-shift gate are verified (GCFSB 2000 G500 Europa post). "Prices track 2002-on trucks" was unsupported and was replaced with the GCFSB-quoted seller view on 2002–05 MB-USA electrics.
- **GEOMETRY engineering cell.** Hagerty's 36°/31° is now labelled as Hagerty's generic G figure, and the 2015 G 550 manual's 34°/29° was added.
- **Part names.**
  - "Febi drag link / tie-rod end" is actually an **outer tie-rod end** (Febi 12975, OE 002 460 16 48) and was renamed.
  - The Hengst air filter name now notes that 273 094 04 04 supersedes 112 094 06 04, which is the number in the URL.
- **Steering damper.** Removed the unverified "Bilstein B6" suggestion.
- **Photos.**
  - `g500-2003-us-spec.jpg` shows **Dutch plates on a brick street**, not a US-spec truck on a gravel verge. Alt text and caption were corrected; the filename is still misleading.
  - The Grand Edition alt text now says the identification comes from Wikimedia Commons.
- **Family object.**
  - 500 GE summary: "sold quietly to existing Mercedes customers" was unsupported. Replaced with the sourced fact (446 built, no front locker), and years changed from 1993 to 1993–1994 (Mercedes: built over about two years; RM: 1993–1994).
  - W461 years changed from "1992 on" to 1992–2022.
  - BenzWorld URL updated to the redirect target `/forums/g-class.36/`.
- **Extra file (g500).**
  - VIN wording: vPIC decodes WDCYR49E… as "G-Class, 5.0 L, Graz". It does not literally say "G 500".
  - The dead museumspass.com event link (404) was replaced with MB Passion's article on "Unimog trifft G-Klasse 2.0", and its note was corrected: "recovery courses" was not confirmed, and demonstrations and rides in Ötigheim were.

**Verified as written (selection):**
- History and context:
  - Shah, 20,000-unit pre-order and shareholder status (Hagerty).
  - Wooden studies in 1973.
  - Pope in 1980; Ickx/Brasseur 1983 Dakar win.
  - Europa: DOT pressure on Mercedes, $135k prices, SVM status, exclusive G 500 importer (Hagerty, Wikipedia).
  - US launch for MY2002 with the G 500 and G 55.
  - G 500 Classic: 500 built, 12 cabriolets. Grand Edition: 500 units.
  - 2008 three-bar grille.
- Specs and capability:
  - 292 hp / 456 Nm (KBB, Autopadre's 336 lb-ft).
  - KBB 2002 figures: 7,000 lb tow, 1,411 lb payload, 25.4 gal, 8.3 in clearance, 5,423 lb, 43.5 ft turning, 11/13/12 mpg.
  - Lug torque 130 Nm (2015 manual).
- Recalls: 10V366000 and 08V303000 (NHTSA API).
- Owner and shop sources:
  - Expedition Portal tire thread: 275/70R18 and 285/65R18 with a slight rub at full left lock; ET63 vs ET43; recoding with STAR.
  - MBWorld 2005 G 500 locker thread: centre lock vacuum, front and rear hydraulic; reservoir in the front-left wheel well; valve block on the firewall; split Y connector.
  - Toolsource: MB 229.5, 74 mm/14-flute cap wrench, MB 236.14, 40–60k ATF practice, transfer-case ATF note.
  - 500eboard: 14 mm hex plugs, 60 Nm, 60k-mile transfer-case interval.
  - au7o cost ranges: axle seals $600–1,500, damper $300–800, rust $400–8,000.
  - Mercedes-Benz Classic data card: €130, 1986–2010, AMG excluded (Driven Car Guide).

**Removed or softened:** the MB tool number, "torque-to-yield", Bilstein B6, the Europa price-parity claim, and the "sold quietly" line.

**Added:** sources for MercedesMedic, KBB 2002, the 2015 MB-USA manual and the GCFSB 1998 G320 post.

**Still unverified / shortcomings**
- **High:** the diff oil spec "MB 235.0, 85W-90" and the 2002–08 transfer-case fluid (ATF vs GL-4) are owner and secondary-source figures, both marked [CONFIRM IN MANUAL]. Whether 2002–08 axle locks still use brake-fluid hydraulics is described from one MBWorld owner and Expedition Imports listings (EI says the "rear locker hose" is W463 **up to July 2001**). This needs a WIS check.
- **Med:**
  - The harmonic balancer's "$250–450 labor" comes from Go-Parts, which blocks bots (403), so it is unverified.
  - The P265/60R18 tire size depends on Autopadre and TireWheelGuide.
  - Autopadre lists 2007–08 G 500s as "5-speed", which contradicts Wikipedia's 722.9 statement. A human should confirm the 2007 changeover by VIN or EPC.
- **Med:** the only photos are three street shots, with no off-road shot of a 2002–08 G 500 (hero_note admits this). `g500-2003-us-spec.jpg` should be renamed.
- **Low:** Front Runner links redirect to dometic.com (Front Runner is now a Dometic brand). The AutoTempest searches have no model filter beyond "gclass".

---

## W460

**Corrections made**
- Removed "Erich Ledwinka led the design" and the DESIGNER plate row. I couldn't verify it: it isn't in Wikipedia's G-Class article, the German article, Hagerty or Mercedes' milestones, and Wikipedia's Ledwinka page was rate-limited.
- "In 1986 Porsche ran Gs as Dakar support trucks, and one … finished second overall" had conflicting sources: Motor1 says it finished second at the Pharaohs Rally, while WhichCar says it was only a support vehicle. Softened to "Porsche built a G with a 928 V8 as a support vehicle for its 959 rally programme in the mid-1980s", with both sources added.
- Otto callout: "215 countries and territories" changed to **179 countries** (Wikipedia). The 560,000 mi / 900,000 km figure, 26 years, 1988 truck, first Westerner to drive in North Korea and Mercedes Museum are all verified.
- Generations table: 230 G changed from 91 PS to **90 PS** (66 kW), and 250 GD from "≈84–92 PS" to **84 PS** (62 kW). Both from Wikipedia's wikitext table.
- Extra capability: 280 GE changed from 158 PS to **156 PS** (115 kW).
- Water-leak buying check now cites C&SC's actual list (wiper spindles, sunroof, heater plenum).
- The data-card claim now notes that the Mercedes-Benz Classic service covers cars from 1986 only.
- IH8MUD quote: the owner's truck had been swapped to an OM617 **turbodiesel**, so it isn't a stock engine. Buying check and FAQ fixed.
- Tire FAQ: the Expedition Portal post doesn't say "no lift", and the "NA diesel struggles with bigger tires" reasoning wasn't in the source. Rewritten to match the post.
- Updated the PCARMARKET URL to /results/ and the C&SC URL to its canonical form. Fixed the dead museumspass link in the extra file.

**Verified:**
- Mercedes milestones: 1972 cooperation, 1980 BGS and riot police, 1982 230 GE and Swiss tender, 1983 Dakar, 1985 two locks standard.
- Wikipedia: Toulon launch, September 1979, five bodies; 1981 and 1982 options; 50,000 by 1986; no turbodiesel W460; 1988 grey-import law; Puch markets.
- Peugeot P4 order of 15,000 cut to 13,500.
- C&SC rust, overheating and price guide.
- Auto Bild picks (230 GE / 300 GD) and rust spots; dealer parts at high prices, plentiful used parts.
- Wikipedia engine table: 300 GD 88 PS, 27 s, 127 km/h, 11.7–18.8 L/100 km; 280 GE 14 s and 165 km/h; 240 GD 32 s.
- PCARMARKET 1986 300 GD sold for $13,000 on 17 Jan 2022.
- Expedition Imports part numbers and prices: axle kit $610, master kit $142, slave kit $142.70, seal $12.50, outer flange seal $44.60, VG 080, LS2.

**Still unverified / shortcomings**
- **High:** locker hydraulic fluid type and every capacity are [CONFIRM IN MANUAL]. This is correct as marked, but the page has no sourced fluid specs at all.
- **Med:** the hero photo and two gallery photos are W460 250 GD and 300 GD trucks. Two of them are on a paved pass (Timmelsjoch) or a roadside pull-off rather than off-road. They are correctly labelled.
- **Low:** "Otto was a 300 GD" rests on common reporting; Wikipedia only says "1988 G-Wagen". "Original tire 205 R16" relies on TireWheelGuide and Longstone.

---

## W461

**Corrections made**
- "In 1992 the Bundeswehr took delivery of 12,500 Wolf" is now attributed: Mercedes' timeline lists 12,500 under 1992, while Wikipedia says deliveries ran from 1993 and totalled more than 12,000. Changed in the story, the extra timeline and production.
- The buying check "Autocar calls the W461 a safer bet than the W460" is **not in the Autocar guide**, so I removed it. It was replaced with Handsome Motors' and Autocar's actual rust checklists.
- The cardan-shaft recall is attributed to Autocar's report (it is a UK-reported recall, not in the NHTSA data).
- Fixed the dead museumspass link in the extra file.

**Verified:**
- 4X4 Australia figures: 135 kW / 400 Nm, detuned for poor fuel, air-pump bulge, 41.0:1 crawl, 38/35/22°, 245 mm, 2,410 kg kerb, 4,490 kg GVM, about 2,080 kg payload, 2,210 kg towing, 6,700 kg GCM, 97 L, $119,900, centre unlockable in low range.
- WhichCar: $109,900, 96 L, 50:50 split, twin 12 V batteries, dirty-filter warning, locks selectable on the move.
- Expedition Motor Company's Wolf definition.
- Wikipedia: Canada's 1,159; USMC 157 IFAVs based on the 290 GDT; Australia replacing Perentie Land Rovers; 6×6; EDITION.30 PUR; Professional; W464 announced on 1 October 2021; Canning Stock Route story.
- Wikipedia W461 engine table: 290 GD 95 PS and 25–27 s; 290 GDT about 120 PS; G 270 CDI 156 PS; G 280/300 CDI 135 kW.
- Mercedes milestones: 1998 290 GD Turbodiesel (120 hp, automatic only); 2006 Greenliner; 2010 6×6 tender.

**Still unverified / shortcomings**
- **High:** no sourced fluid specs or capacities for any W461 engine; all are [CONFIRM IN MANUAL].
- **Med:** the "Cardan shaft recall check" repair has no parts by nature. The page meets the 6-repair minimum but only barely.
- **Med:** photos.
  - `w461-swiss-army-grass.jpg` shows a non-Swiss-looking plate. It is probably an ex-army truck now in civilian hands.
  - The Swiss forest photo is on a paved road (its alt says "forest track", which I left).
  - The Dutch Army photo is on a concrete apron.
  - The Afghanistan MP wagon is an LWB "Wolf" in Bundeswehr usage, which doesn't match EMC's "a Wolf is a 2-door cabrio" definition. The FAQ already explains the naming ambiguity.

---

## W463

**Corrections made**
- Tire FAQ claimed "offset ET63 wheels help". The Expedition Portal sources conflict: one owner had rubbing on ET63 wheels that went away on ET43 G 550 wheels, and another says ET63 tucks the rear tires for 35s. Rewritten to present both. Also added the 315/75R16 report (verified, Expedition Portal post 1868107) and the 285/65 rub.
- Generations table: G 500/G 550 output changed from "387 → 421 PS" to **388 → 422 PS** (285 kW / 310 kW).
- Headliner buying check: the "2003-on fabric headliner" claim comes from **Handsome Motors**, not Autocar, and was re-attributed. Autocar's point is only that sagging can mean water.
- Plate approach/departure now reads "36°/31° (Hagerty); 34°/29° (2015 G 550)". It previously disagreed with the extra file's manual figure.
- Bridge photo alt text: it is a steel footbridge with a timber deck.
- BenzWorld URL updated.
- Extra recalls: added the missing **NHTSA 22V168000** (2014 G 550 software configuration), found through the API.
- Extra production: the C&SC "c. 400,000 built 1979–2018" figure conflicts with the 400,000th G being built in December 2020 (Wikipedia). The caveat is now noted.
- Fixed the dead museumspass link in the extra file.

**Verified:**
- Handsome Motors: more than 200 Gs owned, about 100 hours of labour, reliability pecking order, 2002–04 gremlins improving by 05–06, M273 starters, cam magnets and swirl flaps, M176 oil separator ($3–5k RMS labour), 3–5k oil changes, 40–50k 7G fluid, flush hydraulics first.
- Autocar: 1991 quote, £1,500 propshaft, £120 per corner for springs, G 320 CDI best all-rounder, AMG look-alikes, rust in inner arches and around the rear bumper.
- Hagerty: 36/31°, 80% grade, 30° side slope.
- AWDwiki: 2.16:1 low range.
- Wikipedia: 1990 launch, 1994 changes, 1996 five-speed, Europa from 1993, 6×6 just over 100, Landaulet 99, 22 colours, USMC/Zetsche saga, first formal crash test, Detroit 2018.
- 2015 manual: 7,000/1,653 lb towing, 96 L / 14 L reserve, 205 and 196 mm clearance, 24 in fording, roof not rated, 44.6 ft turning radius, GVWR 3,200 kg, 34/29° and 27/27°.
- All nine original NHTSA recall entries match the API by model and year.
- G-luxe Travel video titles match their repair descriptions.

**Still unverified / shortcomings**
- **High:** the W463 locker architecture (vacuum to centre and switchover valves, hydraulic slaves on the axles) is sourced to one MBWorld owner plus Expedition Imports parts listings, and EI says the rear locker hose fits W463s "up to July 2001". The architecture may differ on 2002+ and 2013+ trucks. A WIS check is needed before owners bleed lines with DOT 4.
- **Med:** only 2 photos, and neither is truly off-road (a footbridge, and a trailer parked on grass pavers). The "Drive it at 55–70 mph" check (722.6 conductor plate / P0715) has no specific source.
- **Low:** generations-table PS figures for the six-cylinder rows are rounded. "Hagerty says the 1996–99 diesel G was the last field-serviceable" is verified.

---

## 500 GE

**Corrections made**
- Verdict and lead: "all in purple-ish blue" and "one colour" changed to "nearly all" and "one standard colour", because RM Sotheby's sold a special-request Avantgarde Verde car.
- Removed the unsourced **2,370 kg** weight (it isn't in Mercedes' article).
- "The body and chassis work was done with AMG" is now attributed to Wikipedia. Mercedes' own anniversary article does not link AMG to the standard 500 GE, and the page says so.
- AMG 6.0: "bored and stroked to 5,959 cc" was unverified, because Wikipedia says "bored" and RM doesn't say. Changed to "enlarged to 5,959 cc and 220 kW (about 300 PS), according to Mercedes".
- Puch callout: "Puch name until late 1999" changed to **until 2000** (Wikipedia EN and DE).
- Extra timeline: "Puch-badged 500 GEs sold in Austria" changed to "built for the Austrian market". RM describes the car as a homologation, test and press vehicle.
- Tie-rod part renamed (same Febi 12975 fix as the G 500), BenzWorld URL updated, and the dead museumspass link fixed.

**Verified (Mercedes' 500 GE article via WebFetch):**
- Production and specs: 446 of a planned 500, built over about two years; M117 4,973 cc, 177 kW (240 PS), 375 Nm; 11.4 s; 180 km/h.
- Chassis: front lock deleted, slightly shallower fording, comfort-tuned suspension; Bridgestone 265/70 R16 H, the only off-road tyre approved to 210 km/h; LWB 2,850 mm only.
- Equipment: the listed standard equipment and interior; paint on the bumpers, flares and mirrors.
- Prices: DM 178,250 vs a G 320 at DM 88,500 and a 500 SE at DM 129,030. Wikipedia says "300 GE", but Mercedes is the primary source and says G 320, so it was kept.
- H-plate eligibility.

**Verified (RM Sotheby's and GCFSB):**
- RM Sotheby's:
  - AMG 6.0 sold for $218,500; about 13 officially converted; option code ZB6.
  - Prince Sultan car: Avantgarde Verde, wider track and wings, 4.97 L, $148,500.
  - Puch car: VAG463228…, DB3338 Amethystblau, three built, used for homologation, testing and press drives; €60–90k estimate, unsold.
- GCFSB: Wallace test labs in 2005, California-registered, four-speed automatic, fuel pumps and accumulators replaced; a $20–35k range for comparable early US G 500s (that car sold for $25,000).

**Still unverified / shortcomings**
- **High:** all fluid specs are period or owner figures marked [CONFIRM IN MANUAL]. That is correct as marked, but there is no factory data. Repairs reuse 2002+ W463 FCP part numbers; they are labelled "confirm fit by VIN", but some (front axle seal, wheel bearing, damper) may not fit a 1993 truck.
- **Med:** both photos are indoor show displays at Techno-Classica (hero_note admits this). No off-road photo exists.
- **Low:** "four-speed automatic" rests on one documented car. The Motor1 source title says $143,000 while RM's result is $148,500; the page uses RM's figure.

---

## Top 5 remaining problems (group g-class-a)
1. **High: W463 and G 500 locker hydraulics.** The pages tell owners to "bleed the hydraulic locker lines" with brake fluid, based on one MBWorld owner and EI parts that are listed for W463s "up to July 2001". A WIS check is needed on whether 2002–2018 trucks still use DOT-fluid hydraulic slaves.
2. **High: G 500 and W463 fluid specs.** The diff oil (MB 235.0 85W-90) and the 2002–08 transfer-case fluid (ATF vs GL-4) come from owners and secondary sources. They are marked [CONFIRM IN MANUAL] but still drive the parts links (Fuchs ATF, Liqui Moly 75W-90).
3. **High: W460, W461 and 500 GE have no sourced fluid capacities or specs at all.** Every item is [CONFIRM IN MANUAL]. These need a period owner's manual or WIS extract.
4. **Med: 2007 gearbox changeover.** Wikipedia says US G 500s switched to the 722.9 seven-speed during 2007, while Autopadre lists 2007–08 as five-speed. This affects which ATF and service kit an owner buys. Verify by VIN or EPC.
5. **Med: photos.** No off-road photo exists for the G 500 (3 street shots), W463 (bridge and parking area) or 500 GE (indoor show). `g500-2003-us-spec.jpg` is a Dutch-registered truck and should be renamed.
