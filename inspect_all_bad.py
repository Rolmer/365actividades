with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

import re

sec4_match = re.search(r'<section id="que-recibiras"[\s\S]*?</section>', content)
if sec4_match:
    sec4 = sec4_match.group(0)
    # find where  appears
    for m in re.finditer(r'.{0,30}\.{0,30}', sec4):
        print("SEC4 MATCH:", repr(m.group(0)))

script_match = re.search(r'const monthsData = (\[[\s\S]*?\]);', content)
if script_match:
    js_arr = script_match.group(1)
    for m in re.finditer(r'.{0,30}\.{0,30}', js_arr):
        print("JS MATCH:", repr(m.group(0)))
