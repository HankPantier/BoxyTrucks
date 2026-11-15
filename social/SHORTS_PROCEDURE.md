# Second daily post: the Short, on every platform

Hank, Nov 5, 2026: post a second Short every day, on top of the regular daily post, because video is about 78% of our views.
Hank, Nov 6, 2026: post multiple times a day on **every** platform. The Short goes to YouTube, TikTok, Instagram (as a Reel) and Pinterest (as a video pin). Not X: X is a weekly round-up only since Nov 14, 2026 (see X_POST_PROCEDURE.md). Every Short ends with a "Follow for a new truck every day" card.

**Series:** "Biggest tire on a stock <truck>", generated from site data by `scripts/make_tire_shorts.py`:
- hook, then the stock-height size, then one or two lifted sizes, then a call to action pointing to that truck's `/tires/` page (which has the Tire Rack, Mavis and Amazon size links);
- facts come only from `data/extra/<family>/<gen>.json` → `fitment.max_tire`; photos come only from that generation's licensed page photos, credited on screen;
- the queue is `social/shorts.json` (55 Shorts, round-robin across families so the feed varies).

## Daily run (6:23 pm ET)
1. In `/home/claude/boxytrucks`: `git remote set-url origin https://github.com/HankPantier/BoxyTrucks.git`, then `git pull`.
2. Take the first item in `social/shorts.json` whose `status` isn't `posted`. If its `video` file is missing, run `python3 scripts/make_tire_shorts.py render 1`. Check that the MP4 is under 10 MB.
3. **YouTube** (follow `YOUTUBE_PROCEDURE.md`): confirm the channel is **Boxy Trucks** in Studio (never "Hank Pantier"). Upload `video`, title = `yt_title`, description = `yt_description` (set both with JS `execCommand('selectAll')` + `insertText`), "No, it's not made for kids", Next ×3, Public, Publish. Save the URL as `yt_url` and set `yt_status: "posted"`. Then leave and pin a friendly, in-depth comment as **Boxy Trucks** with the site link (`YOUTUBE_PROCEDURE.md` step 7): add a detail from that truck's tires page that wasn't in the video, ask viewers what they run, link `<link>?utm_source=youtube&utm_medium=comment`. Save it as `yt_comment`.
4. **TikTok** (follow `TIKTOK_PROCEDURE.md`): confirm the profile is **@boxytrucks**. Upload `video`. Clear the filename from the description: click the editor, press End, then Backspace about 35 times, and check that it's empty. Type `tt_description`, then each tag in `tt_hashtags` one at a time, each followed by a space. Check the end of the text. Post as Everyone. Save `tt_url` and set `tt_status: "posted"`. It shows "Only me" during review and becomes Everyone afterwards on its own.
### Instagram, X and Pinterest (added Nov 6, 2026)
After YouTube and TikTok, post the same `video` to the other three, verifying the account before each and stopping on a wrong one:
- **Instagram** (`IG_POST_PROCEDURE.md`, the Reel steps): confirm **@boxytrucks**. Caption = `ig_caption`. Save `ig_url`, set `ig_status: "posted"`.
- **X**: skip (weekly round-up only since Nov 14, 2026). Set `x_status: "roundup"`.
- **Pinterest** (`PINTEREST_PROCEDURE.md`): confirm **boxytrucks**. Video pin, title `pin_title`, description `pin_description`, link `pin_link`, board for that family. Save `pin_url`, set `pin_status: "posted"`.
Space the five uploads over the evening if a platform rate-limits. A platform that fails gets skipped for that day and noted, never retried on another account.

5. Set `status: "posted"` and `posted: <date>`, then render the next one ahead (`render 1`). Run `python3 build.py` so that truck's guide and tires page link its new Short in the "Watch on YouTube" box. Commit and push. Tell Hank only if something went wrong.
6. If an account is wrong, Chrome is down, or a platform blocks the upload, post nothing on that platform and tell Hank. Never switch accounts.
7. When the tire series runs out, tell Hank and propose the next data-driven series (for example "Years to avoid: <truck>" from each `/years/` page).

