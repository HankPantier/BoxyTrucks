# Deepen / spec hunt: group spec-b

Pages: `bronco/sixth-gen`, `g-class/g550`, `range-rover/l322`, `range-rover/l460` (page files plus detail files). No build or git was run.

## Counts (before → after)

| Page | Markers | Repairs | FAQs | Buying checks | Service items |
|---|---|---|---|---|---|
| bronco/sixth-gen | 10 → **0** | 7 → 7 | 11 → 11 | 8 → 8 | 13 → 13 |
| g-class/g550 | 10 → **3** (one narrowed) | 8 → 8 | 11 → 11 | 8 → 8 | 14 → 14 |
| range-rover/l322 | 9 → **4** (two narrowed) | 7 → 7 | 11 → 11 | 8 → 8 | 14 → 14 |
| range-rover/l460 | 9 → **9** | 6 → **8** | 11 → 11 | 8 → 8 | 11 → 11 |

## Bronco sixth-gen: all 10 confirmed
Source: Ford's own **2021 Bronco Owner's Manual PDF** (fordservicecontent.com, version 1B, 03/2021). It has been added to `sources`, to the detail file's `docs` and to its `sources`.
- **Wheel-nut torque (detail file):** 100 lb-ft (135 Nm), M12x1.5. Retighten within 100 mi of any wheel removal.
- **Front axle:** Motorcraft 80W-90 (WSP-M2C197-A). 26.2 fl oz with the locker; 29.2 fl oz with no locker and no disconnect; 30.4 fl oz with no locker and the disconnect.
- **Rear axle:** Motorcraft 75W-85 synthetic (WSS-M2C942-A). 63.6 fl oz with the locker; 65.3 without. This settles which axle takes which oil.
- **7-speed manual:** the manual specifies Motorcraft Dual Clutch Transmission Fluid XT-11-QDC (WSS-M2C200-D2), 2.4 qt dry fill.
- **Oil interval:** set by the oil-life monitor. Normal use 7,500–10,000 mi; severe 5,000–7,500 mi; extreme 3,000–5,000 mi. The off-road schedule is 5,000 mi or 6 months. Never more than 1 year or 10,000 mi.
- **Air filter:** every 30,000 mi; inspect frequently in dusty or off-road use. **Cabin filter:** every 20,000 mi.
- **Spark plugs:** every 100,000 mi, or 60,000 mi when towing or idling for long periods.
- **Coolant:** first change at 10 years or 200,000 mi, then every 5 years or 100,000 mi.
- **10R60 automatic:** fluid and filter every 100,000 mi. The manual's special-conditions tables don't shorten this.
- **Brake fluid:** every 3 years.
- **Transfer case and axles:** every 150,000 mi, or when leaking or submerged.

## G 550 (2009–2018 US)
Confirmed. All sources are Mercedes-hosted PDFs: MBUSA operator's manuals for 2013, 2014, 2016 and 2018; the MBUSA 2013 maintenance booklet, which has a G-Class column (read visually); and the Mercedes-Benz Canada 2016 G-Class service booklet.
- **Engine oil:** MB 229.5, 9.0 L with filter, for both the M273 (2013 and 2014 manuals) and the M176 (2016 and 2018 manuals; the 2016 manual also allows 229.3). The page now notes that the manuals list 229.5, not 229.52.
- **Oil interval:** follow the service indicator. The 2013 US booklet sets 10,000 mi or 1 year.
- **Air filter:** M273, 40,000 mi or 4 years (2013 US booklet); M176, 40,000 km or 2 years (2016 Canadian booklet).
- **Spark plugs:** M273, 60,000 mi or 6 years (US 2013); M176, 100,000 km or 5 years (Canada 2016).
- **ATF and filter:** M273, 40,000 mi or 4 years (US 2013); 120,000 km (Canada 2016).
- **Power steering:** level check only. No replacement interval is scheduled.
- **Brake fluid:** DOT 4 Plus (MB 331.0), every 20,000 mi or 2 years (US 2013). The Canadian 2016 booklet says annually; both values are shown on the page.
- **Factory intervals added** (no marker existed): axles and transfer case every 50,000 mi or 5 years (US 2013). Canada 2016 gives axles every 80,000 km or 4 years and the transfer case every 120,000 km.
- **Diff locks (partly confirmed):** both booklets show the diff-lock mechanism has its own reservoir filled with brake fluid, changed together with the brake fluid.

Still open (3):
- **Transfer case capacity.** The fluid type is now given as SAE 80/80W/80W-85 gear oil for the VG 150 E case. This comes from Mercedes' WIS tables as reproduced on bolidenforum.de for a 2011 G 55, so it's a near-primary source and is labelled as such.
- **Front and rear axle capacities.** The grade is now backed by FCP Euro plus the WIS table.
- **Whether the centre lock is vacuum-operated on a given year** (repair 5).

