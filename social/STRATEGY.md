> **Nov 23, 2026: TikTok is back on (Hank). Post every video to TikTok too; see TIKTOK_PROCEDURE.md.**

> **Nov 24, 2026 plan update (Hank: "modify our social media plan as per your suggestions"). This overrides older sections where they conflict.**
> 1. **X is off.** No daily posts and no Friday round-up from Nov 27. The only exception is the Thanksgiving post Hank asked for on Nov 26. Reason: 75 X posts sent 0 site sessions and 0 followers. Keep the @boxytrucks account and its pinned post; don't delete anything.
> 2. **Instagram mix: Reels only.** Each week: 3 reader-rig Reels (as owners submit; the rig-ask run feeds this), 2 "By the numbers" data-hook Reels, plus years and tire Reels on the other days. Spec sheets, stacks and single images go to Pinterest only.
> 3. **"From Hank's garage" weekly clip.** Every Monday the planning run asks Hank for one 15–30 second phone clip of his own trucks (a job, a walkaround, a sound). That clip gets the Thursday slot. If none arrives, use a reader rig.
> 4. **Collab every rig and shop post.** When a Reel features someone's truck or shop, add them with "Add collaborators" on the final Instagram screen before Share, so it posts to both feeds. Log `ig_collab` on the queue item.
> 5. **First 15 minutes after each post.** Hank replies to the first comments from his phone. The daily follow run drafts replies for anything still unanswered (facts from the site only) and posts them as @boxytrucks.
> 6. **Every caption names its page and has a short link.** Line 1 is the hook. Line 2 is `→ boxytrucks.com/r/<code>`. Add the code to `data/shortlinks.json` (`{"code": {"to": "/path/"}}`) before posting. Each `/r/<code>` redirects to the page with `utm_campaign=<code>`, so GA4 shows which post sent each visit. Use the same short link on that day's Story sticker and in the pinned YouTube comment, and replace "link in bio" with it.
> 7. **TikTok and YouTube Shorts** get every Reel. TikTok captions use the short link as text, and YouTube Shorts stay as they are.

# BoxyTrucks social strategy (Instagram + X)

Adopted Nov 1, 2026 at Hank's request: keep the single-image posts, but stop making them the only format. The goal is followers who come to the site, so every post earns a save, a share or a click.


## Refinement, Nov 9, 2026: grow followers AND send people to the site
**What the first scoreboard showed:** 4,436 YouTube/TikTok views → 0 site visits. That's not a content problem: **links in Shorts descriptions and comments aren't clickable** (YouTube policy), TikTok bio links need 1,000 followers or a Business account, and Instagram captions don't link. Views come from Shorts; visits come only from places where a link can be tapped. So every post now has a job: *Shorts and Reels earn followers; a clickable surface turns them into visits.*

