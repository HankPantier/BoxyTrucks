# Deepen report — group spec-a (Task A: spec hunt)

All four pages were SPEC only. No repairs, FAQs or service items were added or removed, so those counts are unchanged.

| Page | Markers | Repairs | FAQs | Service items |
|---|---|---|---|---|
| `nissan-patrol/y61` (`data/pages/nissan-patrol/y61.json`) | 14 → 2 | 7 → 7 | 11 → 11 | 12 → 12 |
| `scout/scout-ii` (`data/scout.json` → `page`) | 12 → 12 | 7 → 7 | 12 → 12 | 14 → 14 |
| `jeep/cj-7` (`data/jeep.json` → `page`) | 11 → 4 | 7 → 7 | 11 → 11 | 15 → 15 |
| `jeep/yj` (`data/pages/jeep/yj.json`) | 11 → 7 | 7 → 7 | 11 → 11 | 13 → 13 |

None of the detail files (`data/extra/...`) had markers or any fluid or torque text, so they were left as they were.

## Note on the two factory-manual sources
The two primary sources used below are scans of the factory manuals hosted on the Internet Archive. Both are user uploads in the Archive's `manuals` collection:
- **Nissan Europe, Patrol GR Y61 Electronic Service Manual.** This is the 1998 edition plus Supplements I to IV (2000, 2001, 2002, 2004), MA and FA sections: https://archive.org/details/ElectronicServiceManualNissanPatrolY61. The Supplement-III fluids table (2002) covers every engine and gives separate "except Europe" figures. Its **maintenance schedules are European only**, and the page labels them that way.
- **Jeep 1981 Technical Service Manual**, Chapter B maintenance schedules, lubricant chart and front-hub procedure: https://archive.org/details/1981jeepfactoryservicemanualocr1294pages. Figures from it are labelled "1981 factory schedule/manual" on the page because they apply to 1981-era CJs.

Hank may want to decide whether he's comfortable linking to Archive-hosted manual scans. If not, the figures could be re-cited to an owner's manual he holds.

## Confirmed: Nissan Patrol Y61 (Nissan ESM)
- **Rear LSD oil** (repair "Rear axle seal" and baseline diffs): Nissan Hypoid LSD gear oil KLD31-14002, or API GL-5 SAE 140 with 10% LSD friction modifier 38469-C6000. This matches the ExplorOz owner's quote. Open diffs take API GL-5, with 80W-90 preferred.
- **Diff capacities:** front 5.4 L. Rear is 2.1 L with LSD (outside Europe; this matches the ExplorOz handbook figure). The H233B takes 2.4 L open or 3.0 L with a diff lock, and the H260 takes 4.7 L open or 3.7 L with a lock.
- **Transfer (TX12A):** 1.9 L of Genuine Nissan ATF (Dexron III) or API GL-4. Replace every 60,000 km, or every 30,000 km in severe use (Europe schedule).
- **Manual gearbox:** API GL-4. The FS5R30A takes 5.1 L of 75W-90. The FS5R50B is listed at 3.8 L in the 1998 edition but 3.5 L in the 2001–02 supplements, which give 75W-90 and then 75W-85. Both values are shown.
- **Auto:** the RE4R03A takes 11.8 L of Genuine Nissan ATF (Dexron III/Mercon). The TB48's RE5R05A takes 10.4–10.7 L of Matic Fluid J only.
- **Engine oil, other engines:** ZD30 outside Europe takes API CD to CF-4 or JASO DH-1, 8.2 L with filter; the ESM says never use API CG-4. TD42 takes API CC to CF-4 or JASO DH-1, 10.5 L. TB45 takes 7.6 L and TB48DE takes 6.8 L. The 2004 European supplement prefers 5W-30 for diesels, which conflicts with the Australian 10W-40 bulletin, so the page shows both.
- **Oil interval** (also buying check 2): Europe schedule is every 15,000 km or 12 months for the ZD30 and TB48, and every 10,000 km or 6 months for the RD28, halved in severe use.
- **Diesel fuel filter:** the ZD30 uses a spin-on filter with a water drain cock. Screw it on until it seats, then turn a further 2/3 of a turn, and bleed the air afterwards. Europe interval is 45,000 km or 36 months for the ZD30 and 40,000 km for the RD28.
- **RD28 timing belt:** Europe schedule replaces it at 80,000 km or 48 months, or 90,000 km for high-mileage use. Column positions were checked with PDF coordinates.
- **Coolant:** Nissan Genuine Engine Coolant, or L2N in Europe, at a 50% mix. Capacities are given per engine. Europe interval is first change at 90,000 km or 60 months, then every 60,000 km or 48 months.
- **Front wheel bearings** (baseline item and repair 1 text): lock nut to 167–196 Nm, back off, retighten to 3–5 Nm, preload 0–18.6 N, zero end play. These Nissan FA-section figures match Gregory's. Grease is replaced every 30,000 km on the ZD30 Europe schedule.
- **Brake fluid:** DOT 3 outside Europe; DOT 3 or DOT 4 in Europe, never mixed. The Europe schedule replaces it about every 2 years.

