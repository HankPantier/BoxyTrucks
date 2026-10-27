# Mod link tightening: list B

Files in `reports/modlinks-B.txt`: 69 links on 31 pages. Every new URL was fetched with UA `BoxyTrucksBot/1.0` and returned HTTP 200 with no redirect to a homepage. Each page names the model or generation. The Superior Engineering page sits behind Cloudflare, so it was checked with WebFetch instead.

## Counts

- Tightened to a model-specific page: **47**
- Built to order (quote or build page linked, `why` notes 'built to order'): **2**
- Replaced with a different supplier: **6**
- Removed (the category still has other suppliers): **7**
- Universal product page (no vehicle-specific pages exist): **2**
- Category-level fallback (no model page found anywhere): **1**
- Left unchanged: **4** (3 sites blocked by Cloudflare; 1 was already specific)

## Dead or wrong domains found

- `nitrogear.com` is a parked domain (`/lander`).
- `bits4vits.co.uk` is a parked 'for sale' domain.
- `icon4x4.com` is ICON 4x4 (the Jonathan Ward restomod company), not ICON Vehicle Dynamics. It was fixed on the 200-series and FJ Cruiser pages and kept on FJ40, where the restomod builder is the correct link.
- `frontrunneroutfitters.com` now redirects to dometic.com.
- `dobinsonsusa.com` redirects to `dobinsonusa.com`.
- **Not on my list, needs follow-up:** `https://www.oldmanemu.com/en-au` (in the 160-mq.json SUSPENSION LIFT `who`) is a parked domain whose sitemap is only `/lander`.
- **Not on my list:** these G-class mods have an empty `who`: `data/g-class.json` WHEELS & TIRES; `data/pages/g-class/4x4-squared.json` PORTAL CONVERSIONS and WHEELS & TIRES; and WHEELS & TIRES on europa, g55-amg, 500ge and g550.

## Per page

### `data/hummer.json`

- [LOCKERS] https://www.arbusa.com/ → **removed**: REMOVED. ARB lists no Air Locker for the H1 (no H1 product on arb.com.au or store.arbusa.com); Flash Off-Road entry remains.

### `data/lexus.json`

- [REAR AIR: COIL CONVERSION OR REPAIR] https://www.iconvehicledynamics.com/ → https://iconvehicledynamics.com/products/56110 ("ICON GX460/GX470 rear coil conversion kit"): tightened.
- [REAR AIR: COIL CONVERSION OR REPAIR] https://www.airliftcompany.com/ → **removed**: REMOVED. Air Lift's vehicle catalog covers GX460, LX450, LX470 but not the GX470; Metal Tech and ICON remain.
- [STEERING & FRONT END] https://cvjreman.com/ → https://cvjreman.com/product-category/lexus-truck-axles/gx470/ ("CVJ (reman GX470 CV axles)"): tightened.
- [RECOVERY] https://www.warn.com/ → https://www.metaltech4x4.com/products/metal-tech-2003-09-gx470-goblin-front-bumper-1 ("Metal Tech 4x4 GX470 Goblin front winch bumper"): REPLACED. Warn has no GX470 bumper or mount (its vehicle collections cover only 4Runner, Land Cruiser 250, Tacoma, Tundra among Toyota/Lexus).

### `data/nissan-patrol.json`

- [LOCKERS] https://www.arb.com.au/ → https://www.arb.com.au/product/rd214-arb-air-locker-34-spline-h260-nissan-patrol-rear-axle ("ARB Air Locker, Patrol H260 rear"): tightened.
- [SNORKEL & BREATHERS] https://www.safari4x4.com.au/ → https://safari4x4.com.au/vehicles/nissan/gq-patrol-y60 ("Safari 4x4 snorkels, GQ Patrol (Y60)"): tightened.

### `data/pages/land-cruiser/200-series.json`

