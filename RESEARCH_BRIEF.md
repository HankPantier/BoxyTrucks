# BoxyTrucks.com — model research brief

BoxyTrucks.com is an enthusiast information portal about boxy, body-on-frame-spirited 4x4s (G-Class, Land Cruiser, Defender, Range Rover, 4Runner, Lexus GX/LX, Ineos Grenadier). Think "Wikipedia meets an overland magazine", with a Top Gear-ish voice: opinionated, witty, story-driven — but every fact must be TRUE and SOURCED.

Audience: off-road / overland enthusiasts who are fairly hands-on (they wrench on their own trucks). NOT the street/luxury-flex crowd.

You are researching ONE model family. Write ONE JSON file (UTF-8, valid JSON) to:
`/tmp/claude-0/-home-claude/6228804b-c069-5f1b-bd5e-d35edcda73bc/scratchpad/bt/data/<family-slug>.json`
and download photos to:
`/tmp/claude-0/-home-claude/6228804b-c069-5f1b-bd5e-d35edcda73bc/scratchpad/bt/site/img/<family-slug>/`

## Hard rules
- NEVER invent facts, numbers, part numbers, handles, URLs or quotes. If you can't verify something, leave it out (or use a clearly bracketed placeholder like "[TO RESEARCH]"). Prefer fewer, correct items.
- Every non-obvious fact should be traceable to an entry in `sources`.
- Instagram/YouTube accounts: only include accounts you actually found referenced on the web for this model. Otherwise omit the `social` entries (empty list is fine).
- Photos: OFF-ROAD ONLY (dirt, trails, desert, sand, snow, mud, mountains, forest, camping/overlanding). NO city streets, parking lots, studios, car shows, dealer lots. Prefer the exact generation of the example page; label honestly in the caption if it's a different generation.
- Voice for verdicts/leads: witty and opinionated, but don't make factual claims in jokes that aren't true.

## Tooling notes (this sandbox)
- WebSearch + WebFetch work. Shell `curl` works for: images.unsplash.com, images.pexels.com, www.autotempest.com, bringatrailer.com. Shell cannot load unsplash.com or pexels.com pages (bot wall) — use WebFetch on photo/search page URLs that came from a WebSearch result.
- Unsplash: find photo pages with WebSearch (allowed_domains ["unsplash.com"]), WebFetch the photo page to get the `images.unsplash.com/photo-XXXX` URL + photographer. Download: `curl -s -o out.jpg "https://images.unsplash.com/photo-XXXX?fm=jpg&q=75&w=1800&fit=crop"`.
- Pexels: WebSearch (allowed_domains ["pexels.com"]) for search pages, WebFetch a search page to list photo IDs; download `https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=1800`. Get the photographer name by WebFetching the photo page.
- After downloading, LOOK at the photos (make a small contact sheet with PIL and Read it) and drop any that are street/studio shots or the wrong vehicle. Resize to max 1800px wide, JPEG quality ~78, with PIL (`ImageOps.exif_transpose` first). Keep 4–6 good ones. Name them `<short-descriptor>.jpg`.
- AutoTempest search URLs: `https://www.autotempest.com/results?make=<make>&model=<model>&minyear=YYYY&maxyear=YYYY`. Verify the make/model slugs by curling the URL and checking the `<title>` (e.g. G-Class is `make=mercedesbenz&model=gclass`). 
- Bring a Trailer has model pages (e.g. `https://bringatrailer.com/toyota/land-cruiser-fj80-fzj80/`, `https://bringatrailer.com/mercedes-benz/w463-g-class-1991-2018/`). Find them by curling the make page (e.g. `https://bringatrailer.com/toyota/`, `https://bringatrailer.com/land-rover/`) with `-A "Mozilla/5.0"`, html-unescaping, replacing `\/` with `/`, and regex-extracting `"title":"...","url":"https://bringatrailer.com/<make>/<slug>/"` pairs. Verify each chosen URL returns 200. If no BaT model page exists for a generation, use the make page URL.

