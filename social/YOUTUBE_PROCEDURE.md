# YouTube Shorts (Boxy Trucks channel), on every posting day

Hank's rule (Nov 2, 2026): **every day we post anywhere else, we also post to Pinterest and YouTube.**

## Status
**Blocked (Nov 2):** YouTube in Chrome is signed in as Hank's personal account (webhank@gmail.com), whose only channel is "Hank Pantier". Never upload there. Hank needs to create a "Boxy Trucks" channel (or brand account) and switch to it. Until he does, skip YouTube and remind him in the day's one-line report.

## What to post
- **Reel days:** upload the item's `video` as a Short (vertical, under 60 seconds, so YouTube treats it as a Short automatically).
- **Single and carousel days:** YouTube has no image posts for small channels, so post the most recent Reel that isn't on YouTube yet. Once all of them are up, skip the day.
- Backlog when the channel exists: reels 10, 11, 12 and 13 in `social/queue.json`.

## Steps
1. Open https://studio.youtube.com/ and confirm the channel name in the left panel is **Boxy Trucks**. If it says Hank Pantier or anything else, stop and tell Hank. Never switch accounts.
2. Create → Upload videos. `file_upload` the MP4 from `/home/claude/boxytrucks/social/posts/`.
3. **Title** (up to 100 characters): the hook plus #Shorts, e.g. "80 Series Land Cruiser: 5 things to check before you buy #Shorts".
4. **Description:** 2–3 lines from the caption, then `Full guide: https://boxytrucks.com/<link>?utm_source=youtube&utm_medium=social`, then the photo credits.
5. Audience: "No, it's not made for kids." Altered content (AI): No, because our videos are real photos with text.
6. Visibility: Public → Publish. Copy the video URL into the queue item as `yt_url`, and set `yt_status: "posted"`. Commit and push.
