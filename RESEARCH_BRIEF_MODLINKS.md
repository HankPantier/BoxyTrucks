# Brief: tighten mod supplier links to model-specific pages

BoxyTrucks.com (repo `/home/claude/boxytrucks`): each model page's `mods` list has items `{"cat","why","who":[{"name","url"}]}`. Many `who` links point only at a company's homepage (for example `https://www.alcanspring.com/`). Readers have to dig to find the part for their truck. Your list file, `reports/modlinks-<X>.txt`, gives the page file, the category and the supplier's homepage URL for each one.

## For each link
1. Find that supplier's page for the **exact product or category for this model and generation**, matching the mod's `cat` and `why`. That could be the product page, the model's fitment or category page, or the supplier's vehicle-filtered listing. Try the supplier's site navigation, their sitemap (`/sitemap.xml`), or a site search URL.
2. Verify it before using it: curl it (HTTP 200, not a redirect to the homepage or a "not found" page) and check that the page actually names this model or generation. If the curl is blocked, WebFetch is fine.
3. Replace the `url`. If the specific page names a slightly different product, you may tweak `name` (for example "Alcan Spring custom leaf packs").
4. If the supplier has no page for this model (it's a custom shop, or the parts are made to order):
   - If the supplier makes custom parts for any vehicle (like Alcan, which builds springs to order), link their custom or quote page if one exists and mention "built to order" in the `why`.
   - If the supplier has no relevant offering for this model at all, replace them with a supplier that does have a verified model-specific page, or remove that `who` entry if the category still has another supplier. Never leave a category with an empty `who`.
5. Don't change anything else on the page.

## Rules (hard)
- Never invent URLs. Every URL must be fetched and checked.
- Never use olathetoyotaparts.com or goosegear.com (it's now a spam site).
- Amazon search links with tag `boxytrucks-20` are fine where they already exist. Don't convert direct suppliers to Amazon.
- Other agents are editing these files at the same time (timeline flags, FAQs). Re-load each JSON immediately before writing it, change only `mods[].who`, and write it straight back with `json.dump(d, f, ensure_ascii=False, indent=1)`. For family flagship files (`data/<family>.json`), the mods are under `page`.
- Don't run `build.py` or git.
- Use User-Agent `BoxyTrucksBot/1.0 (+https://boxytrucks.com)` and never put an email address in any header. Search is shared and limited, so prefer the suppliers' own sitemaps and navigation.

## Report
Write `reports/modlinks-<X>-done.md`: per page, old URL → new URL, plus anything replaced or removed and why. Your final reply is short: the counts (tightened, built-to-order, replaced, removed) and the report path.
