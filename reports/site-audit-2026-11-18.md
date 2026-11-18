# Weekly site audit — Nov 18, 2026

Second weekly audit. Previous: reports/site-audit-2026-11-11.md. Social numbers come from the Nov 16 scoreboard (reports/scoreboard.md).

## Numbers
**GA4, Nov 11–17 vs Nov 4–10** (the internal-traffic filter applies to both weeks)
- Sessions 235 (vs 232, flat). Views 363 (vs 309, +17%). Users 206 (flat).
- **Engagement rate 52% (vs 31%). Average engagement 59 s per session (vs 22 s).** Engaged sessions 123 (vs 72, +71%).
- By channel:
  - Organic Search 83 (flat), 65% engaged (was 37%), 1 m 30 s (was 26 s).
  - Direct 72 (vs 64).
  - AI assistants 51 (vs 55).
  - Organic Social 27 (vs 28), 74% engaged, 42 s.
  - Organic Video 2: the first sessions from YouTube, 3 m 13 s.
- Top pages:
  - Home 58 views. **Engagement 25 s, up from 6 s**, so the Nov 10 redesign is working.
  - /links/ 8 (3 s), G500 guide 8, /submit/ 7 (1 m 22 s), /tires/ 7, Hummer H1 6, G-Class family 5, G-Class best years 5, 80 Series 5, GX550 12V battery repair 5.
- Events:
  - affiliate_click 8 (vs 4), from only 4 users.
  - click 24 (vs 6). scroll 54 (vs 29). form_start 6. rig_submission 1.
  - newsletter_signup 0.
  - Revenue $0.

**Search Console** (last 7 days to ~Nov 16, vs the 7 days before)
- 98 clicks (vs 67, +46%) and 7.37K impressions (vs 4.39K, +68%). CTR 1.3% (vs 1.5%). Average position 12.0 (vs 13.6).
- Indexing:
  - **1.31K pages indexed, 102 not indexed** (75 Discovered, 14 Crawled-not-indexed, 7 canonical alternates, 3 noindex, 3 redirects). On Nov 5 it was 784 indexed and 619 not indexed.
  - Google read the sitemap on Nov 17: 1,072 URLs, success. Last week's move 3 (resubmit) is no longer needed.
- **/best/boxy-suvs/ went backwards after the Nov 12 retitle:** 181 impressions at position 14.5 (vs 360 at 11.9), 1 click (vs 6). "boxy suvs" fell from 157 impressions to 101, at position 10.4 (was 9.3). Over 28 days it's still the top page (553 impressions at 12.7).
  - Old title: "Boxy SUVs: Every Boxy 4x4 You Can Buy, New & Used".
  - New title: "Boxy SUVs: The Best Boxy 4x4s to Buy, New & Used".
- **/models/g-class/best-years/ moved up** to position 7.0 (from 8.9), 131 impressions, 2 clicks. "g wagon years to avoid" had 43 impressions over 28 days at position 6.8, with 0 clicks.
- Pages close to page 1 with few or no clicks (28 days):
  - Y60 guide 164 impressions at 11.5
  - Y61 years 141 at 6.7
  - **LX 470 years 135 at 6.9, 0 clicks**
  - **Unimog U1300L specs 117 at 6.4, 0 clicks**
  - Trooper II 100 at 12.3
  - Y61 specs 99 at 9.9
  - 1st-gen K5 Blazer 93 at 11.9
  - 80 vs 100 compare 88 at 8.0
- New this week: the Patrol best-years page got 70 impressions at position 5.5 (3 clicks). The GX550 12V battery repair got 33 at 6.2 (3 clicks, 9% CTR). Two Jimny JB23 repair guides each got 2 clicks.
- Queries still without a page that ranks for them:
  - "fj40 brake conversion kit": 19 impressions, position 37.8
  - "nissan patrol y62": 13, position 47
  - "k5 blazer": 13, position 30
  - "jeep yj": 12, position 80

**Social** (Nov 16 scoreboard)
- Followers: Instagram 53 (+10), YouTube 4 (+3), TikTok 1 (paused), X 0, Pinterest 0.
- Cumulative views 13,964 (vs 5,651).
- Hank's own-truck videos do best: they average 714 views across platforms, vs 405 for tire Shorts.
- Social still sends little traffic (27 sessions), but it's the best-quality traffic on the site.

