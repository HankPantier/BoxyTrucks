# Spec Sheet series (twice a week)

> **Nov 24, 2026 mix change (weekly planning, from the Nov 23 scoreboard): Instagram gets Reels only.** Spec sheets, spec stacks and single-image posts go to Pinterest only, not Instagram, because 15 singles averaged 44 IG views and 17 carousels 58, against 2,227 for the 2 reader-rig Reels, 884 for the 3 data-hook Reels, 141 for 9 years Reels and 117 for 17 tire Reels. Targets per week: 3 reader-rig Reels (when owners submit), 2 data-hook Reels ("By the numbers #NN": one surprising, sourced number from our pages, voice B), and years-to-avoid Reels. Carousels stay only for Hank's own trucks. For this format: post to Pinterest (and YouTube Community if the procedure says so); skip Instagram, and log ig_status "skipped (Reels only, Nov 24)".


Hank, Nov 11, 2026: "I love this — not for always but for something different worked into the schedule."
Inspired by the one-page build sheets on @the_landcruisers_official: a single 1080x1350 image with a hero photo, two detail tiles,
a spec table, which years to buy or avoid, five things to check and either an owner note (Hank's own words) or the guide's short verdict.
It's built to be saved, so the caption asks people to save it and asks a "which would you buy" question.

**When:** Tuesdays and Saturdays at 5:17 pm ET (between the 4:07 pins and the 6:23 tire Short). That's a change of pace, not a daily series.
**Where:** Instagram feed post and Pinterest (image pin on the Boxy 4x4 Buying Guides board).

## Files
- `scripts/make_specsheets.py queue` builds `social/specsheets/queue.json` and one spec per truck in `social/specsheets/specs/`, keeping posted items.
  Every fact comes from the site's data (page, `data/extra/<family>/<gen>.json`); photos are that page's licensed photos, Hank's own first.
  The owner note only uses `page.owner_notes` (things Hank told us); otherwise the box shows the guide's verdict.
- `scripts/make_specsheets.py render N` renders the next N images with `social/specsheets/make_sheet.js` (it shrinks text to fit and says if it can't).
- `social/specsheets/g500.json` is hand-made (Hank's 2007, his photos) and goes first.

## Run
1. In `/home/claude/boxytrucks`: `git remote set-url origin https://github.com/HankPantier/BoxyTrucks.git`, `git pull`.
2. Take the first item in `social/specsheets/queue.json` whose status isn't `posted` or `hold`. Render it if the image is missing.
3. **Look at the image before posting.** Check that nothing overlaps or is cut off, and look for readable number plates in the hero
   and both tiles. Blur any plate in the source photo under `site/img/` (PIL GaussianBlur(12) twice on the box) and re-render.
   If a fact looks wrong, fix it in the site data, rebuild the queue and re-render, rather than editing the image.
4. Copy the image to `/mnt/user-data/uploads/BoxyTrucks/social-upload/`.
5. **Instagram** (IG_POST_PROCEDURE.md): confirm @boxytrucks, Create → Post, crop **Original** (4:5), caption = `ig_caption` typed line by line. Save `ig_url`.
6. **X**: skip (weekly round-up only since Nov 14, 2026; a good sheet can go in Friday's round-up).
7. **Pinterest** (PINTEREST_PROCEDURE.md): confirm boxytrucks, image pin, `pin_title`, `pin_description`, `pin_link`, board Boxy 4x4 Buying Guides. Save `pin_url`.
8. Set `status: "posted"`, `posted: <date>` and the per-platform statuses; log the URLs in README.md and X.md. Render the next one ahead. Commit and push.
9. Tell Hank only if something failed. A platform that fails is skipped that day, never retried on another account.

When the queue runs out, rebuild it (pages gain photos and data over time) and tell Hank how many new sheets it found.
