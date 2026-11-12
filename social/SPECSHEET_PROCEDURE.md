# Spec Sheet series (twice a week)

Hank, Nov 11, 2026: "I love this — not for always but for something different worked into the schedule."
Inspired by the one-page build sheets on @the_landcruisers_official: a single 1080x1350 image with a hero photo, two detail tiles,
a spec table, which years to buy or avoid, five things to check and either an owner note (Hank's own words) or the guide's short verdict.
It's built to be saved, so the caption asks people to save it and asks a "which would you buy" question.

**When:** Tuesdays and Saturdays at 5:17 pm ET (between the 4:07 pins and the 6:23 tire Short). That's a change of pace, not a daily series.
**Where:** Instagram feed post, X (image, link in the first reply) and Pinterest (image pin on the Boxy 4x4 Buying Guides board).

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
6. **X** (X_POST_PROCEDURE.md): confirm @boxytrucks, attach the image, text = `x_text` (no link), then reply with `x_reply`. Save `x_url` and `x_reply_url`.
7. **Pinterest** (PINTEREST_PROCEDURE.md): confirm boxytrucks, image pin, `pin_title`, `pin_description`, `pin_link`, board Boxy 4x4 Buying Guides. Save `pin_url`.
8. Set `status: "posted"`, `posted: <date>` and the per-platform statuses; log the URLs in README.md and X.md. Render the next one ahead. Commit and push.
9. Tell Hank only if something failed. A platform that fails is skipped that day, never retried on another account.

When the queue runs out, rebuild it (pages gain photos and data over time) and tell Hank how many new sheets it found.
