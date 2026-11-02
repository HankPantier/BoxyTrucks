# Outreach

- `vendors.json`: every shop the site links to (Oct 29, 2026), with page counts.
- `contacts_0-3.json`: research on each shop: contact, person, affiliate program and notes.
- `tracker.html`: source of the live Sponsor Outreach tracker (claude.ai artifact RZTLvdjnzNMBedundYzGoR). Shop records live in that artifact's database (`shops/<domain>`), not in this file.

## Site reputation (Oct 29, 2026)

Jack Wagon said his browser flagged boxytrucks.com as malicious. Findings:
- Google Safe Browsing: no unsafe content. Search Console Security issues: none. Cisco Talos: Neutral, category Transportation, not blocklisted.
- VirusTotal: 2/92 vendors say "phishing": Gridinsoft (automated: domain was 5 days old) and SOCRadar.
- Norton Safe Web: "Warning" (automated). Likely what Jack hit.
- Many business web filters block "newly registered domains" for the first 30 days (registered Oct 22, 2026, so that window ends around Nov 21).
- False-positive reports: Norton form (filled Oct 29; Hank to tick CAPTCHA and submit), Gridinsoft (virus@gridinsoft.com / legal@gridinsoft.com), SOCRadar (vt@socradar.io).

## Reputation recheck, Nov 2, 2026
- **Norton Safe Web: now "Safe".** The Oct 29 dispute worked.
- **Google Safe Browsing:** no unsafe content (last updated Oct 29).
- **VirusTotal:** still 2/92, with Gridinsoft and SOCRadar saying "phishing". A re-scan was requested Nov 2. VirusTotal dates the domain's creation to about Oct 22, so the 30-day mark is around Nov 21–22.
- **Gridinsoft:** its public report page (gridinsoft.com/online-virus-scanner/url/boxytrucks-com) shows "Phishing, 1/100 trust score". The stated reasons are all automated: a 10-day-old domain, no public review history, no external provider warnings. The fix is "Flag for Reevaluation", which needs a free account at portal.gridinsoft.com (Hank to create; Claude can't). Ticket type: domain review for boxytrucks.com. Suggested text:
  > BoxyTrucks.com is an independent, ad-free buyer's guide to 4x4 trucks (Land Cruiser, G-Wagen, Defender and more), published by Hank Pantier in South Carolina. It has no login forms, no payment forms and no downloads; it's a static site hosted on GitHub Pages. Google Safe Browsing and Norton Safe Web both rate it clean, and 90 of 92 VirusTotal vendors report it clean. The phishing verdict appears to come only from the domain's age. Please re-evaluate. Contact: boxytrucks@gmail.com.
- **SOCRadar:** no reply yet to the Oct 29 email to vt@socradar.io. Follow up after Nov 21 if still listed.
