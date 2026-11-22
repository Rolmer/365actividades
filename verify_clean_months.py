import json

with open('clean_months.json', 'r', encoding='utf-8') as f:
    months = json.load(f)

print(f"Total months: {len(months)}")
for i, m in enumerate(months, 1):
    print(f"\nMes {i}: {m['name']}")
    print(f"  Lema: {m['tagline']}")
    print(f"  Desc: {m['description']}")
    print(f"  Rango: {m['range']}")
    print(f"  Ejemplos: {', '.join(m['examples'])}")
    print(f"  Img: {m['image']}")
