# rig-api

The Show Us Your Rig form handler. A single Vercel function (`api/rig.js`) that takes the form from
boxytrucks.com/submit/ and emails it, photos attached, to boxytrucks@gmail.com through Resend.

Vercel project: root directory `rig-api`, no build command. Environment variables (set in Vercel only):
- `RESEND_API_KEY` (required)
- `RIG_TO` (optional, default boxytrucks@gmail.com)
- `RIG_FROM` (optional; default is Resend's test sender, which only delivers to the Resend account's own
  email. After boxytrucks.com is verified in Resend, set it to `BoxyTrucks Rigs <rigs@boxytrucks.com>`.)

Vercel caps a request at 4.5 MB, so the page shrinks photos to 1600 px and sends at most about 4 MB.

Live Nov 5, 2026: Vercel team "Boxy Trucks" (boxytrucks@gmail.com), project `boxytrucks-rigs`,
https://boxytrucks-rigs.vercel.app/api/rig. Tested end to end: 3 photos arrived in boxytrucks@gmail.com.
`vercel.json` skips Vercel builds on pushes that don't touch this folder.
