# Fact-check: site-wide (everything that is not a model page)

Scope: `data/resources/*.json`, `data/resources_manual.json`, `data/social_manual.json`, `data/reading.json`, `data/suppliers.json`, `data/affiliates.json`, the `BUILDERS` / `STORIES` / `LATER` constants and the `faqs = [...]` block in `build.py`, `templates/home.html`, `templates/disclaimer.html` and `templates/disclosure.html`.

Method:
- **Links.** I curled all 299 URLs in these files with a browser User-Agent and followed redirects.
- **YouTube.** A missing `@handle` returns 404, so a 200 confirms the channel exists. For each channel I pulled the description, subscriber count and a channel search to check its stated focus.
- **Instagram.** Profiles were checked through Instagram's public profile endpoint, which is heavily rate-limited. See the Instagram section below.
- **Forums and other links.** Forums behind Cloudflare, captcha or WAF pages (403, 202, or "Just a moment"/"Checking your browser") are real sites that block bots, so I counted them as OK.
- **Reading and story articles.** Each one was read via curl or WebFetch.

---

## data/resources/*.json

### Corrections made
- **4runner, Hagerty.** The `?p=6601` URL changed to its canonical address: https://www.hagerty.com/media/car-profiles/rise-of-1984-89-toyota-4runners/
- **4runner, TrailCo.** The focus now names Brenan Greene. He founded both TrailCo and Trail4Runner.com, according to the channel description and the trail4runner.com author box.
- **g-class, Club G-Wagen.** Removed "founded 1998": the site does not state it. The `/forum/` link redirects to an IconCaptcha "validate your humanity" page, and the note now says so.
- **g-class, Four By Four Club.** Removed "(a one-man shop)", which is unsourced.
- **g-class, Handsome Motors.** The URL now uses `www.`. I confirmed "200+ Gs" on the buyer's guide page and "Charleston, SC" on the homepage.
- **grenadier, Quartermaster page.** The URL now uses the redirect target `https://ineosgrenadier.com/en/us/quartermaster`.
- **grenadier, Norweld.** The URL now uses the redirect target `/ute-canopies/vehicle/ineos-quartermaster/`.
- **grenadier, NHTSA recall IDs.** 23V828, 23V903 and 25V147 are all INEOS Grenadier campaigns for 2023–24 (NHTSA campaign API). No change needed.
- **land-rover, Bluelandy.** The focus said "Overlanding the Americas". The channel describes an "overland journey around the world" (Kai and Irati, 1998 Defender 110 Td5), and the focus now says that.
- **land-rover, Series 2 Club.** The URL now uses `https://landrover.series2club.co.uk/`.
- **lexus, LX 470 TSB thread.** `showthread.php?p=` changed to the canonical thread URL.
- **nissan-patrol, 4X4 Australia (YouTube).** The focus claimed "Patrol buyers guides and a long-running 1988 GQ project truck". A channel search found no such project. It found a Patrol ST road test plus Hilux, Ranger and BJ73 projects. The focus is now "road tests (including the Patrol), comparisons and project builds".
- **nissan-patrol, Off Course 4x4.** Removed "recommended on the Patrol 4x4 Club SA forum", which I can't verify (the forum blocks bots). The channel does carry many Patrol trail videos.
- **range-rover, Blackbox Solutions.** Removed "channel began as BBSP38", which is unverifiable.
- **range-rover, Dunsfold.** I kept "Darién Gap Range Rover": the collection's own videos show the "Darrian Gap" Trans-Americas Expedition Range Rover. The wording now matches.

### Removed (dead, empty or mismatched)
- **nissan-patrol: `@4wdaction` (YouTube).** The channel has 535 subscribers, no videos and a generic description. It is not the 4WD Action TV show channel, and the note's claim about a ZD30/Y62 episode can't be supported.
- **nissan-patrol: `@Hulk4x4` (YouTube).** It has 15 subscribers and a single power-station video, so the "free-wheeling hubs for GQ/GU Patrols" focus isn't supported. The `@hulk_4x4` Instagram entry stays (see the Instagram section).
- **jeep: Advance Adapters (YouTube `@AdvanceAdapters`).** It has 51 subscribers and 4 videos from 2007–08, so it is effectively dormant. The company's active Instagram (`@advanceadapters`, about 23.7k followers) stays.

