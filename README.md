# Sum up 18 November's world news in one image

A one-image editorial poster summing up the world news of **Wednesday,
18 November 2026**, built for the make.fun bounty `news-image-20261118`.

**Status: local draft only — not registered, not submitted anywhere.**

## What the image says

The day was dominated by diplomacy on the surface and war underneath it:

- **Shenzhen / APEC** — Xi Jinping and Vladimir Putin met ahead of a
  first-ever U.S.–China–Russia trilateral with Donald Trump (set for
  Thursday); Xi said China and Russia should "lead the push to a multipolar
  world".
- **The Gulf escalates** — the U.S. struck Iran's Qeshm Island in the Strait
  of Hormuz; Iran fired drones at U.S. bases in Kuwait, Bahrain intercepted
  attacks, and a tanker was hit in the strait.
- **Ukraine** — Kyiv hit the Crimean Bridge again as 141 drones crossed
  Ukraine overnight.
- **Quad in Manila** — U.S., Japan, India and Australia leaders met for the
  first time in over two years.
- **America** — the U.S. lost its measles-free status after 26 years
  (5,400+ cases this year); a tech-outage wave reached the NSA.
- Ticker: Russian military plane crash in Siberia (19 killed) · Cyclone
  Akvan closing in on India's east coast · Nvidia's record $115.8B quarter.

The judging AI has no news feed, so the poster is deliberately text-forward:
every story is stated in words on the image itself, newspaper-front-page
style, rather than implied by artwork alone.

## Layout of this entry

- `main.py` — the graded entrypoint. Standard library only. Copies
  `assets/entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (falling back to
  `/output`, then `./output`), byte for byte, so repeated runs are identical.
- `assets/entry.png` — the poster: PNG, 1024×1024, ~137 KB (limit: 1 MiB).
- `generate_image.py` — how the poster was rendered locally (Pillow + system
  fonts). Documentation/provenance only; the grader never runs it.
- `LICENSE` — MIT.

## Run it the way the grader does

```sh
MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
# writes /tmp/out/entry.png — identical bytes on every run
```

## Sources (checked 19 Nov 2026, Asia/Shanghai)

Cross-checked across at least two independent outlets per story:
Open Chronicle global brief (18 Nov 2026), Korea Herald world page,
Outlook India live updates (18 Nov 2026), Daily Mirror (Sri Lanka) world
news, The Japan Times latest news, Dawn international (18 Nov 2026),
E-news Tainan international top-10 (18 Nov 2026). Conflicting or
single-source items (e.g. the Nvidia CEO-return story) were left out.
