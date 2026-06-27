import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\giantech_files\22961-b5e844867516afbb.js.download"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the navbar logo area
idx = content.find('"aria-label":"Linear"')
if idx == -1:
    idx = content.find("'aria-label':'Linear'")
    
if idx != -1:
    start = max(0, idx - 500)
    end = min(len(content), idx + 500)
    print("=== NAVBAR LOGO CONTEXT ===")
    print(content[start:end])
else:
    # Try other patterns
    idx = content.find('aria-label')
    print("aria-label at:", idx)
    if idx != -1:
        print(content[max(0,idx-200):idx+200])