- [SUSPENSION LIFT] https://www.icon4x4.com → https://iconvehicledynamics.com/products/k53071 ("ICON Vehicle Dynamics 2008+ Land Cruiser 1.5–3.5 in systems"): tightened. Old URL icon4x4.com is ICON 4x4 (the restomod builder), not ICON Vehicle Dynamics.
- [GEARS & LOCKERS] https://www.nitrogear.com → https://revolutiongear.com/revolution-gear-package-for-toyota-land-cruiser-2008-23-4-88-gear-package-t9-5-t9r/ ("Revolution Gear LC200 4.88 gear package"): REPLACED. nitrogear.com is a parked domain (sitemap = /lander) and nitro-gear.com refused connections. Revolution's package page is titled 2008-15.
- [GEARS & LOCKERS] https://www.harrop.com.au → https://www.harrop.com.au/elocker-toyota-landcruiser-200-tundra-front ("Harrop E-Locker, LC200 front"): tightened.
- [SNORKEL] https://safari4x4.com.au → https://safari4x4.com.au/vehicles/toyota/200-series-landcruiser ("Safari 4x4 snorkels, 200 Series"): tightened.

### `data/pages/land-cruiser/250-series.json`

- [SUSPENSION LIFT] https://www.dobinsonsusa.com → https://dobinsonusa.com/product/dobinsons-1-3-lift-kit-for-toyota-land-cruiser-250-series-2024-on/ ("Dobinsons LC250 1–3 in kit"): tightened. Dobinsons' US domain is dobinsonusa.com.
- [FUEL RANGE] https://longrangeamerica.com/ → https://sleeoffroad.com/products/fk-lc250-main-tank/ ("Slee Off-Road LC250 main tank upgrade (integrated skid)"): REPLACED. Long Range America lists no LC250 tank (only LC250 bumpers). Slee's tank is the one the why describes.

### `data/pages/land-cruiser/300-series.json`

- [PORTAL AXLES] https://74weld.com → https://74weld.com/products/new-gen-toyota-portal-axle ("74Weld New-Gen Toyota portal axles (LC300)"): tightened.

### `data/pages/land-cruiser/70-series.json`

- [SUSPENSION & GVM] https://www.superiorengineering.com.au → https://www.superiorengineering.com.au/toyota-79-series-landcruiser-coil-conversion-kit ("Superior Engineering — 79 Series coil conversion kit"): tightened. Site is behind a Cloudflare challenge for curl; verified with WebFetch (page loads, titled 'Toyota 79 Series Landcruiser Coil Conversion Kit').
- [LOCKERS] https://www.harrop.com.au → https://www.harrop.com.au/elocker-toyota-landcruiser-70-100-200-rear ("Harrop E-Locker, LandCruiser 70/100/200 rear"): tightened.
- [SEATS & SOUND DEADENING] https://www.blackduck.com.au → https://www.blackduck.com.au/popular-models/toyota-landcruiser-seat-covers/ ("Black Duck seat covers (70 Series)"): tightened.
- [SEATS & SOUND DEADENING] https://www.carbuilders.com.au → https://www.carbuilders.com.au/vehicle-packs/4x4/ ("Carbuilders pre-cut sound-deadening packs (76, 79, Troopy)"): tightened.
- [SNORKEL & INTAKE] https://safari4x4.com.au → https://safari4x4.com.au/vehicles/toyota/71-73-75-76-78-79-series-wide-front-landcruiser ("Safari 4x4 snorkels, 70 Series (wide front)"): tightened.

### `data/pages/land-cruiser/fj-cruiser.json`

- [SUSPENSION LIFT] https://www.icon4x4.com → https://iconvehicledynamics.com/products/k53058 ("ICON 2007–2009 FJ Cruiser 0–3.5 in systems"): tightened. Old URL icon4x4.com is ICON 4x4 (restomods), not ICON Vehicle Dynamics. Complements the existing 2010–14 Metal Tech link.
- [UPPER CONTROL ARMS] https://www.chaosfab.com/ → https://www.chaosfab.com/product/2010-2017-Toyota-FJ-Cruiser-Upper-Control-Arms ("Total Chaos 2010–2014 FJ Cruiser upper control arms"): tightened.
- [FRONT LOCKER & GEARS] https://www.harrop.com.au → https://www.harrop.com.au/elocker-toyota-front-391-up ("Harrop E-Locker, FJ Cruiser front (3.91 and up)"): tightened.
- [FRONT LOCKER & GEARS] https://www.nitrogear.com → https://revolutiongear.com/revolution-gear-package-for-toyota-fj-and-4runner-2010-4-56-4-88-ratio-w-factory-locker-t8-2-t8ifs-thick-front-3-73-down-carrier/ ("Revolution Gear FJ Cruiser gear package (factory locker, 4.56–4.88)"): REPLACED. nitrogear.com is a parked domain.

