with open('routes.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# Let's find sections or components
print("Contains 'seccion' or 'Section'?")
# Let's search for text around the sections
matches = re.findall(r'(\{[^}]*titulo[^}]*\})', js)
print("Matches with titulo:", len(matches))
for m in matches[:5]:
    print(" ", m[:100])
