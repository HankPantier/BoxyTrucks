# Boxy Trucks Field Notes

Short takes in Hank's voice (bylined "Hank", never his last name) on timely boxy-4x4 news (started Nov 3, 2026). The job of each note is social reach, Hank's voice and fresh pages that pass readers to our evergreen guides. Google news traffic is a bonus, not the goal.

## Where things live
- Notes: `data/notes/YYYY-MM-DD-<slug>.md`, YAML front matter plus a Markdown body. Copy the first note's front matter.
- Built pages: `/field-notes/` (index), `/field-notes/<slug>/` and `/field-notes/feed.xml` (RSS). They're linked from the Garage menu, the Garage page and a "Latest Field Notes" block on the home page.
- **Byline: first name only, "Hank", everywhere in Field Notes** (page, schema, captions). Never his last name. Hank's rule, Nov 3, 2026.
- Schema: BlogPosting with "Hank" as the Person author, inside a Blog. Breadcrumbs come automatically.
- Only `status: published` builds. To preview a draft locally, run `NOTES_DRAFTS=1 python3 build.py`, then run a plain `python3 build.py` and `rm -rf` any draft folders under `site/field-notes/` before committing.

## What qualifies
News about a truck family we cover, where the news changes what a buyer or owner should do or think. Examples:
- concepts and reveals (SEMA, Easter Jeep Safari, auto shows);
- new model years or discontinuations;
- recalls on trucks we cover;
- big auction results (BaT records);
- price or tariff changes;
- notable aftermarket launches.

Skip anything that's only a press release, a rumor with one source, or a truck we don't cover.

## Writing rules
- **Length:** 300–600 words. The headline is an opinion, not a news label.
- **Structure:**
  1. What happened, linked to the original reporting, with every fact checked against at least one primary or reputable source.
  2. Why it matters.
  3. Hank's take.
  4. "What it means if you're shopping," with 3–5 internal links (`[[family/gen|text]]` or `/path/`) and a `related:` sidebar.
- **Voice:** opinionated, plain, a little Top Gear. Personal claims use only facts Hank has stated: his trucks, his repairs. Never invent an anecdote. When a note needs his opinion on something we don't know, ask him.
- **Photos:** Use our own licensed photos only (off-road, never wrecks). Brand press photos aren't on our license list. When the photo isn't the news vehicle, say so in the caption ("Today's JL, not the concept").
- **Sources:** cite them in the `sources:` list.

## Approval
Every note waits for Hank's OK before `status: published`. The automation drafts, Hank approves or edits, and only then does it publish. Unattended, it holds.

## Publishing day (every note goes to social the same day)
Hank OK'd extra social posts on note days. Each one is on top of the regular daily post, not a replacement.
1. Set `status: published`, build, commit and push. Request indexing for the note URL in Search Console. Only if it's not already indexed; the page is new, so it won't be.
2. **Assets:**
   - a carousel spec in `social/carousels/fn-<slug>.json` (3 slides plus an end card; `node social/carousels/make_carousel.js …`);
   - a reel spec in `social/reels/fn-<slug>.json` (about 15s; `node social/reels/make_reel.js …`).
3. **Post:**
   - Instagram carousel, per IG_POST_PROCEDURE.md (verify @boxytrucks first);
   - X with a direct link to the note (verify @boxytrucks);
   - a Pinterest pin of slide 1 linking to the note;
   - the reel to YouTube Shorts (Boxy Trucks channel only) and TikTok (then switch it to Everyone).
4. Log it in `social/queue.json` with `n: "fn-<slug>"`, and add it to the next Dispatch's candidate list in NEWSLETTER.md.

## Automation
A scheduled task scans the news every morning. When something qualifies, it drafts the note and the social assets as `status: draft`, commits them, and notifies Hank with the headline and a summary. Hank replies in that run to approve or edit, and the same run publishes and posts.

Pace: 1–2 notes a week normally, more in a big week like SEMA. On a day with nothing worth writing, it drafts nothing and sends no notification.
