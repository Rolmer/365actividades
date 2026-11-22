import json

with open('months.json', 'r', encoding='utf-16') as f:
    months = json.load(f)

# Save as clean utf-8
with open('months_utf8.json', 'w', encoding='utf-8') as f:
    json.dump(months, f, ensure_ascii=False, indent=2)

print(f"Total months: {len(months)}")
for i, m in enumerate(months, 1):
    print(f"Mes {i}: {m['name']} | Dot: {m['dot']} | Range: {m['range']}")
