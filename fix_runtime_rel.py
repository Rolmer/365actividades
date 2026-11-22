with open('build_landing.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add relative replacement for all sections right after reading them
anchor = "print(\"Sections 1-5 read successfully.\")"
addition = """
sec1 = sec1.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')
sec2 = sec2.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')
sec3 = sec3.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')
sec4 = sec4.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')
sec5 = sec5.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')
"""
if anchor in code:
    code = code.replace(anchor, anchor + addition)
    # Also replace in the final assembled html just to be 100% sure:
    code = code.replace("with open('index.html', 'w', encoding='utf-8') as f:", 
                        "html = html.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')\nwith open('index.html', 'w', encoding='utf-8') as f:")
    with open('build_landing.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Updated build_landing.py with runtime replacements!")
else:
    print("Anchor not found")
