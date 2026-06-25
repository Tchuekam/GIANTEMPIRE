import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for tags containing Product, Pricing, Features, etc.
# We will match things like <a...Product</a>, <button...Product</button>, etc.
pattern = r'<[a-zA-Z0-9]+[^>]*>(?:Product|Pricing|Features|Customers|Contact|Changelog)</[a-zA-Z0-9]+>'
matches = list(re.finditer(pattern, content))
print(f"Found {len(matches)} exact text matches for menu items:")
for m in matches:
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 100)
    print(f"Match at pos {m.start()}:")
    print(content[start:end])
    print("-" * 60)
