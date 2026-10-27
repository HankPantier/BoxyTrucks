# Brief: head-to-head comparison pages

BoxyTrucks.com (repo `/home/claude/boxytrucks`) is adding comparison pages for questions buyers search for, like "80 Series vs 100 Series". Read `RESEARCH_BRIEF.md` first: it sets the voice (direct, a little dry, Top Gear-ish, opinionated but fair) and the **hard rules** (never invent facts, numbers, part numbers, URLs or handles).

## Where the facts come from
Every model already has a sourced guide:
- the page: `data/pages/<family>/<slug>.json`, or for a family's flagship model, `data/<family>.json` → `page`
- its detail file: `data/extra/<family>/<slug>.json`, which holds the timeline (with buy/avoid/recall flags), capability numbers, fitment, values and recalls

**Build each comparison from those files first.** They're already sourced, so carry each fact's source over into the comparison's `sources`. Look a fact up fresh only where a head-to-head needs something the guides lack, such as a direct comparison from a reputable outlet (Car and Driver, MotorTrend, Outside, Expedition Portal, IH8MUD consensus or similar). Fetch every source you use. Don't contradict the guides; if you find one is wrong, say so in your report.

## File to write: `data/compare/<slug>.json`
```json
{
 "slug": "80-series-vs-100-series",
 "title": "Land Cruiser 80 Series vs 100 Series",
 "models": ["land-cruiser/80-series", "land-cruiser/100-series"],
 "description": "≤155 characters, for the meta description",
 "lead": "One or two sentences: the answer, then why.",
 "verdict": [{"model": "land-cruiser/80-series", "pick_if": "you want solid axles, factory lockers and the simplest truck to fix"}, {"model": "land-cruiser/100-series", "pick_if": "..."}],
 "table": [{"label": "Years (US)", "values": ["1991–97", "1998–2007"]}, {"label": "Front suspension", "values": ["...", "..."]}],
 "sections": [{"h": "Off-road", "body": ["paragraph", "paragraph"]}, {"h": "Reliability and what breaks", "body": ["..."]}, {"h": "Buying one now", "body": ["..."]}],
 "faqs": [{"q": "...", "a": "..."}],
 "sources": [{"name": "...", "url": "..."}]
}
```
- `table`: 10–16 rows. Cover years, engines (power and torque), transmission, transfer case, axles and suspension, lockers, wheelbase, ground clearance, approach and departure angles, towing, fuel economy, the biggest tire without a lift, typical prices now, and the best years. Keep the values short. If one model has no figure for a row, write "—".
- `sections`: 4–6 sections, 1–3 short paragraphs each. Cover off-road, on-road and daily use, reliability and common failures, running costs and parts, modifying, and buying one now.
- `faqs`: 4–6 real questions people ask about this matchup.
- Inline cross-links use `[[family/slug|text]]`, as on the guides.
- Write with `json.dump(d, f, ensure_ascii=False, indent=1)`. Don't edit any other file, and don't run `build.py` or git.

## Rules (hard)
- Never use olathetoyotaparts.com. Never link factory manuals on archive.org or other user-uploaded scan sites.
- Use User-Agent `BoxyTrucksBot/1.0 (+https://boxytrucks.com)`, and never put an email address in a request header. Search is shared and limited, so lean on the existing data.

## Report
Your final reply is short: the files written, anything you couldn't verify, and any guide facts you found to be wrong.
