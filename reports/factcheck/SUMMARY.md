# BoxyTrucks fact-check: summary of shortcomings

**Date:** October 22, 2026
**Scope:** 14 groups covering every model page, its detail file and photos, plus the site-wide content (resources, reading, suppliers, builders, stories, home FAQ and legal pages).
**Group reports:** the other files in this folder.

## What was checked and fixed
- **About 4,800 links** were tested. Broken, parked or redirected ones were replaced, including oldmanemu.com (now a parked domain), Rancho, Rough Country, The FJ Company, Club G-Wagen and DiscoWeb.
- **Recall numbers** were checked against NHTSA's API, and missing campaigns were added: L663, W463, 4Runner, FJ40, YJ/TJ, Grenadier, 100/200/250, LJ.
- **Fuel-economy figures** were replaced with EPA ratings where they were wrong: G 55, JL/JK, LJ, GX 460.
- **Every photo was opened.** Mismatched captions and alt texts were fixed, and the duplicate W463/G 55 hero was resolved.
- **Invented or misattributed material was removed:**
  - a fake CarsGuide quote (Patrol Y61)
  - a Car and Driver quote (1st-gen 4Runner) and an Autocar claim (W461) that don't appear in those articles
  - a RealTruck quote (LJ)
  - invented garage heights (G 500)
- **Safety and fitment errors were corrected:**
  - L663 wading depth: 850 mm on coil-sprung trucks, not 900 mm
  - 4Runner fuel-pump recall years
  - JK Unlimited coolant type (HOAT vs OAT)
  - JL coolant capacity (litres and quarts were mixed up)
  - 4th-gen 4Runner rear diff oil: 80W-90, not 75W-90
  - Y61 rear diff oil: 85W-140 LSD
  - LX 570 towing: 7,000 lb on 2016-on trucks
  - TJ towing: 1,000 lb on the 2.4 and some automatics
  - Series brake-shoe fitment
  - L322 transfer-fluid part
  - a Mopar part number that was really a different gear oil
- **Owner-supplied accounts and articles were protected.** When an agent removed @gzilla500, it was restored on four pages. Otto's journey now shows both counts: Mercedes' 215 countries and territories, and Guinness's 180 countries.

## Remaining shortcomings, in priority order

### 1. Factory fluid specs, capacities and torques (HIGH, every family)
This is the biggest gap on the site. Many fluid grades, capacities and torque values come from forums, lubricant-seller lookups, wheel-spec databases or a Gregory's quote rather than a factory manual. Most are now marked **[CONFIRM IN MANUAL]**, but owners will act on these numbers. The highest-risk items, each needing a factory service manual or owner's manual:

