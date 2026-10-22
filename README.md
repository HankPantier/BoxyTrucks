# BoxyTrucks.com

An enthusiast resource for boxy 4x4s — G-Class, Land Cruiser, Lexus LX/GX, 4Runner, Land Rover, Range Rover and Ineos Grenadier. Static site generated from JSON content, hosted on GitHub Pages.

## To do

- [x] **Google Analytics hooked up** — GA4 measurement ID `G-XHC493ES9X` is set in `GA_MEASUREMENT_ID` in `build.py`.
- [ ] Activate the Show Us Your Rig form: send one test submission from the live site, then click the FormSubmit activation email sent to the inbox. Optionally swap the email in `SUBMIT_EMAIL` (build.py) for FormSubmit's random alias.
- [ ] Submit `https://boxytrucks.com/sitemap.xml` in Google Search Console.
- [ ] Replace placeholder / stand-in photos (pages captioned "different generation" or "placeholder"), especially the Grenadier and 1st-gen 4Runner.
- [ ] Featured Build and "Life on the road" placeholders on the home page.

## How it works

- `data/<family>.json` — family landing page + the family's flagship guide (`page`).
- `data/pages/<family>/<gen>.json` — full guide for every other generation.
- `data/resources/<family>.json` — YouTube, Instagram, forums and references found in research.
- `data/resources_manual.json` / `data/social_manual.json` — accounts added by hand (always kept).
- `data/reading.json` — "Further reading" articles keyed by `family/gen`.
- `data/suppliers.json` — fallback parts-search links per family.
- `templates/` — Jinja2 templates. `site/assets/site.css` — the design system.
- Inline links between models in any text: `[[family/gen|link text]]`.

## Build locally

```bash
pip install -r requirements.txt
python3 build.py        # writes site/
open site/index.html
```

Every push to `main` rebuilds and deploys via `.github/workflows/pages.yml`.

## SEO

Every page has a canonical URL, Open Graph/Twitter tags and JSON-LD (Article + FAQPage + BreadcrumbList on model guides; CollectionPage on hubs; WebSite + Organization on the home page). `sitemap.xml` and `robots.txt` are generated on each build.
