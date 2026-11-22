import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's check all sections
sections = re.findall(r'<section[^>]*id="([^"]+)"', html)
print("Sections by ID in index.html:")
for s in sections:
    print(" -", s)
