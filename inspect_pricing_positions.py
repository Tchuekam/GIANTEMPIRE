path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\linear-the-system-for-product-development_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer("Pricing", content)]
print(f"Total 'Pricing' matches: {len(matches)}")
for idx in matches:
    print(f"=== Match at {idx} ===")
    print(content[max(0, idx-150):min(len(content), idx+150)])
    print()
