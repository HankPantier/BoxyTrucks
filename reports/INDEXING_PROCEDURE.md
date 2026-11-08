# Daily Search Console indexing requests

Hank, Nov 7, 2026 (optimization plan item 1): only ~73 of ~1,400 sitemap pages are indexed, so request indexing for the
highest-value pages, about 10 a day (Google's daily quota).

1. Open https://search.google.com/search-console?resource_id=sc-domain%3Aboxytrucks.com in Claude in Chrome.
2. Take the next 10 `todo` URLs from `reports/indexing-queue.json` (ordered: years, tires, problems pages, most-searched families first).
3. For each: focus the "Inspect any URL" box with JS (`input` whose aria-label contains "Inspect any URL"; `focus()` + `select()`),
   type the URL, Return, wait ~10 s. If it says "URL is on Google", set `status: "indexed"`. If "URL is not on Google",
   click the visible "Request indexing" button with JS, wait ~20–30 s for "Indexing requested", set `status: "requested"` and `date`.
   Close the dialog ("Got it") before the next one. Run one URL per browser batch (bigger batches time out).
4. Stop on "Quota exceeded" and leave the rest for tomorrow.
5. Commit `reports/indexing-queue.json` ("Indexing requests <date>: N") and push. No message to Hank unless something breaks.
