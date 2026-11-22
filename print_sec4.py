with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
sec4 = re.search(r'<section id="que-recibiras"[\s\S]*?</section>', content).group(0)
print(sec4)