## Range Rover L322
Confirmed. The main source is Land Rover North America's **2006–2008 Range Rover maintenance schedule** (LRNA, 7/26/2007). It's hosted by a dealer or shop at jcsbritish4x4.kukui.com, with a matching copy on fullfatrr.com, and I read it visually. Two TOPIx owner-guide PDFs (maintenance; routine services 12MY on) back it up.
- **Oil:** every 7,500 mi or 6 months (LRNA 2006–08); 15,000 mi or 12 months under the 12MY UK/Euro plan (4.4 TDV8: 16,000 mi).
- **Air filter:** every 60,000 mi or 48 months. **Cabin filter:** every 15,000 mi or 12 months.
- **Coolant:** every 10 years for petrols (LRNA; owner guides). The older owner guide gives 4 years for diesels.
- **Brake fluid:** every 3 years regardless of distance.
- **Power steering:** check and top up only. No replacement interval.
- **Added:** spark plugs at 105,000 mi (2006–08 only); fuel filter at 150,000 mi (petrol); drive belts at 150,000 mi; supercharger belt at 105,000 mi. Factory transmission, transfer case and axle intervals were added alongside the Atlantic British advice: ATF at 10 years or 150,000 mi; transfer case at 75,000 and 150,000 mi; electronic rear diff at 75,000 and 150,000 mi; axles every 10 years.

Still open (4):
- Cabin filter part by model year (`[CONFIRM BY VIN]`).
- DD295 fitment on 2006 model-year trucks (`[CONFIRM BY VIN]`).
- Spark plug interval for 2002–05 and 2010–12. This marker is now narrowed to those years.
- Diesel fuel-filter interval. This marker is now narrowed to diesels.

## Range Rover L460
**Specs:** none confirmed (9 open). I couldn't find a public L460 owner handbook PDF. The TOPIx owner-guide PDFs I found run only up to the L405, Land Rover's owner-site handbook pages return 404, and the fluid makers' lookup tools load data only in the browser. Forum material (FullFatRR) is owner opinion, and it disagrees on transfer-box fluid. The open items are:
- petrol and PHEV oil spec
- air and cabin filter parts and intervals
- spark plug interval
- ATF spec
- transfer box fluid
- front disconnect and active-diff fluid
- brake fluid spec

**Deepen:** repairs went from 6 to 8.
- **Cracked oil filter housing:** NHTSA recall 24V-450 (Land Rover N908). The remedy is a new housing, filter and O-rings.
- **Rear camera water damage:** NHTSA recalls 24V-947 (2022–23) and 26V-678 (2022–26: dealers drill drain holes and replace the camera if needed).
- **Rear brake-pad repair:** added NHTSA owner-complaint evidence from 2023–24 trucks (pads worn at roughly 10,000–17,000 mi).
- **Detail file:** added recall 26V-678. The VIN-recall buying check now mentions it.

FAQs (11), buying checks (8) and service items (11) were already in range, so I left them alone. I stopped at 8 repairs rather than pad the list. Other NHTSA complaints (coolant leaks, one transfer-case failure, cracked glass) were one-offs without forum or bulletin backing.

## Source URLs added
- https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2021-Ford-Bronco-Owners-Manual-version-1B_om_EN-US_03_2021.pdf
- https://www.mbusa.com/content/dam/mb-nafta/us/owners/manuals/2013/operators/MY13_G-Class_Operator.pdf
- https://www.mbusa.com/content/dam/mb-nafta/us/owners/manuals/2014/operators/MY14_G-Class_Operator.pdf
- https://www.mbusa.com/vcm/MB/DigitalAssets/pdfmb/ownersmanual/MY16_G.pdf
- https://www.mbusa.com/vcm/MB/DigitalAssets/pdfmb/ownersmanual/MY18_G_Class_Operators_Manual.pdf
- https://www.mbusa.com/vcm/MB/DigitalAssets/pdfmb/maintenancebooklets/MY13_Maintenance_Booklet.pdf
- https://www.mercedes-benz.ca/content/dam/mb-nafta/ca/owners/operators-manual/2016/service-booklets/MY16_SERVICE_BOOK_G-CLASS_463_ENG_6515869413_ED12016.pdf
- https://www.bolidenforum.de/portal/fahrzeugdaten/mercedes-benz-2011-g55/?vd_lang=en
- https://jcsbritish4x4.kukui.com/Files/Documents/06-08-range-rover.pdf
- https://topix.landrover.jlrext.com/topix/service/procedure/66354/PDF/b9ff2387-7f12-4623-a059-e95e1c37b7be/en_GB
- https://topix.landrover.jlrext.com/topix/service/procedure/162966/PDF/fc8ac85e-a478-4f63-b8cf-a832a121f299/en_GB
- NHTSA recall pages 24V450000, 24V947000, 26V678000; NHTSA complaints API for the 2023 and 2024 Range Rover
