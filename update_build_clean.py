with open('build_landing.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace months_utf8.json with clean_months.json
code = code.replace("open('months_utf8.json'", "open('clean_months.json'")

with open('build_landing.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_landing.py updated with clean_months.json!")
