# Daily Instagram post (@boxytrucks)

Hank pre-approved the queued drafts (one post a day). The mix and the rules are in `STRATEGY.md`.

1. In Claude in Chrome, open https://www.instagram.com/accounts/edit/ and confirm the account is **boxytrucks**. If it's anything else, stop and tell Hank.
2. Open instagram.com, then Create (+), then Post. Use `find` to locate the file input and `file_upload` the media:
   - `single`: the item's `image`.
   - `carousel`: every path in `images`, in order, in one upload call (up to 10).
   - `reel`: the item's `video`. Instagram makes any video post a Reel.
3. Crop:
   - single and carousel: 4:5.
   - reel: choose "Original" (9:16), and don't crop to 4:5.
   - For a reel, if a "Cover" option appears, pick the frame showing the hook text.
4. Skip filters and edits (Next, Next).
5. Click the caption box and type the caption exactly. Don't press Escape, because it opens "Discard post?". If a hashtag or tag popup opens, click empty space in the side panel.
6. Leave the AI label off: our media is real photos with text. Turn it on only if the item has `"ai": true`.
7. Share, then wait for "Your post has been shared".
8. In queue.json set `status: "posted"` and `posted: <date>`, add a row to the Posts table in `README.md`, then rebuild the site (`python3 build.py`) so /links/ lists the new post. Commit and push, and tell Hank in one line.
9. Remind Hank in that line to share it to Stories from his phone. Web Instagram can't post Stories.
10. If Chrome or the account isn't available, leave the item queued and tell Hank.

11. **Then Pinterest, YouTube and TikTok, every day, no exceptions** (Hank, Nov 4, 2026: post to ALL channels every day). If the day's post is image-only and no Reel is waiting for YouTube/TikTok, make a 10–15 second video version of it with `social/reels/make_reel.js` (2–3 scenes from the post's photos plus a CTA scene) and post that. Earlier rule: (Hank's rule, Nov 2, 2026): follow `PINTEREST_PROCEDURE.md`, `YOUTUBE_PROCEDURE.md` and `TIKTOK_PROCEDURE.md` for the same item. If either account isn't the Boxy Trucks one, skip that platform and say so in the one-line report.
