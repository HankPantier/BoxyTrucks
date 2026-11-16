# Hank's own videos

Each folder is one video of Hank's trucks. `posted.json` needs `id`, `title`, `video` (the mp4), `yt_url`, `link` (the site page it belongs on, e.g. `repairs/g-class/g500/oil-filter-housing-gasket-leak/` or `models/g-class/g500/`), `posted` and optionally `thumb_at` (seconds) and `description`.

On build, `hank_videos()` in build.py embeds every video with a `yt_url` and `link` in the "From Hank's garage" box on that page: a click-to-load YouTube player (youtube-nocookie, nothing loads until tapped), a 540x960 poster made from the mp4 at `thumb_at` (site/img/hank-video/<id>.jpg; delete it to regenerate), and VideoObject schema. Repair pages and model pages are supported (not problems pages). Check the poster frame for number plates.
