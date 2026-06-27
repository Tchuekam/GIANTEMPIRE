import sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\giantech_files\22961-b5e844867516afbb.js.download"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# The key part: replace the navbar logo SVG component call with an img element
# Original: (0,t.jsx)(R,{size:22,color:"currentColor","aria-label":"Linear"})
# Replace with: (0,t.jsx)("img",{src:"./giantech_files/logo.png",alt:"GianTecH Empire",style:{height:"22px",width:"auto",objectFit:"contain"}})

old = '(0,t.jsx)(R,{size:22,color:"currentColor","aria-label":"Linear"})'
new = '(0,t.jsx)("img",{src:"./giantech_files/logo.png",alt:"GianTecH Empire",style:{height:"22px",width:"auto",objectFit:"contain"}})'

count = content.count(old)
print(f"Found {count} occurrence(s) of the navbar logo component")

if count > 0:
    content = content.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully replaced the navbar logo SVG with img tag!")
else:
    # Try to find it with different quoting
    alt = "(0,t.jsx)(R,{size:22,color:\"currentColor\",\"aria-label\":\"Linear\"})"
    count2 = content.count(alt)
    print(f"Alt pattern found: {count2}")
    
    # Find nearby context
    idx = content.find('"aria-label":"Linear"')
    if idx != -1:
        # Get the full jsx call
        # Walk back to find the start of this jsx call
        start = content.rfind('(0,t.jsx)(', max(0, idx-200), idx)
        if start != -1:
            end = content.find(')', idx) + 1
            exact = content[start:end]
            print(f"Exact pattern found: [{exact}]")
            
            # Replace it
            new_code = '(0,t.jsx)("img",{src:"./giantech_files/logo.png",alt:"GianTecH Empire",style:{height:"22px",width:"auto",objectFit:"contain"}})'
            content = content.replace(exact, new_code)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Replaced with img tag!")
