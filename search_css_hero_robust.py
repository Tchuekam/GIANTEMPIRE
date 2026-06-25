import re
import os

css_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Match rules where selector contains "hero"
matches = re.finditer(r'([^{]*?hero[^{]*?)\s*\{([^}]*)\}', content, re.IGNORECASE)
print("CSS rules matching 'hero' selector:")
for m in matches:
    print(f"Selector: {m.group(1).strip()}")
    print(f"Content: {m.group(2).strip()}")
    print("-" * 40)
