import re

with open('page.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("HTML size:", len(html))

# Let's extract links, scripts, imgs, styles
links = re.findall(r'<link[^>]+href=["\'](.*?)["\']', html)
scripts = re.findall(r'<script[^>]+src=["\'](.*?)["\']', html)
imgs = re.findall(r'<img[^>]+src=["\'](.*?)["\']', html)

print("LINKS:")
for l in sorted(set(links)):
    print(" ", l)

print("SCRIPTS:")
for s in sorted(set(scripts)):
    print(" ", s)

print("IMAGES:")
for i in sorted(set(imgs)):
    print(" ", i)
