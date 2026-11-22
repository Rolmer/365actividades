with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

import re

# Find section 4
sec4_match = re.search(r'<section id="que-recibiras"[\s\S]*?</section>', content)
if sec4_match:
    sec4 = sec4_match.group(0)
    # find all  or non-ascii
    bad_chars = [c for c in sec4 if ord(c) > 127 and c not in 'áéíóúÁÉÍÓÚñÑüÜ¡¿·—']
    print(f"Section 4 bad characters count: {len(bad_chars)}")
    # Find lines with  or unusual sequences
    for line in sec4.split('\n'):
        if '' in line:
            print("BAD LINE:", line[:150])

# Also check monthsData script
script_match = re.search(r'const monthsData = (\[[\s\S]*?\]);', content)
if script_match:
    js_arr = script_match.group(1)
    if '' in js_arr:
        print("\nFound  in monthsData script!")
