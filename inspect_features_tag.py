path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\giantech_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("A new species of product tool")
if idx != -1:
    # Print 800 characters before this text to find the parent tag
    start = max(0, idx - 800)
    end = min(len(content), idx + 200)
    print("=== Features section context ===")
    print(content[start:end])
else:
    print("Text not found")
