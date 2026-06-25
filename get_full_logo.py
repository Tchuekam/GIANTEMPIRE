import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Get the full SVG element inside the logo link
idx = content.find('Header_logoLink__Sgfy4')
if idx != -1:
    # Find the <a> tag start
    a_start = content.rfind('<a ', max(0, idx-200), idx)
    # Find the closing </a>
    a_end = content.find('</a>', idx)
    if a_end != -1:
        a_end += 4
    
    logo_html = content[a_start:a_end]
    print("=== FULL LOGO LINK HTML ===")
    print(logo_html)
    print()
    print(f"Length: {len(logo_html)} chars")
    print(f"Start pos: {a_start}")
    print(f"End pos: {a_end}")
