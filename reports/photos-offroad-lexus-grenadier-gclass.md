# Off-road photo pass: Lexus, Grenadier, G-Class

Date: 2026-10-23. Scope: `data/lexus.json` + `data/pages/lexus/*`, `data/grenadier.json` + `data/pages/grenadier/*`, `data/g-class.json` (G 500) + the G-Class pages `w463`, `500ge`, `g550`, `4x4-squared`, `europa`, `g63-6x6`. Only `hero_photo`, `hero_focus`, `hero_note` and `photos` were edited. `build.py` was not run.

## Summary
- **Pages changed: 3.** LX 470 page, Lexus family landing, Grenadier Station Wagon gallery.
- **Heroes now off-road (were not): 2.** LX 470 page and Lexus family landing.
- **New gallery photos: 4.** 3 LX 470 (Pexels), 1 Grenadier (Flickr CC BY-SA 2.0).
- **Pages still not off-road: 13.** No freely licensed off-road photo of the right generation could be found. Their current photos and honest captions were kept, and no wrong-generation swaps were made.

## Per page

### Lexus
| Page | Hero before → after | Gallery | Still not off-road |
|---|---|---|---|
| **Family landing** (`data/lexus.json` family) | `lx470-snorkel-build.jpg` (car park) → **`lx470-coastal-sand-flats.jpg`**, focus `62% 62%` | n/a | — |
| **LX 470** | `lx470-snorkel-build.jpg` (car park) → **`lx470-coastal-sand-flats.jpg`**, focus `62% 62%` | Now 3, all off-road: coastal sand flats, water crossing on sand, sand track by mangroves. Removed: snorkel build (car park), 2005 facelift (grass verge by a street) and `lx470-sand.jpg` (a portrait shot from the same session as the new photos). | Nothing. Note that all 3 photos show the same pre-facelift truck, so no 2003+ facelift is pictured now. |
| **GX 470** (flagship `page` in `data/lexus.json`) | unchanged `gx470-silver-2004.jpg` | unchanged (3, all street) | **Yes, all 3.** Commons has 33 GX 470 files and every one is street, lot, show or interior. Flickr CC has 16, all street or dealer. |
| **GX 460** | unchanged `gx460-snow-pair.jpg` (snowy lot) | unchanged | 2010 street, 2014 driveway, Osaka show concept. I scanned all 68 Commons GX 460 files and found none off-road. |
| **GX 550** | unchanged `gx550-overtrail-beige-black.jpg` | unchanged | **Yes, all 3.** All 38 Commons GX 550/550h files are street, dealer or show. |
| **LX 450** | unchanged (dirt mound) | unchanged | 1 of 3 is a street shot (`lx450-white.jpg`). The other two are fine. |
| **LX 570** | unchanged (red dirt, Chile) | unchanged | None. All three are acceptable (dirt, mountain pass, snow). |
| **LX 600** | unchanged `lx600-sonic-quartz.jpg` (dealer lot) | unchanged | **Yes, all 3** (dealer lot, show stand, event lawn). Commons, Flickr CC and Openverse have no LX 600 off-road shot. |

New Lexus sources: all by Pareekshith Indeever, Pexels licence. The truck has Qatar plates, which the photographer already blurred.
- `lx470-coastal-sand-flats.jpg`: https://www.pexels.com/photo/car-on-desert-10697778/
- `lx470-water-splash.jpg`: https://www.pexels.com/photo/car-splashing-water-in-puddle-10697776/
- `lx470-sand-mangroves.jpg`: https://www.pexels.com/photo/lexus-suv-car-10697775/

I checked the generation on each: a 100-series body, LX 470 grille and pre-facelift clear-lens headlights.

