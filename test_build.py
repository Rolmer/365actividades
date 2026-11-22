import json

with open('months_utf8.json', 'r', encoding='utf-8') as f:
    months_data = json.load(f)

print(f"Loaded {len(months_data)} months.")

# Read sections 1 to 5
with open('section_1.html', 'r', encoding='utf-8') as f:
    sec1 = f.read()

with open('section_2.html', 'r', encoding='utf-8') as f:
    sec2 = f.read()

with open('section_3.html', 'r', encoding='utf-8') as f:
    sec3 = f.read()

with open('section_4.html', 'r', encoding='utf-8') as f:
    sec4 = f.read()

with open('section_5.html', 'r', encoding='utf-8') as f:
    sec5 = f.read()

print("Sections 1-5 read successfully.")
