import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check all src and href
local_files = re.findall(r'(?:src|href)=["\'](\.[^"\']+)["\']', html)
# also metodos-pago-hotmart.svg
local_files += re.findall(r'src=["\']([a-zA-Z0-9_\-]+\.svg)["\']', html)

missing = []
for p in set(local_files):
    norm_p = p.replace('/', os.sep)
    if not os.path.exists(norm_p):
        missing.append(norm_p)
    else:
        print(f"EXISTS: {norm_p} ({os.path.getsize(norm_p)} bytes)")

if missing:
    print("\nMISSING FILES:", missing)
else:
    print("\nALL LOCAL REFERENCED FILES EXIST ON DISK!")
