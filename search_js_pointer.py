import re
import os

js_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

# search for pointerEvents in JS
matches = re.finditer(r'pointerEvents|pointer-events', content, re.IGNORECASE)
print("Matches in JS:")
for m in matches:
    start = max(0, m.start() - 100)
    end = min(len(content), m.start() + 150)
    print(content[start:end].replace('\n', ' '))
