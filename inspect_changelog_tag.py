path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('kkJAGU">Changelog</h2>')
if idx != -1:
    start = max(0, idx - 400)
    end = min(len(content), idx + 200)
    print("=== Changelog section context ===")
    print(content[start:end])
else:
    print("Text not found")