### Verified as listed (spot-checked focus)
- **All YouTube channels.** All 77 resolve, and the channel names match.
- **Focus claims confirmed from channel descriptions or searches:**
  - Quadratec "since 1990" and Morris "since 1991".
  - ToyTec "since 2004" and Anything Scout "1980".
  - LC Engineering as a Toyota 4-cylinder specialist.
  - Alliance Motorworks in Loveland, CO, and Nothing But G's as its G channel.
  - Expedition Motor Company's Wolf builds and ExpedImports' focus on Unimog, G and Pinzgauer.
  - Owl's and Agile's Grenadier videos in Moab.
  - Lucky8's 1995 5-speed Discovery project.
  - Atlantic British's P38 how-tos.
  - Driving Line's Built2Wander 1975 Scout II.
  - The Scout II projects on Velocity Restorations, Jacks Custom Restoration and Cars with Nash.
  - Jammy Gits' 2005 Defender 110.
  - Matt's Off Road Recovery in southern Utah.
- **Other page facts:**
  - TLCA "since 1976" is on tlca.org.
  - 4X4 Australia's Patrol history is by Dean Mellor, dated 15 Oct 2026.
  - The Super Scout Specialists FAQ has production figures.
  - Binder Books sells "original and licensed reprint manuals".

---

## data/resources_manual.json and data/social_manual.json (owner-supplied; nothing removed)
- **YouTube.** The manual entries (`@Gluxetravel`, `@Littlehandegan`, `@Nothing-but-Gs`) all resolve. `@Gluxetravel`'s description names its Instagram as `gluxetravel_g500`.
- **Instagram.** See the Instagram section. Per the coordinator's rule, I removed nothing from these files.
- **Labels and handles.** The manual YouTube labels are bare handles (`@Littlehandegan`), while `data/resources/g-class.json` names the same channel "Handsome Motors". That is cosmetic only.
- **@gwagonrally.** I couldn't find what this account is from outside Instagram.

## Instagram
INSTAGRAM_PLACEHOLDER

---

## data/reading.json (owner-supplied; text corrected, nothing removed)
- **g-class/w460, MotorTrend "Mercedes-Benz G-Class Travels the World".**
  - Author added: Brett T. Evans. Date is now October 2014 (published 13 Oct 2014).
  - The note said "bought in 1988… roughly 559,000 miles… between 1990 and 2014". The article says Holtorf **set out in 1988** and spent **26 years** covering **more than 550,000 miles** and **215 countries**, and that Otto was going to the Mercedes-Benz Museum in Stuttgart. The note is rewritten to match.
  - Note: the article itself calls the truck "10-year-old" in 1988, which conflicts with other accounts of Otto. I left that out.
- **land-cruiser/fj40, MotorTrend.**
  - The title was wrong ("Toyota Land Cruiser classic drive review", the URL slug). The real headline is **"We Drive Five Classic Toyota Land Cruiser Off-Road SUVs"**.
  - Author added: Aaron Gold. Date added: July 2023.
  - The note now lists the five trucks (FJ40, FJ55, FJ60, FJ80, 100 Series) and says they were borrowed from the Land Cruiser Heritage Museum.
- **land-cruiser/70-series, Overland Journal.**
  - This is a **podcast episode with transcript** (Expedition Portal podcast), not an article, so the publisher is now labelled that way.
  - The note said "the narrow rear track". Paul Marsh says "a very narrow track", so "rear" is removed.