## Confirmed: Jeep CJ-7 (1981 Jeep FSM)
- **Front-hub outer locknut 50 ft-lb (68 N·m)**, with the lock washer bent over. The inner nut is 50 ft-lb, then backed off 1/6 turn. Updated in repair 6 and in the baseline item. Two Off-Road.com owners also quote the factory manual with the same figure.
- **Oil:** first change at 5,000 mi, then every 7,500 mi or 7.5 months.
- **Fuel filter:** first at 12,500 mi, then every 15,000 mi.
- **Spark plugs:** every 30,000 mi.
- **Coolant:** change at 12,500 mi or 12.5 months, then at the start of each winter season, keeping a 50/50 mix.
- **Automatics (999/904):** Dexron or Dexron II. Drain and refill every 25,000 mi, or 10,000 mi in heavy-duty use. ExtremeTerrain's ATF+4 is shown alongside.
- **Wheel-bearing repack:** every 30,000 mi, or 15,000 mi in heavy-duty use, plus after water deep enough to cover the hubs.
- **Disagreement now shown:** the 1981 FSM specifies SAE 85W-90 GL-5 for the axles, the manual gearboxes and the Dana 300, while ExtremeTerrain lists 80W-90. Both appear in the FAQ and the axle and transfer-case items.

## Confirmed: Jeep YJ (ExtremeTerrain YJ factory torque tables)
- **Rear main bearing cap**, 4.0/4.2: 80 ft-lb (repair "Replace the rear main seal"). Source: https://www.extremeterrain.com/wrangler-yj-engine-torque-specs.html
- **Spark plugs**, all YJ engines: 27 ft-lb (same page).
- **30RH/32RH filter screws:** 35 in-lb, with pan bolts at 14 ft-lb. Source: https://www.extremeterrain.com/wrangler-yj-drivetrain-torque-specs.html
- **NP231 drain and fill plugs:** 15–25 ft-lb (same page).

## Still open
- **Y61:** glow-plug spec. Oil interval for non-European markets is still marked "Other markets: [CONFIRM IN MANUAL]", because no Australian or Middle East owner's manual was found online.
- **Scout II: all 12 open.** No vendor or IH fluid chart could be found that says it reproduces the IH manual. The IHPA forum gives only owners' practice, with no manual citation. The archive.org IH CTS-2306 light-duty manuals are access-restricted, and the IHPA product pages for the manual sets list contents only. Open items: oil interval, plug gap, coolant capacity and type, A727 capacity and type, manual-gearbox lube, Dana 20 capacity and grade, axle grade and capacity, hub repack interval, and PS fluid type.
- **CJ-7:** drive-belt type, TH400 fluid (the 1981 FSM doesn't cover the 1976–79 Quadra-Trac TH400), T-4/T-5 fluid (FAQ), and brake-fluid interval (the 1981 schedule has no replacement interval).
- **YJ:** oil drain-plug torque, diff cover-bolt torque (neither is in ExtremeTerrain's YJ tables), antifreeze type, AX-5/AX-15 and diff capacities (retailer charts only), automatic ATF type, and the FAQ "fill to the hole" capacity note. Archive.org's Chilton YJ manual is lending-only.
