# Sweet spot / Beware audit — british-scout

Group pages: land-rover (defender-90-110, defender-l663, discovery-1, discovery-2, lr3, lr4, series), range-rover (classic, l322, l405, l460, p38), scout (scout-80-800, scout-ii, scout-motors).

Every flag was checked against buyer's guides, NHTSA data and owner forums that were fetched during this audit. Where a flag was kept, its `change` text now says why. Where the sources gave no consensus, the flag was removed. A "Which years are the best to buy?" FAQ was added to 11 pages, and L405's "Pre-facelift or facelift?" FAQ was updated instead. All new sources were added to each page's `sources` as `{name, url}`. `build.py` and git were not run.

## Summary of wrong flags fixed

- **LR4 2013 MY was Sweet spot. It is now a note, and the Beware range is widened to 2010–13.** The 2021 US class-action settlement covered 2012–2014 LR4s and Range Rover Sports with the 5.0. A parts-catalogue lookup posted on LandRoverWorld also shows the revised tensioners, levers and guides only from VIN DA696315, partway through 2013.
- **Discovery 2 2003 MY was Sweet spot while 2003–04 was Beware.** The two flags contradicted each other. The Buy flag is removed, and the Beware on 2003–04 4.6 liners and oil pumps stays.
- **L460 2024 was Sweet spot.** It rested only on owners finding the S68 V8 more refined. 2024 has as many NHTSA recalls as 2022–23 (10 vs 10/11), and the page itself says it's too early for reliability data. It is now a note, and the L460 page has no flags.
- **Scout II 1975 and 1980 were Sweet spot. Scout 80/800 1969 was Sweet spot.** None of the sources recommends these years. Moses Ludel prefers the 1979 and says the 1980's only advantage is the Dana 300. Hagerty names no years. The 1975 claim that Dana 44s front and rear are "the axle combination owners want" was unsourced and is removed.
- **Series 1980–82 was Sweet spot.** These were axle upgrades, and no guide recommends those years. It is now a note. The Series IIA (1961) gets a Sweet spot flag that is sourced.
- **L322 2010 was a note. It is now Beware.** The 5.0's timing-chain tensioners were already flagged in the page's own FAQ, The Autopian and ReRev.
- **LR3 2005 MY was a note. It is now Beware,** based on its NHTSA complaint and recall counts and ReRev.
- **Defender 1998–2002 is a new Beware entry** for early 10P Td5s. **Defender 2011 is a new Sweet spot entry** for the PistonHeads Puma pick.
- **L405 2018 was a note. It is now Sweet spot**, alongside the existing 2020 flag.

---

## land-rover / defender-90-110 (flagship, `data/land-rover.json`)

| Entry | Before | After |
|---|---|---|
| 1990 (200Tdi) | buy | buy (reworded with reason) |
| 1994 (300Tdi) | buy | buy (reworded with reason) |
| 1998–2002 (early 10P Td5) | — | **avoid (new)** |
| 2011 (Puma) | — | **buy (new)** |

**Reason.** ECD rates the 300Tdi the "top choice for longevity" and the 200Tdi an honourable mention. Classic Car Hub calls the 300Tdi "widely considered the most reliable engine ever fitted to a Defender".

For the Td5, Wikipedia says early engines had oil-pump-drive failures and "cylinder head shuffle" from weak studs, both fixed within two years. Heritage Parts Centre says 10P heads crack around the injectors, while 15P engines and '52-plate-on trucks are fine.

PistonHeads says that within the Puma range, "a 2011 model of either capacity" is the sweet spot. FAQ added.

**Sources:**
- https://ecdautodesign.com/blog/most-reliable-engine-land-rover-defender
- https://classiccarhub.co.uk/?p=492
- https://www.heritagepartscentre.com/uk/blog/land-rover-defender-buying-guide.html
- https://en.wikipedia.org/wiki/Land_Rover_engines
- https://www.pistonheads.com/news/ph-buying-guides/land-rover-defender--ph-used-buying-guide/41057 (already cited)

## land-rover / defender-l663

No flags before, and none after. There is no buyer consensus on years. Recalls are spread across every model year: NHTSA shows 7–10 per year for 2020–2024. No change.

## land-rover / discovery-1

| Entry | Before | After |
|---|---|---|
| 1994 facelift (300Tdi) | buy | buy (reworded) |

**Reason.** Classic Car Hub says the 300Tdi is "the more sensible choice" and commands a premium over the V8. In the LandyZone thread already cited on the page, a member suggests a late ES (1997–98 model year) or a 1998 Anniversary. FAQ added.

**Sources:**
- https://classiccarhub.co.uk/?p=492
- https://www.landyzone.co.uk/land-rover/buying-guide.378992/ (already cited)

