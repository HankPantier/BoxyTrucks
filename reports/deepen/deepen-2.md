# Deepen group `deepen-2`

**Flagship check:** `data/4runner.json` → `page.slug` is `3rd-gen`. The 1st gen is not the flagship; it lives at `data/pages/4runner/1st-gen.json`. The 3rd gen was edited in `data/4runner.json`.

## Counts (before → after)

| Page | Repairs | FAQs | Buying checks | Service items | `[CONFIRM` markers (page + extra) |
|---|---|---|---|---|---|
| 4runner/1st-gen | 6 → 8 | 11 → 11 | 8 → 8 | 13 → 13 | 6 + 0 → 6 + 0 (5 of 6 now partly filled, see below) |
| 4runner/2nd-gen | 6 → 8 | 11 → 11 | 8 → 8 | 14 → 14 | 7 + 0 → 6 + 0 (4 more partly filled) |
| 4runner/3rd-gen (flagship) | 6 → 8 | 11 → 11 | 8 → 8 | 14 → 14 | 1 + 1 → 0 + 0 |
| jeep/grand-cherokee-zj | 6 → 8 | 11 → 11 | 8 → 8 | 13 → 13 | 2 + 1 → 2 + 1 (oil now shows both conflicting values) |

FAQs, buying checks and service items were already within the target ranges, so I added nothing there. Every new repair has symptoms, a fix, tools, difficulty, time, cost and `parts`, and all parts URLs were checked (HTTP 200).

## New repairs and their sources
- **1st gen: swap failing auto hubs for manual hubs.** Sources: 4Runners.com hub ID thread, and LC Engineering's conversion kit, Aisin hub and gasket product pages (prices and the Toyota gasket number 43531-60010 come from LCE).
- **1st gen: power tailgate window.** Sources: the IH8MUD weak-point note already on the page, and Toyota-4Runner.org thread 38646.
- **2nd gen: power tailgate window.** Sources: Toyota-4Runner.org thread 38646 (a 1994 SR5).
- **2nd gen: 4WD won't engage (ADD vacuum system).** Sources: 4Runners.com (how ADD works, lockout and delete), IH8MUD "92 truck 4x4 issue" (vacuum lines at the diff, vacuum valves on the inner fender), and LCE (no conversion kit needed on ADD trucks).
- **3rd gen: 4WD won't engage (ADD vacuum, VSVs, actuators).** Sources: Toyota-4Runner.org VSV troubleshooting (182929) and actuator-rebuild thread (part 36410-35040 is from that thread), and Expedition Portal (1998 SR5, relay location).
- **3rd gen: rear hatch window drops or won't rise.** Source: Toyota-4Runner.org 3136109 (burned relay and limit-switch wiring; limit switch 84290-35020 is from that thread).
- **ZJ: stalling, crankshaft position sensor.** Source: NHTSA complaints filtered to Grand Cherokee only, about 28 crank-sensor stall reports (ODI 878399, 10460757, and motor-mount chafing in 784679). Part: Crown 56026921 at Quadratec.
- **ZJ: fuel pump failure and a flaking tank.** Source: NHTSA complaints, clustered on 1995–96 (ODI 756730, 8001105, 758045; the $600 + $300 cost is from 761423).

## Specs confirmed or added (with sources)
**3rd gen**, from Toyota-hosted owner's manuals (1999 OM35749U, 2001 OM35768U, 2002 OM35787U on assets.sia.toyota.com; these are manufacturer-hosted, so linking them is allowed):
- Oil: SAE 5W-30 preferred, API SJ/SL or ILSAC, 5.2 L with filter. This replaces the viscosity marker.
- Wheel-nut torque: 110 N·m / 83 lb-ft. This replaces the extra file's "81 lb-ft per Limitless Tire [CONFIRM]"; Limitless had the N·m right but converted it wrongly.
- Plug: Denso K16TR11 or NGK BKR5EKB-11, 1.1 mm. This corroborates the existing figure.
- **Sources disagree on the front diff:** the manual gives 75W-90 for A.D.D. trucks, while Toyota-Club gives 80W-90. Both are now shown. For the rear diff the manual gives SAE 90 (80W/80W-90 below −18 °C). The FAQ "What are the fluid capacities?" has been rewritten from the manual to match.

**1st and 2nd gen.** AMSOIL application guide (a fluid-maker lookup; one source only):
- 1987 22R-E: oil grades, 4.5 qt with filter, 9 qt coolant, MT GL-4/5 75W-90/80W-90, transfer case 3.4 pt GL-4/5.
- 1992 3VZ-E: oil 10W-30 / 5W-30, 4.8 qt with filter, 4WD coolant 9.5 qt, transfer case 2.3 pt (ADD) or 3.4 pt GL-4/5 and 1.7 pt ATF on A340H, front diff (ADD) 4 pt GL-5 90 / 80W-90.

Spark plugs come from Denso's overseas-market catalogue via the Toyota-Club plug table: 22R-E W16EXR-U and 3VZ-E K16R-U, both 0.8 mm. Every one of these figures is labeled "AMSOIL" or "Denso catalogue" in the spec text.

**ZJ oil:** ExtremeTerrain (4.0 5 qt / 5.2 4 qt / 5.9 6 qt) and AMSOIL 1998 (6 / 5 / 5 qt) disagree. Both are now shown and the marker is kept. The intro and the fluids FAQ were updated to match.

## Still open
- **1st gen:** oil, plugs, coolant capacity and transmission fluid for the 3VZ-E V6; the automatic fluid; diff grades and capacities; plugs for pre-08/87 trucks; brake fluid type.
- **2nd gen:** 22R-E oil and coolant capacities; A340H ATF type and capacity (AMSOIL gives only its own code and an implausible 4.8 qt drain-and-refill, so I didn't use it); transfer case viscosity; rear diff; brake fluid type.
- **ZJ:** oil capacity (conflicting sources); lug torque (only Quadratec's general 75–85 lb-ft range); the repair-tools note "factory manual for torque specs [CONFIRM IN MANUAL]".
- Toyota doesn't appear to host pre-1996 4Runner owner's manuals, and 4x4wire.com was unreachable (proxy 502).
- I found no ZJ-specific blend-door source; the only blend-door sources were for the WJ, so I left it out.
