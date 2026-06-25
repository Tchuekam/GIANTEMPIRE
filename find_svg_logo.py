import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\layout-36ce25f36e86ec77.js.download"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Find SVG viewBox patterns
for m in re.finditer(r'viewBox[=:]["\']?\s*([\d\s.]+)["\']?', content):
    start = max(0, m.start()-200)
    end = min(len(content), m.end()+300)
    ctx = content[start:end]
    print("--- Match at pos", m.start(), "---")
    print(ctx[:500])
    print()
