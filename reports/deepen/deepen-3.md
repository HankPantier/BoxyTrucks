# deepen-3 report

Pages: `lexus/lx600`, `lexus/gx470` (flagship, `data/lexus.json` → `page`), `g-class/w460`, `g-class/w461`, `g-class/4x4-squared`, `g-class/second-gen`.

## Before → after

| Page | Markers | Repairs | FAQs | Buying checks | Service items | Story paras |
|---|---|---|---|---|---|---|
| lexus/lx600 | 0 → 0 | 5 → 8 | 11 → 11 | 6 → 8 | 12 → 12 | 9 → 9 |
| lexus/gx470 | 1 → 0 | 6 → 8 | 11 → 11 | 8 → 8 | 14 → 14 | 9 → 9 |
| g-class/w460 | 9 → 9 | 6 → 8 | 11 → 11 | 7 → 7 | 13 → 13 | 9 → 9 |
| g-class/w461 | 6 → 6 | 6 → 8 | 11 → 11 | 7 → 7 | 13 → 13 | 8 → 8 |
| g-class/4x4-squared | 9 → 7 | 6 → 8 | 11 → 11 | 8 → 8 | 14 → 14 | 7 → 8 |
| g-class/second-gen | 8 → 5 | 6 → 8 | 11 → 11 | 7 → 8 | 14 → 14 | 7 → 7 |

FAQs (11) and service items (12–14) were already in range, so they weren't padded. Detail files were left unchanged, except for the GX 470 manual-link fix below. They had no markers.

## New repairs (all have parts lists, some empty by nature)
- **LX 600:**
  - Front brake squeal: Lexus TSB L-SB-0036-24, which covers 2022–24 LX 600 and 2024 GX 550.
  - Windshield molding buzz above 55 mph: TSB L-SB-0019-24, plus the owner-found leaves in the cowl.
  - Power back door won't close: pinch sensors replaced under warranty for two IH8MUD owners, plus the kick-sensor reset.
  - Sources: ClubLexus TSB listing (mirrors NHTSA) and the IH8MUD 300/600/700 issues thread.
- **GX 470:**
  - Front differential support upgrade, 2003–early 2005, part 52380-60021 (GXOR).
  - Secondary air injection pump, 2005–09: GXOR and the ClubLexus thread for codes, the $2k quote and the bypass outcome.
- **W460:**
  - Springs and shocks (Classic & Sports Car's broken springs and leaking dampers).
  - Water leaks at the wiper spindles, windscreen, sunroof and plenum (C&SC, Handsome Motors). Expedition Imports parts are verified.
- **W461:**
  - Sagging doors and hinge rust.
  - Windscreen gasket, wiper spindle and floor leaks.
  - Sources: Handsome Motors rust zones, plus Expedition Imports W460-body parts and the 461 floor drain kit.
- **4×4²:**
  - Brake booster vacuum hose recall NHTSA 17V-817, which names the G 550 4×4².
  - M176 crankcase-vent oil separator, valve cover and rear main seal leaks (Handsome Motors on the 2016–18 M176). FCP Euro lists separators 177 010 79 03 and 80 03 for the G 550 4×4².
- **Second gen:**
  - Diff-lock module recall 20V-090.
  - Rear door latch recalls 21V-353 and 24V-659. Details are from the NHTSA API.
- **Story:** added one 4×4² paragraph (Wikipedia, citing Car and Driver) covering the "Extreme-G" concept, the 2014 demand, KW suspension, 0–60 under 6 s and the Hummer H1 comparison.

## Specs confirmed (marker replaced)
- **GX 470 cabin filter:** every 30,000 mi / 36 months, from the Lexus 2008 Warranty & Services Guide (assets.sia.toyota.com, L-MMS-08GX470).
- **4×4² engine oil:** MB 229.5, 2.4 US gal (9.0 L) with filter (G 550), from the MBUSA **2018 G-Class Operator's Manual**. That manual explicitly covers the G 500 4×4². AMSOIL's 2017 G550 lookup independently gives 9.5 US qt.
- **4×4² oil interval:** follow the ASSYST service interval display (same manual).
- **Second-gen engine oil:** MB 229.52 or 229.61, 10.0 US qt (9.5 L) with filter, 2019 G 550 V8, from the MBUSA **2019 G-Class Owner's Manual**.
- **Second-gen oil interval:** ASSYST PLUS display, shortened for arduous use (same manual).
- **Second-gen 12 V battery:** AGM required (same manual).
- **Extra facts added without removing markers:**
  - Brake fluid MB approval 331.0 (both manuals).
  - Coolant capacity 14.1 L (both manuals, G 550).
  - The 4×4² portal and differential oil should be changed after the 2,000-mile break-in (2018 manual).

## Coordinator rule applied
- The GX 470 factory repair manual (RM1164U) was linked to a lexusgxor.com-hosted PDF. That link is removed from `data/lexus.json` sources and `data/extra/lexus/gx470.json` sources, and the manual is now cited by name only. The MBUSA and Lexus/Toyota-hosted manuals are manufacturer-hosted, so they stay linked.

## Still open
- **W460 (9) and W461 (6):** every fluid grade and capacity is still `[CONFIRM IN MANUAL]`.
  - No manufacturer-hosted manual exists for these trucks.
  - Mercedes BeVo (operatingfluids.mercedes-benz.com) only maps sheets by FIN, not by model series.
  - A period owner's manual or WIS extract is still needed.
- **4×4² (7):** still open:
  - spark plug interval
  - ATF interval
  - transfer case, differential and portal-hub oil type and capacity
  - power steering fluid
  - brake fluid interval
  - The 2018 manual doesn't list these.
- **Second gen (5):** still open:
  - spark plug interval
  - ATF interval
  - transfer case and differential oil
  - brake fluid interval
- **Gaps in the new material:**
  - LX 600: the remedy details for TSBs L-SB-0036-24 and L-SB-0019-24 come from an owner's dealer and the TSB summary. The full TSB text wasn't available.
  - LX 600: the center diff lock actuator failure had only one IH8MUD report, so I didn't add it.
  - 4×4²: the brake booster recall has no parts linked, because FCP Euro has no G550 brake-booster vacuum hose category.
