with open('page.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

sections = re.findall(r'<section[\s\S]*?</section>', html)
print(f"Total sections: {len(sections)}")

for i, sec in enumerate(sections, 1):
    print(f"\n{'='*20} SECTION {i} {'='*20}")
    # Get headings
    h1s = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', sec)
    h2s = re.findall(r'<h2[^>]*>([\s\S]*?)</h2>', sec)
    h3s = re.findall(r'<h3[^>]*>([\s\S]*?)</h3>', sec)
    print("H1:", [re.sub('<[^<]+?>', '', x).strip() for x in h1s])
    print("H2:", [re.sub('<[^<]+?>', '', x).strip() for x in h2s])
    print("H3:", [re.sub('<[^<]+?>', '', x).strip() for x in h3s])
    # print first 300 chars
    print("Snippet:", sec[:300].replace('\n', ' '))
