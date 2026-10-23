# Brief: model detail data (fitment, recalls, timeline, ID, capability, values, docs, import, production, clubs)

BoxyTrucks.com is a guide to boxy 4x4s for hands-on, off-road owners. The repo is at `/home/claude/boxytrucks`. Read `RESEARCH_BRIEF.md` for the voice and the **hard rules**: never invent facts, numbers, part numbers, URLs, handles or prices, and leave out anything you can't verify. Every page already exists in `data/<family>.json` (`page`) or `data/pages/<family>/<slug>.json`. Read the page for context, but **don't edit it**: other agents are writing to those files.

For each model you're given, write **one new file**: `data/extra/<family>/<slug>.json`. Create the folder if needed. Use `json.dump(d, f, ensure_ascii=False, indent=1)` and don't run `build.py`. All sections are optional, so leave out any you can't source rather than filling them with guesses. Add every source you used to `sources` in this file.

```json
{
 "fitment": {
  "stock": ["265/70R16 (base)", "275/70R16 (VX)"],
  "wheel": {"bolt_pattern": "6x139.7 (6x5.5\")", "offset": "+15 mm (stock alloy)", "center_bore": "106.1 mm", "lug_thread": "M12x1.5", "lug_torque": "97 lb-ft (131 N·m)"},
  "max_tire": [
   {"lift": "Stock", "size": "285/75R16", "note": "minor trimming of the front mud flap; may rub at full lock"},
   {"lift": "2 in", "size": "315/75R16", "note": "..."},
   {"lift": "3 in", "size": "35x12.50R17", "note": "needs wheel offset/backspacing, trimming, regear advised"}
  ]
 },
 "recalls": {
  "lookup": "US",
  "items": [{"title": "Takata passenger airbag inflator", "years": "2003–2006", "ref": "NHTSA 18V-xxx", "url": "https://www.nhtsa.gov/...", "summary": "one line"}],
  "tsbs": [{"title": "Front driveshaft vibration", "ref": "TSB number if sourced", "summary": "one line", "url": ""}]
 },
 "timeline": [
  {"year": "1993", "change": "Full-time 4WD with lockable centre diff; 1FZ-FE replaces 3F-E", "flag": "buy"},
  {"year": "1995", "change": "Airbags and OBD-II arrive", "flag": "note"}
 ],
 "identify": {
  "intro": "One or two sentences on why identification matters for this model (clones, re-badges, gray imports).",
  "items": [{"head": "Factory lockers", "body": "Option code / dash switch / axle tag detail..."}, {"head": "VIN", "body": "Which characters encode what for this model."}]
 },
 "capability": [
  {"k": "Towing", "v": "8,000 lb (3,630 kg)", "note": "braked"},
  {"k": "Payload", "v": "1,250 lb"}, {"k": "Roof load", "v": "..."}, {"k": "Fuel tank", "v": "..."},
  {"k": "Ground clearance", "v": "..."}, {"k": "Approach / departure / breakover", "v": "..."},
  {"k": "Wading depth", "v": "..."}, {"k": "Fuel economy", "v": "EPA 13 city / 15 hwy", "note": "or real-world if that's what's sourced"},
  {"k": "Curb weight", "v": "..."}, {"k": "Turning circle", "v": "..."}
 ],
 "values": {
  "checked": "October 2026",
  "intro": "One sentence on the market: rising, flat, what drives premiums.",
  "ranges": [{"cond": "Project / needs work", "range": "$8k–15k"}, {"cond": "Driver", "range": "$15k–30k"}, {"cond": "Excellent / restored", "range": "$40k–80k+"}],
  "note": "e.g. 'Based on N Bring a Trailer sales from 2025–26; factory-locker and low-mileage trucks sit at the top.'"
 },
 "docs": [{"name": "Factory service manual (FSM) 1993–97", "url": "https://...", "note": "where to buy or download legitimately"}],
 "import": {"paragraphs": ["Only when it matters: the US 25-year rule for gray-market versions (e.g. 70 Series, Patrol Y60/Y61, 90/110 Defender, diesel G-Wagens), plus state titling, emissions and California issues. Use dates and sources."]},
 "production": {
  "intro": "One sentence.",
  "items": [{"k": "Total built", "v": "..."}, {"k": "US sales", "v": "..."}],
  "editions": [{"name": "Collector's Edition", "years": "1997", "note": "what it is, how many"}],
  "paint": "Optional one-liner on notable paint codes, if sourced"
 },
 "community": [{"kind": "club|event", "name": "Cruise Moab", "url": "https://...", "note": "Annual Toyota Land Cruiser Association trail event, Moab UT, April"}],
 "sources": [{"name": "Publisher — title", "url": "https://..."}]
}
```

## Notes by section
- **fitment:** use owner-forum consensus for "biggest tire" at stock, 2 in and 3 in (the page's FAQ may already have the stock answer, so stay consistent with it). Wheel specs come from the owner's manual or a reputable tire or wheel retailer (Tire Rack, wheel-size.com, Discount Tire). Lug torque comes from the owner's manual or FSM.
- **recalls:** for US-sold models, list the notable NHTSA campaigns with the campaign number and a link. Search nhtsa.gov, or use reputable press that quotes campaign IDs. Set `"lookup": "US"` and the page will link NHTSA's VIN lookup. For models not sold in the US (or not sold there new), set `"lookup": "UK"` for the UK DVSA checker, or `"lookup": "none"`. Put well-known service bulletins in `tsbs` (JK death-wobble fixes, Toyota frame-rust campaigns, Land Rover's engine and air-suspension updates). Only include a number if it's sourced.
- **timeline:** list model-year changes in order, from model-year differences and the "which years to buy" guidance on forums, Wikipedia and buyer guides. The `flag` is `buy` (a sweet spot), `avoid` (a known-bad change) or `note` (neutral). Aim for 5–12 rows.
- **identify:** how to tell the real thing from a clone or re-badge: trim, engine and locker identification, VIN position meanings, build-plate and option codes, axle tags. Include 3–6 items.
- **capability:** factory figures from manufacturer brochures, owner's manuals, Wikipedia (if it cites them) or reputable press. Give US and metric units where you can. Leave out anything unsourced. "Roof load" means the manufacturer's dynamic roof load rating, if published.
- **values:** use Bring a Trailer sold results for the generation (curl the BaT model page with `-A "Mozilla/5.0"`, or WebFetch it, and read the sold prices), plus Hagerty valuation if it's available. Use broad ranges by condition, always with `checked: "October 2026"`, and say what the range is based on. For brand-new models, use MSRP ranges from the manufacturer instead.
- **docs:** factory service manuals (Toyota TIS, Mercedes WIS/STAR, Land Rover TOPIx, Jeep/Mopar, Nissan FSM sites), owner's manual PDFs hosted by the manufacturer, reputable reprints (Helm, Faxon) and parts catalogues (EPC/microcat). Link only legitimate sources, never pirated PDFs.
- **import:** include this only when it's relevant to the model; otherwise leave it out.
- **production:** production totals and special editions, from sourced figures only.
- **community:** owners' clubs, registries and trail events (Easter Jeep Safari, Cruise Moab, Overland Expo, Defender clubs, G-Class clubs, Land Cruiser Heritage Museum events). Only real, current ones.

Budget: search is shared with many agents, so prefer WebFetch on known-good pages. Commons downloads aren't needed here.

## Report back
Give one line per model: which sections you wrote and anything you left out for lack of sources.
