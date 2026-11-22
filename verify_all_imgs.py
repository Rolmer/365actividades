import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total img tags: {len(srcs)}")
all_ok = True
for s in sorted(set(srcs)):
    # normalize path
    norm = s.replace('/', os.sep)
    if norm.startswith('.' + os.sep):
        norm = norm[2:]
    if os.path.exists(norm):
        print(f"  OK: {s} ({os.path.getsize(norm)} bytes)")
    else:
        print(f"  FAILED: {s} (not found on disk!)")
        all_ok = False

if all_ok:
    print("\nALL <img> TAGS HAVE VALID LOCAL ASSETS!")
else:
    print("\nSOME <img> TAGS ARE MISSING!")
