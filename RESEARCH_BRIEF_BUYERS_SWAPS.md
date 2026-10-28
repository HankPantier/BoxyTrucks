# Brief: buyer's guides and engine-swap guides

BoxyTrucks.com (repo `/home/claude/boxytrucks`) is adding two kinds of evergreen article. Read `RESEARCH_BRIEF.md` first: it sets the voice (direct, dry, Top Gear-ish, opinionated but fair) and the **hard rules**: never invent facts, numbers, prices, part numbers, URLs or handles; never use olathetoyotaparts.com or goosegear.com; never link factory manuals on archive.org or other user-uploaded scan sites; use User-Agent `BoxyTrucksBot/1.0 (+https://boxytrucks.com)` and never put an email address in a request header.

## Where facts come from
Every truck has a sourced guide: `data/pages/<family>/<slug>.json` (or `data/<family>.json` → `page` for a family's flagship) plus `data/extra/<family>/<slug>.json`, which holds values (checked October 2026), the timeline with buy/avoid/recall flags, capability, fitment and recalls. **Build from those first**, and carry the sources over. Families and slugs are listed in each `data/<family>.json` → `family.generations`. Don't contradict the guides; if you find a guide that's wrong, say so in your report. Search is shared and limited.

## A. Buyer's guides: `data/buyers/<slug>.json`
```json
{
 "slug": "best-under-15k",
 "title": "The best boxy 4x4s under $15,000",
 "description": "≤155 characters",
 "lead": ["paragraph", "paragraph"],
 "how": "One short paragraph: how we picked (driver-quality prices from our October 2026 value checks, owner-consensus best years, what breaks).",
 "picks": [
  {"model": "4runner/4th-gen", "rank": 1, "label": "Best all-rounder", "years": "2005–09 V8 or 2006–09", "price": "$8k–23k for a driver", "why": ["paragraph", "paragraph"], "watch": "One sentence: the thing to check before you buy."}
 ],
 "faqs": [{"q": "...", "a": "..."}],
 "sources": [{"name": "...", "url": "..."}]
}
```
- 6–8 picks. Every pick's `model` must be an existing `family/slug`. Prices must come from that guide's `values`. Best years must match its timeline `buy` flags.
- 3–5 FAQs.
- Inline cross-links use `[[family/slug|text]]`.
- Never give investment advice. Talk about what values have done, never promise what they'll do.

## B. Engine-swap guides: `data/swaps/<slug>.json`
```json
{
 "slug": "ls-swap",
 "title": "LS swaps in boxy 4x4s",
 "engine": "GM LS family (4.8/5.3/6.0/6.2 V8)",
 "description": "≤155 characters",
 "lead": ["paragraph", "paragraph"],
 "trucks": [{"model": "land-cruiser/fj40", "note": "what's involved for this truck, sourced: kits, mounts, transmission choice"}],
 "sections": [{"h": "Why people do it", "body": ["..."]}, {"h": "What it takes", "body": ["..."]}, {"h": "Parts and kits", "body": ["..."]}, {"h": "Emissions and registration", "body": ["..."]}, {"h": "What it costs", "body": ["..."]}],
 "suppliers": [{"name": "Advance Adapters", "url": "https://...", "what": "adapters and mounts for ..."}],
 "faqs": [{"q": "...", "a": "..."}],
 "sources": [{"name": "...", "url": "..."}]
}
```
- `trucks`: only the boxy 4x4s on our site where the swap is well documented (forum build threads, kit makers). Use 3–10.
- Emissions: state the federal and California facts carefully and with sources. In California an engine change must generally be the same or newer model year and pass a BAR referee; cite the BAR or CARB source if you state that.
- Costs: give only ranges you found sourced (kit prices from suppliers, builder quotes, forum build totals), and say what they're based on.
- `suppliers`: real companies with their real URLs.

Write with `json.dump(d, f, ensure_ascii=False, indent=1)`. Don't edit any other file, and don't run build.py or git.

## Final reply
Keep it short: the files written, counts, anything you couldn't verify, and any guide facts you found wrong.
