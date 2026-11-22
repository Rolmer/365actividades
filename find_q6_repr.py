with open('build_landing.py', 'r', encoding='utf-8') as f:
    code = f.read()

idx = code.find("¿Cómo funcionan el pago y el acceso?")
print(repr(code[idx+200:idx+600]))
