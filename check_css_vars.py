import re
import os

css_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for color variables
matches = re.finditer(r'--[a-zA-Z0-9_-]+\s*:[^;]+;', content)
print("Color variables in CSS:")
for m in matches:
    print(m.group(0))
