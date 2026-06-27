import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\giantech_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for "Header_list" or "Header_logoLink"
match = re.search(r'Header_list__[a-zA-Z0-9_-]+', content)
if match:
    print("Found header list class:", match.group(0))
    idx = content.find(match.group(0))
    print(content[idx-200:idx+1500])
else:
    print("Header list class not found")

# Let's search for "Features" or "Pricing" or "Method" or "Customer" or "Changelog"
for word in ["Features", "Pricing", "Method", "Customer", "Changelog", "Contact", "Product"]:
    match_word = re.findall(rf'[^<]*{word}[^>]*', content)
    print(f"Word '{word}' matches count: {len(match_word)}")
    if match_word:
        print(f"Sample matches for {word}:", match_word[:3])
