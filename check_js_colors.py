import re

js_path = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find hex colors
hex_colors = set(re.findall(r'#[0-9a-fA-F]{3,8}\b', content))
print("Hex colors found in main.js:", hex_colors)
