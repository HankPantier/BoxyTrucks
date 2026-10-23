# Brief: add a missing model to an existing family

BoxyTrucks.com (repo `/home/claude/boxytrucks`) is adding full guides for models we left out. Every new guide needs the same depth as the existing ones.

Read these first, all in the repo:
1. `RESEARCH_BRIEF.md`: voice, hard rules (never invent facts, URLs, part numbers or handles), the `page` schema and its content targets (story, engineering, generations_table, 6–8 buying checks, 6–8 repairs, about 10 FAQs including "biggest tire without a lift", mods, forums, searches, plate, sources).
2. `RESEARCH_BRIEF_PARTS_SERVICE.md`: every repair gets `parts`, and every page gets `baseline_service`. **Never use olathetoyotaparts.com.**
3. `RESEARCH_BRIEF_PHOTOS.md`: photos of the **exact generation**, off-road first, under a usable licence, credited, with `hero_focus` set. Look at every image with Read before you use it.
4. `RESEARCH_BRIEF_DETAILS.md`: also write the detail file (fitment, recalls, timeline, identify, capability, values, docs, import if relevant, production, community).
5. Read one existing page in the same family for tone and depth, plus the family's `data/<family>.json`.

## Write
- `data/pages/<family>/<slug>.json`: the `page` object only. `page.slug` must equal `<slug>`.
- `data/extra/<family>/<slug>.json`: the detail file.
- Images go in `site/img/<family>/`, with filenames that start with the model.

**Don't edit `data/<family>.json`**; the coordinator adds the generation entry. Don't run `build.py`, and don't touch any other model's files. Cross-link with `[[family/slug|text]]` to existing models where it's natural; families and slugs are listed in each `data/<family>.json` → `family.generations`.

Never put an email address in any request header. Use User-Agent `BoxyTrucksBot/1.0 (+https://boxytrucks.com)`. If Commons rate-limits you, use `https://commons.wikimedia.org/w/thumb.php?f=<File>&w=2000` and wait. Search is shared and limited, so prefer WebFetch or curl on known-good sources. These work well:
- NHTSA recalls API: `https://api.nhtsa.gov/recalls/recallsByVehicle?make=&model=&modelYear=`
- BaT model pages and the listings-filter JSON
- Quadratec's sitemap for Jeep parts
- Land Rover's TOPIx owner-guide PDFs

## Final reply
Give the coordinator the generation entry to add, as JSON: `{"slug","name","years","codes":[...],"summary","at_url","bat_url"}`, with AutoTempest and BaT URLs verified (check the `<title>` and a 200 status). Then list the counts per section and anything you couldn't verify.
