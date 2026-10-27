# Sweet spot / Beware audit — group: jeep

Scope: 17 pages. Timeline flags live in `data/extra/jeep/<slug>.json`; page text in `data/pages/jeep/<slug>.json` (CJ-7 is the family flagship in `data/jeep.json` → `page`). New sources were added to each page's `sources` list using the existing `{"name","url"}` schema.

Summary: 41 flag decisions were reviewed. Most of the old `buy` flags marked years when something changed, not years that buyers are told to look for, so 22 were removed. 7 new `avoid` flags were added, all for documented problems. No year got a `buy` flag without a source naming it.

Fetch notes: NAXJA, JLWranglerForums and JeepGladiatorForum blocked automated fetches with 403s or challenges, so no claims rest on them. Hagerty pages were read through WebFetch.

---

## cherokee-xj
| Year | Before | After | Why |
|---|---|---|---|
| 1984 | note | **avoid** | Off Road Xtreme: "XJs from 1984 to 1986 didn't have the 4.0 … we would recommend staying away from those years." Text reworded. |
| 1987 | buy | note | The Renix 4.0 is "pretty good too" (ORX), but it isn't the recommended version, and it's harder to diagnose. |
| 1991 | buy | buy | ORX: "We would recommend buying an XJ with the H.O. engine." Text now says why. |
| 1997 | buy | note | No source names the facelift years as the ones to buy. |
| 2000 | note | **avoid** | Wikipedia (AMC straight-6): early 0331 heads crack between cylinders 3 and 4 and let coolant into the oil; the TUPY fix came late in 2001. Text reworded to lead with the head. |

The page was already consistent: the FAQ and the "Know the electronics era" check both say to avoid 1984–86 and check the head on 2000–01. Sources were already on the page: Off Road Xtreme XJ buyer's guide and Wikipedia AMC straight-6.

## comanche-mj
| Year | Before | After | Why |
|---|---|---|---|
| 1987 | buy | note | The Renix era. No source recommends it over the HO. |
| 1989 | buy | note | The AX-15 change is not a reason buyers are told to pick a year. Comanche Club members say not to spend money on the 1987–89.5 Peugeot gearbox. |
| 1991 | buy | buy | The 1991–92 HO: easier to diagnose, with 190 hp. ORX recommends the HO in the XJ, which shares the engine. Text reworded. |

The FAQ "Which years and engines should I buy?" now also cites ORX. Added source: Off Road Xtreme XJ buyer's guide. Caveat: I found no Comanche-specific buyer's guide that names years, so the flag rests on the shared-engine recommendation and the page's existing Renix/HO guidance.

## cj-5
| Year | Before | After | Why |
|---|---|---|---|
| 1965 | buy | buy | Jeep-CJ.com calls the 1966–71 Dauntless V6 "desirable … strong, reliable". The Drive says to make the Dauntless or the 258 your priority. |
| 1972 | buy | buy | Hagerty UK: "the CJ-5 we'd aim for is one of the 3.8- or 4.2-litre straight-six cars from the AMC era from 1972 onwards." |
| 1977 | buy | note | Disc brakes and a boxed frame, but no source recommends the year. The Drive says boxed frames from 1976 on tend to rust. |
| 1980–1983 | note | note | Text now quotes Jeep-CJ.com on the Iron Duke four ("particularly weak … to avoid"). It is left as `note` because the 258 six was still optional. |

Added FAQ "Which years are the best to buy?". Added source: The Drive classic Jeep buyer's guide.

## cj-7 (flagship, data/jeep.json)
| Year | Before | After | Why |
|---|---|---|---|
| 1980 | buy | note | No consensus. |
| 1982 | buy | note | No consensus. |
| 1986 | buy | note | No consensus. |

Opinion splits: owners on Off-Road.com favour 1976–79 trucks for the T-18 and 304, or 1982-on trucks for the wide-track axles, and call a 1986 with the Dana 44 rear "a nice find". Jeep-CJ.com rates the T-18 as the best CJ gearbox. With no agreement, there are no buy flags. Added FAQ "Which years are the best to buy?". Added sources: The Drive and the Off-Road.com CJ7 thread.

## cj-8
No flags before or after. No source names best years. No changes.

## gladiator-jt
| Year | Before | After | Why |
|---|---|---|---|
| 2021 | buy | note | The EcoDiesel year, but the diesel later got two high-pressure fuel-pump recalls (NHTSA 22V-767, 23V-263), and 2021 manuals needed a second clutch fix (24V-572). Text notes the recalls. |
| 2024 | buy | note | No source names the refresh as the year to buy. |

Added FAQ "Which years are the best to buy?", which walks through the recalls by year. Added sources: NHTSA recalls API for the 2020 and 2021 Gladiator.

