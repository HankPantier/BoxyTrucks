# Brief: fact-check, correct and fill gaps

BoxyTrucks.com (repo `/home/claude/boxytrucks`) is a guide to boxy 4x4s for hands-on owners who will actually use the specs, part numbers and fluid figures. Your job is an **adversarial fact-check** of the pages you're assigned. Assume things are wrong until a source says otherwise. Read `RESEARCH_BRIEF.md` for the voice and schema, and treat its hard rules as absolute: never invent facts, numbers, part numbers, URLs or handles.

## What's in scope for each model
- The page JSON: `data/pages/<family>/<slug>.json`, or for the flagship `data/<family>.json` → `page`. If you're assigned the flagship, also check the `family` object (intro, verdict, years, generations list, summaries, forums).
- The detail file: `data/extra/<family>/<slug>.json`, if there is one.
- The photo files referenced in `photos`: **open each image with Read** and confirm it really shows that generation and matches its caption and alt text.

## What to check
1. **Every factual claim.** That means dates, model years, production figures, engines, outputs, gearboxes, axles, transfer cases, dimensions, capacities, fluid specs, torque values, intervals, prices, recall numbers, people, places and events. Confirm each against a reliable source: a manufacturer's document, an owner's or service manual, NHTSA, Wikipedia (where it cites a source), a respected specialist, or reputable press.
2. **Consistency inside the model.** The page and the detail file must agree with each other. Check the story against the engineering section, the generations table, the plate, the FAQs, the timeline, capability and fitment. Tire sizes, engines, years and outputs mustn't contradict across sections.
3. **Repairs and service.** Symptoms, fix steps and tools must make mechanical sense for this vehicle. Fluid types and capacities need a source, or must carry the `[CONFIRM IN MANUAL]` marker. Part links must point to the right part for this vehicle. Spot-check at least 10 links per page with `curl -s -o /dev/null -w '%{http_code}' -L -A 'Mozilla/5.0'`; a 403 from a site that blocks bots is fine if the URL is the supplier's real URL format. **Never use olathetoyotaparts.com.**
4. **Links.** Every URL in `sources`, `forums`, `social`, `mods` (`who`), `docs`, `community`, `searches` and `recalls` must resolve and be the right page. Fix any that are broken or wrong. Drop social handles you can't confirm exist.
5. **Cross-links.** Every `[[family/slug|text]]` must point to a real model. The families and slugs are listed in each `data/<family>.json` → `family.generations`.
6. **Tone vs truth.** The witty lines must not slip in a false claim.
7. **Gaps.** Each page should have about 10 FAQs (including "biggest tire without a lift"), 6–8 repairs each with parts, 8–14 `baseline_service` items, 6–8 buying checks, a mods section with real suppliers, and sources. Add what's missing **only if you can source it**. Detail-file sections can be filled in where they're empty, under the same rule.

## How to edit
- Edit in place: load the JSON, change it, and write it back with `json.dump(d, f, ensure_ascii=False, indent=1)`. Keep the schema exactly as it is, and only touch files for your assigned models.
- Correct what's wrong. If a claim can't be verified, soften it ("owners report…", "reportedly") or remove it. Don't leave a false or unsupported claim standing. Add every new source to `sources`.
- Don't run `build.py`, don't touch templates, and **never put an email address in any request header**. Use User-Agent `BoxyTrucksBot/1.0 (+https://boxytrucks.com)`.
- Search is shared across many agents and limited. Prefer WebFetch or curl on known-good sources (manufacturer PDFs, Wikipedia, NHTSA's API `https://api.nhtsa.gov/recalls/recallsByVehicle?make=&model=&modelYear=`, BaT, specialist shops).

## Report (required)
Write `reports/factcheck/<your-group>.md` in the repo, with one section per model:
- **Corrections made:** what was wrong, what you changed it to, and the source.
- **Removed or softened:** claims you couldn't verify.
- **Added:** new content, with sources.
- **Still unverified / shortcomings:** thin sections, weak or wrong photos, missing specs, dead links you couldn't replace, and anything a human expert should check. Mark each **High** (could mislead an owner: wrong fluid, torque, fitment or safety information), **Med** or **Low**.

End the report with a top-5 list of the most important remaining problems for your group. Your final reply should be a short summary pointing to the report.
