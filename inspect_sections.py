import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for Pricing in HTML elements (e.g. h1, h2, h3, section, div with id or class)
for word in ["Pricing", "Features", "Method", "Changelog"]:
    matches = [m.start() for m in re.finditer(word, content)]
    print(f"Word '{word}' found {len(matches)} times.")
    for idx in matches:
        # Find enclosing elements or id attributes
        start = max(0, idx - 150)
        end = min(len(content), idx + 150)
        snippet = content[start:end]
        if 'id=' in snippet or 'class=' in snippet or '<h' in snippet:
            print(f"  Snippet for {word} at {idx}:")
            print(snippet)
            print("-" * 50)
