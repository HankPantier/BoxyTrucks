# Phase 2 — build out every generation

Read `/tmp/claude-0/-home-claude/6228804b-c069-5f1b-bd5e-d35edcda73bc/scratchpad/bt/RESEARCH_BRIEF.md` first: the hard rules, tooling notes, voice and the `page` schema all still apply.

Differences for this phase:

1. You are writing deep pages for SPECIFIC generations (listed in your task). For each one, write ONLY the `page` object (same schema as the brief's `page`, no `family` wrapper) to:
   `/tmp/claude-0/-home-claude/6228804b-c069-5f1b-bd5e-d35edcda73bc/scratchpad/bt/data/pages/<family-slug>/<gen-slug>.json`
   (create the folder). `page.slug` must equal the gen slug. Do NOT edit `data/<family>.json` — read it for context (the family's generation list, years, AutoTempest/BaT URLs, and the existing example page for tone/format).

2. BUDGET: web searches are a SHARED, limited pool across many parallel agents. Use at most ~35 WebSearch calls per generation page. Prefer WebFetch on known-good sources (Wikipedia pages, a forum's FAQ/sticky threads, enthusiast shops' buyer guides, Hagerty, BaT model pages) over extra searches. Don't search for photos unless you still have budget after the content is done.

3. PHOTOS: First reuse photos already in `site/img/<family-slug>/` (list the folder; you may reuse any, captioning honestly which generation is shown). Only add new photos if you find an OFF-ROAD photo of the actual generation; save into the same folder with a unique descriptive name. `hero_photo` must be a file that exists in `site/img/<family-slug>/` (or null).

4. SOCIAL on each page: include real YouTube channels and Instagram accounts that focus on THIS generation (or the family, if that's all you can find), each verified by appearing in a search result or by fetching the URL. Format: `{"kind": "YT"|"IG", "name": "@handle or channel name", "focus": "SHORT CAPS FOCUS", "url": "https://www.youtube.com/@... | https://www.instagram.com/.../"}`.

5. If your task says you own the family RESOURCES, also write `/tmp/claude-0/-home-claude/6228804b-c069-5f1b-bd5e-d35edcda73bc/scratchpad/bt/data/resources/<family-slug>.json`:
```json
{
  "youtube":   [{"name": "Channel name", "url": "https://www.youtube.com/@...", "focus": "What it covers (one line)"}],
  "instagram": [{"name": "@handle", "url": "https://www.instagram.com/handle/", "focus": "What it posts (one line)"}],
  "forums":    [{"name": "", "url": "", "note": ""}],
  "other":     [{"name": "Club / registry / parts catalog / manual source", "url": "", "note": ""}]
}
```
   Aim for 5–10 YouTube, 5–10 Instagram, 3–6 forums, 3–6 other (owners' clubs, registries, parts catalogs, factory manual sources, model-specific buyer's guides). Only real, verified entries. Quality builders, overlanders and wrenching channels — not dealership spam or street/flex accounts.

When done, reply briefly: files written, counts per page (faq/repairs/photos/social), anything unverified.
