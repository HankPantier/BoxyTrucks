# Deepen report: group spec-d (Task A, spec hunt)

All five pages were SPEC only. I didn't add or remove any repairs, FAQs or service items, so those counts haven't changed. The detail files (`data/extra/...`) had no markers and no figures that clash with the changes, so I left them alone.

| Page | Markers | Repairs | FAQs | Service items | Sources |
|---|---|---|---|---|---|
| `pajero/pajero-gen1` (`data/pages/pajero/pajero-gen1.json`) | 6 → 4 | 6 → 6 | 10 → 10 | 14 → 14 | 31 → 33 |
| `pajero/pajero-gen2` (`data/pajero.json` → `page`) | 5 → 3 | 6 → 6 | 11 → 11 | 14 → 14 | 49 → 52 |
| `trooper/trooper-1` (`data/trooper.json` → `page`) | 10 → 8 | 7 → 7 | 11 → 11 | 13 → 13 | 20 → 23 |
| `trooper/trooper-2` (`data/pages/trooper/trooper-2.json`) | 7 → 2 | 8 → 8 | 11 → 11 | 13 → 13 | 34 → 38 |
| `hummer/h1` (`data/hummer.json` → `page`) | 4 → 2 | 8 → 8 | 11 → 11 | 14 → 14 | 38 → 40 |

Several Trooper 1 markers were confirmed in part: the type and capacity are now sourced, and a narrower marker stays on the viscosity or the US-specific figure. That's why its count falls only from 10 to 8.

## Sources used, and what was tried
- **Liqui Moly oil guide (Olyslager data).** This is the fluid maker's lookup tool and the main source for this group. The JS widget on liqui-moly.com is backed by plain HTML recommendation pages on `openapi.liqui-moly.com`, and those are what the new `sources` entries link to. They return 200 with the BoxyTrucks User-Agent. The tool gives capacities and change intervals. For fluid *types* it lists Liqui Moly products rather than naming OEM specs, so where the page now gives a type I've worded it as the product class (for example "Dexron-III-type ATF (Liqui Moly lists its ATF III)").
- **Flash Off-Road** (`Maintenance/Brakes/Brakes.html`, which was already cited) for the H1 brake fluid.
- **Didn't work:**
  - AMSOIL returns a Cloudflare 403 to curl, and WebFetch refuses it (not on the allowlist).
  - Honda's techinfo owner-manual PDFs fail TLS through the proxy, and I found no SLX manual code.
  - Mitsubishi US and Isuzu don't host owner's manuals for these years.
  - The 1999 H1 brochure has no capacities.
  - The Army HMMWV TM that Flash Off-Road hosts covers the engine only.
  - Castrol, Mobil, Valvoline and Fuchs finder URLs all returned 404.
- No archive.org or user-uploaded manual scans were used or linked.

## Confirmed specs

### Pajero gen 1
- **Engine oil interval:** Mitsubishi's European schedule is 10,000 km or 6 months, or 5,000 km in severe use. Liqui Moly's EU 2.6 4WD and 3.0 V6 1989–91 entries both give this. The US schedule wasn't found, so a narrower `US schedule [CONFIRM IN MANUAL]` stays.
- **Automatic transmission:** Dexron-III-type ATF (ATF III listed), 7.2 L, from Liqui Moly's EU 2.6 and V6 automatic entries. AMSOIL has no data for the US auto, and the page says so.
- **Brake fluid interval:** every 2 years or 30,000 km (Liqui Moly, EU schedule). This matches the page's existing "every 2 years".
- I changed the baseline intro to say these figures come from Liqui Moly's European data.

### Pajero gen 2
- **Engine oil interval:** 7,500 mi or 12 months, or 3,000 mi or 3 months in severe use. This is from Liqui Moly's US Montero 3.5 (1992–2000) entry. Its EU schedule for the 3.0 and 3.5 is 15,000 km or 12 months, and the page shows both.
- **Brake fluid interval:** every 2 years or 30,000 km (Liqui Moly, EU 3.0/3.5). The US entry gives only a yearly check, and the page notes that.
- **Cross-check:** Liqui Moly's 3.5 figures match the AMSOIL figures already on the page: front diff 1.2 L (2.5 pt), rear 3.2 L (6.8 pt), transfer 2.5 L (5.3 pt). I mentioned this in the intro.

