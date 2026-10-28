# The Boxy Dispatch (newsletter)

- **Provider:** Kit (kit.com), account boxytrucks@gmail.com. Free plan, with a 14-day Pro trial from Oct 28, 2026.
- **Form:** "BoxyTrucks site signup", id 10110095. Action `https://app.kit.com/forms/10110095/subscriptions`, email field `email_address`. Set in `NEWSLETTER` in build.py.
- **Flow:** a reader subscribes on any page, lands on /newsletter/thanks/, gets the confirmation email ("One click and you're in: confirm BoxyTrucks"), and is sent to /newsletter/welcome/ after confirming.
- **Hidden field:** `fields[signup_page]` carries the page path. Kit only saves it once a custom field named `signup_page` exists. Create it from a subscriber's profile once there is one.
- **Sequences and automations are paid in Kit.** There's no welcome sequence on the free plan; the confirmation email and the /newsletter/welcome/ page do that job.
- **Issue 01:** broadcast draft "Dispatch No. 01: the biggest tire that fits, and a Land Cruiser recall" (Kit campaign 26662307). It covers the tire tool, the 2024–27 Land Cruiser fuel-tube recall (26V673) and the Featured Build call. It's NOT sent; Hank sends it.
- **Format each month:** one new guide, one featured rig, one recall worth knowing.
