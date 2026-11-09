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

## 5 fresh pins a day (Hank, Nov 9, 2026: "yes proceed with 5 per day")
Pinterest is our one big channel where every post is a clickable link, so on top of the post-day pins above we publish **5 new pins a day** from `social/pins/queue.json` (131 pins: years to avoid, biggest tire, things to check, built by `social/pins/make_pins.py` from site data only; held trucks are skipped).
1. `git pull`, then `python3 social/pins/make_pins.py render 5` (renders the next 5 unposted pins to `social/pins/img/`). Look at them; skip any with text running into the footer.
2. Media goes through the Mac: copy each JPG to `/mnt/user-data/outputs/`, `device_commit_files` to `/Users/webhank/LocalSites/BoxyTrucks/social-upload/`, `device_stage_files` back, then `file_upload` from `/mnt/user-data/uploads/BoxyTrucks/social-upload/`.
3. Confirm the username is **boxytrucks** in settings. For each pin, in pin-creation-tool: upload the image, then set Title = `pin_title`, Description = `pin_description` + ` ` + `credit`, Link = `pin_link`, Board = "Boxy 4x4 Buying Guides". Publish (click twice if the first click only saves a draft), then wait about 20 s before the next pin. Five pins, spaced through the run, not burst-posted.
4. Read each pin's `/pin/<id>/` URL from the board page and set `status: posted`, `posted`, `url` in `social/pins/queue.json`. Commit and push.
5. Stop on any account warning, CAPTCHA or "spam" notice and tell Hank. Never create accounts or change account settings.
6. When the queue runs low, rerun `make_pins.py queue` (new pages and flags appear as the site grows).
