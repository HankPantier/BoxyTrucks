# Pinterest (@boxytrucks), on every posting day

Hank's rule (Nov 2, 2026): **every day we post anywhere else, we also post to Pinterest and YouTube.** Run this right after the Instagram and X posts.

1. In Claude in Chrome, open https://www.pinterest.com/settings/ and confirm username **boxytrucks**. If it's anything else, stop and tell Hank. Never switch accounts.
2. Open https://www.pinterest.com/pin-creation-tool/, `find` the file input and `file_upload` the media from `/home/claude/boxytrucks/`:
   - `single`: `image`.
   - `carousel`: the first slide only (the cover).
   - `reel`: the `video` MP4. Pinterest accepts MP4 up to 200 MB.
3. Fill in the pin:
   - **Title:** a search phrase people type, up to 100 characters (e.g. "Land Cruiser 80 Series: 5 things to check before you buy").
   - **Description:** up to 500 characters. Use the caption's facts and the photo credits. Leave out the hashtags and "link in bio".
   - **Link:** `https://boxytrucks.com/<item link>?utm_source=pinterest&utm_medium=social`.
   - **Board:** "Boxy 4x4 Buying Guides".
4. Wait about 5 seconds, then click Publish. The first click often only saves the draft, so check for "Publish Complete" and click again if needed.
5. Add the entry to `social/pinterest.json` with status, posted date and the `/pin/<id>/` URL from the board page (https://www.pinterest.com/boxytrucks/boxy-4x4-buying-guides/). Commit and push.
6. Skip items whose only link is /submit/. Those community posts don't work as pins.