**Clickable surfaces, and how we use each one**
| Surface | Clickable? | Plan |
|---|---|---|
| YouTube Shorts description/comment | No | Keep the URL on line 1 anyway (people type it), but set every Short's **Related video** to the weekly long-form video |
| YouTube long-form description + pinned comment | Yes (after advanced features, applied Nov 9) | Weekly long-form video, links to every page it covers, timestamps |
| YouTube channel links (up to 14) | Yes | boxytrucks.com + /links, tires, best years (Hank to OK) |
| Instagram Stories link sticker | Yes, all accounts | **One Story a day** with a link sticker to the exact page of that day's post (Hank, phone, ~1 min) |
| Instagram bio (/links) | Yes | Keep the latest post first; deals and YouTube below |
| Pinterest pins | Yes, every pin | **Biggest untapped lever**: from ~1 to 5 fresh pins a day (2:3 images built from site data: years to avoid, biggest tire, problems), keyword titles, one board per family |
| X posts | Yes, but X buries link posts | Image/video post with no link, then the link as the **first reply** |
| TikTok bio | Needs 1,000 followers or a Business account | Check the free Business switch (Hank's call) |

**Followers**
- **Series, not one-offs.** "Biggest tire on a stock ___" (5 a week) and "___ years to avoid" (daily) with the same hook, look and "follow for the next truck" end card. Series give people a reason to follow.
- **Hank's own trucks weekly** ("From Hank's garage" was the top Instagram post and the only post-driven follow). The weekly long-form leans on this too.
- **Other people's audiences:** rig asks (5 a day), Instagram **Collab** posts for every featured rig, comments on 10 accounts a day, and **Trial Reels** (shown to non-followers first) for new formats.
- **Cut:** question-only singles (13–38 views) and code/deal videos (0 on TikTok). Deals live in Stories, /links and the newsletter.
- Reply to every comment within a day, with a question back.

**Targets for Dec 31, 2026** (from Nov 9): Instagram 43 → 150 followers; YouTube 1 → 100 subscribers; site sessions from social 28 → 150 a week; Pinterest 0 → 50 sessions a week. Checked every Monday in the scoreboard.

## Weekly long-form video (from Nov 2026)
- **Format:** "The ___ buyer's guide" (6–8 minutes): best and worst years, what breaks, biggest tire, prices, 16:9, chapters. Built from the site page it links to, using licensed site photos, spec cards, maps and Hank's own footage where it exists.
- **Voice:** Hank, reading a script Claude writes from the page (about 900–1,100 words, one take in Voice Memos, ~10 minutes of his time, dropped in the Mac's BoxyTrucks/voice folder). No AI voices: YouTube's monetization rules penalize mass-produced or synthetic narration, and his voice is what makes it ours.
- **Pipeline:** Claude writes the script on Monday, Hank records Tuesday or Wednesday, Claude cuts it (16:9 version of make_reel.js plus the voice track, captions, chapters), uploads Thursday with clickable links in the description, then points that week's Shorts' Related video at it.
- **Monthly variant:** "From Hank's garage" filmed on his phone (a walkaround or a job on the G500 or 4Runner); Claude edits.
- **Why it matters:** clickable links, watch hours toward the Partner Program (4,000 hours; long-form counts, Shorts don't), and a home for the Shorts traffic.

## Numbered series (Hank, Nov 23, 2026: "i do like the numbered series")
Borrowed from @the_landcruisers_official ("FROM JAPAN #026"). Every recurring format gets a running number so posts read as a collection worth following.
- Number in the hook line of the caption, the Pinterest/YouTube title and, from the next render on, a small "#NN" badge on the cover image or first frame: e.g. "Years to avoid #07: 100 Series", "Spec Sheet #04: FJ62", "Biggest tire #12: Jimny JB74", "From Hank's garage #01".
- Count continues from what has already posted in that series (count the posted items in its queue file); never renumber or skip.
- Keep the running count in the queue item as `series` and `series_no` so the next draft can read it.
- One-offs (Field Notes, media kit, holiday posts) stay unnumbered.
- The weekly planning run sets this up first (Nov 24) and adds the badge to the spec sheet, tire Short and years Short templates.

## Why the mix changes
- Single-image reach on Instagram is falling: down about 22% year over year, with engagement down about 46% (Metricool 2026 study).
- Carousels get about 9x more saves than single images.
- Reels get more than 4x the interactions.
- Reels are ranked mostly on watch time. Sends (shares) matter most for reaching non-followers. 30–60 seconds is the sweet spot.

> **Nov 24, 2026 mix change (weekly planning, from the Nov 23 scoreboard): Instagram gets Reels only.** Spec sheets, spec stacks and single-image posts go to Pinterest only, not Instagram, because 15 singles averaged 44 IG views and 17 carousels 58, against 2,227 for the 2 reader-rig Reels, 884 for the 3 data-hook Reels, 141 for 9 years Reels and 117 for 17 tire Reels. Targets per week: 3 reader-rig Reels (when owners submit), 2 data-hook Reels ("By the numbers #NN": one surprising, sourced number from our pages, voice B), and years-to-avoid Reels. Carousels stay only for Hank's own trucks. This overrides the weekly rhythm table below until the Nov 30 rebalance.

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

**X is a weekly round-up only (Hank, Nov 14, 2026)**: nothing posts to X day to day; one Friday post sums up the week (see `X_POST_PROCEDURE.md`). **Every day goes to the other four channels: Instagram, Pinterest, YouTube and TikTok** (Hank, Nov 2 and Nov 4, 2026). Image-only days get a short video version for YouTube and TikTok: pins for every guide post (`PINTEREST_PROCEDURE.md`), plus every Reel as a Short (`YOUTUBE_PROCEDURE.md`) and a TikTok (`TIKTOK_PROCEDURE.md`). On X, carousels post as up to 4 images and Reels as the MP4.

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
- **Cut:** mass follows (now ~10/day). **X cut to a weekly round-up (Nov 14):** 1 follower, 1–4 views per post and 6 site visits a week didn't justify daily posts; that time goes to Reddit and the forums (`FORUMS.md`). No empty "show us your rig" posts.
- Re-check against full per-post insights in the Monday scoreboard.

## Field Notes (Nov 3, 2026)
Every published Field Note gets its own social push the same day: an IG carousel, a Pinterest pin, and a YouTube Short and TikTok from the reel. It runs on top of the regular daily post (Hank OK'd multiple posts a day). See FIELD_NOTES.md.

## Waiting on partners
- **Eurowise reader code (Nov 4, 2026):** the day the code arrives, make a social post for it (queue item `deal-eurowise`), add it to the site's deals spot and the next Dispatch. The code runs to Jan 4, 2027.

- **Second daily Short (Nov 5, 2026):** every evening, one "Biggest tire on a stock <truck>" Short on YouTube and TikTok, generated from site data. Queue `social/shorts.json`, procedure `SHORTS_PROCEDURE.md`. Each one links to that truck's /tires/ page.
- **Comment on every YouTube upload (Hank, Nov 5, 2026):** right after a video or Short goes up, comment and pin it as Boxy Trucks: friendly, more in-depth than the video, ask the audience a question, link the site. Step 7 of `YOUTUBE_PROCEDURE.md`.

## YouTube monetization: a goal to keep working toward (Hank, Nov 6, 2026)
Not a core goal, but revenue needs several streams (sponsors, affiliates, reader codes, YouTube ads), so keep moving the channel toward the Partner Program.
- Now: 1,000 subscribers + 4,000 public watch hours in 12 months, or 10M Shorts views in 90 days.
- From Feb 1, 2027 (new applicants): 1,000 subscribers + 8,000 watch hours, or 20M Shorts views in 90 days.
- Where we are (Nov 6): 1 subscriber, about 1,400 views in our first week, all Shorts. At ~500 views a day, Shorts alone won't get there; subscribers and long-form watch hours will.
- What that means for planning: every Short asks for a follow; reply to every comment; and start a long-form series once the Shorts show which trucks pull views (an 8–12 minute "should you buy a ___" walkthrough per generation, built from the site's guides; Hank on camera with his own trucks when he can). Track subscribers and watch hours in the Monday scoreboard.

## Seasonal and holiday posts (Hank, Nov 6, 2026)
Fun but useful. Hank is collecting his own shots of trucks for holidays and seasons (they land in his Mac's photos/ folder; log them in PHOTOS.md). Each seasonal post pairs the fun photo with something useful on the site.
- Dec 1: gift guide launch (boxytrucks.com/best/gifts-for-4x4-owners/), reminder around Dec 10.
- Dec 23: "Happy holidays from Boxy Trucks", Hank's Willys wagon with a wreath (DSC00377).
- Ideas for later: New Year (resolution: do the deferred maintenance; link service schedules), spring (rust check after salt season; inspection checklists), summer (heat and cooling-system checks; overlanding picks), fall (winter prep, tires). Use Hank's photos first, licensed photos otherwise.


## Update, Nov 9, 2026: YouTube advanced features approved
Pinned comments with clickable site links are now on all 16 videos and will go on every new one. Links in long-form descriptions are also clickable. The G500 long-form still goes up Thursday, and the G-Class Shorts' Related video will point to it.
