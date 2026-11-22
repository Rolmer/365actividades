import json
import re

with open('clean_months.json', 'r', encoding='utf-8') as f:
    clean_months = json.load(f)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace monthsData in script
clean_json_str = json.dumps(clean_months, ensure_ascii=False)
pattern = r'const monthsData = \[[\s\S]*?\];'
assert re.search(pattern, content), "Could not find monthsData in index.html"

new_content = re.sub(pattern, f'const monthsData = {clean_json_str};', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html with clean monthsData!")
