import re

with open('page.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[\s\S]*?</section>', html)
for i, s in enumerate(sections, 1):
    with open(f'section_{i}.html', 'w', encoding='utf-8') as sf:
        sf.write(s)
print(f"Dumped {len(sections)} sections.")
