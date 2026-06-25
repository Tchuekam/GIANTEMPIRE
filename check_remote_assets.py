import os
import re

PROJECT_DIR = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

for filename in os.listdir(PROJECT_DIR):
    if filename.endswith(".html"):
        path = os.path.join(PROJECT_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        urls = re.findall(r'src="([^"]*(?:website-files|webflow)\.com[^"]*)"', content)
        srcset_urls = re.findall(r'srcset="([^"]*(?:website-files|webflow)\.com[^"]*)"', content)
        
        if urls or srcset_urls:
            print(f"\n--- Remote assets in {filename} ---")
            for url in urls:
                print(f"  src: {url}")
            for url in srcset_urls:
                print(f"  srcset: {url[:100]}...")
