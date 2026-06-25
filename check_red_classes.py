import re
import os

css_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# search for col-red or stroke-red rules
matches = re.finditer(r'([^{]*?(?:col-red|stroke-red)[^{]*?)\s*\{([^}]*)\}', content, re.IGNORECASE)
print("col-red and stroke-red rules in CSS:")
for m in matches:
    print(f"Selector: {m.group(1).strip()}")
    print(f"Content: {m.group(2).strip()}")
    print("-" * 40)
