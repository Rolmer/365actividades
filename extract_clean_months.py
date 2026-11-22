import json
import re

with open('routes.js', 'r', encoding='utf-8') as f:
    js = f.read()

start = js.find('qt=[')
end = js.find('];', start)
raw_qt = js[start+3:end+1]

# In raw_qt, replace backticks with double quotes, and extract image url
# Let's write a small node script or python regex to cleanly parse it
# In python:
def extract_clean_months(raw):
    # Split into objects
    items = re.findall(r'\{name:`([^`]+)`,tagline:`([^`]+)`,description:`([^`]+)`,range:`([^`]+)`,examples:\[([^\]]+)\],image:\{[^}]+url:`([^`]+)`[^}]+\},dot:`([^`]+)`\}', raw)
    print(f"Matched {len(items)} months via regex!")
    months = []
    for name, tagline, description, range_text, examples_str, url, dot in items:
        # parse examples
        examples = re.findall(r'`([^`]+)`', examples_str)
        # make url relative
        rel_url = '.' + url if url.startswith('/') else url
        months.append({
            "name": name,
            "tagline": tagline,
            "description": description,
            "range": range_text,
            "examples": examples,
            "image": rel_url,
            "dot": dot
        })
    return months

clean_months = extract_clean_months(raw_qt)
with open('clean_months.json', 'w', encoding='utf-8') as f:
    json.dump(clean_months, f, ensure_ascii=False, indent=2)

print("Saved clean_months.json. Checking entries:")
for i, m in enumerate(clean_months, 1):
    print(f"Mes {i}: {m['name']} | {m['tagline']}")
    for ex in m['examples']:
        print(f"   - {ex}")
