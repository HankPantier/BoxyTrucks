# Deepen report — group spec-f (Task A: spec hunt)

All seven pages were SPEC only. No repairs, FAQs or service items were added or removed.

| Page | Markers | Repairs | FAQs | Service items |
|---|---|---|---|---|
| `land-cruiser/prado-90` | 3 → 3 (1 narrowed) | 8 → 8 | 10 → 10 | 13 → 13 |
| `land-cruiser/prado-120` | 3 → 3 (1 narrowed) | 8 → 8 | 10 → 10 | 14 → 14 |
| `land-cruiser/prado-150` | 6 → 3 (2 narrowed) | 7 → 7 | 11 → 11 | 12 → 12 |
| `land-cruiser/mega-cruiser` | 10 → 10 | 5 → 5 | 10 → 10 | 12 → 12 |
| `nissan-patrol/patrol-60` | 4 → 4 (2 narrowed, capacities added) | 7 → 7 | 10 → 10 | 11 → 11 |
| `nissan-patrol/y62` | 5 → 3 (2 narrowed) | 8 → 8 | 11 → 11 | 13 → 13 |
| `jeep/wagoneer-ws` | 6 → 0 | 7 → 7 | 11 → 11 | 13 → 13 |

In total, 37 markers became 26. "Narrowed" means part of the item is now confirmed and the marker only covers what's still open. For example, "[CONFIRM GRADE & CAPACITY]" became a sourced capacity plus "[CONFIRM GRADE]". No marker was removed without a source.

The detail files had no markers. I added owner's-manual entries to `docs` in `data/extra/land-cruiser/prado-150.json` and `data/extra/jeep/wagoneer-ws.json`.

## Sources used
- **Toyota Japan owner's-manual archive** (manufacturer-hosted, in Japanese). Two Japanese-market Prado 150 manuals were used, both from the maintenance-data table:
  - August 2020 edition (TRJ150W 2TR-FE; GDJ150W/151W 1GD-FTV): https://manual.toyota.jp/pdf/landcruiserprado/landcruiserprado_202008.pdf, pp. 464–471
  - October 2011 edition (2TR-FE, 1GR-FE): https://manual.toyota.jp/pdf/landcruiserprado/landcruiserprado_201110.pdf, pp. 406–409

  The archive has no 90, 120 or Mega Cruiser manuals.
- **Nissan USA Armada owner's manuals** for 2018 and 2020 (the US-market Y62, VK56VD): capacities table, maintenance schedules and engine specifications. Both are under `nissanusa.com/content/dam/Nissan/us/manuals-and-guides/armada/`.
- **Mopar owner's manuals:**
  - 2022 Wagoneer/Grand Wagoneer: `vehicleinfo.mopar.com/.../2022/Wagoneer/5633299-22_WS_OM_EN_USC_DIGITAL_E6.pdf`
  - 2025 Wagoneer/Grand Wagoneer: `.../2025/Grand_Wagoneer/103579_25_WS_OM_EN_USC_DIGITAL_E2.pdf`
- **Penrite Oil's recommendation lookup** (Infomedia NetLube data, http://www.datateck.com.au/Lube/PenriteAus/). This is the fluid-maker tool I used. I took **capacities only** from it. Its oil and gear-oil "recommendations" are Penrite's own products, not OEM grades, so no grade on any page relies on Penrite.

Roughtrax, Toyota Australia, mopar.com and the AMSOIL lookup all blocked the bot user agent or weren't on the fetch allowlist.

## Confirmed: Prado 150
- **Engine oil:** The 1GD-FTV (Japanese manual) recommends ACEA C5 0W-20, with JASO DL-1 0W-30 or 5W-30 acceptable. It takes 7.2 L oil only, or 7.7 L with the filter. Penrite gives 7.5 L with filter for Australian DPF trucks, so both values are shown.
- **Other engines' oil:** The 1KD-FTV takes 7.0 L with filter (Penrite). In the Japanese manuals, the 1GR-FE takes 5.7 L oil only, or 6.1 L with the filter. The 2TR-FE takes 5.5 L, or 5.9 L with the filter, in the 2020 manual, but 5.0 L, or 5.7 L with the filter, in the 2011 manual; both are shown.
- **Diesel oil interval:** The Japanese manual changes oil and filter about every 20,000 km or 12 months and warns against grades other than C5. This is in the item note.
- **Coolant:** Toyota Super Long Life Coolant. The 1GD-FTV takes 10.2 L plus 2.6 L in the intercooler circuit, the 1GR-FE 11.0 L and the 2TR-FE 8.1 L.
- **ATF:** Toyota ATF WS for every engine in the Japanese manuals. The 1GD-FTV takes 9.6 L and the 1GR-FE 10.9 L. The 2TR-FE takes 9.9 L in the 2011 manual and 8.5 L in the 2020 manual.
- **Transfer case:** Toyota Transfer Gear Oil LF, SAE 75W, 1.4 L. Penrite also gives 1.4 L.
- **Differentials:** Toyota Differential Gear Oil LT, GL-5 75W-85. The front takes 1.4 L. The rear takes 2.7 L, or 2.65 L with the diff lock. A Torsen rear LSD takes 2.55 L of Gear Oil LX (GL-5 75W-85).
- The service intro now names these sources, and notes that Japan never got the 1KD-FTV and that other markets may specify different grades.

