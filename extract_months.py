import re
import json

with open('routes.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's find qt array
start = js.find('qt=[')
if start != -1:
    end = js.find('];', start)
    array_code = js[start+3:end+1]
    print("Found qt array snippet:")
    print(array_code[:500])
    with open('months_data.js', 'w', encoding='utf-8') as mf:
        mf.write("var months = " + array_code + ";\nconsole.log(JSON.stringify(months, null, 2));")
    print("Saved months_data.js")
else:
    print("qt=[ not found")
