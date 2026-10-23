# Affiliate programs: supplier-by-supplier verification

Checked 2026-10-22 against primary sources: each supplier's own pages (homepage footer, `/affiliate`-style paths, the network scripts installed on the store) and the networks' own sign-up and portal pages. Every rate, URL and email below was seen on one of those pages. "Unknown" means it could not be confirmed. Nothing was filled in from aggregator sites. FlexOffers/Lasso-style listings were ignored because the ones checked were stale ("not currently offering this program").

**Sort order.** Rows are sorted by value, meaning links times likely commission:

- Programs that exist come first, ordered by expected value.
- Unpublished rates are treated as roughly 3% (the network's typical rate).
- Programs whose placement is already planned in `AFFILIATES.md` (Tire Rack, eBay) are counted at their planned reach.
- Suppliers with no public program come after that, in link order. Their value depends on asking them.

**Corrections to the repo's guesses:**

- **Lucky8:** the program is **discontinued**. Its UpPromote portal says so.
- **Metal Tech 4x4:** **has** a 10% program.
- **ARB:** the 3–5%, 30-day figures are confirmed.
- **Tire Rack:** 6% confirmed. The cookie length is not published.
- **Front Runner:** frontrunneroutfitters.com now redirects to dometic.com.
- **RockAuto:** no program found.
- The link counts in `AFFILIATES.md` are out of date. The counts below are the current ones from the brief.

**Deep-link notes for `data/affiliates.json`:**

- **Parameter-style programs** (eBay, UpPromote, GoAffPro, Tire Rack) should use `"params"`, the same way the Amazon entry does, not `template`.
- **AvantLink:** the current format documented in AvantLink's support article "Anatomy of an Affiliate Tracking Link" is `https://www.avantlink.com/click.php?tt=cl&merchant_id=<merchant UUID>&website_id=<your website UUID>&url={url}`. The legacy `mi=/pw=` form wasn't confirmed in their docs. Copy whatever the AvantLink Custom Link Builder gives you after approval.
- **Impact:** the format is `https://<brand vanity domain>/c/<pubid>/<adid>/<campid>?u={url}`. The vanity domain (`*.sjv.io`, `*.pxf.io`, etc.) is shown in your Impact account after approval.
- **CJ:** the format is `https://www.anrdoezrs.net/links/<pid>/type/dlg/{raw}`.

| Supplier | Links | Program? | Network | Commission / cookie | Apply at | Deep-link format | Notes/source |
|---|---|---|---|---|---|---|---|
| Metal Tech 4x4 (metaltech4x4.com) | 46 | **Yes** | UpPromote (Shopify app, in-house) | **10%** of referral sales (link or coupon); cookie not stated | https://af.uppromote.com/metal-tech-4x4/register | Param: `?sca_ref=<affiliate id>.<hash>` (confirmed in the store's uppromote.js). Use `"params": {"sca_ref": "…"}` | UpPromote script on homepage; register page meta: "You will get a 10% commission on total referral sales…" |
| ARB / Old Man Emu (arbusa.com) | 33 | **Yes** | AvantLink (merchant 40329) | **3–5%** (5% headline; "3-5% depending on creator size and engagement"); **30-day** cookie | https://www.avantlink.com/signup/publisher-united-states/?merchant=40329 | AvantLink: `https://www.avantlink.com/click.php?tt=cl&merchant_id=<UUID>&website_id=<UUID>&url={url}` | https://arbusa.com/affiliates. High average order value (lockers, bumpers, suspension) |
| Tire Rack (tirerack.com) | 0 now, planned on every model ("biggest tire" answers) | **Yes** | In-house | **6%** ("Earn 6% commission on every sale"); cookie not published | https://www.tirerack.com/affiliate (application: https://www.tirerack.com/modalPopups/affiliateAgreement.jsp) | Appears to be a URL param `?affiliate=<code>` (seen on indexed tirerack.com URLs). Confirm in welcome email | Policies: https://www.tirerack.com/affiliate-policies. Phone only, no email shown |
| eBay Partner Network | 0 now (planned) | **Yes** | EPN (in-house) | **1–6%** by category (Auto Parts & Accessories example: 2.5%); per-transaction caps apply; **24-hour** click window (auction wins within 10 days); last-click | https://partner.ebay.com/campaign-promo-signup/eBay-Partner-Network.brand | Params on any ebay.com URL: `mkevt=1&mkcid=1&mkrid=711-53200-19255-0&campid=<campaign id>&toolid=10001` (optional `customid=`), per developer.ebay.com "Creating an EPN Tracking Link" | Good for NLA/used parts (Scout, FJ40, classic Defender, early Bronco). Rate card: partnernetwork.ebay.com/our-program/rate-card |
| Goal Zero (goalzero.com) | 0 | **Yes** | Partnerize (Ascend/Pepperjam) | **Up to 10%** "dynamic"; **30-day** cookie; average order $600+ | Creators: https://www.ascendpartner.com/affiliate/registration?refid=138677&usertype=1. Businesses: …&usertype=2 | Generated in the Partnerize/Ascend dashboard (format not published) | https://goalzero.com/pages/affiliate-marketing-program ("This program is managed by Partnerize") |
| RealTruck (realtruck.com) | 0 | **Yes** | Impact | Rate not published ("competitive"); **30-day** attribution window | https://app.impact.com/campaign-promo-signup/RealTruck.brand?execution=e1s1#/?viewkey=signUpPreStart | Impact: `https://<vanity>/c/<pubid>/<adid>/<campid>?u={url}` | https://realtruck.com/affiliate/. Jeep, Bronco and Toyota accessories |
| Summit Racing (summitracing.com) | 0 | **Yes** | Not stated (no network domain on the page) | **5%**; cookie not stated | https://www.summitracing.com/summit-racing-affiliate | Unknown (issued after approval) | Footer "Become an Affiliate". Site blocks bots; read via WebFetch |
| CJ Pony Parts (cjponyparts.com) | 0 | **Yes** ("CJ Creators") | CJ (signup.cj.com) | Rate and cookie not published | https://signup.cj.com/member/signup/publisher/?cid=6969901#/branded | CJ: `https://www.anrdoezrs.net/links/<pid>/type/dlg/{raw}` | https://www.cjponyparts.com/creators. Strong in Bronco parts |
| JEGS (jegs.com) | 0 | **Yes** | Impact | **1%** (3% on JEGS-brand products); **5-day** cookie | https://app.impact.com/campaign-promo-signup/JEGS-High-Performance.brand?execution=e1s1#/?viewkey=signUpPreStart | Impact (as above) | https://www.jegs.com/AffiliateMarketing. Low value for this site |
| Garmin (inReach) | 0 | **Yes** ("affiliate program allows you to earn commission") | Not stated; application runs on a CreatorIQ portal | Not published | https://ambassadors.garmin.com/media (Media/blogger track; from https://www.garmin.com/en-US/ambassadors-and-affiliates/) | Unknown | Relevant to overlanding/satellite-messenger content |
| Overland Journal / Expedition Portal store (overlandjournal.com) | 0 | **Yes** | GoAffPro (Shopify) | Rate not published; store config sets a **7-day** cookie (604800 s) | Portal: https://overland-journal-9e35.goaffpro.com/create-account | Param: `?ref=<code>` (GoAffPro loader identifiers `ref`/`aff`) | GoAffPro loader on homepage. Contact: Service@overlandinternational.com |
| Dometic (incl. Front Runner, which now redirects to dometic.com) | 0 (Front Runner planned) | **Likely yes, unverified** | Unknown | Unknown | Affiliate page: https://partners.dometic.com/affiliates/ (search-indexed as "Affiliate program", but the site has an expired TLS certificate and blocks crawlers, so it could not be read). Ambassadors: https://www.dometic.com/en-us/lp/ambassador-signup (Airtable form) | Unknown | Open the partners page in a browser to confirm the terms. The ambassador track is creator sponsorship, not confirmed as commission-based |
| iKamper (rooftop tents) | 0 | **Partial**: Ambassador/creator program | AvantLink tracking is installed on the store (Shopify AvantLink app config) | Not published | Ambassador application (Notion form linked from https://ikamper.com/pages/ambassadors-creator-partnerships) | If on AvantLink, use the AvantLink format | Once in AvantLink (via ARB), search the merchant list for iKamper. dometic.com's own promo terms mention iKamper products, so the Dometic program may cover it too |
| Discount Tire / America's Tire | 0 | **Yes, a page exists** | Unknown | Unknown | https://www.discounttire.com/customer-service/affiliate-program (same on americastire.com) | Unknown | The page is a JavaScript app and the terms didn't render for any fetcher. Open it in a browser |
| Morris 4x4 Center (morris4x4center.com) | 0 | **Yes, a page exists** | Unknown | Unknown | https://www.morris4x4center.com/affiliate-program | Unknown | Search-indexed as "Affiliate Program". The site returned 503 to every fetch, so the terms weren't seen |
| Quadratec (quadratec.com) | **652** | **No public program found** | — | — | — | — | Only a Jeep-club link exchange (quadratec.com/community/jeep-clubs/sign-up, no commission). **Ask:** customerservice@quadratec.com (on homepage) or https://www.quadratec.com/help |
| RockAuto | **379** | **No** | — | — | — | — | Nothing in footer, help pages or affiliate paths. Contact via https://www.rockauto.com/help/ |
| FCP Euro | **362** | **No public program found** | — | — | — | — | Nothing in footer or affiliate paths, and no info.fcpeuro.com program. **Ask:** https://www.fcpeuro.com/contact-us or https://help.fcpeuro.com |
| Lucky8 (lucky8llc.com) | **353** | **Discontinued** | UpPromote (Secomapp) | — | (was https://lucky8llc.com/pages/register-affiliate-account) | (was `?sca_ref=`) | Portal https://af.secomapp.com/lucky8offroad/register says "Affiliate Program Discontinued". **Ask to reinstate:** https://lucky8llc.com/pages/contact-us |
| Cruiser Corps | **219** | **No public program found** | — (Shopify) | — | — | — | **Ask:** contact@cruisercorps.com. As a Shopify store they could switch on UpPromote/GoAffPro/Collabs quickly |
| CruiserTeq | **196** | **No public program found** | — (BigCommerce) | — | — | — | **Ask:** https://cruiserteq.com/contact-us/ |
| LR Direct | **134** | **No public program found** | — | — | — | — | **Ask:** https://www.lrdirect.com/contact |
| Expedition Imports | **128** | **No public program found** | — (BigCommerce) | — | — | — | **Ask:** https://www.expedition-imports.com/contact-us |
| ExtremeTerrain (Turn5) | **106** | **No**: dealer program only | — | — | — | — | Help center describes a dealer pricing program only. **Ask:** https://www.extremeterrain.com/contact.html |
| Bronco Graveyard | **103** | **Unknown** | — | — | — | — | Footer "Affiliates" page (broncograveyard.com/rt-1286-affiliates.html) has no content. **Ask:** http://www.broncograveyard.com/contact.html |
| LC Engineering (lceperformance.com) | **94** | **No public program found** | — | — | — | — | Has a sponsorships page (/Sponsorships-s/23146.htm). **Ask:** https://www.lceperformance.com/contact-us/ (submissions@lcengineering.com is for reader-ride photos only) |
| ToyotaPartsDeal | **93** | **No public program found** | — | — | — | — | Discount OEM dealer. **Ask:** https://www.toyotapartsdeal.com/service/contact/us.html |
| IH Parts America | **91** | **No public program found** | — | — | — | — | **Ask:** https://www.ihpartsamerica.com/contact-us-5054.html |
| Patrol A Part (AU) | **86** | **No public program found** | — | — | — | — | Australian; low US conversion. **Ask:** https://www.patrolapart.com.au/contact-us |
| Rovers North | **77** | **No public program found** | — | — | — | — | Site blocks bots. Sells Rovers Magazine ads (media kit form: https://blog.roversnorth.com/media-kit/, 1-800-403-7591) |
| GwagenParts.com | **57** | **No public program found** | — | — | — | — | Has a customer "$5 off" share-a-gift feature only. **Ask:** info@gwagenparts.com / sales@gwagenparts.com |
| Slee Off-Road | **53** | **No public program found** | — | — | — | — | **Ask:** info@sleeoffroad.com (on homepage) |
| Super Scout Specialists | **35** | **No public program found** | — | — | — | — | **Ask:** superscout1318@gmail.com (published on /sss-contact-information) |
| Atlantic British / RoverParts.com | **35 + 27** | **No public program found** | — | — | — | — | Both domains block bots, and the search index shows no program. Use the site's contact page in a browser |
| LexusPartsNow | **29** | **No public program found** | — | — | — | — | Same operator style as ToyotaPartsDeal. **Ask:** https://www.lexuspartsnow.com/service/contact/us.html |
| Eurowise | **29** | **No public program found** | — (Shopify) | — | — | — | **Ask:** info@eurowise.com |
| 4 Wheel Parts | 0 | **No public program found** | — | — | — | — | Only a customer Reward Points program. `/affiliate` paths redirect home. **Ask:** https://www.4wheelparts.com/contact-us |
| Rough Country | 0 | **No**: sponsorship/partnership program (free product, no commission) | — | — | https://www.roughcountry.com/partnership-program | — | Trail Crew ambassadors: /ambassadors |
| TeraFlex | 0 | **Unknown** | — | — | — | — | Site blocks bots and no program is indexed. Contact page lists "Event Donations & Individual Sponsorships": https://teraflex.com/contact-us |
| WARN | 0 | **No public program found** | — | — | — | — | partners.warn.com is a dealer portal. Sponsorships: https://www.warn.com/pages/sponsorships-donations |
| MAXTRAX | 0 | **No public program found** | — | — | — | — | maxtraxusa.com redirects to us.maxtrax.com.au (refused connection). AU sponsorship form: https://maxtrax.com.au/pages/sponsorship-request |
| Hagerty | 0 | **No public publisher program found (US)** | — | — | — | — | Only a members' refer-a-friend (/drivers-club/marketing/referral) and referral.hagerty.com (crawler-blocked). Ad/sponsor partnerships: https://www.hagerty.com/media/partnerships/ |
| Bring a Trailer | 0 | **No** | — | — | — | — | /partners/ lists brand partners only: "reach out to us at partnerships@bringatrailer.com" |
| AutoTempest | 0 | **No** | — | — | — | — | /partners lists creators AutoTempest sponsors (it pays out, not in). contact@autotempest.com |

## Do these first (top 8 applications)

1. **ARB via AvantLink** (33 links, 3–5%, 30 days, high average order). The AvantLink account also lets you check whether iKamper and other overland brands are on AvantLink.
2. **Metal Tech 4x4 via UpPromote** (46 links, 10%). After approval, add `"params": {"sca_ref": "<id>.<hash>"}`.
3. **Tire Rack** (6%, in-house). This unlocks the planned tire-size link on every model page.
4. **eBay Partner Network** (1–6%). Use `params` with `campid` for parts that are no longer available new and for used parts on vintage trucks.
5. **RealTruck via Impact** (30-day). The same Impact account then covers JEGS with one more click.
6. **Goal Zero via Partnerize/Ascend** (up to 10%, 30 days, $600+ average order). Fits overlanding power content.
7. **Summit Racing** (5%). Broad catalog for fluids, filters and tools in the service tables.
8. **CJ Pony Parts via CJ**. Bronco coverage, and the CJ publisher account it creates is reusable.

Send these emails in parallel (no public program; highest link counts):

- Quadratec (652): customerservice@quadratec.com
- FCP Euro (362): contact form
- Lucky8 (353): ask them to reinstate the UpPromote program
- Cruiser Corps (219): contact@cruisercorps.com
- CruiserTeq (196): contact form

Pitch each one with their exact outbound-link count from BoxyTrucks.
