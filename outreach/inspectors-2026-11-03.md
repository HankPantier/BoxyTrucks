# PPI page outreach: inspection shops and networks (Nov 3, 2026)

Page: https://boxytrucks.com/pre-purchase-inspection/
Source: `data/inspectors.json` (updated 2026-10-30), deduped by URL: 15 shops + 7 networks = 22.

**Read before sending**

- **No per-family anchors exist.** `site/pre-purchase-inspection/index.html` has no id on the family blocks (`div.ins-fam`), only on the whole section (`id="specialists"`). So every shop link below uses `#specialists`, and the family column gives the label the shop appears under. Adding ids (e.g. `id="g-class"`) to the `ins-fam` divs in the template would let each email point straight to the right block.
- **Six of the seven networks are not on the page.** They're in `data/inspectors.json`, but the built page links only Lemon Squad (in the "Far away" card). Telling the others they're "listed" would be untrue, so hold them until they're on the page.
- **Most sites could not be fetched this session.** WebFetch only allowed URLs found through WebSearch, and search didn't return most of these shops' own domains. Only two sites were checked live: lemonsquad.com and vehicleinspectors.com. Where the table shows "(repo data, not re-verified)", the contact comes from earlier research in `data/inspectors.json` or `outreach/contacts_2.json`. Check those against the shop's site before sending. "None found" means nobody looked, not that the shop has no contact.
- **Expedition Imports** already got a sponsor pitch in `drafts_2026-10-29.json` (to Scott, via the contact form). Fold this into that thread, or wait for a reply, so they don't get two cold notes.
- The page footer says "Some links on this page are affiliate links". That's the VIN-check and tool links, not the shops, and the page also says "We have no business relationship with these shops." So "free, no strings" is accurate.

## Shops (listed on the page)

| Shop | Listed under (page link) | Contact | Notes |
|---|---|---|---|
| Classic Cruisers (classiccruisers.com) | Toyota Land Cruiser: https://boxytrucks.com/pre-purchase-inspection/#specialists | info@ClassicCruisers.com (repo data, not re-verified) | Site fetch blocked this session. Phone 888-376-2420. |
| Noah's Arks of SoCal (noahsarkstlc.com) | Toyota Land Cruiser: #specialists | Noahsarkstlc@gmail.com (repo data, not re-verified) | Site fetch blocked. Phone 760-497-1027. |
| Land Cruiser Heaven (landcruiserheaven.com) | Toyota Land Cruiser: #specialists | None found | Site fetch blocked. Phone 888-377-0710. Check the site for a form or IG. |
| Drewmotive (drewmotive.com) | Land Cruiser, Jeep, Ford Bronco, International Scout, Chevrolet K5 Blazer & Suburban, AM General Hummer: #specialists | clientcare@drewmotive.com (repo data, not re-verified) | Site fetch blocked. Listed under 6 families. Use "Bronco, Scout, Blazer and Land Cruiser" for [truck]. Phone 214-886-0200. |
| G&G Autohaus (ggmercedesrepair.com) | Mercedes-Benz G-Class: #specialists | None found | Site fetch blocked. Phone (702) 919-7397. |
| Expedition Imports (expedition-imports.com) | Mercedes-Benz G-Class, Unimog, Steyr-Puch Pinzgauer: #specialists | Form: https://support.expeditionimports.com/hc/en-us/requests/new (repo data, not re-verified) | Site fetch blocked. Already pitched as a sponsor Oct 29 (see above). Scott Ingham, President. |
| JC's British & 4x4 (jcbritish.com) | Land Rover Series & Defender, Land Rover Range Rover, Ineos Grenadier: #specialists | None found | Site fetch blocked. Phone (720) 586-4756. Search also found jcsbritish4x4.kukui.com, a vendor-hosted copy. Not used. |
| Rover Specialist (roverspecialist.com) | Land Rover Series & Defender, Land Rover Range Rover: #specialists | vinnie@roverspecialist.com (repo data, not re-verified) | Site fetch blocked. Phone 201-688-0049. |
| Austin RoverWorks (austinroverworks.com) | Land Rover Series & Defender: #specialists | None found | Site fetch blocked. Phone (512) 985-5191. |
| INDEPENDENT Land Rover Specialists (indlr.com) | Land Rover Series & Defender, Land Rover Range Rover: #specialists | None found | Site fetch blocked. Phone 301-656-5651. |
| John's European Auto Service (europeanautoreseda.com) | Land Rover Range Rover: #specialists | None found | Site fetch blocked. Phone (818) 343-7284. Search found johnseuropeanauto.mechanicnet.com, a vendor-hosted copy. Not used. |
| REV Outfitters (revoutfitters.com) | Jeep: #specialists | None found | Site fetch blocked. Phone 970-425-5831. |
| Reed Consulting LLC (reedconsultingllc.com) | Ford Bronco: #specialists | Details@reedconsultingllc.com (repo data, not re-verified) | Site fetch blocked. Phone (414) 559-2455. |
| LexTechs of Atlanta (lextechsofatlanta.com) | Toyota 4Runner, Lexus LX & GX: #specialists | None found | Site fetch blocked. Phone (678) 705-4620. |
| ATLR (atlr.net) | Toyota 4Runner, Lexus LX & GX: #specialists | None found | Site fetch blocked. Phone (303) 487-6195. |

