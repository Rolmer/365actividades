import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("="*50)
print("AUDIT REPORT")
print("="*50)

# 1. Sections count
sections = re.findall(r'<section[\s\S]*?</section>', html)
print(f"Total <section> elements: {len(sections)} (Expected: 9)")
assert len(sections) == 9, f"Found {len(sections)} sections instead of 9"

# 2. Check each section order and content
sec_titles = []
for i, s in enumerate(sections, 1):
    h1 = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', s)
    h2 = re.findall(r'<h2[^>]*>([\s\S]*?)</h2>', s)
    title = (h1 + h2)[0] if (h1 + h2) else "No h1/h2"
    clean_title = re.sub(r'<[^>]+>', '', title).strip().replace('\n', ' ')
    clean_title = ' '.join(clean_title.split())
    sec_titles.append((i, clean_title[:60]))
    print(f"Section {i}: {clean_title[:60]}")

# 3. Check buy buttons count and locations
# A buy button is a commercial CTA to buy the product.
# We also have month tabs buttons and FAQ toggle buttons.
# Let's count all buttons and verify specifically CTA buttons.
all_buttons = re.findall(r'<button[^>]*>([\s\S]*?)</button>', html)
print(f"\nTotal <button> tags: {len(all_buttons)}")

cta_buttons = []
for i, s in enumerate(sections, 1):
    b_in_s = re.findall(r'<button[^>]*>([\s\S]*?)</button>', s)
    for b in b_in_s:
        clean_b = re.sub(r'<[^>]+>', '', b).strip().replace('\n', ' ')
        clean_b = ' '.join(clean_b.split())
        if 'QUIERO' in clean_b.upper():
            cta_buttons.append((i, clean_b))

print(f"Total CTA / Buy buttons: {len(cta_buttons)} (Expected: exactly 2)")
for sec_num, text in cta_buttons:
    print(f"  In Section {sec_num}: '{text}'")

assert len(cta_buttons) == 2, f"Expected 2 CTA buttons, found {len(cta_buttons)}"
assert cta_buttons[0][0] == 6, f"First CTA button should be in Section 6, found in Section {cta_buttons[0][0]}"
assert cta_buttons[1][0] == 8, f"Second CTA button should be in Section 8, found in Section {cta_buttons[1][0]}"

# Check no href, onClick, etc. on buy buttons
for btn in re.findall(r'<button[^>]*>[^<]*QUIERO[\s\S]*?</button>', html):
    assert 'href' not in btn, f"Found href in CTA button: {btn}"
    assert 'onclick' not in btn.lower(), f"Found onClick in CTA button: {btn}"
    assert '<a ' not in btn, f"Found link in CTA button: {btn}"
print("CTA buttons have no href, no onClick, no redirection. PASSED.")

# 4. Check prices in each section
# Price anchors: $27 USD tachado, $7 USD destacado only in Section 6 and 8.
print("\nPrice check across sections:")
for i, s in enumerate(sections, 1):
    prices = re.findall(r'\$\d+(?:\s*USD)?', s)
    print(f"  Section {i} prices found: {prices}")
    if i in [1, 2, 3, 4, 5, 7, 9]:
        assert len(prices) == 0, f"Section {i} should NOT contain any prices, but found: {prices}"
    elif i in [6, 8]:
        assert '$27 USD' in s, f"Section {i} missing $27 USD"
        assert '$7 USD' in s, f"Section {i} missing $7 USD"
        assert 'line-through' in s, f"Section {i} missing strikethrough for previous price"

# Check footer for CTA or prices
footer_match = re.search(r'<footer[\s\S]*?</footer>', html)
if footer_match:
    f_content = footer_match.group(0)
    assert 'QUIERO' not in f_content.upper(), "Footer has CTA"
    assert '<button' not in f_content, "Footer has button"
    print("Footer has no CTA, no button. PASSED.")

# 5. Check Section 7 testimonials
sec7_content = sections[6]
testimonio_reemplazar = sec7_content.count("Reemplazar por testimonio real")
print(f"\nSection 7 'Reemplazar por testimonio real' count: {testimonio_reemplazar} (Expected: 4)")
assert testimonio_reemplazar == 4, f"Expected 4 placeholder texts, found {testimonio_reemplazar}"
assert '<button' not in sec7_content, "Section 7 must not have buttons"

# 6. Check Section 9 FAQ
sec9_content = sections[8]
faq_items = re.findall(r'faq-toggle', sec9_content)
print(f"\nSection 9 FAQ questions count: {len(faq_items)} (Expected: 6)")
assert len(faq_items) == 6, f"Expected 6 FAQ questions, found {len(faq_items)}"
assert 'QUIERO' not in sec9_content.upper(), "Section 9 must not have buy button"

# 7. Check payment methods image
print("\nPayment methods image check:")
for i in [5, 7]: # Sections 6 and 8 (0-indexed 5 and 7)
    sec_html = sections[i]
    assert '<img' in sec_html and 'metodos-pago' in sec_html, f"Section {i+1} must contain horizontal payment methods image"
print("Payment methods image correctly in Section 6 and Section 8. PASSED.")

# 8. Check technical words
for banned in ['Sección 1', 'Sección 2', 'Sección 3', 'Sección 4', 'Sección 5', 'Sección 6', 'Sección 7', 'Sección 8', 'Sección 9']:
    assert banned not in html, f"Found technical label: {banned}"
print("No technical 'Sección X' labels visible in the HTML. PASSED.")

print("\n" + "="*50)
print("ALL AUDIT CHECKS PASSED PERFECTLY!")
print("="*50)
