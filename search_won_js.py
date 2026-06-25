import re
import os

js_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

matches = re.finditer(r'[Ww][Oo][Nn]', content)
matches_list = list(matches)
print(f"Found {len(matches_list)} occurrences of 'won' (case-insensitive) in main.js")
for m in matches_list[:10]:
    start = max(0, m.start() - 50)
    end = min(len(content), m.start() + 100)
    snippet = content[start:end].replace('\n', ' ')
    print(f"  [{m.start()}]: ... {snippet} ...")
