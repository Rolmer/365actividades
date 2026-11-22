import os
import urllib.request
import re

with open('routes.js', 'r', encoding='utf-8') as f:
    routes_content = f.read()

with open('page.html', 'r', encoding='utf-8') as f:
    page_content = f.read()

all_content = routes_content + page_content

# Match clean image paths ending in file extensions
img_urls = set(re.findall(r'(/__l5e/assets-v1/[a-f0-9\-]+/[a-zA-Z0-9_\-]+\.(?:jpg|png|svg|webp)|/assets/[a-zA-Z0-9_\-]+\.(?:jpg|png|svg|webp|ico|css|js))', all_content))

print(f"Found {len(img_urls)} clean image URLs:")
base_url = "https://bonos-y-beneficios.lovable.app"

for rel_path in sorted(img_urls):
    local_path = "." + rel_path.replace("/", os.sep)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    if not os.path.exists(local_path):
        full_url = base_url + rel_path
        print(f"Downloading {rel_path} ...")
        try:
            req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp, open(local_path, 'wb') as out_f:
                out_f.write(resp.read())
            print(f"  OK ({os.path.getsize(local_path)} bytes)")
        except Exception as e:
            print(f"  Error: {e}")
    else:
        print(f"  Already exists: {rel_path}")

print("All downloads finished.")
