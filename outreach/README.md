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
