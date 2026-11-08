# Weekly metrics pull (every Monday, inside the Monday scoreboard run)

Hank, Nov 4, 2026: track views for everything and use them to judge what to do next. The numbers live in three JSON files in `social/metrics/` and feed the **BoxyTrucks Scoreboard** dashboard (https://claude.ai/artifact/VyjjikiZcDsbMntpk2VLGE).

## The files (append, never rewrite history)
- `posts.json`: one row per post per platform. Columns: post_id (the queue `n`, or `fn-<slug>` / `deal-<shop>`), platform (instagram, x, youtube, tiktok, pinterest), platform_name, date, title, format (single, carousel, reel; video on YouTube/TikTok), format_name, family (a data/*.json slug, or `multi`), pillar (buy, fix, fit, community, field-notes, deals), views, likes, comments, saves, shares, profile_visits, url, snapshot (date pulled). **Update each existing row in place** with the latest totals (and the new snapshot date); add rows for new posts.
- `followers.json`: one row per channel per week (week = that Monday's date), followers. Append the new week; keep old weeks.
- `site.json`: one row per measure per week (week, metric, label, value, period, source). Append. Measures: search_clicks, search_impressions, search_position, pages_indexed (Search Console, last 7 days); page_views, users (GA4, last 7 days); sessions_instagram, sessions_x, sessions_pinterest, sessions_youtube, sessions_tiktok, sessions_reddit, sessions_google (GA4 sessions by source, last 7 days); affiliate_clicks, newsletter_signups, deal_clicks, deal_code_copies (GA4 key events, last 7 days). Give every row a `label` in plain words.

- `revenue.json`: one row per program per month (month YYYY-MM, program, detail, earnings in USD, clicks, orders, status, source). Update the current month's rows in place each Monday (month to date); start new rows on the 1st. `status` is "Confirmed" once read from the program's own report, "Pending" for earnings the program hasn't locked yet (say so in detail), "Not read yet" if the report couldn't be reached, "Needs Hank sign-in" when the report is behind a login Claude can't do, "Site under review" while a program hasn't approved the site. Never estimate.

## Where each number comes from (Claude in Chrome; read only, change no settings)
- **Instagram**: for each post on instagram.com/boxytrucks, open the post and run `social/metrics/ig_insights.js` with javascript_tool. It clicks View insights and returns views, viewers, likes, comments, saves, shares, profile visits, link taps and the non-follower share. Brand-new Reels may show no insights yet; leave them for next week. Followers from the profile header. Confirm the account is @boxytrucks first.
- **X**: x.com/boxytrucks, scroll the timeline; each article's `[role=group]` aria-label holds its views. Followers from the profile.
- **YouTube**: studio.youtube.com (Boxy Trucks channel only) → Content → Shorts: views and comments per Short. Subscribers from the dashboard.
- **TikTok**: tiktok.com/tiktokstudio/content lists views, likes and comments per post. Followers from tiktok.com/@boxytrucks.
- **Pinterest**: per-pin numbers need a business account (Hank's call; it's an account change). Until then record followers only.
- **Revenue** (Hank asked Nov 4, 2026; read only, never change settings):
  - Amazon Associates: affiliate-program.amazon.com → Reports. Earnings for **tracking ID boxytrucks-20 only** (the account also holds pullabook-20, Hank's other site): Commissions tab grouped by Tracking ID, or Download Reports → Tracking ID summary. Month to date: earnings, clicks, items ordered.
  - CJ: members.cj.com → Reports → Performance (by advertiser), month to date: commissions, clicks, sales.
  - Sovrn Commerce: platform.sovrn.com → Commerce reports, month to date: estimated earnings, clicks.
  - eBay Partner Network: partner.ebay.com → Reports, campaign 5339233573, month to date: earnings, clicks.
  - Sponsors: data/sponsors.json (paid amount; free months are 0).
- **GA4** (property a401243700p560377838) and **Search Console** (sc-domain:boxytrucks.com): as in the scoreboard task.
- **Affiliate clicks by page** (optimization plan item 9, Nov 7, 2026): GA4 → Reports → Engagement → Events → `affiliate_click` (also `buybox_click`, `kit_click`, `gift_click`), add the secondary dimension "Page path" (and the `placement` parameter where set), last 7 days. Append one `site.json` row per page with clicks (metric `affiliate_clicks_page`, label "Affiliate clicks: <page path>"), top 10 pages only. In the weekly plan, say which placement (buy box at top, kit, deals, gift guide) earns the clicks and move links toward it.
- **Internal traffic**: from Nov 7, 2026 Hank's own visits are tagged `traffic_type=internal` and excluded once the GA4 data filter is Active (see GA4 Admin → Data filters). Note in the first scoreboard after the change that numbers dropped because of it, not because readers left.

## Publishing to the dashboard
1. Write the three files, validate them with `python3 -c "import json;json.load(open(...))"`, commit and push.
2. Upload each as an asset to the dashboard (Artifact publish with `url` + `asset: true` + `file_path`), then `ArtifactData update` the matching `datasets/<id>` document (posts, followers, site) with the new `source.url`, `source.name`, `updated: {at, by}` and `edit: {via: "claude", at}`. Delete the old asset after the update.
3. Don't change the page (`files/index.html`) unless Hank asks; its source is `social/metrics/dashboard-index.html`.

## Using it (the weekly planning run reads this first)
- Rank formats, truck families and topics by average views, and above all by **site visits and saves**. Views on new accounts are noisy, so a pattern needs at least 3 posts behind it.
- Each week, make at least one deliberate shift toward what's working (e.g. more Reels if video keeps beating stills, more of the best family) and write it in the plan with the numbers that justify it.
- After four weeks of data (from Nov 30, 2026), rebalance the weekly rhythm in STRATEGY.md and tell Hank what changed and why.
