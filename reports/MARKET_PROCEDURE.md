# Market report (monthly) and for-sale picks (weekly)

Started Nov 25, 2026 at Hank's request ("do one through three on increasing traffic" and "add the weekly best boxy trucks for sale ... as a feature on the site and ... in our newsletter").

## Getting the data (Chrome, read-only)
Bring a Trailer's own pages are the source. WebFetch can't reach them, so use Chrome:
1. Open https://bringatrailer.com/auctions/results/ in a Claude tab.
2. **Results (monthly):** from that page, call `fetch('/wp-json/bringatrailer/1.0/data/listings-filter?page=N&per_page=36&get_items=1&get_stats=0&sort=td&base_filter%5Bkeyword_s%5D=<keyword>&base_filter%5Bitems_type%5D=listing', {headers:{'x-requested-with':'XMLHttpRequest'}})` for each keyword (g500, g550, g63, 250gd, 300gd, 230ge, land cruiser, fj cruiser, 4runner, defender, range rover, discovery, bronco, wagoneer, cherokee, scout, cj-5, cj-7, cj-8, grenadier, patrol, montero, pajero, trooper, samurai, jimny, hummer, unimog, pinzgauer, blazer, lx450, lx470, gx470, delica, ramcharger, wrangler, series iii). Stop paging when `timestamp_end` falls before the window. Store the items in `window.__all` keyed by id. Wait about 2.5 s between requests: BaT returns 429 if you go faster.
   - Fields: `title` (HTML entities: decode `&#215;` etc.), `sold_text` ("Sold for…" or "Bid to…"), `current_bid`, `currency`, `timestamp_end`, `url`. `year` is null, so parse the year from the title.
   - Group in the browser (regexes by generation, as in the Nov 2026 run) and read back only the aggregates: listed, sold, no-sale, median, low and high sale (USD only), plus the slug of the top sale. Tool output truncates at about 1,000 characters, so read it in small chunks.
3. **Live auctions (weekly picks):** `fetch('/auctions/')` and parse the JSON after `auctionsCurrentInitialData` (about 1,000 items). Filter to our trucks with auctions ending at least 2 days out, and pick 8 across families, mixing no-reserve and interesting lots. Skip replicas, charity or show trucks and Grand Cherokees.

## Writing it up
- **Monthly:** write `data/market/YYYY-MM.json`. Use the same shape as 2026-11.json: groups (fam, gen, label, listed, sold, no_sale, median, low, high), notable (top 10 sales, with the BaT URL), and 4–5 takeaways. Every number in a takeaway must come from the groups or notable entries. The page builds at /market-report/YYYY-MM/, and /market-report/ redirects to the newest one.
- **Weekly:** write `data/for-sale/YYYY-MM-DD.json` with 8 picks: title, url, bid, ends (UTC ISO), no_reserve, fam, gen, and a context line built only from the latest market report. The newest file shows on /for-sale/#picks.
- Then build, check both pages at 400 px, commit and push. Put the picks in the next Dispatch draft (NEWSLETTER.md "For sale this week").
- **Credit:** link to BaT and quote no listing text, only titles, prices and dates.

## Photos on the picks (Hank, Nov 25, 2026)
Each card shows our own licensed hero photo for that generation, captioned "Same model, not this truck · credit". We never use Bring a Trailer's listing photos. Before publishing, check every card's photo:
- No readable plates. If one is readable, blur it in the source under site/img/ and delete its site/img/_r/ variants.
- No parked, street or lot shots. If the generation only has parked photos (as with the GX 470 on Nov 25), swap that pick for a truck whose generation has an off-road photo.
