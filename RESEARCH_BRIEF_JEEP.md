# Brief: Jeep family (CJ through JL)

We're adding a **Jeep** family to BoxyTrucks.com. Repo: `/home/claude/boxytrucks`. This brief overrides any file paths in the older briefs, because everything now lives in the repo and not in the scratchpad.

Before writing anything, read these four files in the repo:
1. `RESEARCH_BRIEF.md`: voice, hard rules (never invent facts, URLs or handles), and the full `family` and `page` JSON schema with content targets: story, engineering, buying checks, 6–8 repairs, about 10 FAQs including "biggest tire without a lift", mods, forums, searches, plate, sources.
2. `RESEARCH_BRIEF_PARTS_SERVICE.md`: every repair gets `parts` links, and every page gets `baseline_service` (the "After you buy it" section). For Jeep, the suppliers are **Quadratec**, **ExtremeTerrain**, **Morris 4x4 Center**, **4 Wheel Parts**, **Omix-ADA** (vintage and CJ), **Crown Automotive** (Mopar replacement), **RockAuto**, and **Mopar** OEM dealer parts sites. **Never use olathetoyotaparts.com.**
3. `RESEARCH_BRIEF_PHOTOS.md`: photos of the **exact generation**, off-road first, with credited licences you can use. Include `hero_focus`. Images go in `site/img/jeep/`, named with a prefix for the model, e.g. `tj-…jpg`.
4. Read one finished page for tone and depth, e.g. `data/pages/land-cruiser/100-series.json`, and `data/g-class.json` → `page`.

## The family (slug `jeep`, maker `Jeep`, name `Jeep`)
Generation slugs (use exactly these):
| slug | name | years | notes |
|---|---|---|---|
| cj-5 | CJ-5 | 1955–1983 | |
| cj-7 | CJ-7 | 1976–1986 | **flagship page** |
| cj-8 | CJ-8 Scrambler | 1981–1986 | |
| yj | Wrangler YJ | 1987–1995 | square headlights, leaf springs |
| tj | Wrangler TJ | 1997–2006 | coil springs, short wheelbase |
| tj-unlimited | Wrangler Unlimited (LJ) | 2004–2006 | long-wheelbase TJ, its own page |
| jk | Wrangler JK (2-door) | 2007–2018 | |
| jk-unlimited | Wrangler JK Unlimited (4-door) | 2007–2018 | its own page |
| jl | Wrangler JL (2-door) | 2018–present | include the 2024 refresh |
| jl-unlimited | Wrangler JL Unlimited (4-door) | 2018–present | include 4xe and 392 |
| grand-wagoneer | Grand Wagoneer (SJ) | 1984–1991 | added later; 1963–83 Wagoneer as background |
| cherokee-xj | Cherokee XJ | 1984–2001 | added later |

Willys and CJ-2A/3A/3B are left out on purpose. Mention them in the CJ-5 story as history only. The Gladiator JT can be mentioned in related or story text, but it gets no page.

Cross-link other models with `[[jeep/<slug>|text]]`, or to other families (`[[land-cruiser/fj40|FJ40]]`, `[[land-rover/defender-90-110|Defender]]` and so on) where it's natural. The CJ-5 vs FJ40 vs Series rivalry is a good one.

## Files
- Flagship agent only: write `data/jeep.json` as `{"family": {...}, "page": {...CJ-7...}}`. The `family.generations` list must contain all 12 slugs above, in chronological order, each with `has_page: true`, a verified `at_url` (AutoTempest; confirm the make/model slugs by curling and checking the `<title>`) and a `bat_url` (the BaT model page if one exists, e.g. find it under `https://bringatrailer.com/jeep/`), plus `forums`, `related_families` (e.g. `["land-cruiser","land-rover","4runner"]`) and `hero_photo`. Also write `data/resources/jeep.json` using the resources schema in `RESEARCH_BRIEF_PHASE2.md` §5.
- Every other agent writes only its own `data/pages/jeep/<slug>.json`, containing the `page` object only. Create the folder if it's missing.
- Use `json.dump(..., ensure_ascii=False, indent=1)`. Don't run `build.py`. Don't edit any other family's files, `build.py` or the templates.

## Budget
Search is shared with other agents. Prefer WebFetch on known-good sources over extra searches: Wikipedia, JeepForum, WranglerForum, JKOwners, JLWranglerForums, Quadratec's "Jeep 101" and buyer guides, ExtremeTerrain guides, Hagerty, Morris 4x4 tech articles, and factory owner's manuals for fluids and capacities. Commons rate-limits, so wait 3 seconds between image downloads.

## Report back
For each page: number of FAQs, repairs (with parts), baseline items, photos and social entries, plus anything you couldn't verify.
