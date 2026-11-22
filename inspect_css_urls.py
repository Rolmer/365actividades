import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

urls = re.findall(r'url\((.*?)\)', css)
print("CSS URLs:", set(urls))
