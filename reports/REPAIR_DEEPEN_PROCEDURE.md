# Deepen the repair pages people search for (from Nov 10, 2026)

Hank, Nov 10, 2026: "fix them all" (site review item 1). 332 thin repair pages with no Search Console impressions were taken out of Google (noindex, follow; out of the sitemap; listed in `data/repair_noindex.json`) and their fixes folded into each truck's problems page ("How to fix them"). The 40 repair pages that do get impressions are queued in `reports/repair-deepen-queue.json` to be deepened, 5 a day.

## Daily run (1:47 pm ET)
1. In `/home/claude/boxytrucks`: `git remote set-url origin https://github.com/HankPantier/BoxyTrucks.git`, then `git pull`.
2. Take the next 5 `todo` items. Each path is `<family>/<gen>/<repair slug>`; the repair lives in `data/pages/<family>/<gen>.json` → `repairs[]` (match by title; the slug is made from the title by `repair_slug`).
3. Research each with WebSearch/WebFetch: owner forums (IH8MUD, Expedition Portal, TacomaWorld/T4R.org, JK/JL/WranglerForum, Patrol4x4, LR4x4, G-Class forums), specialist shops and parts suppliers. Never olathetoyotaparts.com or goosegear.com; no archive.org.
4. Add, only from sources: `know` (3–5 "before you start" points: which years/engines, parts that differ, what to check first), a fuller `fix` (one action per sentence, in order; the build splits steps on sentences), `mistakes` (3–5), `cost_note` (parts and shop prices with who quotes them), and `refs` (2+ sources, name + url). Keep `title`, `diff`, `time`, `cost`, `tools`, `parts` unless a source corrects them. Plain words, no invented torque figures or part numbers.
5. Target 600+ words on the built page. Build (`python3 build.py`), check the page, set the item `status: "done"`, `date`, `words_after`. If the path is in `data/repair_noindex.json`, remove it (it now earns its place in Google).
6. Commit ("Deepen repair pages: …") and push. Tell Hank only if something breaks. When the queue is empty, re-pull Search Console (Performance → Pages, filter `/repairs/`, 3 months) and queue the next 40 by impressions, and re-check whether any noindexed page has started to earn impressions on other URLs of the same truck.
