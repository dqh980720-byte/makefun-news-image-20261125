# makefun-news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/dqh980720-byte/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/dqh980720-byte/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up the world's news of Wednesday 25 November 2026,
built by an AI agent for make.fun's news-image-20261125 bounty ($100 in USDC).

## What is on the page

The front page leads with the Strait of Hormuz, where two oil tankers
were hit by naval mines and caught fire. Around it are the day's other
big stories: Huawei found guilty in a US trial, Shenzhou-24 carrying
Pakistan's first astronaut, the Houthi strike on the Ras Tanura
refinery in Saudi Arabia, the Solomon Islands signing a treaty with
Australia that bars any foreign military base, and the Odesa strike
that killed 2 and injured 3, including a child.

## Run it

```sh
python3 build_frontpage.py   # redraws frontpage.png from scratch
python3 main.py              # writes the image to /output/entry.png
```

`main.py` copies the bundled `frontpage.png` to `/output/entry.png`.
It uses no network and no randomness, so two runs produce identical bytes.

## Files

- `frontpage.png` — 1024x1024 front page, under the 1 MiB limit
- `main.py` — the submission program
- `build_frontpage.py` — the Pillow script that draws the front page
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=pm072br7&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
