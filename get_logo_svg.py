import re

html_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\linear-the-system-for-product-development.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's find any SVG with aria-label="Linear Logo"
matches = list(re.finditer(r'<svg[^>]*aria-label="Linear Logo"[^>]*>.*?</svg>', content, re.DOTALL))
print(f"Found {len(matches)} SVGs with aria-label='Linear Logo'")
for i, m in enumerate(matches):
    print(f"Match #{i} (index {m.start()} to {m.end()}):")
    print(m.group(0))
    print("-" * 60)
