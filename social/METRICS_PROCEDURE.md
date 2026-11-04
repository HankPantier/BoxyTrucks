# Weekly metrics pull (every Monday, inside the Monday scoreboard run)

Hank, Nov 4, 2026: track views for everything and use them to judge what to do next. The numbers live in three JSON files in `social/metrics/` and feed the **BoxyTrucks Scoreboard** dashboard (https://claude.ai/artifact/VyjjikiZcDsbMntpk2VLGE).

## The files (append, never rewrite history)
- `posts.json`: one row per post per platform. Columns: post_id (the queue `n`, or `fn-<slug>` / `deal-<shop>`), platform (instagram, x, youtube, tiktok, pinterest), platform_name, date, title, format (single, carousel, reel; video on YouTube/TikTok), format_name, family (a data/*.json slug, or `multi`), pillar (buy, fix, fit, community, field-notes, deals), views, likes, comments, saves, shares, profile_visits, url, snapshot (date pulled). **Update each existing row in place** with the latest totals (and the new snapshot date); add rows for new posts.
- `followers.json`: one row per channel per week (week = that Monday's date), followers. Append the new week; keep old weeks.
- `site.json`: one row per measure per week (week, metric, label, value, period, source). Append. Measures: search_clicks, search_impressions, search_position, pages_indexed (Search Console, last 7 days); page_views, users (GA4, last 7 days); sessions_instagram, sessions_x, sessions_pinterest, sessions_youtube, sessions_tiktok, sessions_reddit, sessions_google (GA4 sessions by source, last 7 days); affiliate_clicks, newsletter_signups, deal_clicks, deal_code_copies (GA4 key events, last 7 days). Give every row a `label` in plain words.

## Where each number comes from (Claude in Chrome; read only, change no settings)
- **Instagram**: for each post on instagram.com/boxytrucks, open the post and run `social/metrics/ig_insights.js` with javascript_tool. It clicks View insights and returns views, viewers, likes, comments, saves, shares, profile visits, link taps and the non-follower share. Brand-new Reels may show no insights yet; leave them for next week. Followers from the profile header. Confirm the account is @boxytrucks first.
- **X**: x.com/boxytrucks, scroll the timeline; each article's `[role=group]` aria-label holds its views. Followers from the profile.
- **YouTube**: studio.youtube.com (Boxy Trucks channel only) → Content → Shorts: views and comments per Short. Subscribers from the dashboard.
- **TikTok**: tiktok.com/tiktokstudio/content lists views, likes and comments per post. Followers from tiktok.com/@boxytrucks.
- **Pinterest**: per-pin numbers need a business account (Hank's call; it's an account change). Until then record followers only.
- **GA4** (property a401243700p560377838) and **Search Console** (sc-domain:boxytrucks.com): as in the scoreboard task.

## Publishing to the dashboard
1. Write the three files, validate them with `python3 -c "import json;json.load(open(...))"`, commit and push.
2. Upload each as an asset to the dashboard (Artifact publish with `url` + `asset: true` + `file_path`), then `ArtifactData update` the matching `datasets/<id>` document (posts, followers, site) with the new `source.url`, `source.name`, `updated: {at, by}` and `edit: {via: "claude", at}`. Delete the old asset after the update.
3. Don't change the page (`files/index.html`) unless Hank asks; its source is `social/metrics/dashboard-index.html`.

## Using it (the weekly planning run reads this first)
- Rank formats, truck families and topics by average views, and above all by **site visits and saves**. Views on new accounts are noisy, so a pattern needs at least 3 posts behind it.
- Each week, make at least one deliberate shift toward what's working (e.g. more Reels if video keeps beating stills, more of the best family) and write it in the plan with the numbers that justify it.
- After four weeks of data (from Nov 30, 2026), rebalance the weekly rhythm in STRATEGY.md and tell Hank what changed and why.
