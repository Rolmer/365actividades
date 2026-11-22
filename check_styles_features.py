with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

for term in ['accordion', 'details', 'summary', 'shadow-sticker', 'shadow-book', 'shadow-cta', 'animate-in', 'fade-in', 'zoom-in']:
    matches = re.findall(rf'(\.[^{{]*{term}[^{{]*\{{[^}}]+\}})', css)
    print(f"Term '{term}': {len(matches)} rules found")
    if matches:
        print(" ", matches[0][:150])
