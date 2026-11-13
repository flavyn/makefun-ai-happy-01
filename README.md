# ai-happy-01 — He gave her a pebble

An entry in make.fun's [Make the AI judge happy](https://make.fun/bounty/ai-happy-01) bounty.

The image the judge sees is `entry.png`: two emperor penguins on snow at golden
hour, one offering the other a pebble — a real courtship gesture, and the whole
proposal in one frame. The line under it is the entry's idea:

> He gave her a pebble. She said yes.

`main.py` writes that image to `/output/entry.png` (Python 3.13, standard
library only, the same bytes on both runs). The picture was drawn by code in
the agent session that built this entry: flat shapes, warm light, no photo or
artwork copied from anywhere, so the licence below covers it cleanly.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT, see [LICENSE](LICENSE).
