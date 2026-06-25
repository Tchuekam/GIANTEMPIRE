import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the SVG element inside the logo link and replace it with an img tag
# The SVG starts with: <svg height="22" viewBox="0 0 400 100" fill="currentColor" size="22" color="currentColor" aria-label="GianTecH Empire">
# And ends with: </svg>

# Find the start of the SVG inside the logo link
logo_link_start = content.find('Header_logoLink__Sgfy4')
if logo_link_start == -1:
    print("ERROR: Could not find logo link class")
    sys.exit(1)

# Find the SVG after this position
svg_start = content.find('<svg', logo_link_start)
svg_end = content.find('</svg>', svg_start)
if svg_end == -1:
    print("ERROR: Could not find end of SVG")
    sys.exit(1)
svg_end += 6  # include </svg>

old_svg = content[svg_start:svg_end]
print(f"Found SVG logo ({len(old_svg)} chars)")
print(f"First 100 chars: {old_svg[:100]}")

# Replace with img tag
new_img = '<img src="./giantech_files/logo.png" alt="GianTecH Empire" style="height:28px;width:auto;object-fit:contain">'

content = content[:svg_start] + new_img + content[svg_end:]

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("\nDone! Replaced SVG with img tag in the HTML body.")
