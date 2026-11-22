import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

links = re.findall(r'<a[^>]+href=["\'](https://pay\.hotmart\.com/[^"\']+)["\'][^>]*>([\s\S]*?)</a>', html)
print(f"Found {len(links)} Hotmart checkout links:")
for i, (href, text) in enumerate(links, 1):
    clean_text = ' '.join(re.sub(r'<[^>]+>', '', text).split())
    print(f"Link {i}: {href} -> Text: '{clean_text}'")
