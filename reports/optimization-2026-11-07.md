# Metrics review and optimization plan (Nov 7, 2026)

Window: Oct 31 – Nov 6 (GA4), Oct 29 – Nov 4 (Search Console, 2-day lag), platform dashboards as of Nov 7 morning.

## Numbers
- Site (GA4): 188 sessions, 163 users, 296 views, 36% engaged, 23s average engagement. Sources: ChatGPT 77, direct 49, Google 33–35, social 28 (t.co 19, Instagram 4), Bing 1.
  Caveats: includes Hank's and Claude's own checks (G500 page: 10 views from 2 users) and data-centre traffic (Council Bluffs, Ashburn).
- Key events: 10 affiliate_click (some are tests), 3 form_submit (rig form tests). Newsletter: 1 subscriber (Hank). Revenue: $0 confirmed.
- Search Console: 17 clicks, 1.4K impressions, CTR 1.2%, average position 12.8. 73 pages indexed of 1,399 in the sitemap (19 known but not indexed).
  Best impressions: /best/boxy-suvs/ (99), /models/g-class/best-years/ (99); "years to avoid" queries rank ~5–10.
- YouTube: 2,064 views in 28 days, 1 subscriber. Tire Shorts lead: G500 352, 80 Series 301 (in ~13 h), garage 301; buying-check Shorts 178–366; 4th Gen 4Runner checks 19.
- TikTok: 75–263 views per post; the Eurowise deal post has 0 (likely held for review as promotional).
- Instagram: 36 followers, 212 following; 2–5 likes a post. X: 1 follower, 2–31 views a post.

## Plan
Traffic
1. Indexing is the ceiling: request indexing in Search Console for the top best-years and tires pages (about 10 a day), and send the pending link asks (Hummer Club, Battle Born Cruisers, Upstate Cruisers) for the first backlinks.
2. YouTube: the tire series is the winner. Keep it daily; test a third daily Short drawn from the same data ("Years to avoid: <truck>") once the tire queue shows a pattern. Re-title or re-cut the 4th Gen 4Runner checks Short.
3. TikTok: check the Eurowise post (0 views); keep promotional posts off TikTok, or make them useful first and promotional second.
4. Instagram: Reels of the tire Shorts now run daily; feature submitted rigs as Collab posts so they reach the owner's followers.
5. X stays on autopilot (lowest return).
Engagement
6. Home page: 52 views, 10s average. Lead with the best-years tool and the 5-question quiz above the fold.
7. Newsletter: no real signups. Add an inline "free <truck> inspection checklist" signup in the middle of every best-years page (the highest-intent search landing pages), not only at the foot.
Revenue
8. The fastest money is reader codes and sponsors: Hank sending the 27 drafted follow-ups in the tracker.
9. Put the buy box (inspect kit + first-service parts) at the top of best-years pages for search visitors, and check affiliate clicks by page in the Monday scoreboard.
Data hygiene
10. Exclude internal traffic in GA4 (Admin → Data streams → Configure tag settings → Define internal traffic, Hank's IP) so the scoreboard reflects real readers.

## Status (Nov 7, 2026, evening; Hank: "tackle all of optimization-2026-11-07.md")
1. Done: indexing requested for 10 high-value pages (G500, 80 Series, Defender, 4th Gen 4Runner, early Bronco years; 80 Series, G500, 3rd Gen 4Runner tires; W463 and 80 Series problems), all "Discovered – currently not indexed". `reports/indexing-queue.json` holds the next 271; a scheduled task requests 10 more every morning (11:17 am ET). Link asks: waiting on Hank's OK to send (item 8).
2. Done: 4th Gen 4Runner Short retitled ("Don't buy a 4th Gen 4Runner until you check these 5 things (the $4,000 V8 problem)"). New third daily Short series "Years to avoid" (11 trucks, reasons from the sourced timelines), first post tomorrow at 12:37 pm ET, daily after.
3. Done: the Eurowise TikTok is public but held back (0 views). New rule in TIKTOK_PROCEDURE.md: no codes in TikTok posts; useful first, deal in a comment, Content disclosure on for brand posts.
4. Done: Collab-post rule for featured rigs (RIG_ASKS_PROCEDURE.md step 8).
6. Done: home hero now leads with a "Years to avoid" truck picker and the quiz; the years-to-avoid chips moved up above the shopping band; hero shorter.
7. Done: inline "free inspection checklist" signup now mid-page on every generation guide (before "What to check before you buy") and every problems page (best-years and years pages already had it).
9. Done: what-to-buy box near the top of every per-generation years page (family best-years and guide pages already had it). Monday scoreboard now records affiliate clicks by page (METRICS_PROCEDURE.md).
10. Done: GA4 internal traffic rule "Hank home" (153.66.109.170/32) and the Internal Traffic data filter is Active. If Hank's home IP changes, update the rule.
8. Waiting on Hank: send the drafted follow-ups and link asks.
