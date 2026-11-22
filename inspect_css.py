with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("CSS length:", len(css))
# check colors/vars
import re
root_match = re.search(r':root\s*\{([^}]+)\}', css)
if root_match:
    print(":root variables:")
    print(root_match.group(1)[:500])

# Check some classes
print("\nSome class matches:")
for cls in ['bg-confetti', 'text-primary', 'shadow-sticker', 'shadow-book', 'shadow-cta', 'font-hand', 'font-display', 'bg-sunshine', 'bg-leaf', 'bg-teal', 'bg-grape', 'bg-tangerine', 'bg-blush', 'bg-sky']:
    print(f"{cls}: {cls in css}")
