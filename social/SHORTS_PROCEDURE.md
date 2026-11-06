# Second daily Short (YouTube + TikTok)

Hank, Nov 5, 2026: post a second Short every day, on top of the regular daily post, because video is about 78% of our views.

**Series:** "Biggest tire on a stock <truck>", generated from site data by `scripts/make_tire_shorts.py`:
- hook, then the stock-height size, then one or two lifted sizes, then a call to action pointing to that truck's `/tires/` page (which has the Tire Rack, Mavis and Amazon size links);
- facts come only from `data/extra/<family>/<gen>.json` → `fitment.max_tire`; photos come only from that generation's licensed page photos, credited on screen;
- the queue is `social/shorts.json` (55 Shorts, round-robin across families so the feed varies).

## Daily run (6:23 pm ET)
1. In `/home/claude/boxytrucks`: `git remote set-url origin https://github.com/HankPantier/BoxyTrucks.git`, then `git pull`.
2. Take the first item in `social/shorts.json` whose `status` isn't `posted`. If its `video` file is missing, run `python3 scripts/make_tire_shorts.py render 1`. Check that the MP4 is under 10 MB.
3. **YouTube** (follow `YOUTUBE_PROCEDURE.md`): confirm the channel is **Boxy Trucks** in Studio (never "Hank Pantier"). Upload `video`, title = `yt_title`, description = `yt_description` (set both with JS `execCommand('selectAll')` + `insertText`), "No, it's not made for kids", Next ×3, Public, Publish. Save the URL as `yt_url` and set `yt_status: "posted"`. Then leave and pin a friendly, in-depth comment as **Boxy Trucks** with the site link (`YOUTUBE_PROCEDURE.md` step 7): add a detail from that truck's tires page that wasn't in the video, ask viewers what they run, link `<link>?utm_source=youtube&utm_medium=comment`. Save it as `yt_comment`.
4. **TikTok** (follow `TIKTOK_PROCEDURE.md`): confirm the profile is **@boxytrucks**. Upload `video`. Clear the filename from the description: click the editor, press End, then Backspace about 35 times, and check that it's empty. Type `tt_description`, then each tag in `tt_hashtags` one at a time, each followed by a space. Check the end of the text. Post as Everyone. Save `tt_url` and set `tt_status: "posted"`. It shows "Only me" during review and becomes Everyone afterwards on its own.
5. Set `status: "posted"` and `posted: <date>`, then render the next one ahead (`render 1`). Commit and push. Tell Hank only if something went wrong.
6. If an account is wrong, Chrome is down, or a platform blocks the upload, post nothing on that platform and tell Hank. Never switch accounts.
7. When the tire series runs out, tell Hank and propose the next data-driven series (for example "Years to avoid: <truck>" from each `/years/` page).

Regenerating the queue (`python3 scripts/make_tire_shorts.py queue`) keeps the posted status of every item.
