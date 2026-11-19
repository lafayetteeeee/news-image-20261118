#!/usr/bin/env python3
"""Render the 1024x1024 news poster for 18 November 2026.

Local build tool only (uses Pillow). The graded entrypoint main.py does NOT
depend on this script or on Pillow: it copies assets/entry.png byte-for-byte
using only the Python standard library.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = Path(__file__).resolve().parent / "assets" / "entry.png"

SERIF_BLACK = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Black.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
SANS_BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"
SERIF_IT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"

PAPER = (250, 246, 237)
INK = (20, 20, 20)
GRAY = (74, 74, 68)
NAVY = (16, 38, 63)
RED = (178, 32, 24)
WHITE = (255, 255, 255)
GOLD_TXT = (240, 199, 94)
PALE = (170, 195, 225)


def f(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, font, fill, max_w, leading=1.2):
    x, y = xy
    for line in wrap(draw, text, font, max_w):
        draw.text((x, y), line, font=font, fill=fill)
        y += int(font.size * leading)
    return y


def centered(draw, cx, y, text, font, fill):
    draw.text((cx - draw.textlength(text, font=font) / 2, y),
              text, font=font, fill=fill)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 46

# ---------- masthead (0-70) ----------
d.rectangle([0, 0, W, 62], fill=INK)
d.text((M, 15), "THE WORLD IN ONE IMAGE", font=f(SANS_BLACK, 27), fill=WHITE)
date_txt = "WEDNESDAY  •  18 NOVEMBER 2026"
d.text((W - M - d.textlength(date_txt, font=f(SANS_BOLD, 22)), 19),
       date_txt, font=f(SANS_BOLD, 22), fill=GOLD_TXT)
d.rectangle([0, 62, W, 70], fill=RED)

# ---------- headline (84-232) + subhead ----------
d.text((M, 84), "SUMMITS IN CHINA,", font=f(SERIF_BLACK, 66), fill=INK)
d.text((M, 156), "STRIKES IN THE GULF", font=f(SERIF_BLACK, 66), fill=RED)
y = text_block(
    d, (M, 232),
    "Xi Jinping and Vladimir Putin meet in Shenzhen ahead of a first-ever "
    "U.S.–China–Russia trilateral with Donald Trump — while Washington and "
    "Tehran trade blows over Hormuz and Ukraine hits the Crimean Bridge.",
    f(SANS, 24), GRAY, W - 2 * M, leading=1.25)
d.line([M, y + 6, W - M, y + 6], fill=INK, width=2)

# ---------- central panel: Shenzhen / APEC ----------
top = y + 18
panel_h = 176
d.rounded_rectangle([M, top, W - M, top + panel_h], radius=14, fill=NAVY)
d.text((M + 28, top + 14), "SHENZHEN  •  APEC SUMMIT", font=f(SANS_BLACK, 24),
       fill=GOLD_TXT)
sub = "THE THREE LEADERS, ONE TABLE"
d.text((W - M - 28 - d.textlength(sub, font=f(SANS_BOLD, 16)), top + 19),
       sub, font=f(SANS_BOLD, 16), fill=PALE)

leaders = [
    ("XI", "XI JINPING", "CHINA", (196, 44, 34)),
    ("PUTIN", "VLADIMIR PUTIN", "RUSSIA", (84, 96, 120)),
    ("TRUMP", "DONALD TRUMP", "USA · JOINS THU", (43, 84, 160)),
]
cx = [268, 512, 756]
cy = top + 84
for x1, x2 in [(310, 470), (554, 714)]:
    d.line([x1, cy, x2, cy], fill=GOLD_TXT, width=3)
for (initials, name, country, col), x in zip(leaders, cx):
    d.ellipse([x - 42, cy - 42, x + 42, cy + 42], fill=col,
              outline=WHITE, width=3)
    centered(d, x, cy - 12, initials, f(SANS_BLACK, 19), WHITE)
    centered(d, x, cy + 50, name, f(SANS_BOLD, 18), WHITE)
    centered(d, x, cy + 72, country, f(SANS_BOLD, 13), PALE)

quote_y = top + panel_h + 8
centered(d, W // 2, quote_y,
         "Xi: China and Russia should “lead the push to a multipolar world”",
         f(SERIF_IT, 21), INK)

# ---------- 2x2 news grid ----------
grid_top = quote_y + 34
box_w = (W - 2 * M - 16) // 2
box_h = 148
boxes = [
    ("THE GULF ESCALATES", RED,
     "U.S. strikes Iran’s Qeshm Island in the Strait of Hormuz. Iran fires "
     "drones at U.S. bases in Kuwait; Bahrain intercepts attacks and a "
     "tanker is hit in the strait."),
    ("UKRAINE WAR", (90, 60, 130),
     "Kyiv hits the Crimean Bridge again as 141 drones cross Ukraine "
     "overnight. Washington and Europe weigh how to tempt Russia into talks."),
    ("QUAD IN MANILA", (13, 110, 100),
     "U.S., Japan, India and Australia leaders meet for the first time in "
     "over two years, opposing any change to the status quo by force."),
    ("AMERICA", (150, 96, 10),
     "The U.S. loses its measles-free status after 26 years, with 5,400+ "
     "cases this year — as a tech-outage wave reaches the NSA."),
]
for i, (kicker, col, body) in enumerate(boxes):
    bx = M + (i % 2) * (box_w + 16)
    by = grid_top + (i // 2) * (box_h + 12)
    d.rounded_rectangle([bx, by, bx + box_w, by + box_h], radius=10,
                        fill=WHITE, outline=(216, 208, 192), width=2)
    d.rectangle([bx, by, bx + box_w, by + 8], fill=col)
    d.text((bx + 18, by + 16), kicker, font=f(SANS_BLACK, 21), fill=col)
    text_block(d, (bx + 18, by + 48), body, f(SANS, 20), INK,
               box_w - 36, leading=1.2)

# ---------- bottom ticker ----------
tick_top = grid_top + 2 * box_h + 12 + 14
d.rectangle([0, tick_top, W, tick_top + 88], fill=INK)
ticker = [
    "Russian military plane crashes in Siberia — all 19 aboard killed",
    "Cyclone Akvan, a severe storm, closes in on India’s east coast",
    "Nvidia posts a record $115.8B quarter as AI spending surges",
]
ty = tick_top + 9
for line in ticker:
    d.polygon([(M, ty + 10), (M + 7, ty + 3), (M + 14, ty + 10), (M + 7, ty + 17)],
              fill=GOLD_TXT)
    d.text((M + 26, ty), line, font=f(SANS_BOLD, 20), fill=WHITE)
    ty += 26

# ---------- footer ----------
foot = "18 NOV 2026 — DIPLOMACY AT THE TOP TABLE, WAR UNDERNEATH IT"
centered(d, W // 2, tick_top + 98, foot, f(SANS_BLACK, 20), INK)
assert tick_top + 98 + 26 <= H, tick_top

img.save(OUT, format="PNG", optimize=True)
print(OUT, OUT.stat().st_size, "bytes; footer ends at", tick_top + 98 + 26)
