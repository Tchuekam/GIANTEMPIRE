import re, os, sys

sys.stdout.reconfigure(encoding='utf-8')

# The navbar in Linear's website has a specific structure
# Let's look for the header/nav component that renders the logo
# The key is to find where the brand icon SVG is defined
# Linear's logo is a rounded square with horizontal lines (the "Linear" mark)

files_dir = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files"

# Search for the specific SVG path data that makes up the Linear logo
# The Linear logo is like a rounded square with 5 horizontal lines
for fname in sorted(os.listdir(files_dir)):
    if not fname.endswith('.js.download'):
        continue
    fpath = os.path.join(files_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Search for "Linear" as text being rendered (not in URLs or variable names)
    # In JSX, text "Linear" would appear as children text
    # Like: children:"Linear" or ,"Linear") or >Linear<
    patterns = [
        r'"Linear"',  # String literal "Linear"
        r"'Linear'",  # String literal 'Linear'
    ]
    for pat in patterns:
        for m in re.finditer(re.escape(pat) if not pat.startswith('r') else pat, content):
            start = max(0, m.start()-200)
            end = min(len(content), m.end()+200)
            ctx = content[start:end]
            # Filter out things that are clearly not display text
            if 'linear.app' in ctx.lower() or 'github' in ctx.lower():
                continue
            print(f"=== {fname} at pos {m.start()} ===")
            print(ctx)
            print()