## grand-cherokee-zj
| Year | Before | After | Why |
|---|---|---|---|
| 1996 | buy | note | **Wrong flag.** SlashGear lists 1995–96 as the ZJ years to *avoid*. NHTSA complaint counts don't support that either: about 1,220–1,560 per year for every year from 1993 to 1998, and 1998 has the most powertrain complaints. CarComplaints shows no standout year. With no consensus either way, both flags were removed. |
| 1998 | buy | note | The 5.9 is a collectible pick (the FAQ already covers it), not a reliability sweet spot. |

Added FAQ "Which years are the best to buy?", which explains the lack of consensus. Added sources: SlashGear ZJ best/worst years, CarComplaints Grand Cherokee by year, NHTSA complaints API for 1994, 1997 and 1998.

## grand-wagoneer
| Year | Before | After | Why |
|---|---|---|---|
| 1986 | buy | note | Hagerty lists the 1986 changes without recommending the year. |
| 1989 | buy | buy | Wikipedia: experts consider 1989–91 "the best of the breed" (electrocoat primer, base/clear paint, better A/C compressor). |
| 1991 | buy | buy | Part of the 1989–91 range. Hagerty: low-mileage Final Editions are "both desirable and expensive to source." Text reworded. |

The FAQ and the "Know the year" check already say 1989–91, so they agree. Sources were already on the page: Wikipedia SJ and Hagerty's buyer's guide. Note: Hagerty's specialist calls the 1989 rear wiper "problematic at best", which the timeline still lists as an improvement. That is factual history, so I left it.

## jk and jk-unlimited (same changes on both)
| Year | Before | After | Why |
|---|---|---|---|
| 2007 | note | **avoid** | SlashGear: several first-year recalls. CarGurus, citing CarComplaints: 2007 and 2008 have more complaints than any other Wrangler year. Driving Line: the 3.8 burns oil, fails intake gaskets and cracks exhaust manifolds. |
| 2012 | buy | buy | The 3.8 vs 3.6 question. Quadratec, Driving Line and SlashGear all prefer the Pentastar. Driving Line's daily-driver pick is 2013 or newer. Text reworded to say so. |
| 2012–13 | note | note | Left-head issue (X56 extension). Kept as the caveat, not as `avoid`: SlashGear calls 2012–13 the standout years and Driving Line recommends 2013-on, so there's no consensus to avoid them. |
| 2015 | buy | note | A trim-launch year. No source recommends it. |

Disagreement noted in the new FAQ: RealTruck lists 2012–14 among its worst years. Added FAQ "Which years are the best to buy?" on both pages. Added sources: SlashGear Wrangler best years, CarGurus Wrangler guide, RealTruck best/worst, Driving Line JK guide and Quadratec checklist, each where missing.

## jl and jl-unlimited
| Year | Before | After | Why |
|---|---|---|---|
| 2018 | note | **avoid** | The early steering and clutch problems. NHTSA: 18V-675 (track-bar bracket welds, 2018–19), 18V-343 (steering-shaft weld), 18V-231 (rear ladder-rail corrosion), and the manual-clutch recalls 20V-124, 21V-028 and 23V-116, which start with 2018. SlashGear: 2018 was "particularly problematic", with more than 1,000 complaints, mostly highway wander. Quadratec: early JLs had vague steering, and Jeep moved from aluminum to cast-iron steering boxes. |
| 2024 | buy | note | No source names the refresh as the sweet spot. The page's own check calls a fixed 2018–23 truck the value buy. |

JL: the existing FAQ "Which years should I avoid?" was rewritten with the NHTSA campaign numbers. JL Unlimited: added FAQ "Which years are the best to buy?". Added sources: SlashGear and the NHTSA recalls API for 2018, 2019 and 2021 (where missing).

## sj-wagoneer
| Year | Before | After | Why |
|---|---|---|---|
| 1976 | buy | note | The boxed frame is a real change, but no source recommends 1976 or later SJs. No consensus. |

## tj
| Year | Before | After | Why |
|---|---|---|---|
| 1997–99 | avoid | avoid | Kept, but the reasoning was re-sourced. The old text credited Quadratec with the exhaust-manifold claim, which I couldn't find in Quadratec's checklist. New sources: SlashGear (seven 1997 recalls, early bugs), Driving Line (cracked manifolds most common on 1997–2000), Off Road Xtreme (leaking early cowl, revised later). |
| 2003 | buy | note | No consensus. |
| 2006 | buy | note | No consensus. SlashGear favours 2005–06, RealTruck lists 2005 and 2006 among its *worst* years, and Quadratec warns about the OPDA on 2005–06. |

TJ frame rust: Quadratec ("This is the TJ issue") and owner complaints on CarComplaints describe it on every TJ from 1997 to 2006. I found no source tying it to particular years and no recall, so there is no year flag. The new FAQ "Which years are the best to buy?" says the frame matters more than the year. Added sources: SlashGear and RealTruck.

## tj-unlimited
| Year | Before | After | Why |
|---|---|---|---|
| 2005 | buy | note | The Rubicon Unlimited is a trim choice, not a year sweet spot, and 2005–06 4.0s carry the OPDA warning (Quadratec). No source names a best LJ year. |

