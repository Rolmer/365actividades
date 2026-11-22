with open('routes.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's see the main return statement of the page component
idx = js.find("bg-confetti")
if idx != -1:
    print(js[max(0, idx-500):idx+3000])