## JSON schema
```json
{
  "family": {
    "slug": "land-cruiser",
    "name": "Land Cruiser",
    "maker": "Toyota",
    "years": "1951–present",
    "verdict": "One or two witty sentences.",
    "intro": ["paragraph", "paragraph", "paragraph"],
    "hero_photo": "file.jpg",
    "generations": [
      {"slug": "80-series", "name": "80 Series", "years": "1990–1998", "codes": ["FJ80","FZJ80"], "summary": "One line on what it is / why it matters.", "at_url": "verified AutoTempest URL", "bat_url": "verified BaT URL", "has_page": true}
    ],
    "forums": [{"name": "IH8MUD — 80 Series", "url": "https://...", "note": "What it's good for"}],
    "related_families": ["g-class", "range-rover"]
  },
  "page": {
    "slug": "80-series",
    "title": "Land Cruiser 80 Series",
    "eyebrow": "TOYOTA LAND CRUISER · J80 · 1990–1998",
    "verdict": "Witty one-to-two sentence verdict.",
    "codes": ["FZJ80", "1FZ-FE 4.5 I6", "3 LOCKERS OPTIONAL"],
    "hero_photo": "file.jpg",
    "story": [
      {"heading": null, "paragraphs": ["The big opening paragraph (lead)."]},
      {"heading": "SECTION HEADING IN CAPS", "paragraphs": ["...", "..."]}
    ],
    "callout": {"label": "SIDEBAR · ...", "title": "...", "paragraphs": ["..."]},
    "engineering_intro": "One paragraph on how it's built.",
    "engineering": [{"k": "CHASSIS", "v": "Ladder frame", "note": "short note"}],
    "generations_table": [{"years": "", "platform": "", "engine": "", "output": "", "note": ""}],
    "buying_checks": [{"head": "", "body": ""}],
    "repairs": [{"title": "", "diff": "3 / 5", "time": "≈ 2 hours", "cost": "$X–Y or 'Parts plus labor'", "symptoms": "", "fix": "", "tools": "tools · parts · part numbers only if sourced"}],
    "faq": [{"q": "", "a": "", "src": "SHORT SOURCE LABEL"}],
    "mods": [{"cat": "SUSPENSION LIFT", "why": "", "who": [{"name": "Old Man Emu", "url": "https://..."}]}],
    "searches": [{"years": "1991–1997 · US", "label": "FZJ80", "at_url": "", "bat_url": ""}],
    "social": [{"kind": "IG|YT", "name": "@handle or channel name", "focus": "SHORT CAPS FOCUS", "url": "https://..."}],
    "forums": [{"name": "", "url": "", "note": ""}],
    "related": [{"rel": "PREDECESSOR", "name": "60 Series", "family": "land-cruiser", "gen": "60-series"}],
    "plate": [{"k": "CHASSIS", "v": "J80"}],
    "photos": [{"file": "file.jpg", "alt": "descriptive alt text", "caption": "SHORT CAPS CAPTION", "credit": "Photographer Name", "source": "Unsplash|Pexels", "source_url": "https://..."}],
    "sources": [{"name": "Publisher — title", "url": "https://..."}]
  }
}
```

Content targets for `page` (the deep example page):
- story: lead + 3–4 headed sections (origins, development, what made it special, how it ended / legacy). 6–10 paragraphs total, 60–120 words each. Inline links to OTHER models: write them as `[[family-slug/gen-slug|link text]]` (e.g. `[[land-cruiser/60-series|60 Series]]`, or `[[g-class/g500|G 500]]`). Link every mention of another model/generation that appears in your family's `generations` list or other families (g-class, land-cruiser, lexus, 4runner, land-rover, range-rover, grenadier).
- engineering: 6 cells. Optional `callout` sidebar for an interesting tangent (special editions, a gray-market story, a famous expedition).
- generations_table: the example model's variants/years/engines (4–7 rows).
- buying_checks: 6–8.
- repairs: 6–8 real, common jobs for hands-on owners, with symptoms, the fix (actual steps), tools & parts. Use forum DIY threads, enthusiast shops, and reputable guides. Give difficulty 1–5, time, typical shop cost if sourced.
- faq: ~10 of the MOST COMMON owner questions found on forums/search, with researched answers. MUST include "What's the biggest tire I can fit without a lift?" (with the actual size consensus), plus things like towing, fuel economy, fluids/capacities if sourced, lockers/4WD use, lift options, which years/engines to buy or avoid, reliability.
- mods: 5–7 categories with real suppliers known for this model (e.g. Old Man Emu, Slee Off-Road, Metal Tech 4x4, ARB, Front Runner, Rovers North, Terrafirma, etc.) with their real URLs.
- forums: model-specific message boards (e.g. IH8MUD subforum, Defender Source, RangeRovers.net, Toyota-4Runner.org, GX Owners forums) with real URLs.
- searches: 2–4 AutoTempest + BaT links for the example model's year ranges.
- plate: 10–12 spec rows.
- sources: everything you used.

When done, reply with a short summary: file path, number of FAQs/repairs/photos, and anything you couldn't verify.

## Manuals: what you may link
Never link factory manuals hosted on archive.org or other user-uploaded scan sites; they are probably unauthorized copies. You may use their figures, but cite the manual by name in `sources` with no `url` key. Manufacturer-hosted owner manuals and legitimate sellers (Helm, Faxon, the manufacturer) are fine to link.
