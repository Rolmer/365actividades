with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
leading_slash_paths = re.findall(r'(?:src|href)=["\'](/[^"\']+)["\']', html)
print(f"Found {len(leading_slash_paths)} paths with leading slash:")
for p in set(leading_slash_paths):
    print(" ", p)
