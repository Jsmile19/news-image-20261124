# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Jsmile19/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Jsmile19/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A 1024 × 1024 news poster for **Tuesday, 24 November 2026**, drawn from the supplied news brief. The lead stories are a US jury finding Huawei guilty and four tankers mined in the Strait of Hormuz, followed by Ukraine's strikes on Russian ships, Israel killing Hamas's internal security chief in Gaza, a Houthi drone hitting the PIF tower in Riyadh, a Turkish Air Force helicopter crash, and 25 hostages held in a Cartagena supermarket, with smaller news extras below.

## Run it

```sh
python3 draw_poster.py
node main.ts
```

To regenerate the poster, run `python3 draw_poster.py`, which draws the image with ImageMagick and writes `entry.png`. To produce the entry output, run `node main.ts` (Node 22+): it relies only on the Node standard library, performs no network access, and copies the `entry.png` sitting next to it into the output folder (`/output` by default, or the folder named by the `MAKEFUN_OUTPUT_DIR` environment variable), creating that folder first when needed. Two runs of the program produce byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=q3bse5cn&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
