"""
VARI vegetation map from a drone photo (pure Python + Pillow).

Computes the Visible Atmospherically Resistant Index (VARI) for every
pixel and renders two maps:
  - grayscale map  (dark = soil, bright = vegetation)
  - red-yellow-green vigor map (red = soil, green = vegetation)

VARI = (Green - Red) / (Green + Red - Blue)   (Gitelson et al. 2002)

Usage:
  1. Put your drone photo next to this script and name it photo.jpg
  2. pip install -r requirements.txt
  3. python vari_map.py

Note: the working resolution below is Full HD. Computing at the full
48 MP sensor resolution works but is slow in pure Python (no numpy).
"""

import os
from PIL import Image

# --- settings ---
INPUT = "photo.jpg"
WORK_WIDTH, WORK_HEIGHT = 1920, 1080  # working resolution
GRAY_OUT = os.path.join("output", "vari_map_gray.png")
COLOR_OUT = os.path.join("output", "vari_map_color.png")


def vari(r, g, b):
    """Visible Atmospherically Resistant Index for one pixel."""
    d = g + r - b
    if d == 0:
        return 0  # avoid division by zero
    return (g - r) / d


img = Image.open(INPUT)
small = img.resize((WORK_WIDTH, WORK_HEIGHT))
w, h = small.size

gray_map = Image.new("L", (w, h))      # black-and-white canvas
color_map = Image.new("RGB", (w, h))   # color canvas

values = []
for y in range(h):
    for x in range(w):
        r, g, b = small.getpixel((x, y))
        v = vari(r, g, b)
        values.append(v)

        t = (v + 1) / 2  # VARI (-1..1) -> fraction (0..1)
        gray_map.putpixel((x, y), int(t * 255))
        color_map.putpixel((x, y), (int(255 * (1 - t)), int(255 * t), 0))

    if y % 500 == 0:
        print(f"row {y} of {h}")

print(f"pixels: {len(values)}")
print(f"VARI min {min(values):.3f} / max {max(values):.3f}")

os.makedirs("output", exist_ok=True)
gray_map.save(GRAY_OUT)
color_map.save(COLOR_OUT)
print("saved!")
