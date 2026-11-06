# BoxyTrucks social strategy (Instagram + X)

Adopted Nov 1, 2026 at Hank's request: keep the single-image posts, but stop making them the only format. The goal is followers who come to the site, so every post earns a save, a share or a click.

## Why the mix changes
- Single-image reach on Instagram is falling: down about 22% year over year, with engagement down about 46% (Metricool 2026 study).
- Carousels get about 9x more saves than single images.
- Reels get more than 4x the interactions.
- Reels are ranked mostly on watch time. Sends (shares) matter most for reaching non-followers. 30–60 seconds is the sweet spot.

## Weekly rhythm (7 posts: 3 singles, 2 carousels, 2 Reels)
| Day | Format | What |
|---|---|---|
| Mon | Single image | One sharp buyer's fact: best years, a tire size, a known fault |
| Tue | Carousel | A list from the site: years by generation, a head-to-head, "5 checks" |
| Wed | Reel | Motion graphics (`social/reels/make_reel.js`), or Hank's own footage when there is some |
| Thu | Single image or carousel | **From Hank's garage** (weekly, from Nov 5): Hank's own trucks, repairs or trucks he spotted. If Hank hasn't sent material, ask him on Monday, and fall back to a reader rig or a question. Only run "show us your rig" posts when a real submission can be featured (and invite that owner as a Collab). |
| Fri | Carousel | Comparison or problems list |
| Sat | Reel | Hank's footage first (G500, 4Runner, lockers, repairs); otherwise motion graphics |
| Sun | Single image | A great off-road photo plus a question that invites comments |

Every post also goes to X 30 minutes later (see `X_POST_PROCEDURE.md`). **Every day goes to ALL five channels: Instagram, X, Pinterest, YouTube and TikTok** (Hank, Nov 2 and Nov 4, 2026). Image-only days get a short video version for YouTube and TikTok: pins for every guide post (`PINTEREST_PROCEDURE.md`), plus every Reel as a Short (`YOUTUBE_PROCEDURE.md`) and a TikTok (`TIKTOK_PROCEDURE.md`). On X, carousels post as up to 4 images and Reels as the MP4.

## Content pillars
1. **Buy it right:** best years, years to avoid, what to check. This is the core, and it links to the guides.
2. **Fix it:** common problems and DIY repairs, ideally from Hank's own trucks.
3. **Fit it:** tires, lifts and mods.
4. **The community:** reader rigs and stories, posted with Collab invites, and questions that start comments.

## Rules for every post
- **First line is a search phrase.** Instagram search reads captions, so use phrasing like "Land Cruiser 80 Series buying guide" or "Defender vs Grenadier vs G-Class".
- **3–5 specific hashtags**, never a block of 10. Pick from the truck's model tags plus #overland or #4x4.
- **One call to action.** "Save this", "Which would you buy?" or "Link in bio". The bio link goes to boxytrucks.com/links/, which always lists the latest three posts.
- **Credit every photo** on the image and in the caption. Use off-road photos only, never wrecks or breakdowns. Licenses: Unsplash, Pexels, public domain, CC0, CC BY, CC BY-SA.
- **Never use AI-generated images or video of a specific truck model.** Enthusiasts spot the wrong details, and it undercuts "sourced and real". Higgsfield is fine for generic atmosphere (a trail, dunes, weather) used as an intro or transition, and then the AI label must be on.
- **Facts come from the site's sourced pages.** Hank's first-hand notes are the strongest content we have, so use them when they fit.

## Formats and tools
- **Single image:** 1080×1350, made as before.
- **Carousel:** `node social/carousels/make_carousel.js social/carousels/<spec>.json`. Use 5–7 slides: a cover, one slide per item with its own photo, and a closing "save this" slide. In the queue, set `"format": "carousel"` and `"images": [...]`.
- **Reel:** `node social/reels/make_reel.js social/reels/<spec>.json`. Output is 1080×1920 MP4, 20–30 seconds, about 3.5 seconds per scene. Put the hook in the first frame and the call to action on the last scene. Use `"align": "top"` when the subject sits low in the photo. In the queue, set `"format": "reel"`, `"video"` and `"image"` (the cover).
- **Hank's video:** he drops phone clips (vertical, under 60 seconds) in a shared folder or attaches them. We add captions and the brand bar, then queue them.