Regenerating the queue (`python3 scripts/make_tire_shorts.py queue`) keeps the posted status of every item.

## Third daily Short: "Years to avoid" (Hank approved Nov 7, 2026, optimization plan item 2)
Same steps as above, but take the first item from `social/shorts-years.json` whose status is not posted or hold (built by `scripts/make_years_shorts.py queue`,
rendered with `render 1`). Facts come only from the timeline entries flagged avoid/buy in `data/extra/<family>/<gen>.json`, using the
sentence that gives the reason. YouTube comment: add one more sourced detail from that truck's /years/ page and ask "Which year is yours?".
Link: the truck's /years/ page. Runs daily at 12:37 pm ET. When the 11 in the queue run out, rebuild the queue (new flagged years may exist) and tell Hank.

## Pin the Boxy Trucks comment (from Nov 9, 2026)
YouTube approved the channel's advanced features (video verification) on Nov 9, so links in our comments are now clickable.
After posting the in-depth comment on every new video, pin it: the comment's ⋮ menu → Pin → confirm "Pin" in the dialog.
Click the confirm button with a real click (find "Pin confirm button in the dialog", then computer left_click); a JS `.click()` on it does nothing.
Check the thread shows "Pinned by @BoxyTrucks". All 16 earlier videos were pinned on Nov 9.

Upload gotcha (Nov 9): if the watch page says "Comments are not supported on private videos", the upload was saved as a draft.
Open it in Studio, click "Edit draft", tick "Not made for kids", Next ×3, Public, Done.

## Hook v2 and search titles (Nov 12, 2026)
YouTube analytics, last 28 days: 70% of Short views came from the Shorts feed but only 19% "stayed to watch" (81% swiped away), so the feed stopped
testing new Shorts (Nov 10–11 uploads got 33–147 views against 300–540 for Nov 7–9). Search brought 29%, steadily.
- `social/reels/make_reel.js`: the opening scene (`hook: true, align: "top"`) puts a big question at the top from frame one with a fast zoom; all text sits
  above the bottom ~540 px and left of the right-hand buttons (the Shorts overlay); brand moved to the top; the follow card is folded into the CTA (≈11 s total).
- Tire titles now lead with the search phrase: "<truck> tire size: the biggest tire with no lift (<size>)". GX 470, Defender, early Bronco and CJ-5 retitled on YouTube.
- First v2 Shorts: Patrol Y61 years (Nov 12, 12:37) and Range Rover Classic tires (Nov 12, 6:23). Compare their "stayed to watch" with the 19% baseline on Nov 14.
- **Nov 14 check (YouTube Studio, since published):**
  | Short | Views | Stayed to watch | Search | Shorts feed |
  |---|---|---|---|---|
  | Patrol Y61 years (v2, Nov 12) | 238 | 32.8% | 89.8% | 9.8% |
  | Range Rover Classic tires (v2, Nov 12) | 69 | 50.0% | 70.0% | 27.1% |
  | Prado 150 years (v2, Nov 13) | 111 | 29.0% | | |
  | Grenadier SW tires (v2, Nov 13) | 170 | 20.8% | | |
  | G500 oil housing (Hank's footage + voice, Nov 13) | 74 | 51.8% | | |
  | Defender years (v1, Nov 11, for comparison) | 151 | 37.5% | | |
  Retitled tire Shorts, traffic share: GX 470 (115 views) search 93.9% / feed 5.2%; Defender 90/110 (120) search 95.8% / feed 3.3%; early Bronco (85) search 62.6% / feed 35.2%; CJ-5 (310) feed 62.5% / search 36.9% (mostly feed views from before the retitle).
  Read: stayed-to-watch is up from the 19% channel baseline on every v2 Short, but the feed is still barely testing them (under 30% of views); search is carrying views, and the search-first titles work. The real footage with voice held best (52%).
  Next: open on a real-photo close-up (tire or trouble spot) instead of a wide shot, put a number in the first 1 s of the hook ("34 in, no lift?"), cut tire Shorts to ~8 s, and try voice B on generated Shorts.
