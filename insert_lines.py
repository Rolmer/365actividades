with open('build_landing.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if "sec5 = f.read()" in line:
        new_lines.append("\nsec1 = sec1.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')\n")
        new_lines.append("sec2 = sec2.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')\n")
        new_lines.append("sec3 = sec3.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')\n")
        new_lines.append("sec4 = sec4.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')\n")
        new_lines.append("sec5 = sec5.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')\n")

with open('build_landing.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Inserted runtime relative replacement lines successfully!")