## land-rover / discovery-2

| Entry | Before | After |
|---|---|---|
| 1998–2000 (early Td5) | avoid | avoid (verified) |
| 2003 MY facelift | **buy** | **note** |
| 2003–04 (liners) | avoid | avoid |

**Reason.** Wikipedia confirms the early Td5 failures were fixed within two years.

An Expedition Portal purchasing-guide post says 2003–04 trucks were the worst for cracked oil pumps and more prone to loose liners. In a LandRoverForums thread, the 2003–04 4.6 has the "worst reputation". Owners disagree about the best year: some favour 1999–2002, others the 2004. So there is no Buy flag. FAQ added.

**Sources:**
- https://forum.expeditionportal.com/goto/post?id=1281350
- https://landroverforums.com/forum/discovery-ii-18/so-what-best-year-d2-97544/?nojs=1
- https://landroverforums.com/forum/discovery-ii-18/whats-best-year-buy-52108
- https://en.wikipedia.org/wiki/Land_Rover_engines

## land-rover / lr3

| Entry | Before | After |
|---|---|---|
| 2005 MY | note | **avoid** |
| 2008 MY | buy | buy (reworded) |
| 2009 | buy | buy |

**Reason.** NHTSA complaints by model year fall steadily: 96 (2005), 51, 17, 8, 3 (2009). The 2005 model year also has five recalls. ReRev names 2005 the year to avoid and 2008–09 the most reliable.

The FAQ notes two caveats: the counts aren't adjusted for sales volume, and PistonHeads calls any phase-one D3 high-risk. FAQ added.

**Sources:**
- https://rerev.com/years-to-avoid/vehicles/land-rover-lr3/
- NHTSA complaints API for the 2005, 2008 and 2009 LR3
- NHTSA recalls API for the 2005 LR3
- PistonHeads and Carbuyer guides (already cited)

## land-rover / lr4

| Entry | Before | After |
|---|---|---|
| 2010–2012 MY (LTB00474) | avoid | **2010–13 MY, avoid** |
| 2013 MY | **buy** | **note** |

**Reason.** Bulletin LTB00474 covers 2010–12 trucks in VIN range AA513326–CA652214. A parts-catalogue lookup posted on LandRoverWorld shows the revised tensioner, lever and guides only from VIN DA696315 (mid-2013). The US class action covered 2012–2014 5.0 LR4s and Range Rover Sports (Open Class Actions; KGG law firm).

ReRev prefers 2014–16. It is the only source for that, and US 2014+ trucks lost standard low range, so there is no Buy flag.

The FAQ "Is the 5.0 timing-chain problem a deal-breaker?" said owners believe 2013 engines got the update. It now gives the catalogue VIN and the class-action facts instead. "Which years" FAQ added.

**Sources:**
- https://openclassactions.com/settlements/jaguar-land-rover-timing-chain-class-action-settlement.php
- https://www.kgglaw.com/class-action/land-rover-and-jaguar-timing-chain-defect-class-action/
- https://www.landroverworld.org/goto/post?id=230563
- https://rerev.com/years-to-avoid/vehicles/land-rover-lr4/
- The LandRoverWorld chain-guide thread (already cited)

## land-rover / series

| Entry | Before | After |
|---|---|---|
| 1961 Series IIA | note | **buy** |
| 1971 Series III | buy | buy (reworded) |
| 1980–82 axle upgrades | **buy** | **note** |

**Reason.**
- **Series IIA:** Classic Car Hub calls an 88 or 109 IIA "generally considered the sweet spot of the Series Land Rover range".
- **Series III:** Octane says the SIII is "by far the easiest of all the Series Land Rovers to live with". It recommends a SWB 2.25 petrol for the average buyer.
- **1980–82:** no guide recommends these years.

Two related claims went into the FAQ. Series123 notes the SIII gearbox isn't as strong as the SII's. Heritage Parts Centre rates the 2.25 petrol the preferable engine. FAQ added.

Heritage Parts Centre's claim that five-bearing engines arrived "from 1971" was not used.

**Sources:**
- https://classiccarhub.co.uk/?p=492
- https://www.octane-magazine.com/articles/land-rover-series-3-buying-guide-history-and-review/
- https://www.heritagepartscentre.com/uk/blog/land-rover-series-1-3-buying-guide.html
- https://series123.com/s3buyguide.html (already cited)

## range-rover / classic (flagship, `data/range-rover.json`)

No flags before, and none after. Hagerty UK's guide says to buy "the best you can afford", and the existing FAQ already says condition matters more than year. No change.

## range-rover / l322

| Entry | Before | After |
|---|---|---|
| 2003–05 (BMW M62) | avoid | avoid |
| 2006 (Jaguar AJ-V8 facelift) | note | note |
| 2007 | buy | buy (reworded: 2007–09 Jaguar trucks) |
| 2010 (5.0) | **note** | **avoid** |

