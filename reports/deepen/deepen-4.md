# deepen-4 report

**Task B (repairs):**
- `pajero/pajero-gen1`
- `pajero/pajero-gen2` (flagship, `data/pajero.json` → `page`)
- `suzuki/lj-series`
- `suzuki/jimny-jb74`
- `land-cruiser/mega-cruiser`

**Mods:**
- `pajero/pajero-gen1` and `pajero/pajero-gen2`
- `trooper/trooper-1` (flagship) and `trooper/trooper-2`
- `nissan-patrol/patrol-60`
- `lexus/lx600` and `lexus/gx550`
- `range-rover/l460`
- `g-class/second-gen`

## Before → after

| Page | Markers | Repairs | FAQs | Buying checks | Service items | Mods |
|---|---|---|---|---|---|---|
| pajero/pajero-gen1 | 4 → 4 | 6 → 8 | 10 → 10 | 8 → 8 | 14 → 14 | 3 → 6 |
| pajero/pajero-gen2 | 3 → 3 | 6 → 8 | 11 → 11 | 8 → 8 | 14 → 14 | 3 → 5 |
| suzuki/lj-series | 5 → 5 | 6 → **7** | 10 → 10 | 7 → 7 | 11 → 11 | 5 → 5 |
| suzuki/jimny-jb74 | 0 → 0 | 6 → **7** | 11 → 11 | 8 → 8 | 12 → 12 | 6 → 6 |
| land-cruiser/mega-cruiser | 10 → 10 | 5 → **7** | 10 → 10 | 7 → 7 | 12 → 12 | 0 → 0 |
| trooper/trooper-1 | — | 7 | — | — | — | 4 → 5 |
| trooper/trooper-2 | — | 8 | — | — | — | 4 → 5 |
| nissan-patrol/patrol-60 | — | 7 | — | — | — | 4 → 5 |
| lexus/lx600 | — | 8 | — | — | — | 4 → 5 |
| lexus/gx550 | — | 8 | — | — | — | 4 → 7 |
| range-rover/l460 | — | 8 | — | — | — | 4 → 5 |
| g-class/second-gen | — | 8 | — | — | — | 4 → 5 (and the empty WHEELS & TIRES now has suppliers) |

- FAQs, buying checks and baseline service were already in range on every Task B page, so they weren't padded.
- Markers weren't part of this task and weren't touched.
- No detail files needed changes: they hold no repairs or mods, and nothing new contradicts their fitment or recall data.

## New repairs (all have `parts`)

**Pajero gen 1**
- **Oil leaks: valve covers, intake gasket and oil-pressure sender.**
  - Bring a Trailer listings: a 1989 Raider V6 (valve cover gaskets, sender, front timing-cover and pan seals), a 1990 Montero 3.0 (valve cover and intake gaskets) and a 1988 Montero Sport (oil leak).
  - NHTSA recall 84V098 (1984 sender leak).
  - Parts: RockAuto engine catalogs (3.0 and 2.6).
- **Rust repair: windshield frame, roof and floors.**
  - BaT: the 1989 Raider (corrosion on the hood, windshield surround and roof) and the 1988 Montero Sport (corrosion, failing clearcoat).
  - Parts: Eastwood weld-through primer and frame-coating searches, RockAuto body catalog.

**Pajero gen 2**
- **V6 valve stem seals.**
  - ExplorOz threads 54167 ("normally need replacing at 200000ks") and 44769 ("a lot of smoke or expensive repair").
  - Parts: RockAuto 1995 3.0 and 3.5 engine catalogs.
- **Sill and chassis rust repair.**
  - Steven Taylor's Mk2 video and BaT's 1998 Montero.
  - Parts: Eastwood and RockAuto.
  - Both sources were already cited on the page.

