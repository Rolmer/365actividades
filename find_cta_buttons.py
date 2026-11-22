import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find buttons with QUIERO
buttons = re.findall(r'(<button[^>]*>[\s\S]*?QUIERO[\s\S]*?</button>)', content)
print(f"Found {len(buttons)} CTA buttons:")
for i, b in enumerate(buttons, 1):
    print(f"\n--- Button {i} ---")
    print(b)