### `data/pages/land-cruiser/fj25.json`

- [F-ENGINE & SERVICE PARTS] https://sor.com/ → https://www.sor.com/cat/032 ("Specter Off-Road F-engine gasket sets (1958 on)"): tightened.
- [COOLING] https://www.coolcruisers.com/ → https://www.coolcruisers.com/radfj19thru1.html ("Cool Cruisers of Texas radiators (FJ40/45, 1958 on)"): tightened.
- [RESTORATION SPECIALISTS] https://www.coolcruisers.com/ → **removed**: REMOVED. Cool Cruisers has no FJ25 page (its catalog is FJ40/45/60). The FJ Company remains (it has an FJ25 restoration listing at https://www.fj.co/detail/1960-Land-Cruiser-FJ25_107, seen in search, not fetched or used).

### `data/pages/land-cruiser/fj40.json`

- [RESTORATION & OEM PARTS] https://www.coolcruisers.com/ → https://www.coolcruisers.com/bodyparts.html ("Cool Cruisers of Texas body parts (FJ40/45)"): tightened.
- [RESTORATION & OEM PARTS] https://jtoutfitters.com/ → https://jtoutfitters.com/collections/land-cruiser-40-series-parts ("JT Outfitters — 40 Series parts"): tightened.
- [BUILDS & RESTOMODS] https://www.icon4x4.com/ → https://www.icon4x4.com/fj ("ICON FJ"): tightened.
- [BUILDS & RESTOMODS] https://www.valleyhybrids.com/ → https://valleyhybrids.com/ ("Valley Hybrids (build wait list)"): built to order. No model pages; the homepage is the build-request / wait-list form. Why gets 'built to order'.

### `data/pages/land-cruiser/fj45-fj55.json`

- [RESTORATION PARTS] https://www.coolcruisers.com/ → https://www.coolcruisers.com/bodyparts.html ("Cool Cruisers of Texas body parts (FJ40/45)"): tightened.
- [RESTORATION PARTS] https://jtoutfitters.com/ → https://jtoutfitters.com/collections/land-cruiser-fj55-parts ("JT Outfitters — FJ55 parts"): tightened.

### `data/pages/land-cruiser/fj60.json`

- [OEM & RESTORATION PARTS] https://www.cruiserparts.net/ → https://shop.cruiserparts.net/index.php?main_page=index&cPath=4 ("CruiserParts LLC — 60 Series parts"): tightened.
- [RESTOMODS] https://www.corsetticruisers.com/ → https://www.corsetticruisers.com/toyota-land-cruiser-fj60 ("Corsetti Cruisers FJ60 restoration"): tightened.

### `data/pages/land-cruiser/fj62.json`

- [OEM & RESTORATION PARTS] https://www.cruiserparts.net/ → https://shop.cruiserparts.net/index.php?main_page=index&cPath=4 ("CruiserParts LLC — 60 Series parts"): tightened.
- [RESTOMODS] https://www.corsetticruisers.com/ → https://www.corsetticruisers.com/toyota-land-cruiser-fj62-ls3-conversion ("Corsetti Cruisers FJ62 LS3 conversion"): tightened.

### `data/pages/land-cruiser/prado-120.json`

- [SUSPENSION LIFT] https://dobinsonsusa.com/ → https://dobinsonusa.com/product/dobinsons-1-to-3-5-lift-kit-toyota-landcruiser-prado-120-4x4-2003-2009/ ("Dobinsons Prado 120 1–3.5 in kit"): tightened.

### `data/pages/land-cruiser/prado-150.json`

- [SUSPENSION] https://www.arb.com.au/ → https://www.arb.com.au/Vehicles/Toyota/landcruiser/prado/150-series ("ARB / Old Man Emu (Prado 150)"): tightened.
- [SUSPENSION] https://www.ironman4x4.com/ → https://www.ironman4x4.com.au/collections/toyota-prado-150-series-suspension ("Ironman 4x4 Prado 150 suspension kits"): tightened. ironman4x4.com is the US store (no Prado 150); the Australian store has it.
- [BULL BARS & RECOVERY] https://www.arb.com.au/ → https://www.arb.com.au/Vehicles/Toyota/landcruiser/prado/150-series/bull-bars ("ARB Prado 150 bull bars"): tightened.
- [BULL BARS & RECOVERY] https://www.ironman4x4.com/ → https://www.ironman4x4.com.au/pages/toyota-prado-150-bull-bars ("Ironman 4x4 Prado 150 bull bars (2017–24)"): tightened.
- [ROOF RACKS & TOURING] https://www.frontrunneroutfitters.com/ → https://www.dometic.com/en-au/product/toyota-prado-150-slii-roof-rack-kit ("Front Runner Slimline II roof rack, Prado 150 (Dometic)"): tightened. frontrunneroutfitters.com now redirects to dometic.com.
- [ROOF RACKS & TOURING] https://www.arb.com.au/ → https://www.arb.com.au/product/b00580-arb-base-rack-1835-x-1155mm-with-mount-kit-toyota-prado-150-series ("ARB Base Rack, Prado 150"): tightened.