| Model | Open question |
|---|---|
| Cherokee XJ | AW4 fluid type, AX-15 gear-oil grade (the wrong oil can damage the gearbox), NP231 fill, coolant capacity |
| Grenadier / Quartermaster | diff oil (80W-90 per owners quoting the manual, 75W-140 per Agile Offroad), transfer case, plug and filter part numbers, BMW-listed transmission-pan kit fitment |
| G 500 / W463 (2002–18) | diff-lock bleeding with brake fluid (one owner's account, with parts listed for trucks up to 2001); diff and transfer-case fluids; whether the 7-speed arrived in 2007 or 2008 |
| W460 / W461 / 500 GE / 4×4² | no sourced fluid specs at all (portal-hub oil for the 4×4²) |
| 5th-gen 4Runner | rear diff capacity (locker vs open), lug torque (76, 83 or 85 ft-lb) |
| JK | 3.8 spark-plug torque (12 lb-ft looks low), lug torque |
| JL Unlimited 4xe / 392 | oil spec |
| 80 Series | A343F fluid capacity (6.0 vs 1.9 L), steel-wheel lug torque |
| 70 Series V8 | capacities come from a table labelled with the wrong engine |
| 200 Series | transfer-case oil spec |
| 300 Series | only US LX 600 specs; no diesel, V6 or hybrid specs |
| LX 570 | capacities from the 2016-on manual; need checking for 2008–15 |
| GX 550 | owner's manual not yet available; 6 specs open, only 2 repairs |
| Range Rover (all) | capacities from forums, TOPIx files behind a login and BolidenForum; P38 lug torque conflict; whether the L322 transfer box changed in 2006 or 2007 |
| Classic Defender | wheel-nut torque (130 vs 170 N·m); 1994–97 swivels (one-shot grease vs EP oil) |
| Grand Wagoneer | capacities from AMSOIL only; no rear-main or head-bolt torques |
| YJ / TJ | no YJ-specific torque source; ExtremeTerrain's own table gives two different TJ plug torques |
| Patrol Y60 / Y61 | no factory capacities; GU bearing preload, TD42 tappets and RD28 belt interval each rest on a single post |
| Scout (all) | no factory fluid specs; needs an IH shop manual |

**Fix:** buy or borrow the factory service manuals (Toyota TIS, Mercedes WIS, Land Rover TOPIx, Mopar/TechAuthority, Helm and Faxon reprints, the INEOS workshop manual) and work through this table.

### 2. Photos that break the off-road rule (MED)
The correct generation is shown, but the setting is a street, show lawn or dealer lot:
- **Lexus:** about two-thirds of the photos, including every GX 470, GX 550 and LX 600 shot
- **G-Class:** G 500, W463 gallery, 500 GE (indoor show), G 550, 4×4², Europa. The Europa hero isn't confirmed as a Europa truck.
- **Grenadier and Quartermaster:** all on Goodwood lawns
- **Land Cruiser:** FJ62 (street), 250 and 300 (display shots); the FJ40 photos may not be short-wheelbase trucks
- **Range Rover:** P38 (ambulance on tarmac), L322 (no trail shot), L460 (one dealer car)
- **Other:** 6th-gen 4Runner, CJ-8 (ranch), Grand Wagoneer (roadside), CJ-5 (all three show the same Brazilian Jeep), Y61 cab-chassis
- **Scout Motors:** no photo exists yet

**Fix:** Show Us Your Rig submissions, or licensed photos from owners and builders.

### 3. Sources that couldn't be re-read (MED)
- **Forums:** IH8MUD, toyota-4runner.org, JK-Forum, wranglertjforum, NissanPatrol.com.au and others block automated access, so some repair details and tire-fitment answers rest on threads that weren't re-checked.
- **Slee Off-Road pages** behind several 100/200/250 claims couldn't be re-read.
- **Bring a Trailer price statistics** in several detail files couldn't be re-run and are labelled as estimates.
- **Instagram:** about 55 of 80 handles are unverified because Instagram blocks lookups. Someone logged in should click through them, starting with the small hobby accounts listed in `site-wide.md`.

### 4. Parts links (MED)
- Range Rover Classic and P38 repairs often link to supplier search pages rather than products.
- Europa parts are listed by FCP for 2002-on trucks only, and the G 320 head-gasket parts aren't listed for that engine.
- GX 470 / LX 470 part numbers that came from forums need checking against Toyota's parts catalog.
- The Morris 4x4 Center site was down (503) during the check. Its links in the Jeep pages are real addresses.

### 5. Sources that disagree (LOW–MED, shown on the pages)
- RD28T and TD42T introduction dates; when the TD42 ended
- HJ60 start year, and whether US FJ62s have push-button 4WD
- LX 470 2006–07 output
- the G 500 7-speed changeover year
- early Bronco 200-six availability in 1975–77
- XLC weight rating (1975 vs 1976)

### 6. Thin pages (LOW–MED)
- **GX 550:** 2 repairs.
- **FJ Cruiser:** 6 repairs.
- **Scout Motors:** empty repair and service sections by design, until the truck exists.
- **No social accounts:** Y61, Grand Wagoneer, XJ, Disco II, CJ-5 and CJ-8 have none. LR3 has one.

### 7. Legal and compliance (flag for a lawyer)
- **Privacy:** a privacy policy now exists (`/about/privacy.html`), covering GA4, FormSubmit, affiliate cookies and hosting. There is still no cookie-consent banner; that isn't generally required in the US but matters for EU and UK visitors.
- **For a lawyer to look at:** the liability exclusion in the disclaimer, the photo-licence wording on the rig form, and where affiliate disclosures sit on pages.

## Suggested next steps
1. Get the factory manuals for the models in section 1, starting with the XJ, Grenadier, G 500/W463, 5th-gen 4Runner and 80 Series.
2. Click through the unverified Instagram handles while logged in.
3. Ask builders and owners for off-road photos of the models in section 2, and push Show Us Your Rig.
4. Have a lawyer review the disclaimer, the privacy policy and the submission terms.
