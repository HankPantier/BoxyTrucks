# Brief: audit the "Sweet spot" and "Beware" year flags

BoxyTrucks.com (repo `/home/claude/boxytrucks`) is a sourced guide to boxy 4x4s. Each model's detail file `data/extra/<family>/<slug>.json` has a `timeline` list. Each entry is `{"year","change","flag"}`, and `flag` is one of `note`, `buy` (shown as **Sweet spot**) or `avoid` (shown as **Beware**).

The owner caught a wrong flag. On the G 500, "2001–02" was flagged Sweet spot. But early G 500s are known for electrical problems, and specialists and owners usually point buyers to 2005–2008. The flags were set from "what changed that year", not from what buyers and specialists actually recommend. Audit every flag on your pages.

## For each of your pages
1. Read the `timeline`, plus the page (`data/pages/<family>/<slug>.json`, or for a family flagship `data/<family>.json` → `page`). Look at `verdict`, `buying` checks, `repairs`, FAQs and any text saying "best years", "sweet spot", "avoid" or "years to buy".
2. Research which years or production ranges buyers are actually advised to seek out and to avoid, and why. Good sources:
   - marque specialists and independent shops' buyer's guides
   - Hagerty, BaT model guides, and reputable press buyer's guides (Car and Driver, MotorTrend, Autocar, Outside/Overland Journal, etc.)
   - NHTSA recalls and complaints
   - owner-forum consensus (IH8MUD, Expedition Portal, G-Class forums like BenzWorld/GClassWorld, WranglerForum, Rangerovers.net, LR4x4, etc.)

   Look for the reasons: fixed failure points (head gaskets, frame rust, timing chains, transmissions, electrics), engine and gearbox changes, and recall fixes.
3. Fix the flags:
   - `buy` only on entries for the years that sources actually recommend.
   - `avoid` on years with documented problems (for example an engine with known failures, or years before a fix).
   - Everything else is `note`.
   - If the recommended years have no timeline entry, **add one** (in year order) with a factual, sourced `change` text. For example the G 500 might need "2005–08: …" flagged `buy`, with the reason.
   - You may reword a flagged entry's `change` so it says *why* it's the sweet spot or why to beware. Keep it short and factual.
   - If there's no real consensus, use no `buy` flag at all rather than guessing. A page with zero flags is fine.
4. Make the page consistent: if the `verdict`, buying checks or FAQs name best or worst years, they must agree with the flags. Where it helps buyers, add or update one FAQ: "Which years are the best to buy?" Answer with sourced reasoning, in the site voice (direct, a little dry, Top Gear-ish, never invented).
5. Add every source you used to the page's `sources` list (`{"title","url"}`), or the detail file's `docs`/sources if that's where the page keeps them. Follow the existing schema exactly.

## Rules (hard)
- Never invent facts, years, numbers or URLs. Every claim needs a real source that you actually fetched.
- Never use olathetoyotaparts.com. Never link factory manuals on archive.org or other user-uploaded scan sites.
- Another agent may be editing repairs and mods on some pages at the same time. Re-load each file immediately before writing it, change only the fields you need, and write it straight back with `json.dump(d, f, ensure_ascii=False, indent=1)`. Never remove owner-supplied social or reading entries.
- Don't run `build.py` or git. Edit only your assigned pages.
- Use User-Agent `BoxyTrucksBot/1.0 (+https://boxytrucks.com)` and never put an email address in any header. Search is shared and limited, so prefer WebFetch or curl on known sources.

## Report
Write `reports/sweetspot/<group>.md`. For each page, list the flags before → after, the reason, and the sources. Your final reply is a short summary of what changed (especially flags that were wrong) and the report path.
