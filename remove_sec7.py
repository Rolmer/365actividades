import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'\s*<!-- 7\. Testimonios -->[\s\S]*?</section>'
match = re.search(pattern, content)
if not match:
    pattern = r'\s*<section id="testimonios"[\s\S]*?</section>'
    match = re.search(pattern, content)

if match:
    print("Found match to remove:")
    print(match.group(0)[:200])
    print("...")
    print(match.group(0)[-100:])
    new_content = content[:match.start()] + content[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Removed section 7 from index.html successfully!")
else:
    print("Could not find section 7 in index.html!")