### `data/pages/land-cruiser/prado-90.json`

- [SUSPENSION LIFT] https://www.ironman4x4.com/ → https://www.ironman4x4.com.au/products/suspension-lift-kit-for-toyota-prado-90-1996-2002-nitro-gas-medium ("Ironman 4x4 Prado 90 lift kit"): tightened.

### `data/pages/lexus/lx450.json`

- [LOCKERS] https://www.arbusa.com/ → https://store.arbusa.com/lc-80-lx450-1996-98 ("ARB Air Lockers, LC80/LX450 (ARB USA)"): tightened.

### `data/pages/lexus/lx470.json`

- [MAINTENANCE PARTS] https://www.cruiseroutfitters.com/ → https://cruiserteq.com/100-series-lx470/ ("Cruiser Teq (Cruiser Outfitters) — 100 Series / LX470"): tightened.

### `data/pages/lexus/lx570.json`

- [LOCKERS] https://www.arbusa.com/ → https://store.arbusa.com/buyers-guide/lc-200-2008-21/ ("ARB Air Lockers (LC200 platform, shared with LX 570)"): tightened. ARB USA has no LX570 page; its LC200 2008-21 buyer's guide lists RD151/RD152, the same axles.
- [RECOVERY] https://www.warn.com/ → https://dissentoffroad.com/products/lx570-low-profile-modular-front-bumper-all-years ("Dissent Off-Road LX570 modular winch bumper"): REPLACED. Warn has no LX570 bumper or winch mount.
- [RECOVERY] https://www.arbusa.com/ → **removed**: REMOVED. ARB has no LX570 bumper or recovery-point page; Dissent remains.

### `data/pages/nissan-patrol/160-mq.json`

- [SUSPENSION LIFT] https://www.terraintamer.com/ → https://www.ironman4x4.com.au/products/suspension-lift-kit-for-nissan-patrol-mk-g10-1984-nitro-gas-medium ("Ironman 4x4 lift kit, Patrol MK (1984 on)"): REPLACED. terraintamer.com is behind a Cloudflare challenge and search found no MQ/MK page.
- [DUAL BATTERY & CHARGING] https://www.redarc.com.au/ → https://www.redarcelectronics.com/au/smart-start-sbi-12v ("REDARC Smart Start SBI isolator"): universal product. REDARC has no MQ/MK page; this is the universal isolator the why describes.

### `data/pages/nissan-patrol/patrol-60.json`

- [SUSPENSION] https://www.alcanspring.com/ → https://www.alcanspring.com/pages/request-a-quote ("Alcan Spring custom leaf packs (request a quote)"): built to order.
- [FREE-WHEELING HUBS] https://www.warn.com/ → https://www.warn.com/collections/hubs ("Warn locking hubs"): category fallback. Warn has no current Patrol 60 fitment, and no other supplier with a verified Patrol 60 hub page was found. Linked to Warn's hubs category so the section is not left empty. Needs a better source.
- [RUST PROOFING] https://www.rustbullet.com/ → https://www.rustbullet.com/products/rust-inhibitors/automotive-rust-inhibitors/automotive/ ("Rust Bullet Automotive"): universal product. Universal coating, no vehicle pages.

### `data/pages/nissan-patrol/y61.json`

