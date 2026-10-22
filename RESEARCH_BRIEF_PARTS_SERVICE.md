# Add parts links + baseline service to deep pages

Site goal: be the most COMPREHENSIVE hands-on resource for each truck. Two additions to every deep page JSON (`data/<family>.json` → `page`, or `data/pages/<family>/<gen>.json`):

## 1. `parts` on every repair
Add to each object in `repairs`:
```json
"parts": [{"name": "Elring valve cover gasket set (left)", "supplier": "FCP Euro", "url": "https://..."}]
```
- Link the actual parts needed for THAT repair at reputable suppliers. Prefer a specific product page; if you can't confirm one, use the supplier's search URL for the part + model (a working search URL is fine).
- Reputable suppliers by platform (use what fits; others OK if reputable):
  - Mercedes G-Class: FCP Euro (search: `https://www.fcpeuro.com/products?keywords=<terms>`), GwagenParts.com (search: `https://www.gwagenparts.com/?s=<terms>&post_type=product`), Pelican Parts, Eurowise.
  - Toyota Land Cruiser / Lexus / 4Runner: CruiserTeq (formerly Cruiser Outfitters; search `https://cruiserteq.com/?s=<terms>&post_type=product`), Man-A-Fre, Slee Off-Road, Metal Tech 4x4, ARB/OME, Toyota/Lexus OEM parts dealers (e.g. toyotapartsdeal.com, lexuspartsnow.com product pages), RockAuto catalog (`https://www.rockauto.com/en/catalog/<make>,<year>,<model+with+plus>`), Trail4R for 4Runners.
  - Land Rover / Range Rover: Rovers North (`https://roversnorth.com/search?q=<terms>`), Atlantic British (`https://www.atlanticbritish.com/search?q=<terms>`), Lucky8, Terrafirma, Britpart, Bearmach, Arnott (air suspension).
  - Ineos Grenadier: INEOS official parts/accessories, plus BMW-engine parts at FCP Euro where the part is a BMW B57/B58 part.
- 1–4 parts per repair. Never invent part numbers; include OEM/aftermarket part numbers only if sourced.
- Verify links: `curl -s -o /dev/null -w '%{http_code}' -L -A 'Mozilla/5.0' URL` (some sites return 403 to bots via Cloudflare — those are OK to use if the URL pattern is the supplier's real one).

## 2. `baseline_service` (new section: "After you buy it")
The recommended catch-up service right after purchasing a used example — be as MODEL-SPECIFIC as possible:
```json
"baseline_service": {
  "intro": "One or two sentences: why to baseline everything, anything special about this model.",
  "items": [
    {"item": "Engine oil & filter", "spec": "MB 229.5 5W-40 · ≈8.0 L with filter", "interval": "Then every 5,000–7,500 mi", "note": "Model-specific tip (e.g. cartridge filter on top of engine)", "parts": [{"name": "Mann oil filter cartridge", "supplier": "FCP Euro", "url": "https://..."}]}
  ]
}
```
Cover (as applicable): engine oil & filter; air filter; cabin filter; spark plugs / glow plugs; coolant (type); automatic/manual transmission fluid (type + note on drain-and-fill vs flush); transfer case; front & rear differentials (gear oil grade, LSD/locker notes); swivel housings / knuckles (e.g. Land Rover swivels, 80-series knuckles); power steering fluid; brake fluid; belts & hoses; timing belt where applicable (with interval); suspension-specific items (air suspension, AHC fluid, KDSS); grease points (driveshafts/u-joints); fuel filter; battery. 8–14 items.
- Specs (fluid types, capacities, intervals) must come from sources: factory manuals quoted on forums, enthusiast shop guides (Slee "newbie guides", Atlantic British/Rovers North tech articles, FCP Euro blog), owner's manual PDFs, reputable forums. Put sources in the page's `sources` list. If a capacity or spec isn't sourced, give the fluid type only or write "[CONFIRM IN MANUAL]".
- Budget: web search is nearly exhausted — use WebFetch/curl on known sources (Wikipedia, supplier tech pages, forum FAQ threads, owner's manual PDFs) rather than WebSearch.

Edit the JSON files in place (load → modify → write with `json.dump(..., ensure_ascii=False, indent=1)`); do not change any other fields. Keep files valid JSON. Reply with a short summary per page: repairs with parts / total, baseline items, anything unverified.
