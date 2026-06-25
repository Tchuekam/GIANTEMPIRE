import os
import re

PROJECT_DIR = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"
pages = ["index.html", "life.html", "loves.html", "work.html", "thoughts.html", "contact.html"]

def customize_html_files():
    for page in pages:
        path = os.path.join(PROJECT_DIR, page)
        if not os.path.exists(path):
            continue
            
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. Replace name strings with correct non-breaking spaces
        content = content.replace("WON\xa0J. YOU", "TCHUEKAM\xa0L.\xa0ROSTAND")
        content = content.replace("WON\xa0J\xa0YOU", "TCHUEKAM\xa0L.\xa0ROSTAND")
        content = content.replace("WON&nbsp;J.&nbsp;YOU", "TCHUEKAM&nbsp;L.&nbsp;ROSTAND")
        content = content.replace("WON&nbsp;J. YOU", "TCHUEKAM&nbsp;L.&nbsp;ROSTAND")
        content = content.replace("WON J. YOU", "TCHUEKAM L. ROSTAND")
        content = content.replace("WON J YOU", "TCHUEKAM L. ROSTAND")
        content = content.replace("Won J. You", "Tchuekam Loic Rostand")
        content = content.replace("Won J You", "Tchuekam Loic Rostand")
        
        # 2. Fix navigation logo replacement (regex with re.DOTALL to match multiline SVG)
        content = re.sub(
            r'<a([^>]*class="[^"]*nav__logo[^"]*"[^>]*)>.*?</a>',
            r'<a\1><img src="images/logo.png" alt="Giantect Logo" style="height: 45px; width: auto; object-fit: contain; filter: none !important;"/></a>',
            content,
            flags=re.DOTALL
        )
        
        # 3. Add custom logo inside the .img-popup__logo div
        content = content.replace(
            '<div class="img-popup__logo"></div>',
            '<div class="img-popup__logo"><img src="images/logo.png" style="width: 100%; height: 100%; object-fit: contain; filter: none !important;"/></div>'
        )
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Customized HTML file: {page}")

def customize_js_files():
    js_path = os.path.join(PROJECT_DIR, "js", "main.js")
    if not os.path.exists(js_path):
        print("[ERROR] js/main.js not found!")
        return
        
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace Lottie loader for Signature with a mock object
    lottie_sig = 're=Lottie.loadAnimation({container:document.querySelector(".footer__signature"),renderer:"svg",loop:!1,autoplay:!1,path:"https://uploads-ssl.webflow.com/644918964e907d2eeb9e57a0/6450bf2d08974b7254f134be_Signature.json"})'
    mock_sig = 're={addEventListener:(ev,cb)=>{if(ev==="DOMLoaded")setTimeout(cb,100)},totalFrames:100,goToAndStop:()=>{}}'
    
    # Replace Lottie loader for Logo with a mock object
    lottie_logo = 'le=Lottie.loadAnimation({container:document.querySelector(".img-popup__logo"),renderer:"svg",loop:!1,autoplay:!1,path:"https://uploads-ssl.webflow.com/644918964e907d2eeb9e57a0/6454a87cee2f168516152375_Won_logo2.json"})'
    mock_logo = 'le={addEventListener:(ev,cb)=>{if(ev==="DOMLoaded")setTimeout(cb,100)},totalFrames:100,goToAndStop:()=>{}}'
    
    if lottie_sig in content:
        content = content.replace(lottie_sig, mock_sig)
        print("[OK] Replaced Lottie Signature animation in main.js")
    else:
        print("[WARNING] Lottie Signature string not found in main.js")
        
    if lottie_logo in content:
        content = content.replace(lottie_logo, mock_logo)
        print("[OK] Replaced Lottie Logo animation in main.js")
    else:
        print("[WARNING] Lottie Logo string not found in main.js")
        
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] js/main.js customized")

if __name__ == "__main__":
    customize_html_files()
    customize_js_files()
    print("\nCustomization complete!")
