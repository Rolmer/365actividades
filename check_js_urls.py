with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'"url":\s*"([^"]+)"', html)
print("Month image URLs found in JS:", len(matches))
for m in matches[:3]:
    print(" ", m)