**LJ series**
- **Chassis rust: inspect, treat and wax the frame.**
  - Classic Trader's LJ 80 guide: rust is "a defining drawback… especially affecting the steel body panels and chassis".
  - Parts: LJ80.de Berner underbody wax, zinc spray, Rostlöser penetrant, and frame bolt 01500-1030A / 01500-08307 (part number from LJ80.de's listing).

**Jimny JB74**
- **Rust-proof the chassis and body cavities.**
  - BigJimny Wiki "Rust protection" and "Common problems": "particularly poor rust prevention" on all generations, with the usual spots listed. The article is categorised gen4.
  - Parts: Bilt Hamber Dynax-S50, Dynax-UB and Hydrate-80.

**Mega Cruiser**
- **Inboard disc brake service.**
  - BaT: every truck has four-wheel inboard ventilated discs; listing -3 had its brakes serviced.
  - Parts are genuine Toyota numbers from Nengun's BXD20V brake catalog:
    - front pad kit 04465-65010 ($84.27) and front disc 43512-65010 ($86.73)
    - rear pad kit 04466-65010 ($80.18) and rear disc 42431-65010 ($86.73)
- **Underbody rust treatment.**
  - BaT listings -2, -4/-4-2, -5 and 1997 -2 note underside rust, an underbody painted over rust, and rust repair before a repaint.
  - Parts: Bilt Hamber.

## Where I stopped short (not enough real material)
- **LJ series (7).** Documented LJ faults beyond rust are thin. Classic Trader says the mechanicals are "generally robust", and LJ80.de being a parts catalogue isn't evidence of a common failure. I didn't add kingpin, steering-box or cooling jobs on that basis alone.
- **Jimny JB74 (7).** The other documented items are dealer-only recalls with no owner parts:
  - fuel-pump impeller swelling (two EU campaigns)
  - door-harness lead wires (2018–20)

  I left those to the existing buying check.
- **Mega Cruiser (7).** The other BaT-documented items had no supplier I could verify with Mega Cruiser fitment:
  - inoperative four-wheel steering or central tire inflation
  - a missing deflator hose
  - a left-rear axle boot
  - shocks, lower arms and sway-bar bushings

  Also, the five original repairs still have `parts: []`. I didn't change them.

## New mods (every supplier's page checked for fitment)

**Pajero gen 1**
- LOCKERS: ARB RD210. The SEMA fitment on store.arbusa.com lists 1983–89 Montero 2.6 and 1989–93 3.0.
- SNORKEL: Safari SS20HF, for the NA 2.5 diesel. The note says it's diesel-only.
- WHEELS & TIRES: ThreePiece 1989 Montero (6 x 139.7, 107 mm bore, 15 x 7).

**Pajero gen 2**
- LOCKERS:
  - ARB RD110 front: 1991–97 Monteros, with ARB's note that it "will not fit Pajero/Montero 3000cc automatic".
  - ARB RD210 rear: 1992–96.
- WHEELS & TIRES: Limitless Tire 1998 and ThreePiece 1995.

**Trooper 1 and 2**
- LOCKERS: ARB RD203, the 17-spline Isuzu IFS front. The SEMA fitment lists 1988–91 (gen 1) and 1992–2002 (gen 2).

**Patrol 60**
- LEAF SPRING BUSHINGS: Whiteline's Patrol G60/G61 page (W71294, W71101 and shock bushings).

**LX 600**
- REAR SWING-OUTS & SPARE CARRIERS: Dissent's LX600 & LX700h Dual Swing-Out Rear Bumper. Dissent sells it for installation at its shop only, and the entry says so.

**GX 550**
- LIGHTING: Lazer Lamps GX550 grille kit, and Rago GX 550 A-pillar light mounts.
- STORAGE & MOLLE: C4 Fabrication GX 550 rear-window MOLLE panels and shelf.
- RECOVERY POINTS: Cali Raised's 2024+ GX 550 front recovery points, rated at 11,000 lb.

**L460**
- ROOF RACKS: LR Parts genuine cross bars VPLKR0188 and brackets VPLKR0195. Both are listed under "Range Rover L460 2022-", rated at a 100 kg max carrying capacity.

**G-Class second gen**
- ARMOR, SKIDS & SLIDERS: Eurowise's W463A rear bumper, W463A/W464 skid plates and W463A HD rock sliders.
- The empty WHEELS & TIRES list now has Limitless Tire 2020 G-Class (5 x 130, 84.1 mm) and Eurowise's W463A spare-tire mount.

## Notes for the coordinator
- **goosegear.com is now a gambling spam site.** Don't use it for drawers. No page in `data/` links it today.
- **Weak existing mods.** Several existing entries point to generic homepages with no model fitment. I left them because they were outside the scope:
  - Front Runner (G-Class)
  - Warn, Alcan Spring and Rust Bullet (Patrol 60)
  - Independent4x (Trooper)
- **Front Runner fitment couldn't be verified.** Its product URLs return 404 to non-browser requests, so I used none.
- **Low-confidence checks.**
  - The Cali Raised recovery-point listing names the GX 550 in its title, but its description only mentions Tacoma, 4Runner and LC250.
  - Nengun prices are as of October 2026.
- **URL checks.** Every new mod and part URL returned 200 except nengun.com. That one returns a Cloudflare 403 to curl, but its content was confirmed with WebFetch, which found the BXD20V part numbers and prices.
