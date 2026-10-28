# Daily Instagram follow run (@boxytrucks)

Hank approved this on Oct 28, 2026: follow relevant accounts every day, about 25–30 a day.

1. In Claude in Chrome, open https://www.instagram.com/accounts/edit/ and confirm the profile shown is **boxytrucks**. If it's @webhank or anything else, stop and tell Hank.
2. Take the next `todo` entries from `social/follow-targets.json`, in order, up to 28.
3. For each one, navigate to `https://www.instagram.com/<handle>/` and run `social/follow.js` with javascript_tool. Use browser_batch with no more than 5 profiles per batch; bigger batches time out.
   - Results: FOLLOWED or ALREADY → `status: "followed"`, with the date. MISSING → `status: "missing"`. NOBUTTON or UNSURE → take a screenshot and check by eye.
   - **BLOCKED** ("Try Again Later" or "We restrict certain activity"): stop for the day. Leave the rest as todo and tell Hank. Don't retry until the next day.
4. Once the list has no todo entries left, find new accounts through hashtags. Open `https://www.instagram.com/explore/search/keyword/?q=%23<tag>` for one or two of #landcruiser, #fj40, #80series, #gwagon, #w463, #defender, #landroverdefender, #rangeroverclassic, #broncolife, #earlybronco, #internationalscout, #jeepwrangler, #ineosgrenadier, #nissanpatrol, #4runner. Open the top posts and note each author.
   - Add an author (tier `hashtag`) only if their feed is mostly boxy 4x4s off-road or in build, they post regularly, and they aren't selling followers, adult content or spam.
   - Never follow accounts whose posts glorify wrecks or crashes.
   - Then follow them using the same steps.
5. If Chrome doesn't respond twice in a row, stop, save progress and tell Hank.
6. Commit follow-targets.json (message "Instagram follows <date>: N followed"), push, and message Hank one line with the count.