**Revenue:** $0. 8 affiliate clicks, mostly on repair pages last week. carVertical is still waiting on Hank. FlexOffers declined on Nov 12.

**Crawl of site/:** 2,769 HTML files.
- No broken internal links.
- Every indexable page has a title, a meta description and one H1.
- The one duplicate title was the old /watch/ redirect stub, which reused the Resources title. Fixed this run.

## What changed since Nov 11
- Home engagement went from 6 s to 25 s, and site-wide from 22 s to 59 s. The redesign, the short-version cards and the photos are keeping people on the page.
- Search clicks are up 46% and impressions up 68%. Indexed pages went from 784 to 1.31K.
- The Nov 12 search changes had mixed results:
  - G-Wagon best-years moved up (8.9 → 7.0).
  - /best/boxy-suvs/ fell (11.9 → 14.5, impressions halved). One week is noisy, but it's the site's top page.
- Last week's moves done: 1 (boxy SUVs short answer, FAQ, links), 6 (fluid quick answers on specs pages), 8 (repair deepening; the queue is finished), 10 (checklist signup at the top of years and problems pages). Not done: 2 (years in the family best-years titles; they went into the per-generation years pages instead), 5 (TikTok, now paused), 9 (affiliate sign-ins).

## Done this run (safe fixes)
- /watch/ redirect stub: added noindex and a canonical to /resources/, and gave it its own title. It no longer duplicates the Resources title.

## 10 best next moves
**Traffic**
1. **Restore the /best/boxy-suvs/ title to "Boxy SUVs: Every Boxy 4x4 You Can Buy, New & Used"** and keep the new short answer and FAQ. Impressions halved and position fell 2.6 places in the week after the retitle, on the site's biggest page. Effort: 5 minutes, then check again next week. *Needs your OK (it reverses a change from last week).*
2. **Get clicks on pages already at positions 6–7 with 0% CTR:** LX 470 years (135 impressions) and Unimog U1300L specs (117). Rewrite the description to lead with the answer: the best year and the avoid years for the LX; the oil type and capacity for the U1300L. Effort: 30 minutes. *I can do this.*
3. **Write a G-Wagon-specific best-years title with the years in it,** e.g. "G-Wagon Years to Avoid (2002–04) & Best Years (2005–08)". It now ranks 7.0 for "g wagon years to avoid" with 0 clicks out of 43 impressions. Effort: 15 minutes. *I can do this.*

**Audience**
4. **More of Hank's own-truck footage.** It's the best-performing format on every platform (714 views on average), and YouTube has now sent its first 2 sessions, at 3 m 13 s each. *Needs you to film.*
5. **Fix /links/: 8 visits at 3 s each.** People land there from Instagram and leave. Put "the guide for the truck you just watched" as a single large card at the top, driven by the newest post. Effort: 1 hour. *I can do this.*

**New content**
6. **An FJ40 disc brake conversion kits section** (19 impressions, the query with the most impressions and no page). Add it to the FJ40 brakes repair guide or as its own page, compared from published kit specs. Effort: half a day. *I can do this.*
7. **Strengthen the Y62 and 1st-gen K5 pages for their head terms** ("nissan patrol y62" at position 47, "k5 blazer" at 30). Add a short answer, a specs table up top, and links from the family pages. Effort: 2 hours. *I can do this.*

**Better content**
8. **Lift the Y60 guide (164 impressions at 11.5) and Trooper II (100 at 12.3) onto page 1.** Add a short-version box, years-to-avoid links and photos where they're missing. Effort: 1 hour. *I can do this.*

**Revenue**
9. **Affiliate unlocks need you:** the carVertical sign-up (a VIN-check affiliate that fits every years page), the CJ sign-in so I can read Parts Geek and Eastwood stats, and the 27 drafted sponsor and parts follow-ups. Revenue is still $0. *Needs you.*
10. **Put the parts buy box on the repair pages Google is starting to send traffic to** (the GX550 12V battery and the two Jimny JB23 guides). Repair pages produce most of the affiliate clicks. Effort: 1 hour. *I can do this.*
