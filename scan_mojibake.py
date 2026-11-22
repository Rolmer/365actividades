with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Look for typical mojibake patterns: Ã, Â, ├, ┬, , etc.
mojibake_chars = ['Ã', 'Â', '├', '┬', '', '\ufffd']
found = {}
for ch in mojibake_chars:
    cnt = text.count(ch)
    if cnt > 0:
        found[ch] = cnt

print("Mojibake characters found across index.html:", found)
