with open('build_landing.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all '/__l5e/' with './__l5e/' and '/assets/' with './assets/'
content = content.replace('/__l5e/', './__l5e/')
content = content.replace('/assets/', './assets/')

with open('build_landing.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated build_landing.py with relative paths.")
