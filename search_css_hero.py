import re
import os

css_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all occurrences of hero styles
hero_rules = re.findall(r'\.[a-zA-Z0-9_-]*hero[a-zA-Z0-9_-]*\s*\{[^}]*\}', content)
print("CSS Rules for Hero:")
for rule in hero_rules:
    print(rule)
