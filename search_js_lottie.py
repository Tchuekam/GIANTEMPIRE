import os

js_path = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

pos = content.find("Signature.json")
if pos != -1:
    print("Found Signature.json:")
    print(content[max(0, pos-200):min(len(content), pos+300)])
else:
    print("Signature.json not found")
    
pos2 = content.find("Won_logo2.json")
if pos2 != -1:
    print("\nFound Won_logo2.json:")
    print(content[max(0, pos2-200):min(len(content), pos2+300)])
