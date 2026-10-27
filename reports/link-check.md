# Outbound link check

Checked 150 unique links found in `data/`.

| Result | Count |
|---|---|
| BROKEN | 1 |
| PARKED | 0 |
| MOVED | 1 |
| BLOCKED | 9 |
| OK | 139 |

## Broken: fix or replace

- https://aol.com/history-toyota-4runner-180000317.html — HTTP 404  
  in: pages/4runner/1st-gen.json, pages/4runner/2nd-gen.json, pages/4runner/4th-gen.json

## Redirected: check they still go to the right page

- https://agileoffroad.com/wp-content/uploads/2025/04/AO-P3G-1-X_Front-or-Rear-Differential-Cover-for-INEOS-Grenadier-by-Agile-_Intallation-Manual_LR.pdf — now redirects to cdn.shopify.com → https://cdn.shopify.com/s/files/1/0965/1526/0718/files/AO-P3G-1-X_Front-or-Rear-Differential-Cover-for-INEOS-Grenadier-by-Agile-_Intallation-Manual_LR.pdf?v=1770317487  
  in: grenadier.json, pages/grenadier/quartermaster.json

## Blocked or slow: usually fine (the site blocks bots), listed for reference

- http://forum.bjsoffroad.com/forum/ — HTTP 403  
  in: pages/jeep/grand-wagoneer.json
- https://4lowmagazine.com/old-school-transfer-case-history — HTTP 429  
  in: scout.json
- https://4runnerlifestyle.com/products/b-o-t-c-k-bolt-on-trackbar-correction-kit-land-cruiser-250-gx550-and-6th-gen4runner — HTTP 502  
  in: pages/4runner/6th-gen.json
- https://4runnerlifestyle.com/products/c4-fabrication-full-skid-plate — HTTP 503  
  in: pages/4runner/5th-gen.json
- https://4runnerlifestyle.com/products/cali-raised-4runner-premium-roof-rack — HTTP 503  
  in: pages/4runner/5th-gen.json
- https://4runnerlifestyle.com/products/sxth-element-catch-can-kit-for-6th-gen-4runner — HTTP 503  
  in: pages/4runner/6th-gen.json
- https://67-72chevytrucks.com/vboard/showthread.php?p=7459005 — HTTP 403  
  in: extra/chevrolet/k5-blazer-1st.json, pages/chevrolet/k5-blazer-1st.json
- https://app.commaoil.com/products/results/91007440/print:true — Tunnel connection failed: 502 Bad Gateway  
  in: land-rover.json
- https://arbusa.com/air-locker — HTTP 403  
  in: pages/jeep/jk.json, pages/jeep/tj-unlimited.json, pages/land-cruiser/100-series.json, pages/land-cruiser/200-series.json, pages/land-cruiser/250-series.json, pages/land-cruiser/300-series.json, pages/
