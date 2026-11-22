with open('build_landing.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace sec7 in the main assembly or set sec7 = ""
code = code.replace('{sec7}', '')
code = code.replace('<!-- 7. Testimonios -->\n    {sec7}\n', '')

with open('build_landing.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_landing.py successfully!")