- [SUSPENSION LIFT] https://www.dobinsonsusa.com/ → https://dobinsonusa.com/product/dobinsons-castor-plate-kit-for-nissan-patrol-gq-gu-y60-y61-5-degrees-caster-correction-wa45-513k/ ("Dobinsons caster correction plates, GQ/GU"): tightened. Dobinsons US lists no GU lift kit; the caster plates match the why's caster-correction note.
- [SUSPENSION LIFT] https://www.ironman4x4.com/ → https://www.ironman4x4.com.au/products/suspension-lift-kit-for-nissan-patrol-y61-gu-lwb-wagon-nitro-gas-medium ("Ironman 4x4 Patrol Y61 GU lift kit"): tightened.
- [BARS, ARMOUR & TOURING GEAR] https://www.arb.com.au/ → https://www.arb.com.au/product/3417300-arb-deluxe-bull-bar-winch-compatible-nissan-patrol-gu ("ARB Deluxe bull bar, Patrol GU"): tightened.
- [BARS, ARMOUR & TOURING GEAR] https://www.ironman4x4.com/ → https://www.ironman4x4.com.au/products/nissan-gu-patrol-bull-bar-deluxe ("Ironman 4x4 Deluxe bull bar, Patrol GU"): tightened.

### `data/pages/nissan-patrol/y62.json`

- [BREATHERS & ELECTRICS] https://www.redarc.com.au/ → **removed**: REMOVED. REDARC has no Y62 page (its only Patrol pages are GU BCDC brackets); the two Patrolapart Y62 entries remain.

### `data/pages/suzuki/jimny-jb23.json`

- [KINGPINS & AXLE REBUILD] https://www.bits4vits.co.uk/ → **removed**: REMOVED. bits4vits.co.uk is now a parked 'domain may be for sale' page; the BigJimny store remains.
- [GEARING] https://www.lowrangeoffroad.com/ → unchanged: unchanged. Site blocks curl and WebFetch (Cloudflare). Search shows a Jimny transfer-case page, https://www.lowrangeoffroad.com/suzuki-off-road-parts/1998-present-suzuki-jimny/jimny-transfer-case.html, but it could not be fetched, so it was not used.
- [LIFT & BUSHES] https://www.bits4vits.co.uk/ → **removed**: REMOVED. bits4vits.co.uk is now a parked domain; the BigJimny store remains.

### `data/pages/suzuki/jimny-jb74.json`

- [GVM UPGRADE] https://www.ironman4x4.com → https://www.ironman4x4.com.au/products/gvm-upgrade-for-suzuki-jimny-jb74-post-reg-nitro-gas-permanent-load ("Ironman 4x4 GVM upgrade, Jimny JB74"): tightened.
- [BODY KITS] https://www.damd.co.jp/ → https://www.damd.co.jp/products/suzuki/jimny_sierra_little-g ("DAMD Jimny Sierra 'little G.'"): tightened.

### `data/pages/suzuki/lj-series.json`

- [SOFT TOP] https://www.lj80.de/?cat=c75_Verdeck-Verdeck.html → unchanged: unchanged. Already an LJ80 soft-top category; verified HTTP 200 and it lists LJ80 tops.

### `data/pages/trooper/trooper-2.json`

- [SUSPENSION LIFT] https://www.independent4x.com/ → unchanged: unchanged. Site blocks curl and WebFetch (Cloudflare). Search shows https://www.independent4x.com/shop/isuzu-store/isuzu-suspension-systems/isuzu-trooper/isuzu-trooper-premium-lift-kit-1992-2004-coil-spring/, but it could not be fetched, so it was not used.

### `data/pajero.json`

- [SUSPENSION LIFT] https://www.oldmanemu.com.au/ → https://www.arb.com.au/product/eknp00636-old-man-emu-nitrocharger-plus-kit-pajero-torsion-bar-rear-coil ("Old Man Emu Nitrocharger Plus kit, Pajero (torsion bar / rear coil)"): tightened. oldmanemu.com.au redirects to arb.com.au. The kit page lists the OME front shock for 'Pajero NH-NL'.

### `data/trooper.json`

- [SUSPENSION & BUILD PARTS] https://www.independent4x.com/ → unchanged: unchanged. Site blocks curl and WebFetch. Search shows https://independent4x.com/shop/isuzu-store/isuzu-suspension-systems/isuzu-suspension-system-1987-1997-leaf-spring, but it could not be fetched, so it was not used.
- [COMMUNITY TECH] https://www.planetisuzoo.com/ → https://www.planetisuzoo.com/tags/trooper/ ("Planet Isuzoo — Trooper threads"): tightened. The forum has no Trooper subforum; the 'trooper' tag page lists Trooper threads (first-gen years included).