- **land-cruiser/200-series, Expedition Portal "Staples in Tents".** Confirmed via WebFetch: author Necota Staples, 7 Dec 2022, a 2016 200 Series, first trip through Mexico then Baja, "next voyage will be up to the Arctic Ocean".
- **land-rover/series, Huckberry.**
  - Title, author and date are confirmed (27 Nov 2023), and it is "Part 2" of the scene report.
  - The 1968 Series IIA and the Panama-to-Mexico trip in a friend's truck are confirmed by Xavier himself on Overland Journal's podcast page (https://overlandjournal.com/pages/sinuhe-xavier-on-living-in-the-moment-of-adventure). He says the truck was "a 67, 68", and the guest bio says "Panama to Guatemala".
  - The Huckberry page itself blocks bots, so I couldn't read its body text. Low risk.
- **grenadier/station-wagon, Expedition Portal thread.** Confirmed: Matt P, 25 Jan 2024, a Trialmaster, left the Grenadier pub in London in July 2023, two young kids, Romania and the Stans, "5 year global warranty" and "mostly proven components".
- **land-cruiser/100-series, OVR.** Confirmed: a 1999 truck, five owners, nearly 300,000 miles, Bailey Canyon in the San Bernardino NF, OME rear springs, Tundra wheels, Slee slider steps, BIO dual swing-out rear bumper, and a Smittybilt X20 winch "hidden… behind the front license plate". The mechanic's findings were dirty fluids and filters, a fuel pump, and later a steering rack. The page shows no byline or date, so those stay blank.

---

## data/suppliers.json (search patterns)
Each pattern was tested with "oil filter" and a repair-style query.

**Corrections made:**
- **CruiserTeq (land-cruiser, lexus): it was broken.** The site is BigCommerce, so the WordPress-style `?s={q}&post_type=product` just returned the homepage. The pattern is now `https://cruiserteq.com/search.php?search_query={q}`, which returns results.
- **Quadratec (jeep): it was broken.** `search?keys={q}` returns "0 results" for every query. The path form `https://www.quadratec.com/search/{q}` returns results.
- **RockAuto (nissan-patrol): wrong tool.** `partsearch/?partnum=` only matches part numbers, but the template sends a repair title plus model name, and RockAuto doesn't catalogue the Patrol. It is replaced with Patrolapart's search, `https://patrolapart.com.au/product-search?criteria={q}`, which returned 29 results for "oil filter" and 15 for "swivel hub kit".
- **Atlantic British (land-rover, range-rover).** `atlanticbritish.com/search` gives a 403 to bots and redirects to roverparts.com, so the pattern now goes direct: `https://www.roverparts.com/search/?q={q}`.
- **FCP Euro (g-class).** `/products?keywords=` redirects, so the pattern now uses `https://www.fcpeuro.com/Parts?keywords={q}` directly. It works with a browser User-Agent.
- **Super Scout Specialists (scout).** `/search?q=` redirects, so the pattern now uses `https://www.superscoutspecialists.com/filterSearch?q={q}`.

**Removed:**
- **Morris 4x4 Center (jeep).** The whole site returned **503 Service Unavailable** on every attempt over about an hour. Restore it if the site comes back. `data/jeep.json` (owned by another agent) still links to morris4x4center.com, so those links are currently dead too.

**Unverified:** Rovers North `search?q={q}` sits behind Cloudflare (403). It is the standard Shopify search format, so I left it.

## data/affiliates.json
- **Amazon is live.** Amazon links on the built site carry `tag=boxytrucks-20`, and `affiliate_rewrite` adds `rel="sponsored nofollow"`. The footer shows the Associates statement. I checked `site/models/land-cruiser/fj40.html`, which has 22 tagged links. All other programs have empty templates, so nothing else is monetised yet.
- **Unverified internal notes.** The ARB (AvantLink merchant 40329, 3–5%, 30-day cookie) and Tire Rack (6%) terms are not checked. They are internal notes, not shown on the site.
- **Stale link counts.** The "N links on site" counts are out of date. A count across `data/` today gives FCP Euro about 300, Cruiser Corps 227, Lucky8 236, CruiserTeq 192, Expedition Imports 130, LC Engineering 95, Rovers North 143, LR Direct 92, Slee 59, Metal Tech 36, GwagenParts 35 and Eurowise 38. Other agents are still editing, so I didn't rewrite them.

---

## build.py constants

**BUILDERS:**
- **The FJ Company.** `https://www.thefjcompany.com/` is now a **parked GoDaddy domain** (it redirects to `/lander` with a parking script). The company's live site is **https://www.fj.co/**: its title is "The FJ Company - Custom Land Cruisers Built For Today's Driver", and it links youtube.com/thefjcompany. The URL is fixed.
- **Jack Wagon Overlanding.** The name was spelled "Jackwagon"; the site and YouTube use "Jack Wagon Overlanding". The description is now "overland parts & builds", since they make and install G-Wagen parts.
- **Expedition Motor Company.** "W460 / Wolf restorations" is now "ex-military 250 GD / Wolf restorations", matching the site's title ("Mercedes 250GD Restorations… ex-military, convertible Geländewagens"). Many Wolfs are W461s, so "W460" was too narrow.
- **ICON 4x4 and Arkonik.** Both are OK. ICON's channel says "fully customized Toyota FJ40 builds"; Arkonik builds Defender 90/110 restomods.

**STORIES:**
- All three links and titles are checked against the articles above.
- The `lc-dune.jpg` alt text said "silver"; the truck is **white**. It is now "A white Toyota Land Cruiser 200 Series climbing a desert dune at sunset".
- The photo is a Dubai desert-safari truck (signwriting and a Dubai plate), not the Staples in Tents truck. That is OK as an illustration, but readers may assume it is the featured truck.
- The other two story images match their alt text: a vintage RHD Series cockpit in the desert, and Egyptian tour-company 70 Series Troop Carriers.

**LATER:** None of these makes is covered on the site yet, so the list is accurate. Bronco "1966–77" is correct for the first generation.

## Home page and site FAQ (`faqs` in build.py, templates/home.html)
- **PARTS answer.** It said "Every repair … links to the parts … plus an Amazon search". **10 of 415 repairs have no parts** (recall checks, infotainment, door-hinge sag, sunroof drains and the like), and Amazon appears only where a retail query makes sense. It is softened to "Nearly every repair…, usually with an Amazon search alongside", plus a note that recall checks and a few dealer-only jobs have no parts links.
- **BUYING answer.** It said "Each guide links to … AutoTempest and Bring a Trailer". `scout/scout-motors` (not on sale yet) has no searches, so it now reads "Each guide to a truck you can buy…".
- **Claims confirmed true:**
  - Every generation of all 10 families has a full page.
  - Every page has a non-empty `sources` list, and the template renders it at the bottom.
  - The "Coming later" list renders at the bottom of the models page.
  - The submit form has a required "story" textarea for corrections.
  - The affiliate disclosure page exists.
- **Featured Builds.** home.html and the FAQ say good submissions run "here and on their model page". No Featured Build section exists in `gen_page.html` yet. Both are phrased as a future promise ("we're picking the first…"), so I left them, but someone needs to build that section before the first feature runs.
- **Hero caption.** "LAND CRUISER 80 SERIES · CAUCASUS, GEORGIA": the photo is an 80 Series (DIESEL grille badge, roof rack). I couldn't verify the location from the image. Check the Unsplash or Pexels credit.
- **Not editable in my scope:** the `description=` passed to `render('home.html' …)` in build.py lists "G-Class, Land Cruiser, Defender, Range Rover, 4Runner, Lexus GX/LX and Grenadier". It omits **Jeep, Nissan Patrol and International Scout**, which are now covered. That line is code, outside the constants I was cleared to edit, so it needs a one-line fix by whoever owns build.py.

## templates/disclaimer.html and templates/disclosure.html
**Edits made (accuracy only):**
- The disclosure ended "Use the Show Us Your Rig form or email us." No email address appears anywhere on the site (there is no mailto, and the form posts via a hidden address), so I removed "or email us".
- Fixed the typo "Listings links" to "Listing links".

**Accurate as written:**
- The Amazon statement is accurate: links are tagged and marked sponsored.
- "Links that earn a commission are marked as sponsored in the page code" is true for every rewritten link.
- The "not affiliated" list (Mercedes-Benz, Toyota, Lexus, Land Rover, INEOS "or any other manufacturer") covers Jeep, Nissan, International and Scout Motors through "any other". Naming them would be clearer.

**For a lawyer to review:**
1. **No privacy policy.** The site runs Google Analytics (`G-XHC493ES9X`), and the submit form collects name, email, location, social handles and photos through a third-party form service. GA plus personal data collection usually needs a privacy policy and, for EU/UK visitors, cookie consent. This is the biggest legal gap.
2. **FTC disclosure placement.** The affiliate disclosure sits on a separate page and in the footer. The FTC expects a "clear and conspicuous" disclosure near the affiliate links themselves. Consider a short line beside the parts and "Where to buy" blocks.
3. **Content and photo rights.** The submit form's checkbox licence ("BoxyTrucks may publish my truck, story and photos… on the site and its social accounts") has no linked terms, no way to withdraw consent and no age statement.
4. **The "No liability" clause.** It is a broad exclusion. Whether it is enforceable varies by jurisdiction; personal-injury exclusions are often void for negligence in the UK and EU.
5. **"Never shown" email promise.** The form promises "Only used to contact you about a feature. Never shown." Make sure the form service's handling matches that.

---

## Top 5 remaining problems (site-wide)
1. **High. No privacy policy or cookie consent** while running Google Analytics and collecting personal data through the submit form. Legal review is needed.
2. **Med. Supplier search links send whole repair titles as the query** (for example "Front-axle harness recall (23V097) Second Gen"). Even with the patterns fixed, these long free-text queries mostly return zero results on FCP Euro, CruiserTeq and Super Scout. This only affects repairs without parts (10 sitewide), but those are mostly recall checks where a parts search makes no sense. Consider hiding the supplier search when a repair has no parts, which is a template change.
3. **Med. Morris 4x4 Center's site is down (503).** It is removed from suppliers.json, but `data/jeep.json` still links it. The Jeep page owners should check and replace those links.
4. **Med. Instagram verification is incomplete.** INSTAGRAM_TOP5
5. **Low. The home meta description omits Jeep, Patrol and Scout.** There is also no Featured Build section on model pages yet, despite the home page and FAQ promising one. And the lc-dune and Georgia hero images are illustrative, not the trucks or places the captions might imply.
