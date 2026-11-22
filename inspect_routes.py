with open('routes.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# find image urls
imgs = re.findall(r'[\'"`](/[^\'"`]+\.(?:jpg|png|webp|svg))[\'"`]', js)
print("Images found in routes.js:", set(imgs))

# find months or content
print("\nLength of routes.js:", len(js))