## Networks

| Network | Listed under (page link) | Contact | Notes |
|---|---|---|---|
| Lemon Squad (lemonsquad.com) | Mobile-inspector option ("Far away" card): https://boxytrucks.com/pre-purchase-inspection/ | Form: https://lemonsquad.com/corporate (partnership inquiries; the contact page points there) | **Verified live.** No public email or IG. lemonsquad.com/contact offers only phone (888) 231-7965 and customer login messaging. |
| Vehicle Inspectors (vehicleinspectors.com) | **Not on page** | dispatch@vehicleinspectors.com; IG @vehicle.inspectors | **Verified live** (site footer). Contact page: https://vehicleinspectors.com/contact/. Hold until listed. |
| MotorTech Classic Car Network (motortechappraisals.com) | **Not on page** | None found | Site fetch blocked. Hold. |
| CARCHEX (carchex.com) | **Not on page** | None found | Site fetch blocked. Hold. Inspections are done by Lemon Squad. |
| CarInspections.com | **Not on page** | None found | Site fetch blocked. Hold. |
| PPI Auto (prepurchaseauto.com) | **Not on page** | None found | Site fetch blocked. Hold. |
| American Classic Appraisals (americanclassicappraisals.com) | **Not on page** | None found | Site fetch blocked. Hold. |

**Totals (22):** email 6 (1 verified live, 5 from repo data), form 2 (1 verified live, 1 from repo data), neither 14 (one of those, Vehicle Inspectors, also has an IG handle alongside its email).

## Email template

**Subject:** [Shop] is listed on BoxyTrucks' pre-purchase inspection page

Hi [Name],

I'm Hank Pantier, and I run BoxyTrucks.com, a free buyer's guide to boxy 4x4s. [Shop] is listed on our pre-purchase inspection page as a recommended option for [truck] owners:
https://boxytrucks.com/pre-purchase-inspection/#specialists

It's free, with no strings. If anything is wrong or out of date, like your location, services or whether you travel, just reply and I'll fix it.

If it seems useful, would you consider linking to the page, or sharing it with customers who ask about buying a [truck]? No pressure either way.

Thanks,
Hank Pantier
BoxyTrucks.com

## Instagram DM

Hi, Hank from BoxyTrucks.com here. We list [Shop] free as a recommended pre-purchase inspection option for [truck] buyers (boxytrucks.com/pre-purchase-inspection). Happy to fix any details, and feel free to share it if it helps your customers.


> Update (Nov 3): each family block on the page now has its own anchor, e.g. https://boxytrucks.com/pre-purchase-inspection/#g-class, #land-cruiser, #land-rover, #4runner, #jeep, #bronco, #scout, #range-rover, #lexus, #grenadier, #hummer, #chevrolet, #unimog, #pinzgauer. Use the family anchor instead of #specialists.
