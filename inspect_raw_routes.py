with open('routes.js', 'r', encoding='utf-8', errors='replace') as f:
    js = f.read()

import re

# find qt array
start = js.find('qt=[')
end = js.find('];', start)
raw_qt = js[start:end+2]

print("Snippet of qt from routes.js:")
print(raw_qt[:1000])
