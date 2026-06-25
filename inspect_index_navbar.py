import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for "Product" in index.html (case insensitive)
matches = [m.start() for m in re.finditer(r'product', content, re.IGNORECASE)]
print(f"Total 'product' matches found: {len(matches)}")

# Let's search for navigation-related HTML elements like <nav
nav_matches = [m.start() for m in re.finditer(r'<nav', content)]
print(f"Total <nav matches: {len(nav_matches)}")
for idx in nav_matches:
    print(f"=== <nav found at position {idx} ===")
    print(content[idx:idx+1500])
    print()

# Let's look for "Pricing" or "Features" references
for word in ["Pricing", "Features", "Method", "Customer", "Changelog"]:
    word_matches = [m.start() for m in re.finditer(word, content)]
    print(f"Word '{word}' matches count: {len(word_matches)}")
    for idx in word_matches[:2]:
        print(f"  Context around {word} at {idx}:")
        print(content[max(0, idx-100):min(len(content), idx+100)])
