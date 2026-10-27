# Deepen report: group spec-e (Task A, spec hunt)

All seven pages were SPEC only, so no repairs, FAQs or service items were added or removed. None of the detail files (`data/extra/suzuki/*`, `data/extra/chevrolet/*`) had markers.

| Page | Markers | Repairs | FAQs | Service items |
|---|---|---|---|---|
| `suzuki/lj-series` (`data/pages/suzuki/lj-series.json`) | 6 → 5 (four more partly filled) | 6 → 6 | 10 → 10 | 11 → 11 |
| `suzuki/samurai` (`data/suzuki.json` → `page`) | 4 → 2 | 7 → 7 | 11 → 11 | 13 → 13 |
| `suzuki/jimny-jb23` (`data/pages/suzuki/jimny-jb23.json`) | 0 → 0 (nothing to do) | 8 → 8 | 11 → 11 | 14 → 14 |
| `suzuki/jimny-jb74` (`data/pages/suzuki/jimny-jb74.json`) | 7 → 0 | 6 → 6 | 11 → 11 | 12 → 12 |
| `chevrolet/k5-blazer` (`data/chevrolet.json` → `page`) | 8 → 8 | 7 → 7 | 12 → 12 | 14 → 14 |
| `chevrolet/k5-blazer-1st` (`data/pages/chevrolet/k5-blazer-1st.json`) | 8 → 8 | 7 → 7 | 11 → 11 | 13 → 13 |
| `chevrolet/suburban-square` (`data/pages/chevrolet/suburban-square.json`) | 6 → 6 | 7 → 7 | 11 → 11 | 14 → 14 |

## Main source: Liqui Moly oil guide (Olyslager data)
Liqui Moly's oil guide (https://www.liqui-moly.com/en/service/oil-guide.html) uses Olyslager's OEM-derived lubricant database. I read it through the JSON endpoint the page itself calls (`/en/rest/V1/recommendations/<type_id>`). It gives capacities and service intervals, and lists Liqui Moly products rather than OEM part names, so on the pages any grade it suggests is credited to Liqui Moly. It covers the JB74, LJ80, SJ410/SJ413 and European Samurai. It has **no 1969–91 Chevrolet trucks**: its US Chevrolet data starts in 1985 and covers cars only.

No archive.org or other user-uploaded manual scans were used or linked.

## Confirmed: Jimny JB74 (all 7 markers)
There are three independent sources. **maintenanceschedule.com** transcribes the 2021 JB64/JB74 owner's manual (grades and intervals). **jimny.joker.art.pl** works from Suzuki owner's manual 99011-78RM8-01E (Nov 2023) for the five-door JC74, which has the same K15B engine and gearboxes. **Liqui Moly/Olyslager** covers the "Jimny 1.5 AWD 2018–2024, A6G415", and its capacities match the JC74 handbook figures exactly.
- **Engine oil:** 0W-16 preferred; 0W-20 or 5W-30 also listed (API SL or newer, or ACEA A1/B1 or better in Europe). It takes 3.6 L with the filter (Liqui Moly service fill; the JC74 handbook gives the same). A BigJimny forum owner also quotes the handbook's 0W-16. Intervals are 20,000 km / 12 months in Europe with ACEA oil, otherwise 15,000 km (and in Asia/Australia), with 10,000 km / 6 months (Europe) or 7,500 km (Asia/Australia) in severe use.
- **Spark plugs:** NGK KR6A-10 or Denso ZXU20PR11. Change every 100,000 km / 7 years in Europe, or 30,000 km / 24 months in severe use.
- **Coolant:** Suzuki Super LLC (blue), 5.0 L manual / 4.9 L automatic. First change at 160,000 km / 8 years, then every 80,000 km / 4 years. Green "Standard" coolant is due twice as often.
- **Manual gearbox:** Suzuki Gear Oil 75W, 1.2 L. **Automatic:** Suzuki ATF3317 or Mobil ATF3309, 5.7 L total.
- **Transfer case:** Suzuki Gear Oil 75W. Liqui Moly gives 1.2 L and the JC74 handbook 1.21 L; both are shown.
- **Differentials:** Suzuki Super Gear Oil 75W-85 synthetic, front 1.6 L and rear 1.3 L. Liqui Moly's own product suggestion (GL-5 75W-90 synthetic) is shown alongside.
- **Brake fluid:** DOT 3 / SAE J1703, every 40,000 km / 24 months. On manual trucks the clutch shares the reservoir.
- The baseline intro was rewritten to name these sources. Four sources were added.

## Confirmed: Samurai (2 of 4)
- **Oil interval:** 10,000 km / 6 months, or 5,000 km / 4 months in severe use. This is Liqui Moly/Olyslager data for the European 1990–98 Samurai and is labelled that way.
- **Grease points:** multipurpose grease at the nipples and propeller-shaft joints, checked every 20,000 km / 12 months (Liqui Moly).
- **Cross-check:** Liqui Moly's capacities agree with the AMSOIL figures already on the page: oil 3.7 L (3.9 qt), coolant 5 L (5.3 qt), gearbox 1.3 L (2.7 pt), transfer case 0.8 L (1.7 pt), front diff 2.0 L (4.2 pt, 1992) and rear diff 1.5 L (3.2 pt). The intro now says so, and the source was added.

## Confirmed: LJ series (1 marker removed, 3 partly filled)
All of this is LJ80 data from Liqui Moly/Olyslager. It has no data for the LJ10, LJ20 or LJ50.
- **Brake fluid:** DOT 3 or DOT 4. Liqui Moly lists both, and LJ80.de sells DOT 4. Change every 40,000 km / 24 months. Marker removed.
- **LJ80 engine oil:** about 3.0 L, changed every 10,000 km / 6 months. The grade marker stays.
- **LJ80 coolant:** 3.8 L, every 2 years. The LJ20/LJ50 marker stays.
- **LJ80 driveline:** gearbox 1.0 L; transfer case 0.9 L of GL-4 85W-90; diffs 1.3 L each of GL-5 85W-90 hypoid (grades as Liqui Moly suggests). The LJ10–LJ50 marker stays.

## Still open
- **LJ series:** two-stroke lubrication, in both the buying check and baseline item 2. Suzuki Japan's history pages give engine types only. Also open: the LJ80 oil grade, LJ20/LJ50 coolant, and LJ10–LJ50 gear oils.
- **Samurai:** timing-belt interval (no primary or fluid-maker source found) and coolant type. The 5.3 qt capacity is now cross-checked.
- **All 22 Chevrolet markers** (K5 square body 8, K5 first gen 8, Suburban 6). Attempts that failed:
  - AMSOIL's lookups for the 1987–91 Blazer return 403 to both curl with our User-Agent and WebFetch.
  - The GM Heritage vehicle information kits on gm.com return 403 to our User-Agent, and the listing shows truck kits are not offered for 1969–91. The old gmheritagecenter.com truck PDF redirects away.
  - Liqui Moly/Olyslager has no 1969–91 GM trucks.
  - The CK5 spec resource has no fluid data. The CK5 "fluid capacities" and "recommended fluids" threads quote only Chilton, parts-store lookups or memory, with no GM manual, so I didn't use them.
  - The best remaining route is a legitimately sold GM shop manual (e.g. Helm) or the owner's guide Hank may hold.
