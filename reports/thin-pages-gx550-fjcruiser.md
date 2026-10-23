# Thin pages: Lexus GX 550 and Toyota FJ Cruiser

Files edited (and nothing else):
- `data/pages/lexus/gx550.json`, `data/extra/lexus/gx550.json`
- `data/pages/land-cruiser/fj-cruiser.json` (detail file `data/extra/land-cruiser/fj-cruiser.json` not changed)

## Counts, before → after

| | GX 550 | FJ Cruiser |
|---|---|---|
| Repairs | 2 → 8 | 6 → 8 |
| FAQs | 10 → 11 | 11 (unchanged) |
| `baseline_service` items | 11 → 13 | 14 (unchanged) |
| `[CONFIRM IN MANUAL]` specs | 6 → 0 | 1 (unchanged) |
| Sources | 14 → 25 | 28 → 31 |

## GX 550: what was added

### New repairs
1. **Oil and filter change on the V35A-FTS.** Covers 0W-20 ILSAC GF-6A, 7.7 qt with the filter, and the dipstick and reminder-reset steps, from the owner's manual. The 30 ft-lb drain-plug torque is from AMSOIL. The 10k/12-month interval, or 5k/6-month under severe use, is from the Lexus schedule. Skid-plate access and the tight factory filter come from the IH8MUD oil-change thread. LX 600 filter 90915-10010 is attributed to an LX 600 owner, since the LX 600 has the same engine.
2. **Cabin filter, engine air filters and wiper blades.** The cabin procedure is from the owner's manual. The 30k replacement interval is from the schedule. K&N's fitment page lists two engine air filters.
3. **Front brake squeal and pad checks.** Covers TSB L-SB-0036-24 (ClubLexus TSB list) and owner outcomes from LandCruiserForum. The 1 mm pad wear limit, DOT 3/DOT 4 fluid and 97 ft-lb wheel nuts come from the manual. The 5k pad inspection is from the schedule.
4. **Tire rotation, wheel swaps and TPMS registration.** The procedures are from the manual: wheel-position registration, new-ID registration, the two stored wheel sets, 'Set current air pressure' and the 34.7 ft-lb spare bracket. The 5k rotation is from the schedule.
5. **12V battery: test, jump-start or replace.** The LN4 case, 80 Ah and 689 CCA spec, the jump procedure, the battery indicator and the re-initialization list are from the manual. The smart-key CR2032 is from the manual, and its 30k replacement is from the schedule. The note that there's no room under the hood for a second battery is from IH8MUD's dual-batteries thread.
6. **Clear the camera, cluster and label recalls.** NHTSA 25V-744, 26V-341 and 26V-179, with their remedies and Lexus campaign codes, come from the NHTSA recalls API.

### Specs filled from the GX 550 owner's manual (OM6A563U)
- Oil: 7.7 qt with filter, 7.4 qt without.
- Spark plugs: DENSO EC22HPR-D7, gapped at 0.028 in.
- Coolant: 13.8 qt, or 16.1 qt with rear A/C. The intercooler takes 3.9 qt.
- Automatic transmission: ATF WS, 11.73 qt reference fill. AMSOIL gives 5.4 qt as the initial fill.
- Transfer case: Transfer Gear Oil LF, SAE 75W, 1.88 qt.
- Differentials: LT 75W-85 GL-5. Front 1.23 qt; rear 7.22 qt, or 6.87 qt with the locker.
- Brake fluid: DOT 3 or DOT 4.

### Other GX changes
- New baseline items: 12V battery, and tires & rotation.
- New FAQ: oil type and capacity.
- Detail file: added `recalls.tsbs` (L-SB-0036-24), the owner's manual under `docs`, and 3 sources.

### New GX sources
- Lexus GX 550 Owner's Manual: https://assets.sipb.toyota.com/publications/en/om-s/OM6A563U/pdf/OM6A563U.pdf
- 2025 and 2026 GX 550 Warranty & Services Guides, under `assets.sia.toyota.com/.../L-MMS-25GX550` and `L-MMS-26GX550`. Both still give 10k/12-month oil.
- AMSOIL 2024 GX550 lookup
- NHTSA recallsByVehicle for 2024 and 2025 (`model=GX`)
- ClubLexus 2024 GX TSB list
- LandCruiserForum "Brakes squeal" p.13
- IH8MUD oil-change thread and dual-batteries thread
- K&N GX550 air filter fitment

## FJ Cruiser: what was added
1. **Check, and live with or fix, cracked inner fender walls.** Sources:
   - NHTSA complaints: 72 complaints across 2007–2014 mention fender bulges, cracks or tears.
   - IH8MUD "Body rips update": the Toyota warranty fix used redesigned aprons with welded brackets and required pulling the dash and front end, and there's a welding-fire warning.
   - The existing "Fender bulge" thread: crack growth reports.
2. **Repair a chip before the windshield cracks.** Sources:
   - NHTSA complaints: 62 across 2007–2014 describe cracked windshields.
   - IH8MUD "Windshield dilemma": the $50 chip repair, $1,600–1,800 replacement quotes, the top molding at about $278, and PPG FW02652.

Every FJ repair has `parts`. FAQs (11) and baseline (14 items) were already at target.

## Not done, or still unverified
- **NHTSA query:** `model=GX%20550` returns 0 results for 2024–2026. The model name in NHTSA's database is `GX`, so I used that.
- **GX dealer-only recalls:** the two recall-check repairs (25V-767 and the camera/cluster/label recalls) still have empty `parts`. They're dealer-only, so I didn't add parts just to fill the field.
- **Which manual:** the GX owner's manual found online, OM6A563U, was printed in April 2026, so it's probably the 2027 model year. The powertrain hasn't changed since 2024, but 2024 owners should check capacities against their own glovebox manual.
- **GX oil filter part number:** not confirmed for the GX itself. 90915-10010 is attributed to an LX 600 owner, and the text says to confirm by VIN. Skid-plate access and the filter tightness come from LC250 owners, which the text says.
- **GX engine air filter count:** "two filters" rests only on K&N's fitment page. I didn't find a GX-specific DIY procedure.
- **L-SB-0036-24:** I didn't see the bulletin text itself, only its title and summary on ClubLexus and owner reports. Parts numbers and labor time are unknown.
- **GX wiper blade sizes:** not sourced, so the page links only to the RockAuto catalog.
- **FJ fender-apron TSB:** the bulletin number wasn't found, and there's no OEM apron part number. I couldn't confirm a Toyota parts-dealer search URL for it (toyotapartsdeal returned 404; parts.toyota.com timed out).
- **FJ PPG FW02652 and $278 molding:** both come from a 2008-era IH8MUD post and are attributed as such.
- **FJ candidates not added**, because I couldn't source them well enough:
  - Rear differential breather extension: I found no FJ-specific source; 4Runner forum pages were bot-blocked.
  - 1GR-FE timing chain noise: no source found.
  - A-TRAC/locker: only one thin thread, on the "rolling and turning to engage" behavior.
  - 2010 rear door-check issues: nothing found.
  - Headliner leaks: nothing found.
  - Early-2007 rear differential whine: two dozen NHTSA complaints exist, but there's no repair procedure source.
- **FJ transfer case gear-oil grade:** still `[CONFIRM IN MANUAL]`. This was existing and wasn't in scope.
- **Bot-blocked links:** some parts and source URLs return 403 to bots (K&N, nhtsa.gov recall pages, AMSOIL). They're the suppliers' real URL patterns and were checked through WebFetch where possible.
