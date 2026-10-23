# Deepen / spec hunt — group spec-c

Edited only: `data/pages/bronco/full-size.json`, `data/land-rover.json` (`page`, slug `defender-90-110`), `data/extra/land-rover/defender-90-110.json`, `data/pages/land-cruiser/fj62.json`, `data/pages/land-cruiser/70-series.json`. No build, no git. Detail files for Bronco, FJ62 and 70 Series had no markers and were not changed.

## Before → after

| Page | Markers | Repairs | FAQs | Buying checks | Service items |
|---|---|---|---|---|---|
| bronco/full-size (SPEC) | 9 → 1 | 8 → 8 | 10 → 10 | 8 | 13 → 13 |
| land-rover/defender-90-110 (SPEC; page + extra) | 9 → 3 | 7 → 7 | 10 → 10 | 8 | 14 → 14 |
| land-cruiser/fj62 (SPEC + DEEPEN) | 9 → 8 | 6 → 8 | 10 → 11 | 8 → 8 | 13 → 13 |
| land-cruiser/70-series (SPEC) | 9 → 8 | 8 → 8 | 11 → 11 | 8 | 14 → 14 |

## Confirmed specs and sources

### Bronco full-size: 1996 Ford F-Series/Bronco Workshop Manual (Section 00-03 and others, hosted on diesel-dave.com)
- Oil interval: every 5,000 mi normal, 3,000 mi severe duty. Source: [normal](https://www.diesel-dave.com/vehic/manual/stj/stj03011.htm) and [severe](https://www.diesel-dave.com/vehic/manual/stj/stj03012.htm) schedules.
- Spark plugs: 5.8 ASF-32C, gap 0.042–0.046 in; 5.0 ASF-42P, gap 0.052–0.056 in; 4.9 BSF-44C, gap 0.042–0.046 in. Plugs are replaced at 60,000 mi. Source: [Section 03-07A specs](https://www.diesel-dave.com/vehic/manual/stj/stj37a23.htm). The page notes that earlier trucks should be checked against their VECI decal.
- Coolant: change every 30,000 mi or 36 months, with the first change at 50,000 mi or 48 months. Source: normal schedule.
- M5OD (Mazda R2) manual transmission: Motorcraft MERCON ATF, 3.8 qt (7.6 pints), changed every 60,000 mi. Source: [00-03 specifications](https://www.diesel-dave.com/vehic/manual/stj/stj03017.htm). This agrees with the AMSOIL upper figure.
- Dana 44 IFS front axle: Ford 4x4 Gear Oil F1TZ-19580-A (WSL-M2C191-A), 3.6 pints. The manual gives no viscosity, so I removed the unsourced "80W-90".
- Front wheel and spindle bearings: Ford High Temperature 4x4 Front Axle and Wheel Bearing Grease E8TZ-19590-A (ESA-M1C198-A).
- Brake fluid: DOT 3 (C6AZ-19542-AA/BA, ESA-M6C25-A). The 1996 schedule has no fluid-change interval, so the unsourced "every 2 years" was replaced with that fact.
- Power steering: Ford Premium Power Steering Fluid E4AZ-19582-C or E6AZ-19582-AA (ESW-M2C33-F). Source: [Section 11-02A](https://www.diesel-dave.com/vehic/manual/stj/stjb2a10.htm). The page notes that some owners use Mercon V.
- Air filter interval: 30,000 mi or 30 months. This was added to the interval field; the marker is on the spec field.
- The fluids FAQ was extended to match.

### Defender 90/110
- **Td5 oil:** 7.8 L with filter, 5W-40 or 5W-50. Source: [Haynes routine maintenance guide](https://haynes.com/en-gb/tips-tutorials/land-rover-90-110-defender-routine-maintenance-guide-diesel-engines-1983-2007).
- **Puma 2.4 (2007–12 MY) and 2.2 (2012 MY on) oil:** 6.85 L service fill with filter, 5W-30 to WSS-M2C913-B/C, or WSS-M2C934-B for the 2.2 with DPF. Source: [Land Rover oil recommendations chart (Defender2-hosted PDF)](https://defender2.net/gallery/albums/userpics/11134/en_GB.pdf).
- **V8 fuel filter:** ESR4065. Sources: [Rovers North](https://www.roversnorth.com/parts/esr4065_fuel_filter_v8_threaded_type) (NAS 90 and 110) and [Lucky8](https://lucky8llc.com/products/fuel-filter) (Defender '94–'97). Added as a part.
- **Salisbury 110 rear axle:** 2.26 L (110/130); the 90 rear takes 1.7 L. Source: Haynes.
- **Power steering:** Dexron IID per Haynes. The 1993 US checklist says ATF Type F. Both are shown with sources and the marker was removed.
- **300Tdi belt tension:** the reduced 11 Nm figure is confirmed by [Glencoyne](https://www.glencoyne.co.uk/timing-belt-changes-some-useful-tips) and AULRO. The old figure is 15 Nm according to Glencoyne and 14 Nm according to AULRO, and the page shows both.
- **Wheel nut torque (extra file):** 130 N·m for alloy and 108 N·m for steel wheels (Haynes). A 1993 NAS 110 V8 data set (BolidenForum) also gives 130 N·m. The 170 N·m figure is still noted.

### FJ62: Toyota 3F-E Engine Repair Manual Supplement (FJ62), [Internet Archive PDF](https://archive.org/download/3FEREPAIRMANUAL/3FE%20REPAIR%20MANUAL.pdf)
- **Oil:** 7.8 L (8.2 qt) with filter, 7.0 L without, 8.0 L dry; API SC–SF or better; Toyota's temperature chart runs from 5W-30 to 20W-50. This resolved the viscosity marker.
- **Spark plugs:** ND W16EXR-U or NGK BPR5EY, gap 0.8 mm (0.031 in). Added to the tune-up spec.
- **Coolant:** 17.5 L with front heater, 19.5 L with front and rear heaters. This conflicts with the 16.5 L in the IH8MUD compilation, so the page shows both.

### 70 Series: Toyota 1991 Land Cruiser owner's manual (2L-T/1PZ/1HZ), [Internet Archive PDF](https://archive.org/download/3FEREPAIRMANUAL/1991%20Toyota%20Land%20Cruiser%20Owners%20Manual%20%28Covers%2070%2C%2073%2C%2078%2C%20LJ%2C%20PZJ%2C%20KZJ%29.pdf)
- **Diesel timing belt:** the warning light comes on every 100,000 km, and the belt should be replaced when it does. Marker resolved. I used only the km figure, because the OCR'd miles figure ("80000") looks unreliable.
- **1HZ gearbox:** 4.9 L, GL-4 or GL-5, SAE 90. **Power steering on older trucks:** Dexron-II. Both confirmed and re-attributed to the owner's manual.
- **V8 gearbox grade:** GL-4 75W-90 is now backed by two independent specialists, Unsealed and [70 Series Store](https://70seriesstore.com/blogs/information/what-oil-does-a-79-series-gearbox-take). The V8 capacity still disagrees (Roughtrax says 2.7 L, 70 Series Store about 4.5 L), so that marker stays.

## DEEPEN: FJ62 repairs 6 → 8
1. **Push-button 4WD stuck on: vacuum solenoid and lines.** Owner consensus across three IH8MUD threads (solenoid write-up, 4WD light, T-case solenoids). Parts: CruiserTeq OEM 4WD solenoid ELEC89132 (fit to be confirmed by VIN) and an Amazon search for vacuum hose.
2. **Fuel tank leak and NHTSA recall 91V-110** (1980–1990 Land Cruisers; tank separator welds crack). Backed by NHTSA owner complaints about a split tank and a corroded rear fuel line. Parts: CruiserTeq tank GAS60241, filler hose EGF772136X and grommet INT92002.

I also added one FAQ, "What oil and fluids does it take?", from the 3F-E manual and IH8MUD. Buying checks (8) and service items (13) were already within the target ranges. No story paragraph was added. I stopped at 8 repairs; no padding was needed.

## Still open (markers left in place)
- **Bronco (1):** air filter "panel element" form.
- **Defender (3):**
  - Swivel pin torques and preload. The sources conflict: 65 Nm upper / 25 Nm lower (RAVE, Defender2 quote) against 78/78 Nm (05/99 table). Turning effort is 1.16–1.46 kg (300Tdi manual) against 3.6–4.5 kg (1983–95 manual, Haynes). All values are now shown; the marker stays because this is safety-critical.
  - V8 spark-plug gap. The ERR3799 part is confirmed, but no gap source was found.
  - Swivel fill for 1993–97 NAS trucks. One-shot grease (Lucky8) conflicts with EP oil (BolidenForum, JC's British checklist).
- **FJ62 (8):** all are service intervals: oil, ignition, coolant, A440F, transfer case, front and rear diffs, brake fluid. The FJ62 maintenance schedule was a separate booklet that I couldn't find online. Toyota's 1986 maintenance manual on the Internet Archive covers the FJ60 (2F) and its OCR'd schedule is garbled, so I didn't use it.
- **70 Series (8):** intervals for oil, fuel filter, transfer case, front and rear diffs and brake fluid (also in a separate booklet); V8 gearbox capacity; V8 power steering fluid.
