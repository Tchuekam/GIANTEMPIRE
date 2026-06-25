path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("<footer")
if idx != -1:
    start = max(0, idx - 500)
    end = min(len(content), idx + 2000)
    print("=== Footer context ===")
    print(content[start:end])
else:
    # Try searching for "Footer_" class
    idx2 = content.find("Footer_root")
    if idx2 != -1:
        print("=== Footer_root context ===")
        print(content[max(0, idx2-300):min(len(content), idx2+1500)])
    else:
        print("Footer not found")
