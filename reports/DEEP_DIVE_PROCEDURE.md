# Model deep dive: procedure (Hank, Nov 20, 2026)

Hank asked for a deep dive on every model: find common problems online (oil leaks, mechanical, electrical, interior, body/rust), fill the gaps in our repair and maintenance guides, add maintenance intervals, and give repairs more detail.

His choices (Nov 20): order by search traffic; add missing problems first, and deepen thin guides on the same generation in the same pass; a new maintenance page per generation; write and publish without pre-approval (sourced facts only); a daily summary.

## Order
`reports/deep-dive-queue.json`: the 38 generations with GSC impressions first, by 28-day impressions on Nov 20, then the rest. Take the next `todo` items in order and mark each `done` with the date and what changed.

## Per generation
1. `python3 scripts/deepdive_lib.py <fam>/<gen>` lists the existing repairs (THIN = on the noindex list), the service items, engines and buying checks. The page data lives in `data/pages/<fam>/<gen>.json`, or in `data/<fam>.json` under `page` for each family's flagship generation. Use `load_page` and `save_page` from `scripts/deepdive_lib.py`, which handle both locations and keep the file's indent.
2. Research with WebSearch and WebFetch: owner forums (marque forums, ExplorOz, IH8MUD, AULRO, Pirate4x4), reputable used-car reviews (CarsGuide, Carsales, Redbook, Edmunds, Autocar, Honest John), TSBs and recalls, and specialist workshops and parts sellers. Look for each of these:
   - oil and fluid leaks
   - engine, gearbox and driveline faults
   - electrical faults
   - interior faults
   - rust and body
   - suspension and steering
3. Add 2–4 new repair guides for common problems we don't cover. Use the same schema as existing repairs: `title, diff, time, cost, symptoms, fix, tools, parts[], know[], mistakes[], cost_note, refs[]`.
   - Every figure must come from a source in `refs`, attributed in the text ("one owner", "Carsales says").
   - Never invent part numbers, torque figures, prices or intervals. If sources conflict, say so and point to the manual.
4. Deepen thin guides on the same generation where sources allow: expand `fix` and add `know`, `mistakes` and `refs`. Then remove the guide's path from `data/repair_noindex.json`.
5. Add `maintenance` to `data/extra/<fam>/<gen>.json` with `intro, description, schedule_note, schedule[{at, items[]}], severe, age_items[{item, when, why}], sources[{name, url?}]`.
   - Use the factory schedule where a source publishes it, and say whose schedule it is.
   - If no factory schedule is online, say so plainly and use a purchase baseline plus clearly attributed owner and specialist intervals.
   - The page renders at `/models/<fam>/<gen>/maintenance/` (template `gen_maintenance.html`) and is linked from the generation guide's tools.
6. Build. Check one new page at 400 px width; it must not scroll sideways. Commit and push with the origin URL set first.

## Rules
- Facts only from sources; no invented anecdotes about Hank. Never use olathetoyotaparts.com or goosegear.com. No archive.org links.
- Keep the user's email out of everything.

## Daily run
Do about 3–4 generations a run. Log progress in the queue file. Send Hank one short summary: which generations were done, and how many guides were added, deepened and given maintenance pages.
