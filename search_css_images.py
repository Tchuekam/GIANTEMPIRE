import re
import os

PROJECT_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

def main():
    path = os.path.join(PROJECT_DIR, "css", "styles.css")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    urls = re.findall(r'url\(([^)]+)\)', content)
    print("URLs in CSS:")
    for url in urls:
        print(url)

if __name__ == "__main__":
    main()