**Reason.**
- **2003–05:** ReRev names these the years to avoid. The Autopian describes the M62's timing-guide failures.
- **2007–09:** ReRev calls 2007–09 the "safest bet". The Autopian's editor bought a 2008 and recommends the middle-era Jaguar 4.4.
- **2010–12:** both say the 5.0's tensioners wear, so buy only with proof of updated parts.

The existing FAQ already said this, so it needed no change. 2006 stays a note: The Autopian's "middle era" arguably includes it, but ReRev starts at 2007.

**Sources (both already cited):**
- https://www.theautopian.com/l322-range-rover-timing-chain-flaws-explained/
- https://rerev.com/years-to-avoid/vehicles/range-rover/

## range-rover / l405

| Entry | Before | After |
|---|---|---|
| 2013–14 | avoid | avoid |
| 2018 facelift | note | **buy** |
| 2020 (I6 MHEV) | buy | buy |

**Reason.**
- **2013–14:** PistonHeads says most problems were on pre-2015 cars. ReRev lists 2013–14 to avoid, and also flags 2015 for recall volume and 2017 for windscreen-seal leaks.
- **2018–21:** ReRev rates these the most reliable.
- **2020+:** AutoTrader.ca recommends 2020+ with the straight-six.

The "Pre-facelift or facelift?" FAQ was updated with these points.

**Sources:**
- https://rerev.com/years-to-avoid/vehicles/range-rover/
- PistonHeads and AutoTrader.ca guides (already cited)

## range-rover / l460

| Entry | Before | After |
|---|---|---|
| 2022–23 campaigns | note | note |
| 2024 (S68, P550e) | **buy** | **note** (reworded to list 2024's own recalls) |

**Reason.** NHTSA recall counts are 2022: 10, 2023: 11 and 2024: 10. The 2024 model year has its own campaigns: 23V790000, 23V872000, 24V380000, 24V450000 and 24V678000. The early recalls are real, but later trucks aren't demonstrably better, so 2022–23 doesn't get a Beware flag and 2024 doesn't get a Sweet spot.

Long-term data is too thin for a buy. The only basis for the 2024 flag was owners on FullFatRR finding the S68 more refined. FAQ added.

**Sources:**
- NHTSA recalls API for the 2022 Range Rover (added)
- The 2023 and 2024 recall pages (already cited)

## range-rover / p38

No flags before, and none after. Hagerty UK says "Rather than worry about age, we'd buy on condition and specification". ReRev only notes that 1998 drew the most CarComplaints complaints, and no other source agrees, so no Beware flag. FAQ added.

**Sources:**
- https://hagerty.co.uk/articles/buying-guide-range-rover-1994-2002
- https://rerev.com/years-to-avoid/vehicles/range-rover/

## scout / scout-80-800

| Entry | Before | After |
|---|---|---|
| 1969 (800A) | **buy** | **note** |

**Reason.** No source recommends particular years. Silodrome lists the 800A's Dana 20 and Dana 44 upgrades without recommending it. Cars Counsel rates all 80s and 800s "good with inspection" and says "There are no definitively worst years". FAQ added.

**Sources:**
- https://carscounsel.com/international-harvester-scout-best-worst-years/
- Silodrome (already cited)

## scout / scout-ii (flagship, `data/scout.json`)

| Entry | Before | After |
|---|---|---|
| 1975 (Dana 44 both ends) | **buy** | **note** (unsourced "owners want" claim removed) |
| 1980 (Dana 300) | **buy** | **note** |

**Reason.** Moses Ludel of 4WD Mechanix calls 1979 "a good model year" and says "The only advantage in the 1980 models is use of the Dana 300 transfer case". Hagerty names no preferred years, only the SSII as the most valuable. One expert's forum answer isn't a consensus, so there are no flags. FAQ added.

**Sources:**
- https://forums.4wdmechanix.com/topic/1463-advice-needed-on-buying-a-scout-traveler-ii/
- https://carscounsel.com/international-harvester-scout-best-worst-years/
- Hagerty Scout II article (already cited)

## scout / scout-motors

No flags before, and none after. The truck isn't on sale yet: deliveries are expected in 2028. No change.

---

## Notes and limits

- ReRev, an aggregator built on NHTSA and CarComplaints data plus owner reviews, was used only alongside another source or NHTSA data, never on its own for a Buy flag.
- These sources were unreachable during this audit, so none of their claims are new:
  - hagerty.com: 403
  - the Expedition Portal article page: 403
  - Classics World: 403
  - Famous Four: TLS chain error
- The Hagerty Scout II article was read via WebFetch.
