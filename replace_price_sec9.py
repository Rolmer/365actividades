import re

with open('build_landing.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace any price inside sec9 definition
sec9_start = code.find("sec9 = '''")
sec9_end = code.find("'''", sec9_start + 10)
sec9_part = code[sec9_start:sec9_end]

# remove $7 USD from sec9
sec9_part_fixed = re.sub(r'de tan solo \$7 USD\s*', '', sec9_part)
code = code[:sec9_start] + sec9_part_fixed + code[sec9_end:]

with open('build_landing.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_landing.py successfully!")