### Grenadier
| Page | Hero before → after | Gallery | Still not off-road |
|---|---|---|---|
| **Family landing** | unchanged `station-wagon-trailmaster-overland.jpg` (Goodwood grass) | n/a | Yes |
| **Station Wagon** (`data/grenadier.json` page) | unchanged `station-wagon-goodwood-mud.jpg` | Added **`station-wagon-prototype-meadow.jpg`**: a muddy PT-2B test truck in a rural meadow, by Mario A. P., CC BY-SA 2.0, Flickr (https://www.flickr.com/photos/99058495@N00/51613991297). I cropped off the photographer's bottom-edge watermark line. Removed: `station-wagon-trialmaster-lawn.jpg` (concours lawn). | The hero and the Trailmaster test-truck photo are still Goodwood grass. The prototype photo is only 1024 px wide, too small for a hero. |
| **Quartermaster** | unchanged `quartermaster-goodwood-rear.jpg` | unchanged | **Yes, both.** All 18 Commons Quartermaster files are shows, streets or lawns. The one Flickr CC Quartermaster photo is a street shot. |

I scanned about 100 Grenadier files on Commons visually, including Kavango Safari, the portal-axle prototype, Rally Buzz, Chelsea Truck Co and Fieldmaster. Every one is a show stand, street, car park or event lawn. INEOS press images were not used because no clear reuse licence was found. Pexels and Unsplash searches found no Grenadier.

### G-Class
None of these pages changed. All keep their current photos and honest captions.

| Page | Hero (unchanged) | Status |
|---|---|---|
| **G 500** (`data/g-class.json` page) | `g500-grand-edition.jpg` (street) | All 3 street. The `hero_note` is still accurate. |
| **W463 gallery** | `w463-300gd-bridge.jpg` (timber bridge) | The hero is acceptable. `w463-gersberg-alm.jpg` (alpine inn) stays. The unused `w463-schoeckl.jpg` on disk is the same photo as the G 55 page hero, so I didn't reuse it. |
| **500 GE** | `500ge-techno-classica-side.jpg` | Commons has only 2 500 GE files, both indoor shows. The `hero_note` is still accurate. |
| **G 550** | `g550-miami.jpg` | Street. The Commons G 550 categories show only street, lot or show photos. |
| **4×4²** | `4x4-squared-field.jpg` | All 3 are show field, street or lot. I scanned all 38 Commons 4×4² files (street, garage, show and auction). |
| **Europa** | `europa-w463-swb-grass.jpg` | Still captioned "(NOT A EUROPA TRUCK)". No Europa-import photo in an off-road setting exists. |
| **G 63 6×6** | `g63-6x6-legendy-grass.jpg` | All 45 Commons 6×6 files are street, show or ramp. |

All Pexels and Unsplash G-Class hits were second-generation W464 G 63s, which don't fit any of these pages and are already used on `second-gen`.

## Unused files
- I added only files that are now in use, so there was nothing of mine to delete.
- These existing files are no longer referenced after this pass and were left on disk: `lexus/lx470-snorkel-build.jpg`, `lexus/lx470-2005-facelift.jpg`, `lexus/lx470-sand.jpg`, `grenadier/station-wagon-trialmaster-lawn.jpg`.

## Sourcing constraints found
1. **The Flickr image CDN blocks our User-Agent.** `live.staticflickr.com` returns 403 from CloudFront for any UA containing "Bot". I did not spoof the UA. The Flickr API still works for finding photos and checking licences. The one Flickr photo used was fetched through Openverse's image proxy (`api.openverse.org/v1/images/<id>/thumb/?full_size=true`), which caps it at 1024 px. Flickr photos are therefore usable for galleries but not heroes unless someone downloads them by hand.
2. **The Commons API (`w/api.php`) returned 429** for the whole session, probably because parallel agents share the IP. HTML category pages, `Special:Search` and `Special:FilePath` worked, with 3 s waits between requests.
3. **Pexels search pages can't be fetched** (robots.txt). Photos were found by WebSearch on photo-page titles and previewed straight from the CDN by ID.
4. **Freely licensed off-road photos of luxury-trim or current models basically don't exist** on Commons, Flickr CC, Openverse, Pexels or Unsplash. This applies to the GX 470/550, LX 600, G 500/G 550/4×4²/6×6, 500 GE and Grenadier/Quartermaster. As the fact-check suggests, Show Us Your Rig submissions or licensed owner and builder photos are the realistic fix.

## Leads not used
- Flickr, Mario A. P.: other photos from the same 2021 Grenadier test-fleet day may exist in that photostream. The 1024 px limit above applies.
- Pexels, Pareekshith Indeever (Dubai/Qatar): there are more shots from the same LX 470 session (10697769–10697779) if the gallery needs a swap.