## Confirmed: Nissan Patrol Y62 (US Armada manuals)
- **Engine oil:** 6.5 L with filter, 6.2 L without. Penrite's Australian Patrol data independently gives 6.5 L. The Armada grade is Nissan 0W-20 SN; the 2020 manual also accepts synthetic 0W-20 GF-5 SN.
- **Spark plugs:** replace every 105,000 mi (168,000 km), or sooner if the gap exceeds 1.35 mm. The factory plug is DILKAR7B11 with a 1.1 mm gap.
- **Differentials:** the front takes Nissan Hypoid Super GL-5 80W-90 (conventional, not synthetic). The rear grade changed between years: Hypoid Super-S GL-5 75W-90 synthetic in 2018, Hypoid Fluid S1 GL-5 75W-80 in 2020. Both are shown.
- **Diff capacities and severe service:** front 1.6 L and rear 2.3 L (Penrite, Australian Patrol). The Armada schedule changes diff oil every 20,000 mi or 24 months when towing or on rough or muddy roads; this is now in the interval.
- **Brake fluid:** Nissan Super Heavy Duty Brake Fluid, or an equivalent DOT 3. The schedules disagree, so both are shown: every 20,000 mi or 24 months in 2018, every 30,000 mi or 36 months in 2020, and every 10,000 mi or 12 months in severe use.
- The intro no longer says the oil specs couldn't be found.

## Confirmed: Jeep Wagoneer WS (2022 and 2025 owner's manuals)
- **Cabin filter:** behind the glove box, in the fresh-air inlet. Replace every 12,000 mi (19,000 km).
- **Spark plugs:** the 3.0 Hurricane is due every 60,000 mi (both manuals), the 5.7 every 100,000 mi and the 6.4 every 90,000 mi. Intervals are by mileage only. I read the X positions in the 2022 table against its column headers.
- **Coolant:** Mopar 10-year/150,000-mile OAT coolant to MS.90032, flushed at 10 years or 150,000 mi.
- **Coolant capacities:** the 5.7 takes 17 qt per the manual (AMSOIL says 16.9 qt; both shown). The Hurricane intercooler circuit is 3.2 qt in the 2025 manual and 2.9 qt in 2022; both shown.
- **Transfer case:** the manuals print the fluid as "Mopar® Mobile LT", and the page quotes it that way. The plan inspects it every 30,000 mi and changes it at 150,000 mi. No capacity is listed.
- **Rear axle:** friction-modified GL-5 75W-85 synthetic, both with the ELSD and with a mechanical LSD. AMSOIL's P/N 68083381AA still can't be tied to either variant, and the page says so.
- **Brake fluid:** Mopar DOT 3 (SAE J1703). The 2022 and 2025 plans list no replacement interval, and the item now says that.
- **Consistency edits:** I updated repair "Service the front and rear differentials" (rear-axle fluid) and repair "Engine air filter and Hurricane spark plugs" (it said the plug interval couldn't be confirmed). FAQ "What oil does it take?" now adds the 6.4's MS-12633 spec and notes the manual matches AMSOIL's capacities. I also added MS-12633 to the oil service item.

## Partly confirmed (capacities only, from Penrite)
- **Prado 90:** petrol oil capacities are now 5.2 L with filter for the 5VZ-FE and 5.4 L for the 3RZ-FE. The petrol grade is still marked.
- **Prado 120:** 5.2 L with filter for the 1GR-FE and 5.1 L for the 3RZ-FE 2.7. Grades and the other engines are still marked.
- **Patrol 60:** figures are for the Australian G60 with the P engine, 1968–1980, and are approximate:
  - engine oil about 5.3 L service refill (Penrite doesn't say whether that includes the filter)
  - gearbox 2.0–2.3 L and transfer case 3.4 L
  - front diff 1.2 L and rear 1.0–2.0 L

  Grades, filter type and PTO-box capacity are still marked, and the intro now explains the source.

## Still open
- **Prado 90 and 120:** ATF change interval, petrol oil grades, and the diesel fuel-filter part number by frame. No 90 or 120 owner's manual was reachable: Toyota Japan's archive starts in 2011, and Toyota Australia blocks the bot.
- **Prado 150:** diesel fuel filter, Australian-market oil grades, and ATF type for the Australian 1KD-FTV automatic, which is not covered by the Japanese manuals.
- **Mega Cruiser:** all 10 are still open. No manufacturer or fluid-maker data was found: there's no Toyota Japan manual and no Penrite entry.
- **Patrol 60:** oil grade and filter, gear-oil grades, PTO capacity, and brake fluid.
- **Y62:**
  - non-US Patrol oil grade
  - Patrol rear-locker axle grade (the Armada has no locker)
  - the ATF level procedure in repair 1, which is only in the workshop manual
- **Noted, not changed:** for the 2006–09 KDJ120 1KD-FTV, Penrite lists 7.0 L with filter against the page's 7.4 L from Roughtrax. This wasn't a marker, so the page is unchanged; Hank may want both values shown.
