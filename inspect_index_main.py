import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's find <main> and print the first 2000 characters inside it
idx_main = content.find("<main")
if idx_main != -1:
    print("=== MAIN TAG START ===")
    print(content[idx_main:idx_main + 2500])
else:
    print("No <main> tag found")
