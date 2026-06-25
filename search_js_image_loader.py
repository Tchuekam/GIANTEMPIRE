import re
import os

js_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for hero__img or image-related keywords in main.js
print("Searching for selectors:")
selectors = ["hero__img", "hero__", "canvas", "WebGL", "texture", "Shader", "uniform"]
for sel in selectors:
    matches = [m.start() for m in re.finditer(sel, content, re.IGNORECASE)]
    print(f"Keyword '{sel}': found {len(matches)} occurrences")
    if matches:
        print("First occurrences:")
        for idx in matches[:5]:
            start = max(0, idx - 100)
            end = min(len(content), idx + 150)
            snippet = content[start:end].replace('\n', ' ')
            print(f"  [{idx}]: ... {snippet} ...")
