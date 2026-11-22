with open('routes.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# find main component
idx = js.find("<main")
if idx == -1:
    idx = js.find("main,")
    if idx == -1:
        idx = js.find("children:[")

# Let's find all function declarations or component names
comps = re.findall(r'function ([A-Za-z0-9_]+)\s*\([^)]*\)\s*\{[^}]*return\s*\(0,Q\.jsx', js)
print("Components with return:", comps)

# Let's find where sections are combined
idx2 = js.rfind("return")
print("Last 2000 chars:")
print(js[-2000:])
