import os

PROJECT_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

def main():
    path = os.path.join(PROJECT_DIR, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "passion" in content.lower():
        print("[OK] Found 'passion' in index.html")
        # Print surrounding content
        pos = content.lower().find("passion")
        print(content[max(0, pos-100):min(len(content), pos+200)])
    else:
        print("'passion' not found in index.html")

if __name__ == "__main__":
    main()
