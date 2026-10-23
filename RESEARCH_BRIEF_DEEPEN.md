# Brief: factory-spec hunt and deepening thin guides

BoxyTrucks.com (repo `/home/claude/boxytrucks`) is a guide to boxy 4x4s for hands-on owners who will actually use the specs, so accuracy is everything. Read `RESEARCH_BRIEF.md` (voice and **hard rules**: never invent facts, numbers, part numbers, URLs or handles) and `RESEARCH_BRIEF_PARTS_SERVICE.md` (repairs get `parts`, pages get `baseline_service`; **never use olathetoyotaparts.com**).

Your pages are listed in your task. A page lives at `data/pages/<family>/<slug>.json`, or for a family's flagship at `data/<family>.json` → `page`. Its detail file is `data/extra/<family>/<slug>.json`.

## Task A: spec hunt (pages marked SPEC)
Find every `[CONFIRM IN MANUAL]` (or `[CONFIRM`) marker in the page and its detail file. These are fluid types and grades, capacities, torque values, intervals and wheel specs. For each, try to find a **primary or near-primary source**:
- the factory owner's manual or warranty and maintenance booklet, especially PDFs hosted by the manufacturer (Toyota/Lexus `techinfo` and owner sites, Mopar and Jeep owner sites, Ford owner site, Mercedes owner's manual PDFs, Land Rover TOPIx owner guides, Nissan owner portals)
- a factory service manual excerpt published by a reputable source
- a manufacturer fluid-capacity chart, or the fluid makers' lookup tools (Fuchs, Liqui Moly, Castrol, Mobil, Valvoline), which quote OEM specs; say which
- a reputable specialist whose figure matches another independent source

If you confirm a figure, replace the marker and add the source to `sources`. If sources disagree, show both values with their sources. If you can't confirm one, **leave the marker as it is**. Never remove a marker without a source. Every change must leave the page consistent across its FAQ, service section, repairs and detail file.

## Task B: deepen (pages marked DEEPEN)
- Bring `repairs` to 7–8 using **real, documented** problems for that generation. Sources: NHTSA recalls and complaints, service bulletins reported by reputable press, specialist shops' known-issue pages, and owner-forum consensus.
- Every new repair needs symptoms, a fix, tools, difficulty, time, cost and `parts` (OEM numbers only when sourced; Amazon searches are fine for generic items).
- Also top up FAQs to about 10–12, buying checks to 6–8, and `baseline_service` to 8–14, where they're short.
- If a short story is thin, you may add one sourced story paragraph.
- Don't pad. If there isn't enough real material, stop short and say so.

## Rules
- Edit only your assigned pages and their detail files. Load each file, change it, and write it back with `json.dump(d, f, ensure_ascii=False, indent=1)`. Keep the schema exactly as it is.
- Never remove owner-supplied social or reading entries.
- Don't run `build.py` or git.
- Use User-Agent `BoxyTrucksBot/1.0 (+https://boxytrucks.com)`, and **never put an email address in any request header**.
- Search is shared and limited, so prefer WebFetch or curl on known sources.

## Report
Write `reports/deepen/<your-group>.md` with each page's before → after counts (markers, repairs, FAQs, service items), every spec you confirmed with its source, and what's still open. Your final reply is a short summary and the report path.
