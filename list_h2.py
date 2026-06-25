import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all h2 headings in index.html
h2_matches = re.findall(r'<h2[^>]*>(.*?)</h2>', content)
print("=== H2 HEADINGS ===")
for h2 in h2_matches:
    print("-", re.sub('<[^<]+?>', '', h2).strip())
print("==================")
