# Weekly site audit — Nov 11, 2026

First weekly audit (Hank, Nov 7). Baselines: reports/optimization-2026-11-07.md, reports/scoreboard.md (Nov 9), reports/site-review-2026-11-10.md.

## Numbers
**GA4, Nov 4–10 vs Oct 28–Nov 3** (internal-traffic filter active from Nov 7, so Direct is not comparable)
- Sessions 232 (vs 202, +15%), users 206 (+19%), views 309 (−19%), engagement rate 31% (vs 34%), 22 s per session (vs 28 s).
- By channel: Organic Search 83 (vs 9, ×9), Direct 64 (vs 95; filter), AI assistants 55 (vs 81, −32%), Organic Social 28 (vs 15, +87%, 61% engaged, 41 s, best quality), Referral 0.
- Top pages: home 50 views (6 s; before the Nov 10 home redesign), G500 guide 10 (1 m 30 s), /links/ 8, G-Class family 8, Y60 7, /deals/ 6, CJ-5 6, Grenadier years 5, Pajero Gen 2 5, /best/boxy-suvs/ 4.
- Events: affiliate_click 4 (vs 15, which included tests), form_submit 3, newsletter_signup 0, deal clicks 0. Revenue $0.

**Search Console**
- Last 7 days (to Nov 9): 67 clicks, 4.39K impressions, CTR 1.5%, average position 13.6 (Nov 1–7: 50 clicks, 3,180 impressions, position 14.0).
- Indexing (report data to Nov 5): 784 indexed, 619 not indexed (590 Discovered, 21 Crawled). Sitemap last read Nov 5, before Nov 10's change that took 332 thin repair pages out of the sitemap (1,401 → 1,069 URLs).
- Daily spot-checks: 7 of 8 queued pages checked today were already indexed, so the queue mostly lags behind Google.
- Pages close to page 1 (28 days): /best/boxy-suvs/ 372 impressions at position 11.9 (CTR 1.9%); /models/g-class/best-years/ 208 at 9.5 (2.4%); Trooper II 68 at 9.8; Y61 years 72 at 6.1; Y60 specs 65 at 10.7; 1st-gen K5 Blazer 60 at 13.6; Hummer H1 50 at 18.3.
- Queries with impressions and no page that answers them directly: "fj40 brake conversion kit" (19), "g wagon years to avoid" (18, page at ~9), "jeep tj years to avoid" (7), "5th gen 4runner oil capacity" (5, position 9.8), "prado 150 series" (5, position 58).

**Social** (scoreboard Nov 9): Instagram 43 followers, X 1, YouTube 1, TikTok 1, Pinterest 0. Video views are high (YouTube 3.5K) but send almost no site visits. TikTok has silently dropped 4 uploads since Nov 9.

**Revenue:** $0. Amazon 0 orders; CJ (Parts Geek, Eastwood) needs Hank to sign in to read stats; Sovrn under review; FlexOffers re-check tomorrow; carVertical sign-up waiting on Hank.

## Done this run (safe fixes)
- Replaced 475 visible "[CONFIRM IN MANUAL]"-style placeholders across 116 data files with plain reader-facing wording, e.g. "(check your manual)" or "(confirm by VIN)". Zero placeholders remain on built pages.
- Yesterday (site review): EU-only cookie banner, mobile tire cards, photos on years/tires/problems pages, short-version card on guides, shorter home page, searchable repairs index, 332 thin repair pages noindexed and folded into problems pages, 10 repair guides deepened so far (5 today), number plates blurred in 3 photos.

## 10 best next moves
**Traffic**
1. **/best/boxy-suvs/ to page 1** (372 impressions at 11.9; "boxy suvs" alone 157). Add a "best boxy SUVs to buy right now" short answer and a sortable table at the top, FAQ schema for "what is the boxiest SUV", and links to it from every family page. Effort: half a day. *I can do this.*
2. **Put the years in best-years titles** (G-Wagon best-years: 208 impressions at 9.5, CTR 2.4%; "g wagon years to avoid" 18). Example: "G-Wagon Years to Avoid (2002–04) & Best Years (2005–08)". Applies to all 21 family best-years pages. Effort: 1 hour. *I can do this.*
3. **Resubmit the sitemap in Search Console** so Google picks up the slimmer 1,069-URL sitemap (last read Nov 5). Effort: 2 minutes. *Needs your OK (Search Console action).*

**Audience**
4. **Organic social is the best-quality traffic** (61% engaged, 41 s vs 31% / 22 s site-wide) but it's small (28 sessions). Keep the daily cadence, and add the matching page link to every Story (reminder already runs at 1:13 pm).
5. **TikTok has dropped 4 uploads with no error.** Check the TikTok app for an account warning or restriction. *Needs you.*

**New content**
6. **Answer the specific queries we already get impressions for:** a "5th Gen 4Runner oil capacity" answer box on its specs page (position 9.8), "Jeep TJ years to avoid" on the TJ years page, and an "FJ40 disc brake conversion kits compared" section (19 impressions; the repair guide was deepened yesterday). Effort: half a day. *I can do this.*

**Better content**
7. **Measure the Nov 10 home redesign next week.** The home page had 50 views at 6 s average engagement, before the redesign shipped.
8. **Keep deepening repair pages,** 5 a day: 35 of the 40 in-demand ones are left.

**Revenue**
9. **Affiliate clicks are tiny** (4 this week) and so is revenue ($0). The fastest unlocks need you: sign in to CJ so I can read Parts Geek and Eastwood stats, sign up for carVertical (free, VIN-check affiliate, a natural fit for every years page), and send the 27 drafted sponsor and parts follow-ups in the tracker. *Needs you.*
10. **Newsletter: 0 real sign-ups.** Make the free printable inspection checklist the hook at the *top* of years and problems pages (the highest-intent search landings), not mid-page. Effort: 1 hour. *I can do this.*
