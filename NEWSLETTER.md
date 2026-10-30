# The Boxy Dispatch (newsletter)

- **Provider:** Kit (kit.com), account boxytrucks@gmail.com. Free plan, with a 14-day Pro trial from Oct 28, 2026.
- **Form:** "BoxyTrucks site signup", id 10110095. Action `https://app.kit.com/forms/10110095/subscriptions`, email field `email_address`. Set in `NEWSLETTER` in build.py.
- **Flow:** a reader subscribes on any page, lands on /newsletter/thanks/, gets the confirmation email ("One click and you're in: confirm BoxyTrucks"), and is sent to /newsletter/welcome/ after confirming.
- **Hidden field:** `fields[signup_page]` carries the page path. Kit only saves it once a custom field named `signup_page` exists. Create it from a subscriber's profile once there is one.
- **Sequences and automations are paid in Kit.** There's no welcome sequence on the free plan; the confirmation email and the /newsletter/welcome/ page do that job.
- **Issue 01:** Kit broadcast draft 26702147, "Dispatch No. 01: which year to buy, what breaks, what fits" (Oct 30, Text only template, body in one HTML block; source newsletter/issue-01.md). NOT sent: Hank sends it. The older broadcast 26662307 ("Dispatch No. 01: the biggest tire that fits, and a Land Cruiser recall") went out Oct 28 to 1 recipient.
- **Subject line format (Hank, Oct 30):** "Dispatch No. NN: <three short hooks>", e.g. "Dispatch No. 01: which year to buy, what breaks, what fits". Keep it numbered every issue.
- **Format each month:** one new guide, one featured rig, one recall worth knowing.
