with open('routes.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find("Manualidades con material reciclado")
if idx != -1:
    print("Found at", idx)
    print(js[max(0, idx-500):idx+1500])
else:
    print("Not found")