### Trooper 1 (Liqui Moly's "Isuzu" entries use European data; the page labels them that way)
- **Engine oil capacity:** 4.2 L + 0.5 L filter (1988–90 2.6) and 4.9 L + 0.5 L (1990–92 2.6). The grade stays `[CONFIRM IN MANUAL]`.
- **Coolant:** 9.8 L for the 2.3 and 2.6. The type stays `[CONFIRM IN MANUAL]`.
- **Manual gearbox:** Liqui Moly lists **engine oil**, not gear oil. It gives 2.95 L for the 2.6, and 4.6 L for gearbox and transfer case together on the 2.3. Viscosity stays marked.
- **Transfer case:** engine oil, 1.45 L (2.6). Viscosity stays marked.
- **Automatic:** Dexron-III-type ATF, 4.5 L (1990–92 2.6). This replaces the markers in both the baseline item and the "Automatic transmission service" repair tools.
- **Differentials:** GL-5 hypoid oil, with LSD-rated oil for a limited-slip rear. The 2.6 takes 1.5 L front and 1.8 L rear; the 2.3 takes 1.0 L front and 1.5 L rear. Viscosity stays marked.
- I rewrote the intro to say the figures are Liqui Moly's European-data figures.

### Trooper 2
- **4L30-E:** Dexron-III-type ATF. This is in both the baseline item and the "Service the 4L30-E" repair tools. The **capacities disagree**: 8.6 L in Liqui Moly's US Acura SLX entries, 5.5 L in its European Trooper entries. Both are shown, with a "measure what you drain" note.
- **Transfer case:** the 3.2 SLX (part-time/shift-on-the-fly) takes 5W-30 engine oil, 1.45 L. The 1998–99 SLX 3.5 (Torque On Demand) takes 75W-90-type gear oil, 1.9 L. The **EU Trooper 3.5 entry disagrees**: engine oil, 1.45 L. That's flagged on the page.
- **Differentials:** GL-5 hypoid (75W-90 to 85W-90 listed), front 1.4 L (SLX) to 1.5 L (Isuzu), rear 1.8 L (both). A limited-slip rear takes LS oil, which answers the "additive" question.
- **Power steering:** Dexron-III-type ATF.
- I changed the intro to say Acura's figures cover engine oil and coolant, and Liqui Moly covers the rest.
- **Caution:** Liqui Moly's SLX coolant figure (7.1 L) contradicts Acura's own specs (10.4 L for the 3.5, 8.8 L for the 3.2), so I didn't use it. The page keeps Acura's figures.

### H1
- **Brake fluid:** DOT 5 silicone on 1992–98 trucks and DOT 3 on 1999-on ABS trucks, from Flash Off-Road's "Brakes on a Hummer". I added a "never mix them" note and updated the brake-pad repair's tools. This rests on one specialist source; I couldn't find a second H1-specific one.
- **Differential capacity:** 1.9 L (2.0 US qt) per axle, from Liqui Moly's H1 6.5D and 6.5TD entries. The same entries give 0.5 L per geared hub, which backs up the page's existing "about 1/2 qt per hub".
- **Coolant capacity:** 25 L (≈26 US qt) on the 6.5 diesels (Liqui Moly). The type stays marked.

## Still open (markers left as they were)
- **Pajero gen 1:**
  - US engine-oil schedule.
  - Timing drive interval (4G54 chains, 4D56 belt).
  - Ignition spec (plugs and gap).
  - Fuel filter spec.
- **Pajero gen 2:**
  - V6 timing-belt interval.
  - Spark plug type.
  - Air and fuel filter spec.
- **Trooper 1:**
  - Engine-oil grade.
  - Coolant type (in the baseline item and in the cooling repair's tools).
  - Gearbox, transfer-case and diff viscosities.
  - Timing-belt interval.
  - Wheel-nut torque (stud repair).
- **Trooper 2:**
  - 6VD1/6VE1 timing-belt interval.
  - Intake plenum torque sequence.
- **H1:**
  - Coolant type. One lead: a "HUMMER Cooling Thread" PDF hosted by Flash Off-Road (`/Diesel/Cooling_6.5diesel.pdf`) says "The Hummer calls for Dexcool coolant". It's a compiled forum post with no years or author, so I didn't use it.
  - Alpha Allison 1000 fluid. Liqui Moly lists only its Top Tec ATF 1800 products for the Alpha's Allison and names no OEM spec, so I left the marker.

Most of what's left (belt intervals, plug part numbers, torques, US maintenance schedules) needs the actual owner's or service manual. Hank may want to buy the Helm/Faxon manuals or scan owner's manuals he can get hold of.

## Notes
- No changes outside the five assigned page objects. On the flagship files, I checked that every key other than `page` is unchanged.
- Files were written with `json.dump(..., ensure_ascii=False, indent=1)`. I didn't run `build.py` or git.
