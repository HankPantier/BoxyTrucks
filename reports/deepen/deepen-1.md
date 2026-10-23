# deepen-1 report

All five pages are DEEPEN. Each went from 6 to 8 repairs, and every new repair has symptoms, a fix, tools, difficulty, time, cost and `parts`. Every new parts and source URL returned HTTP 200 except the Rovers North search links, which return 403 to bots; that is expected behaviour for the supplier's real URL pattern. Nothing links to archive.org or any other user-uploaded manual scan, per the coordinator's rule update.

## Counts (before → after)

| Page | Markers | Repairs | FAQs | Buying checks | Service items |
|---|---|---|---|---|---|
| land-rover/series | 7 → 6 | 6 → 8 | 11 | 8 | 13 |
| land-cruiser/fj45-fj55 | 2 → 2 | 6 → 8 | 10 | 8 | 14 |
| land-cruiser/250-series | 0 → 0 | 6 → 8 | 11 | 8 | 13 |
| land-cruiser/300-series | 5 → 5 (one partly filled) | 6 → 8 | 11 → 12 | 7 → 8 | 13 |
| lexus/lx450 | 4 → 4 | 6 → 8 | 11 | 8 | 14 |

FAQs, buying checks and service items were already within the targets, so they were only topped up where the new material called for it (on the 300).

## New repairs and their sources
- **Series:** Steering relay rebuild and reseal (Rovers North forum threads 13806 and 13150; LR Direct 230294 retainer plate). Diagnosing a gearbox that jumps out of gear (Rovers North threads 11791 and 1194; LR Direct 3649 and 56102 detent springs).
- **FJ45/FJ55:** Clutch master and slave cylinders (Off-Road.com project FJ40 clutch upgrade; Cruiser Corps master for 1970–75, slave for 1974–80, prices $114.79 and $34.95). FJ55 power tailgate window (IH8MUD threads 340347 and 820363). The "Test the tailgate window" buying check now points to the repair.
- **250:** Sunroof leak and damp headliner (LandCruiserForum thread 7444, plus NHTSA complaints for 2025). Vibrating driver's mirror (LandCruiserForum thread 669, plus an NHTSA complaint).
- **300:** Diesel DPF/EGR care and seventh-injector faults, and the exposed diesel fuel filter with the GMF4x4 FG-2014 guard at A$160. Both come from Unsealed 4X4's "LandCruiser 300 problems" (July 2026). Also added:
  - a new FAQ, "Is the V6 diesel reliable?"
  - a new buying check, "Diesel: how was it driven?"
  - the Australian transmission recall (February 2026) appended to the transmission-recall buying check.
- **LX 450:** Parking brake that won't hold (Unsealed 4X4's 80 Series article, already a source on the page; CruiserTeq PB8X10XOEM shoes, the rear-disc hardware kit and PB476138X struts). Driveline clunk and slip-yoke greasing (IH8MUD "Clunk is gone"; ExplorOz).

## Detail file: land-cruiser/300-series
- **`recalls`:** Three Australian recalls added, each sourced to CarExpert: transmission over-rev with fire risk (February 2026, 11,020 vehicles), creep in neutral (February 2024), and VSC not defaulting to on (April 2022). `lookup` stays "none" because the 300 isn't sold in the US.
- **`values`:** New section with Australian 2026 list prices (CarExpert, 15 July 2026).
- **`timeline`:** Two entries added: the February 2024 F33A shipment pause over Toyota Industries' certification irregularities, and the 2026 Australian Performance Hybrid.
- **Not added:** `docs` and `community`. I couldn't find a manufacturer-hosted 300 owner's manual or a 300-specific club to cite.

## Specs confirmed
- **Series engine oil capacity** (marker removed): 2.25 holds about 1.9 US gal (about 7.2 L) including the filter, per Series123's Series 2/2A specification page. One owner's shop manual, quoted on the Rovers North forum, gives 13 pints plus 1.8 for the filter, which he works out as 7.4 US qt. Both figures are shown.
- **Series gearbox and transfer box** (Series II/IIA only): gearbox 2.5 imp pt (3 US pt) and transfer box 4.5 imp pt (about 5.5 US pt). Series123 and the "green bible" workshop manual quoted on Rovers North agree. A `[CONFIRM IN MANUAL]` marker is kept for the Series III.
- **300 oil interval** (partial): Toyota Australia's schedule is every 6 months or 10,000 km, per CarExpert (2026). The marker is kept for the US LX and other markets.

## Still open
- **Series:**
  - oil change interval
  - oil-bath air cleaner oil grade
  - coolant type and capacity
  - differential capacity (only Series123 gives one, at 3.5 US pt; no second source)
  - Series III gearbox capacity
  - brake fluid DOT grade
- **FJ45/FJ55:** Plug gap, points dwell and valve clearances. IH8MUD only confirms the 0.008 in intake go/no-go figure; I found no exhaust figure.
- **300:**
  - air filter interval
  - spark plug interval
  - coolant interval
  - E-KDSS and AHC fluid
  - oil interval outside Australia
- **LX 450:**
  - oil interval
  - plug gap
  - coolant interval
  - fuel filter and PCV interval

  Lexus doesn't host a 1996–97 owner's manual, and NHTSA lists no recalls for the LX 450.