The existing FAQ "Which years and drivetrains should I look for?" is already consistent.

## wagoneer-ws
| Year | Before | After | Why |
|---|---|---|---|
| 2024 | buy | note | No source names a best year. The truck is too new for a consensus. |
| 2025 | buy | note | Same reason. |

2022 stays `note`. The air-suspension TSB and the NHTSA eTorque probe are documented on the page, but no source tells buyers to avoid 2022.

## yj
| Year | Before | After | Why |
|---|---|---|---|
| 1991 | buy | buy | Hagerty: the 4.0 sixes are "often the most desirable". Text reworded. |
| 1994 | buy | buy | SlashGear: 1994–95 are the best YJ years because of the external clutch slave (Wikipedia dates it to 1994, 4WD Mechanix to 1993). Text reworded. |
| 1995 | buy | note | Covered by the 1994 entry's 1994–95 wording. Avoids a third flag. |

The FAQ "Which YJ should I buy?" was updated to add the SlashGear 1994–95 point. Added source: SlashGear Wrangler best years.

---

## Sources fetched for this audit
- Off Road Xtreme — XJ buyer's guide: https://www.offroadxtreme.com/news/buyers-guide-how-to-buy-the-perfect-jeep-cherokee-xj/
- Off Road Xtreme — ZJ buyer's guide: https://www.offroadxtreme.com/news/buyers-guide-zj-grand-cherokee/
- Off Road Xtreme — TJ buyer's guide: https://www.offroadxtreme.com/?p=7529
- Wikipedia — AMC straight-6 (0331 head): https://en.wikipedia.org/wiki/AMC_straight-6_engine
- Wikipedia — Jeep Wagoneer (SJ): https://en.wikipedia.org/wiki/Jeep_Wagoneer_(SJ)
- Hagerty — YJ: https://www.hagerty.com/media/?p=6942
- Hagerty — Grand Wagoneer buyer's guide: https://www.hagerty.com/media/?p=6853
- Hagerty UK — CJ-5 buying guide: https://www.hagerty.co.uk/articles/buying-guide-jeep-cj-5-1955-83/
- Jeep-CJ.com — CJ Buyers Guide: https://jeep-cj.com/community/wiki/cjbuyersguide/
- The Drive — How to buy a classic Jeep: https://www.thedrive.com/vintage/4717/how-to-buy-a-classic-jeep-the-complete-buyers-guide
- Off-Road.com forums — CJ7 advice: https://forums.off-road.com/threads/cj7-advise.44617
- Comanche Club — owner tips thread: https://comancheclub.com/topic/13447-what-is-the-most-important-tip-youd-share-with-mj-owners/
- Driving Line — JK buyer's guide: https://drivingline.com/articles/jeep-wrangler-jk-buyer-s-guide
- Driving Line — TJ buyer's guide: https://www.drivingline.com/articles/jeep-wrangler-tj-buyers-guide/
- Quadratec — Used Wrangler inspection checklist by generation: https://www.quadratec.com/c/howto/used-jeep-wrangler-inspection-checklist-by-generation
- Quadratec — JL damper fix: https://www.quadratec.com/c/blog/jeep-fix-jl-death-wobble-issue
- SlashGear — Best years for Jeep Wrangler: https://www.slashgear.com/1597691/jeep-wrangler-best-years-some-stay-away-from/
- SlashGear — Best and worst years for the ZJ: https://www.slashgear.com/1566045/best-and-worst-years-for-jeep-grand-cherokee-zj/
- CarGurus — Wrangler buying guide: https://partnercontent.cargurus.ca/research/articles/jeep-wrangler-buying-guide-best-years-to-buy
- RealTruck — Best and worst Wrangler years: https://realtruck.com/blog/best-worst-years-jeep-wrangler/
- CarComplaints — Grand Cherokee by year: https://www.carcomplaints.com/Jeep/Grand_Cherokee/
- CarComplaints — 1998 Wrangler suspension (TJ frame rust complaints): https://www.carcomplaints.com/Jeep/Wrangler/1998/suspension/suspension.shtml
- NHTSA recalls API — Wrangler 2018/2019/2020/2021, Gladiator 2020/2021: https://api.nhtsa.gov/recalls/recallsByVehicle?make=JEEP&model=WRANGLER&modelYear=2018 (and the matching URLs for the other years)
- NHTSA complaints API — Grand Cherokee 1993–1998: https://api.nhtsa.gov/complaints/complaintsByVehicle?make=jeep&model=grand%20cherokee&modelYear=1995 (and the other years)

Source-quality note: the SlashGear Wrangler and ZJ pieces contain factual slips. They say "Renix" injection on the 1991 YJ and a JK "V8", and the ZJ piece says the 4.0 was only offered in 1993–94. So I used them only for the year recommendations, and only where at least one other source agreed or where the disagreement is stated on the page.
