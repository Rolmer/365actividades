with open('page.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Find position after the 5th section
sections_matches = list(re.finditer(r'<section[\s\S]*?</section>', html))
if len(sections_matches) >= 5:
    last_sec = sections_matches[4]
    after = html[last_sec.end():]
    print("Content after section 5:")
    print(after[:2000])
