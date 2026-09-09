import os
import re

COLS = 6
IMG_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")
README_PATH = "README.md"

# Collect all image files in repo root, sorted alphabetically
images = sorted(
    f for f in os.listdir(".")
    if f.lower().endswith(IMG_EXTENSIONS)
)

if not images:
    print("No images found.")
    exit()

# Pad list to a multiple of COLS
while len(images) % COLS != 0:
    images.append(None)

# Build table rows
rows = []
for i in range(0, len(images), COLS):
    chunk = images[i:i+COLS]
    cells = []
    for img in chunk:
        if img:
            cells.append(f'<td><a href="{img}"><img src="{img}" width="200"/></a></td>')
        else:
            cells.append("<td></td>")
    rows.append("<tr>\n" + "\n".join(cells) + "\n</tr>")

table = "<table>\n" + "\n".join(rows) + "\n</table>"

readme = f"""# Nord Background Collection

This repository contains various wallpapers. Thumbnails below link to the full images.
Credits for the original images go to the respective authors, as listed in the image metadata and the github repositories below.
Original backgrounds from [NoChrisTitusTechrd](https://github.com/ChrisTitusTech/nord-background).
Origanal thumbnail grid for README from [meefs](https://github.com/meefs/nord-background).
Github Actions workflow to update README from [shadowskytech](https://github.com/shadowskytech/nord-background).

{table}
"""

with open(README_PATH, "w") as f:
    f.write(readme)

real_count = len([x for x in images if x])
print(f"README updated with {real_count} images.")
