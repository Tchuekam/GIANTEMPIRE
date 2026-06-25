import os

js_path = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

if "hero-alpha" in content:
    print("[OK] Found hero-alpha in main.js")
else:
    print("hero-alpha not found in main.js")

# Find webp references
import re
webp_refs = re.findall(r'https?://[^\s"\']+\.webp', content)
print("WebP links in main.js:", webp_refs)
