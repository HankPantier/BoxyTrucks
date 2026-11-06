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
7. **Always leave a comment (Hank, Nov 5, 2026).** Right after publishing, open the video's watch page (or Studio → Comments) and comment **as Boxy Trucks**: check that the avatar or name next to the comment box is Boxy Trucks, never Hank Pantier; if it's wrong, stop and tell Hank. Then pin the comment (⋮ → Pin). Pinning needs a one-time phone verification of the channel in YouTube Studio (Hank's to do; as of Nov 5 it isn't done), so until then skip the pin. Type the comment with JS: focus `#contenteditable-root`, then `execCommand('insertText')`; clicking the box and typing can land the text in the search bar. Also reply to any viewer comments, friendly and short, ending with a question.
   - Friendly and conversational, like a fellow owner talking to the people who watched, not an ad.
   - Go deeper than the video: one or two specifics from the guide that didn't fit on screen (a fitment caveat, what to check, why a year matters), all from the site's sourced data. Never invent anecdotes; only mention Hank's own trucks as he has stated them.
   - Ask the audience something they can answer ("What are you running on yours?", "Which year would you pick?").
   - End with the link: `https://boxytrucks.com/<link>?utm_source=youtube&utm_medium=comment` (YouTube may hide links in comments on brand-new channels; post it anyway and check it shows).
   - Save the comment text as `yt_comment` in the queue item.