## Engagement (this is what actually grows the account)
- **Every day, in the follow run:** check the newest 5 posts for comments we haven't answered.
  - Answer questions with facts from the site and a link to the page.
  - Thank people briefly and specifically.
  - Leave anything heated, political or about Hank personally for Hank.
  - Never argue. Log replies in `social/README.md`.
- **Hank, 10 minutes a day on his phone:** leave real comments on 5–10 posts from accounts we follow. Shops, clubs and builders matter most. Automated comments on other people's posts read as spam to Instagram and to people, so these stay human.
- **Collab:** when a post features a reader's rig or a shop, invite them as a collaborator (in the app) so it lands on their feed too.
- **Stories:** share each post to Stories the same day. This is app-only, so Hank does it on his phone; it takes about 10 seconds.
- **Pinned posts:** keep the three best performers pinned. Right now that's the G 500 years post, the free checklist post and 80 vs 100. Pinning is app-only.
- **Follows (changed Nov 3, 2026):** about **10 a day**, and only accounts we'd actually comment on: active owners, shops and clubs for our trucks (`FOLLOW_PROCEDURE.md`). Stop if Instagram shows a block. Mass following gained ~15 followers from ~140 follows and makes the account look spammy, so quality over count.

## Profile (updated Nov 1, 2026)
- **Name:** "Boxy Trucks | 4x4 Buying Guide". This field is searchable, and Instagram only allows changing it twice in 14 days.
- **Bio:** "Which year to buy, what breaks, what fits. / Land Cruiser · G-Wagen · Defender · Jeep · Bronco & more. / Free guides below. Tag us to get featured."
- **Website:** should be https://boxytrucks.com/links/. It's empty right now, and links can only be edited in the app, so Hank has to set it.

## Measuring it (every Monday)
**Since Nov 4, 2026:** per-post numbers from every platform go into `social/metrics/` and the BoxyTrucks Scoreboard dashboard; see `METRICS_PROCEDURE.md`. Weekly planning reads it first and shifts the mix toward what earns site visits and saves.

In Instagram's insights, note each post's reach, saves, shares and profile visits. In GA4, check sessions with source `instagram` (the links page tags its links with `utm_source=instagram`). After four weeks, shift the mix toward whatever earns the most saves and site visits.

## Review, Nov 3, 2026 (first week)
- **Working:** Hank's first-person posts (the G500 "mine's a 2007" post got the most interaction, plus our best comment), reach beyond followers (69% non-followers), and real comment conversations.
- **Do more:** a weekly "From Hank's garage" post; Reels and carousels; Story link stickers for site visits.
- **Cut:** mass follows (now ~10/day). **X on autopilot:** keep the automatic mirror of each post (1 follower, 3–15 views per post), but no extra time there; that time goes to Reddit and the forums (`FORUMS.md`). No empty "show us your rig" posts.
- Re-check against full per-post insights in the Monday scoreboard.

## Field Notes (Nov 3, 2026)
Every published Field Note gets its own social push the same day: an IG carousel, an X post with the link, a Pinterest pin, and a YouTube Short and TikTok from the reel. It runs on top of the regular daily post (Hank OK'd multiple posts a day). See FIELD_NOTES.md.

## Waiting on partners
- **Eurowise reader code (Nov 4, 2026):** the day the code arrives, make a social post for it (queue item `deal-eurowise`), add it to the site's deals spot and the next Dispatch. The code runs to Jan 4, 2027.

- **Second daily Short (Nov 5, 2026):** every evening, one "Biggest tire on a stock <truck>" Short on YouTube and TikTok, generated from site data. Queue `social/shorts.json`, procedure `SHORTS_PROCEDURE.md`. Each one links to that truck's /tires/ page.
- **Comment on every YouTube upload (Hank, Nov 5, 2026):** right after a video or Short goes up, comment and pin it as Boxy Trucks: friendly, more in-depth than the video, ask the audience a question, link the site. Step 7 of `YOUTUBE_PROCEDURE.md`.
