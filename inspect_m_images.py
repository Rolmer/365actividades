import json

with open('months_utf8.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, m in enumerate(data):
    print(f"Month {i+1} image:", m['image'])
