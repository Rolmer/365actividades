with open('build_landing.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace month image loading
old_load = "months_data = json.load(f)"
new_load = """months_data = json.load(f)
for m in months_data:
    if m.get('image') and m['image'].startswith('/'):
        m['image'] = '.' + m['image']"""

code = code.replace(old_load, new_load)

with open('build_landing.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_landing.py for month images!")
