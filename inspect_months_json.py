import json

with open('months.json', 'r', encoding='utf-8') as f:
    months = json.load(f)

print(f"Total months: {len(months)}")
for i, m in enumerate(months, 1):
    print(f"Mes {i}: {m['name']} | Dot: {m['dot']} | Range: {m['range']}")
    print(f"  Tagline: {m['tagline']}")
    print(f"  Examples: {m['examples']}")
    print(f"  Image: {m['image']}")
