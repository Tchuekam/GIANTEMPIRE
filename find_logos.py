from html.parser import HTMLParser
import re

html_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\linear-the-system-for-product-development.html"

class SVGParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_svg = False
        self.svg_content = []
        self.svgs = []
        self.current_attrs = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'svg':
            self.in_svg = True
            self.svg_content = [self.get_starttag_text()]
            self.current_attrs = dict(attrs)
        elif self.in_svg:
            self.svg_content.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if tag == 'svg':
            self.in_svg = False
            self.svg_content.append("</svg>")
            self.svgs.append(("".join(self.svg_content), self.current_attrs))
        elif self.in_svg:
            self.svg_content.append(f"</{tag}>")

    def handle_data(self, data):
        if self.in_svg:
            self.svg_content.append(data)

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

parser = SVGParser()
parser.feed(content)

print(f"Total inline SVGs: {len(parser.svgs)}")
print("\nSVGs containing 'logo' or 'brand' in attrs or classes:")
matching_svgs = []
for i, (svg, attrs) in enumerate(parser.svgs):
    attrs_str = str(attrs).lower()
    if 'logo' in attrs_str or 'brand' in attrs_str or 'icon' in attrs_str:
        print(f"SVG #{i}: attrs={attrs}")
        print(svg[:300] + "...")
        print("-" * 50)
        matching_svgs.append(i)

# If no specific logo attribute, let's print the first 3 SVGs on the page (usually header/logo is first)
if not matching_svgs:
    print("\nPrinting first 3 SVGs on the page:")
    for i, (svg, attrs) in enumerate(parser.svgs[:3]):
        print(f"SVG #{i}: attrs={attrs}")
        print(svg[:400] + "...")
        print("-" * 50)
