import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\giantech_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the first nav tag block
nav_match = re.search(r'<nav aria-label="Main".*?</nav>', content, re.DOTALL)
if nav_match:
    nav_html = nav_match.group(0)
    print("=== NAV BLOCK ===")
    print(nav_html)
    print("=================")
else:
    # If it's a huge block and not easily matched with .*? because of nested tags, let's find the content after '<nav aria-label="Main"'
    start_idx = content.find('<nav aria-label="Main"')
    if start_idx != -1:
        print("=== NAV BLOCK (first 2000 chars) ===")
        print(content[start_idx:start_idx+2500])
    else:
        print("Navbar not found with '<nav aria-label=\"Main\"'")
