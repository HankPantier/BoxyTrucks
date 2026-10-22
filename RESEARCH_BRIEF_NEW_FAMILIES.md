# Brief: new families — Nissan Patrol and International Scout

We're adding two new families,  **Nissan Patrol** and **International Scout**, to BoxyTrucks.com. Repo: `/home/claude/boxytrucks`. This brief overrides any file paths in the older briefs, because everything now lives in the repo and not in the scratchpad.

Before writing anything, read these four files in the repo:
1. `RESEARCH_BRIEF.md`: voice, hard rules (never invent facts, URLs or handles), and the full `family` and `page` JSON schema with content targets: story, engineering, buying checks, 6–8 repairs, about 10 FAQs including "biggest tire without a lift", mods, forums, searches, plate, sources.
2. `RESEARCH_BRIEF_PARTS_SERVICE.md`: every repair gets `parts` links, and every page gets `baseline_service` (the "After you buy it" section). Suppliers for **Patrol**: Nissan OEM parts dealers, RockAuto, Partsouq/Amayama (OEM part-number catalogues), Terrain Tamer, ARB/OME, Dobinsons, and specialist Patrol shops. For **Scout**: Scout Connection, Super Scout Specialists, IH Parts America, Binder Planet's vendor list, Anything Scout, and RockAuto where it applies. **Never use olathetoyotaparts.com.**
3. `RESEARCH_BRIEF_PHOTOS.md`: photos of the **exact generation**, off-road first, with credited licences you can use. Include `hero_focus`. Images go in `site/img/<family-slug>/`, named with a prefix for the model.
4. Read one finished page for tone and depth, e.g. `data/pages/land-cruiser/100-series.json`, and `data/g-class.json` → `page`.

## The families
**Nissan Patrol**: slug `nissan-patrol`, maker `Nissan`, name `Patrol`.
| slug | name | years | notes |
|---|---|---|---|
| y60 | Patrol Y60 (GQ) | 1987–1997 | **flagship page**; coil-sprung solid axles; TB42, RD28, TD42; sold in Australia as the Ford Maverick |
| y61 | Patrol Y61 (GU) | 1997–2016 (later in some markets) | ZD30 problems, TB48, TD42T, ute/cab-chassis |
Mention the earlier 60/160/MQ/MK and the later Y62/Armada in the family intro and story only; they get no pages.

**International Scout**: slug `scout`, maker `International`, name `Scout`.
| slug | name | years | notes |
|---|---|---|---|
| scout-80-800 | Scout 80 / 800 | 1961–1971 | 80, 800, 800A, 800B |
| scout-ii | Scout II | 1971–1980 | **flagship page**; Traveler, Terra, SSII, Dana 44s, IH 345/304 V8s, Nissan SD33 diesel |
| scout-motors | Scout Motors (new) | announced 2024 | the VW-backed revival: Traveler SUV and Terra pickup. **Only include facts confirmed by official announcements or reputable press, with dates.** No repairs, service or buying checks (empty lists are fine). Story, engineering as announced, FAQ about timing, price and EREV/BEV, and photos only if usable-licence images exist. |

Cross-link with `[[<family>/<slug>|text]]` to other models (e.g. `[[land-cruiser/80-series|80 Series]]`, `[[jeep/cj-5|CJ-5]]`, `[[land-rover/defender-90-110|Defender]]`) where it's natural. The families are `4runner`, `g-class`, `grenadier`, `jeep`, `land-cruiser`, `land-rover`, `lexus`, `range-rover`, `nissan-patrol` and `scout`.

## Files
- Flagship agent of each family only: write `data/<family-slug>.json` as `{"family": {...}, "page": {...flagship...}}`. The `family.generations` list must contain all of that family's slugs above, in chronological order, each with `has_page: true`, a verified `at_url` (AutoTempest; confirm the make/model slugs by curling and checking the `<title>`) and a `bat_url` (the BaT model page if one exists, look under `https://bringatrailer.com/nissan/` or `https://bringatrailer.com/international-harvester/`), plus `forums`, `related_families` and `hero_photo`. Also write `data/resources/<family-slug>.json` using the resources schema in `RESEARCH_BRIEF_PHASE2.md` §5.
- Every other agent writes only its own `data/pages/<family-slug>/<slug>.json`, containing the `page` object only. Create the folder if it's missing.
- Use `json.dump(..., ensure_ascii=False, indent=1)`. Don't run `build.py`. Don't edit any other family's files, `build.py` or the templates.

## Budget
Search is shared with other agents. Prefer WebFetch on known-good sources over extra searches: Wikipedia, Patrol4x4.com, PatrolNation, Binder Planet (IH Scout), Hagerty, BaT model pages, and factory owner's manuals for fluids and capacities. Commons rate-limits, so wait 3 seconds between image downloads.

## Report back
For each page: number of FAQs, repairs (with parts), baseline items, photos and social entries, plus anything you couldn't verify.
