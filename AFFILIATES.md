# Affiliate plan — BoxyTrucks

## How it works on the site
- `data/affiliates.json` lists every commercial domain the site links to. Paste a program's deep-link template into `template` once approved, run `python3 build.py`, and every link to that domain is rewritten automatically — on repairs, service tables, mods and the Mods & Builders page — and marked `rel="sponsored nofollow"`.
- Template placeholders: `{url}` (URL-encoded destination, for networks like AvantLink/Impact/CJ) or `{raw}`; parameter-style programs (Amazon) use `"params": {"tag": "…"}` instead, which appends safely to URLs that already have a query string.
- When any program is active, repair sections show an "affiliate links" note, and the footer links to `/about/affiliate-disclosure.html` (FTC disclosure).

## Where the money is (outbound links per domain, current build)
| Rank | Supplier | Links | Program |
|---|---|---|---|
| 1 | Cruiser Corps | 241 | Ask |
| 2 | Lucky8 (Land Rover) | 179 | Ask |
| 3 | FCP Euro (Mercedes, Land Rover, BMW-engine Grenadier) | 176 | Ask |
| 4 | CruiserTeq | 160 | Ask |
| 5 | Expedition Imports (G-Class) | 137 | Ask |
| 6 | LC Engineering (Toyota) | 116 | Ask |
| 7 | RockAuto | 102 | No public program |
| 8 | Rovers North | 94 | Ask |
| 9 | LR Direct | 88 | Ask |
| 10 | Slee Off-Road | 83 | Ask |
| — | ARB / Old Man Emu | 20+ | **Verified: AvantLink, 3–5%, 30-day cookie** |
| — | Tire Rack | (to add) | **Verified: 6% commission** |
| ✅ | Amazon Associates | `boxytrucks-20` (live 2026-10-22) | Every service item gets an Amazon search link; footer + disclosure carry the required Associates statement |
| — | eBay Partner Network | (to add) | Verified, standard program |

## Placements
1. **Repair "Where to buy parts" links** — highest intent: someone mid-repair buying the exact part.
2. **"After you buy it" service tables** — fluids, filters, plugs: recurring, high-volume purchases.
3. **Mods & Builders + model "Common modifications"** — suspension, armor, racks: high ticket (ARB/OME, Slee, Metal Tech, Front Runner).
4. **"Biggest tire without a lift" answers** — add a Tire Rack link to the recommended size on every model (to build once Tire Rack approves).
5. **Tools named in repairs** (torque wrench, counter-hold tools, vacuum pumps) — Amazon links.
6. **Featured builds / Show Us Your Rig** — link the parts list of each featured rig.
7. **Not affiliate:** AutoTempest, Bring a Trailer, forums, YouTube, Instagram.

## Next steps
1. Apply: ARB (AvantLink), Tire Rack, eBay Partner Network (Amazon is done). Join AvantLink, Impact and ShareASale/Awin as a publisher — many parts brands live there; search each network for the "Ask" suppliers.
2. Email the top "Ask" suppliers (Cruiser Corps, Lucky8, FCP Euro, CruiserTeq, Expedition Imports, Slee, Rovers North) — small specialists often run in-house programs or will set one up for a site sending them traffic.
3. Paste templates into `data/affiliates.json` and push.

## CJ status, Oct 30, 2026
- Approved: Eastwood (live site-wide).
- Pending: The Tire Rack, CJ Pony Parts, PartsGeek, FinditParts, Valvoline Instant Oil Change, CanvasCamp.
- Declined: Discount Tire, PriorityTire, TOPOAK Overland. Normal for a site under 2 weeks old; reapply once Search Console shows steady traffic (target: 1,000+ clicks/month).
- AvantLink (ARB): not checked; Claude's browser can't open avantlink.com.
