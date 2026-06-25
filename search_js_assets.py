import re
import os

PROJECT_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

def main():
    path = os.path.join(PROJECT_DIR, "js", "main.js")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Search for all strings starting with http or containing website-files or vercel
    urls = re.findall(r'https?://[^\s"\']+', content)
    print("URLs found in main.js:")
    for url in urls:
        print(url)
        
    # Search for any image extensions (.webp, .jpg, .png, .gif)
    imgs = re.findall(r'[^\s"\']+\.(?:webp|jpg|png|gif|jpeg|svg)', content)
    print("\nImage references found in main.js:")
    for img in imgs:
        print(img)

if __name__ == "__main__":
    main()
