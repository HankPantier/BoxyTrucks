# YouTube Shorts (Boxy Trucks channel), on every posting day

Hank's rule (Nov 2, 2026): **every day we post anywhere else, we also post to Pinterest and YouTube.**

## Status
Live since Nov 2, 2026: channel **Boxy Trucks**, https://www.youtube.com/@BoxyTrucks (Studio channel UCDYI1l32dLwGjMLcoQvodGQ), with banner, logo, description and link set. Reels 10–13 are posted. Hank's Google login also has his personal "Hank Pantier" channel; never upload there.

## What to post
- **Reel days:** upload the item's `video` as a Short (vertical, under 60 seconds, so YouTube treats it as a Short automatically).
- **Single and carousel days:** YouTube has no image posts for small channels, so post the most recent Reel that isn't on YouTube yet. Once all of them are up, skip the day.
- Backlog when the channel exists: reels 10, 11, 12 and 13 in `social/queue.json`.

## Steps
1. Open https://studio.youtube.com/ and confirm the channel name in the left panel is **Boxy Trucks**. If it says Hank Pantier or anything else, stop and tell Hank. Never switch accounts.
2. Create → Upload videos. `file_upload` the MP4 from `/home/claude/boxytrucks/social/posts/`.
3. **Title** (up to 100 characters): the hook, e.g. "Land Cruiser 80 Series: 5 things to check before you buy". Vertical videos under 60 seconds become Shorts automatically. Skip #hashtags, because typing # triggers autocomplete and scrambles the text. Set the title and description with JS: focus the contenteditable, then `document.execCommand('selectAll')` and `insertText`.
4. **Description:** 2–3 lines from the caption, then `Full guide: https://boxytrucks.com/<link>?utm_source=youtube&utm_medium=social`, then the photo credits.
5. Audience: "No, it's not made for kids." Altered content (AI): No, because our videos are real photos with text.
6. Click Next three times, choose Public, then Publish (`#done-button`), and check that the Shorts list shows it as Public. Copy the video URL into the queue item as `yt_url`, and set `yt_status: "posted"`. Commit and push.
