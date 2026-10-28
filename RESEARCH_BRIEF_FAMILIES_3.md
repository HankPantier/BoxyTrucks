# Brief: families round 3 (Oct 2026)

BoxyTrucks.com is adding new trucks. The repo is `/home/claude/boxytrucks`. Everything lives in the repo, not the scratchpad.

Read these first, all in the repo:
1. `RESEARCH_BRIEF.md`: voice, **hard rules** (never invent facts, numbers, URLs, part numbers, handles or prices), and the full `family` and `page` schema with its content targets: story, engineering, generations_table, 6–8 buying checks, 6–8 repairs, about 10 FAQs including "What's the biggest tire I can fit without a lift?", mods, forums, searches, plate and sources.
2. `RESEARCH_BRIEF_PARTS_SERVICE.md`: every repair gets `parts` links, and every page gets `baseline_service`.
3. `RESEARCH_BRIEF_PHOTOS.md`: photos of the **exact generation**, off-road first (dirt, trail, snow, desert, forest), under a usable licence (Unsplash, Pexels, public domain, CC0, CC BY or BY-SA), credited, with `hero_focus` set. **Never use photos of a truck that is broken down, crashed, overturned, abandoned or wrecked.** Look at every image with Read before you use it. Images go in `site/img/<family>/`, with filenames that start with the model.
4. `RESEARCH_BRIEF_DETAILS.md`: also write the detail file `data/extra/<family>/<slug>.json` (fitment, recalls, timeline with buy/avoid/recall/note flags, identify, capability, values checked "October 2026", docs, import if relevant, production, community).
5. For tone and depth, read one finished page, e.g. `data/pages/land-cruiser/100-series.json` with `data/extra/land-cruiser/100-series.json`.

## Timeline flags
A `buy` flag means owners and specialists **recommend** those years, not just that something changed. An `avoid` flag means documented problems. Years whose only issue is a recall get `recall`, not `avoid`. Source every flag.

## Assignments
| family slug | maker | family name | generation slug | name | years | flagship? |
|---|---|---|---|---|---|---|
| hummer | AM General | Hummer | h2 | Hummer H2 | 2003–2009 | no (existing family; H1 is flagship) |
| pajero | Mitsubishi | Pajero / Montero | pajero-gen3 | Pajero / Montero (third generation) | 1999–2006 (US Montero 2001–2006) | no (existing family) |
| delica | Mitsubishi | Delica | delica-l300 | Delica Star Wagon (L300 4WD) | 1986–1999 | **yes** |
| delica | Mitsubishi | Delica | delica-space-gear | Delica Space Gear | 1994–2007 | no |
| unimog | Mercedes-Benz | Unimog | unimog-u1300l | Unimog U1300L (435) | 1975–early 2000s (confirm) | **yes** |
| unimog | Mercedes-Benz | Unimog | unimog-404 | Unimog 404 | 1955–1980 | no |
| pinzgauer | Steyr-Puch | Pinzgauer | pinzgauer-710-712 | Pinzgauer 710 / 712 | 1971–1985 (confirm) | **yes** |
| pinzgauer | Steyr-Puch | Pinzgauer | pinzgauer-716-718 | Pinzgauer 716 / 718 | 1985–2000 (confirm) | no |
| niva | Lada | Niva | niva | Lada Niva (VAZ-2121 / 4x4 Legend) | 1977–present | **yes** (only page) |
| ramcharger | Dodge | Ramcharger | ramcharger-1st | Ramcharger (first generation) | 1974–1980 | no |
| ramcharger | Dodge | Ramcharger | ramcharger-2nd | Ramcharger (second generation) | 1981–1993 | **yes** |

Confirm every year range against sources and use what you find; fix the table's years in your files if they're wrong.

Most of these were never sold new in the US (Delica, Unimog as a civilian truck, Pinzgauer, Niva, much of the Pajero range). Cover how Americans actually get them: military surplus (Pinzgauer, U1300L), 25-year imports (Delica, Niva, diesel Pajeros), and state registration issues. Our importing guide lives at `[[importing|...]]`; don't link it, just cover the model-specific facts in `import`.

## Files
- **Flagship agent:** write `data/<family>.json` as `{"family": {...}, "page": {...flagship page...}}`. `family.generations` lists **every** generation slug for that family above, in chronological order, each with `has_page: true`, a verified `at_url` (AutoTempest: confirm make and model slugs by curling and checking the `<title>`) and a `bat_url` (the BaT model page if one exists, otherwise the make page; check for a 200 status). Also write `family.forums`, `family.related_families`, `family.hero_photo` and `data/resources/<family>.json` (resources schema in `RESEARCH_BRIEF_PHASE2.md` §5), plus the flagship's `data/extra/<family>/<slug>.json`.
- **Other agents in a new family:** write `data/pages/<family>/<slug>.json` (the `page` object only) and `data/extra/<family>/<slug>.json`.
- **Agents adding to an existing family (h2, pajero-gen3):** write the page and extra files only. **Don't edit `data/<family>.json`.** Return the generation entry as JSON in your final reply.
- Use `json.dump(..., ensure_ascii=False, indent=1)`. Don't run `build.py` or git. Don't edit build.py, templates or any other model's files.

Cross-link to existing models with `[[family/slug|text]]` where it's natural. Slugs are listed in each `data/<family>.json` → `family.generations`, and new ones are in the table above.

## Rules for requests
- Use User-Agent `BoxyTrucksBot/1.0 (+https://boxytrucks.com)`, and never put an email address in any request header.
- Never use olathetoyotaparts.com or goosegear.com.
- Never link factory manuals on archive.org or other user-uploaded scan sites; cite them by name with no URL.
- Search is shared and limited, so prefer WebFetch on known-good sources: Wikipedia, BaT model pages, Hagerty, NHTSA's recall API (`https://api.nhtsa.gov/recalls/recallsByVehicle?make=&model=&modelYear=`), specialist forums and shops. If Commons rate-limits you, use `https://commons.wikimedia.org/w/thumb.php?f=<File>&w=2000` and wait 3 seconds between downloads.

## Final reply
Keep it short: files written; counts of FAQs, repairs (with parts), baseline items, photos and timeline rows; for non-flagship generations in existing families, the generation entry JSON (`slug`, `name`, `years`, `codes`, `summary`, `at_url`, `bat_url`); and anything you couldn't verify.
