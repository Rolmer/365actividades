with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.bg-confetti[^{]*\{[^}]+\})', css)
print("bg-confetti:", matches)
