import re
import os

css_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

matches = re.finditer(r'([^{]*?)\s*\{\s*[^}]*?pointer-events:[^}]*?\}', content, re.IGNORECASE)
print("CSS Rules with pointer-events:")
for m in matches:
    print(m.group(0))
