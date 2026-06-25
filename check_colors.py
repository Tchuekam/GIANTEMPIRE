import re

css_path = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find hex colors
hex_colors = set(re.findall(r'#[0-9a-fA-F]{3,8}\b', content))
print("Hex colors found in CSS:", hex_colors)

# Find rgb colors
rgb_colors = set(re.findall(r'rgb\([^)]+\)', content))
print("RGB colors found in CSS:", list(rgb_colors)[:20])
