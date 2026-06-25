import re
import os

css_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# find exact .hero rules
hero_rules = re.findall(r'\.hero\s*\{[^}]*\}', content)
print("Exact .hero rules:")
for rule in hero_rules:
    print(rule)
