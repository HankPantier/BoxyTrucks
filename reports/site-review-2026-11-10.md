# Site review and fixes (Nov 10, 2026)

Hank: "fix them all - for #8 just use Hank everywhere".

1. Indexing: 332 repair pages with no Search Console impressions (Oct 22–Nov 8) and under 400 words are now noindex, follow and out of the sitemap (`data/repair_noindex.json`; sitemap 1,401 → 1,069 URLs). Their fixes are folded into each truck's problems page under "How to fix them". The 40 repair pages with real impressions are queued in `reports/repair-deepen-queue.json`, 5 a day (`reports/REPAIR_DEEPEN_PROCEDURE.md`, daily 1:47 pm ET). First done: FJ40 front disc brake conversion (359 → 945 words, 5 sources). Repair pages also support `know`, `mistakes` and `cost_note`.
2. Cookie banner only shows to UK/EU/EEA/Swiss time zones, and is slimmer (about 110 px on a phone, was about 280). Everyone else is counted by default and can opt out via the footer's Cookie settings. Cookie policy updated.
3. Tire math tables stack as two-column cards on phones (the 900 px table rule had forced them back into a cramped table).
4. Years, tires and problems pages show the generation's licensed hero photo with credit in the header.
5. Model guides: "The short version" card at the top (sweet-spot years, years to watch, biggest stock tire, number of known problems, typical price); the story collapses after 3 paragraphs; repairs show 3 then "Show N more"; sources collapse. The 80 Series guide is about 25% shorter on a phone.
6. Home page: 8 family cards plus chips for the rest, 3 repair cards, 6 for-sale rows; the stories, shops and resources bands moved off the home page (still in the nav). About 35,000 → 15,500 px on a phone. Repairs index: grouped by family, collapsed per truck, searchable; about 104,000 → 10,000 px.
7. Long titles shortened (garage, importing, engine swaps, checklists, gifts).
8. Name: "Hank" everywhere on the site (owner notes, about, partner page, schema Person, social photo credits, newsletter). Hank's own outreach email signatures in reports/ were left alone.
