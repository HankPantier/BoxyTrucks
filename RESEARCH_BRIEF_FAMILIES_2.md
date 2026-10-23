# Brief: new families and new models in existing families (round 2)

BoxyTrucks.com (repo `/home/claude/boxytrucks`) is adding new families and filling gaps in existing ones. Every new guide needs the same depth as the existing ones.

## Read first, all in the repo
1. `RESEARCH_BRIEF.md`: voice, the **hard rules** (never invent facts, numbers, part numbers, URLs or handles), the `family` and `page` schema, and content targets: story, engineering, generations_table, 6–8 buying checks, 6–8 repairs, about 10 FAQs including "biggest tire without a lift", mods, forums, searches, plate and sources.
2. `RESEARCH_BRIEF_PARTS_SERVICE.md`: every repair gets `parts`, and every page gets `baseline_service`. **Never use olathetoyotaparts.com.**
3. `RESEARCH_BRIEF_PHOTOS.md`: photos of the **exact generation**, off-road first, usable licences only, credited, with `hero_focus`. Open every image with Read before you use it. **Never use a photo that shows the vehicle broken down, crashed, overturned, abandoned or wrecked.** Enthusiasts read the site.
4. `RESEARCH_BRIEF_DETAILS.md`: also write the detail file, covering fitment, recalls, timeline, identify, capability, values, docs, import if relevant, production and community.
5. For tone and depth, read one finished page, e.g. `data/pages/land-cruiser/100-series.json`, plus a family file such as `data/scout.json`.

## Files you write
- **Flagship or family agent** (your task will say so): write `data/<family-slug>.json` as `{"family": {...}, "page": {...flagship page...}}`. The `family` keys are `slug`, `name`, `maker`, `years`, `verdict`, `intro` (a list of paragraphs), `hero_photo`, `generations`, `forums` and `related_families`. `family.generations` must list **all** of the family's slugs (given in your task) in chronological order. Each entry is `{"slug","name","years","codes":[...],"summary","at_url","bat_url","has_page":true}`. Verify the AutoTempest and BaT URLs by curling them and checking the `<title>` and a 200 status. Also write `data/resources/<family-slug>.json` in the same shape as the existing files in `data/resources/`: `{"youtube":[],"instagram":[],"forums":[],"other":[]}`, with items `{"name","url","focus"}`. Include only YouTube channels you have verified and that actually cover the model.
- **Every other agent** writes only `data/pages/<family-slug>/<slug>.json`, containing the `page` object only, with `page.slug` equal to `<slug>`. Create the folder if it's missing.
- **Everyone** writes `data/extra/<family-slug>/<slug>.json` (the detail file) for each of their pages.
- Images go in `site/img/<family-slug>/`, with filenames that start with the model.
- If you're adding a page to an **existing** family (land-cruiser, nissan-patrol, jeep), **don't edit that family's JSON**. In your final reply, give the generation entry as JSON and the coordinator will add it.
- Use `json.dump(d, f, ensure_ascii=False, indent=1)`. Don't run `build.py` or git, and don't edit any other model's files, `build.py` or the templates.

## Cross-links
Use `[[family/slug|text]]`. The existing families are `4runner`, `bronco`, `g-class`, `grenadier`, `jeep`, `land-cruiser`, `land-rover`, `lexus`, `nissan-patrol`, `range-rover` and `scout`. Their slugs are in each `data/<family>.json` → `family.generations`. The new families in this round are `chevrolet` (slugs `k5-blazer-1st`, `k5-blazer`, `suburban-square`), `suzuki` (`lj-series`, `samurai`, `jimny-jb23`, `jimny-jb74`), `pajero` (`pajero-gen1`, `pajero-gen2`), `trooper` (`trooper-1`, `trooper-2`) and `hummer` (`h1`). Link to these only once they will exist (they will by the end of this round).

## Rules
- Use User-Agent `BoxyTrucksBot/1.0 (+https://boxytrucks.com)`, and **never put an email address in any request header**.
- Search is shared and limited, so prefer WebFetch or curl on known-good sources:
  - Wikipedia, NHTSA's recall API (`https://api.nhtsa.gov/recalls/recallsByVehicle?make=&model=&modelYear=`), BaT model pages, Hagerty
  - factory owner's manuals hosted by the manufacturer
  - specialist shops and owner forums
- Wikimedia Commons rate-limits, so wait 3 seconds between downloads; `https://commons.wikimedia.org/w/thumb.php?f=<File>&w=2000` helps.
- Flickr's image server rejects "Bot" User-Agents. Use Commons, Pexels or Unsplash, or Openverse's proxy for gallery-size images.

## Final reply
For each page, give the counts per section and anything you couldn't verify. For pages in existing families, include the generation entry JSON.

## Manuals: what you may link
Never link factory manuals hosted on archive.org or other user-uploaded scan sites; they are probably unauthorized copies. You may use their figures, but cite the manual by name in `sources` with no `url` key. Manufacturer-hosted owner manuals and legitimate sellers (Helm, Faxon, the manufacturer) are fine to link.
