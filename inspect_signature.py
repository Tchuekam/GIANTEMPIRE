import os

js_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

pos = content.find("Signature.json")
if pos != -1:
    print("--- SIGNATURE WIDER CONTEXT ---")
    start = max(0, pos - 250)
    end = min(len(content), pos + 300)
    print(content[start:end])

pos2 = content.find("Won_logo2.json")
if pos2 != -1:
    print("\n--- LOGO WIDER CONTEXT ---")
    start = max(0, pos2 - 250)
    end = min(len(content), pos2 + 300)
    print(content[start:end])
