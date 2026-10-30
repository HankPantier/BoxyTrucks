# Daily X post (@boxytrucks)

Hank approved this on Oct 30, 2026: post on X daily, like Instagram. Use the same message as that day's Instagram post, reworded slightly for X (≤280 characters), and link to the matching page on the site.

## Writing the X version (`x_text` in queue.json)
- Same hook and facts as the Instagram caption, cut to fit. A link counts as 23 characters whatever its length, and so does a bare domain.
- Link to the most specific page on boxytrucks.com (the compare page, the best-years page, /submit/), not just the homepage. Check the page exists in `site/` first.
- Keep the photo credit. Use 0–1 hashtags, never the Instagram hashtag block.
- When drafting a new week of Instagram posts, write `x_text` for each and set `x_status: "queued"`.

## Posting
1. Open https://x.com/compose/post in Claude in Chrome. Read `[data-testid=SideNav_AccountSwitcher_Button]` and confirm it shows **@boxytrucks**. If it shows @webhank or anything else, stop, post nothing and tell Hank. Never switch accounts or sign in.
2. Use `find` to locate the "Add photos or video" file input inside the compose dialog, then `file_upload` the item's image (`/home/claude/boxytrucks/social/posts/...`).
3. Click into the text box at its on-screen position (above the image), then type `x_text`. Don't use ctrl+a. If the text goes wrong, reload the compose page and start again.
4. Check that the dialog's `[data-testid=tweetTextarea_0]` holds the full text and the image is attached, then click Post.
5. Open https://x.com/boxytrucks and read the new post's `/status/<id>` URL.
6. In queue.json set `x_status: "posted"`, `x_posted` (date) and `x_url`. Add a row to the Posts table in `social/X.md`, then commit, push and tell Hank in one line.
7. If Chrome or X isn't available, or X shows a rate limit or lock, leave the item queued and tell Hank.
