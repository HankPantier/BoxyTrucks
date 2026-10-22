# Brief: generation-specific photos for every model page

BoxyTrucks.com is an enthusiast site about boxy 4x4s. Its audience is **off-road and overland people, not the street or luxury crowd**. Today most generation pages borrow photos from other generations; for example, the G 55 AMG page shows a newer G-Class. Every page needs photos of **its own generation**.

Repo: `/home/claude/boxytrucks`. Only edit the files for your family (listed in your task).

## What each page needs
- **Hero photo**: `hero_photo` (filename) on the page object. Also add `hero_focus`, a CSS object-position string such as `"70% 55%"` that marks where the truck sits in the frame. The text panel covers the left half of the hero on desktop, so landscape shots with the truck right of centre are best. Prefer wide landscape images at least 1600px wide.
- **Gallery**: `photos`, a list of 2–4 items. The hero image should be the first item. Use this exact schema (it already exists):
  ```json
  {"file": "g55-dunes.jpg", "alt": "A black G 55 AMG on a sand track", "caption": "G 55 AMG · SAND TRACK", "credit": "Author Name · CC BY-SA 4.0", "source": "Wikimedia Commons", "source_url": "https://commons.wikimedia.org/wiki/File:...."}
  ```
  Captions are short, uppercase and in the form `MODEL · PLACE OR SCENE`. Remove every old "(NOT A …)" or "STAND-IN" caption once that photo has been replaced. The page's `hero_note`, if there is one, must not claim a stand-in that is no longer there. Update it or delete the key.
- **The family landing page:** if the family object in `data/<family>.json` has a `hero_photo`, make sure it shows a real member of the family. Ideally use the most iconic generation.
- Don't reuse the same photo across generations unless the vehicles are genuinely identical. If a page truly has no usable photo, keep its current one and leave its honest stand-in caption.

## Photo rules (in priority order)
1. **Correct generation, verified.** Wikimedia Commons model categories are the most reliable, e.g. `Category:Mercedes-Benz G 55 AMG (W463)`, `Category:Toyota Land Cruiser 100`, `Category:Land Rover Discovery Series I`. Check the photo against the generation's grille, lights and body. Identify facelifts correctly. Pexels and Unsplash are fine when the model is unmistakable.
2. **Setting:** off-road or overland first: dirt, sand, rock, mud, snow, a trail, a campsite or a rural landscape. Avoid city streets, parking lots, motor shows and showrooms. Use one of those only if nothing else of that generation exists, and caption it honestly.
3. **Usable licence only:** CC0, public domain, CC BY, CC BY-SA, or the Pexels or Unsplash licence. Never NC or ND. Credit format: `Author · CC BY-SA 4.0`, or `Author` with `source: "Pexels"` / `"Unsplash"`.
4. **Quality:** sharp, well exposed, the vehicle large in frame, no heavy watermarks, no number plates as the subject.

## Getting the files
- Commons: find candidates with WebFetch on category pages, e.g. `https://commons.wikimedia.org/wiki/Category:Toyota_Land_Cruiser_100`. Read the file page to check the licence and author. Download with curl: `curl -sL -A 'BoxyTrucksBot/1.0 (webhank@gmail.com)' -o out.jpg 'https://commons.wikimedia.org/wiki/Special:FilePath/<File_name.jpg>?width=2000'`. Commons rate-limits, so **wait 3 seconds between downloads**. On HTTP 429, wait 30 seconds and retry.
- Pexels and Unsplash: their search pages only work through WebFetch or WebSearch. Image CDNs work with curl, e.g. `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&w=2000` and `https://images.unsplash.com/photo-...?w=2000`.
- Process every image with Python PIL: convert to RGB, resize so the longest side is at most 2000px, and save as JPEG quality 82 with `optimize=True` to `site/img/<family>/<descriptive-name>.jpg`. Look at every image yourself with the Read tool before using it, to confirm the generation and the setting.
- Delete images that end up unused **only if** they're files you added. Leave existing files alone.

## Editing
Load each JSON, change only `hero_photo`, `hero_focus`, `hero_note` and `photos`, then write it back with `json.dump(d, f, ensure_ascii=False, indent=1)`. Don't run `build.py`. Don't touch any other family's files.

## Report back
For each page, give one line: hero file, number of gallery photos, sources, and anything still a stand-in.
