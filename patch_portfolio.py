import os
import urllib.parse
import re

# Configurations
workspace_dir = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files"
html_path = os.path.join(workspace_dir, "index.html")

graphics_dir = os.path.join(workspace_dir, "Assets", "graphics")
website_dir = os.path.join(workspace_dir, "Assets", "website")

# Mappings for Graphics images
graphics_meta = {
    "#graphicdesign #campaigndesign #modelling #beauty….jpg": ("Fashion Campaign Modeling", "Creative Direction"),
    "#hair #newmonth #hair.jpg": ("Hair Brand Promotion", "Visual Campaign"),
    "1100145015237961922.jpg": ("Cosmetics Branding", "Identity Design"),
    "1105774514778007991.jpg": ("Luxury Perfume Advertisement", "Product Design"),
    "1111192908080178768.jpg": ("Modern Footwear Launch", "Product Styling"),
    "1139621880737258007.jpg": ("Beverage Label Identity", "Packaging Design"),
    "A beautiful product deserves a presentation that….jpg": ("Minimalist Product Showcase", "Creative Direction"),
    "A fictional magazine cover for a new street wear.jpg": ("Streetwear Magazine Cover", "Editorial Design"),
    "Clean but impressive design👌.jpg": ("Premium Cosmetics Ad", "Visual Identity"),
    "Experience the refreshing essence of nature with….jpg": ("Natural Fragrance Campaign", "Creative Advertising"),
    "Flyer Design.jpg": ("Corporate Event Identity", "Marketing Flyer"),
    "How to create clean and simple perfume flyer….jpg": ("Aromatherapy Product Launch", "Branding"),
    "Shoes are never just shoes__They’re style….jpg": ("Premium Sneakers Concept", "Ad Design"),
    "When it comes to professionalism, let's handle….jpg": ("Creative Brand Consultation", "Brand Identity"),
    "Will you be my client_ 😅🌹  Relax kwanza… si….jpg": ("Corporate Visual Assets", "Creative Agency Design")
}

# Mappings for Website assets
website_meta = {
    "#Stuffsus #ui #ux #shop #shopui….jpg": ("E-Commerce Storefront", "UI/UX Development", "ecommerce-shop"),
    "248049891973194616.jpg": ("SaaS Dashboard Interface", "Web Application", "saas-app"),
    "338755203245078169.jpg": ("AI Analytical Platform", "SaaS Platform", "ai-analytics"),
    "751538256612359570.jpg": ("Dark UI Design System", "Web Application", "design-system"),
    "829929037627709661.jpg": ("Fintech Operations Board", "Dashboard Interface", "fintech-ops"),
    "A modern website concept for premium property….jpg": ("Premium Real Estate Portal", "Web Experience", "real-estate"),
    "Alim Joldaspayev (@alimdesigner_) on X.jpg": ("Sleek Portfolios Grid", "Creative Frontend", "portfolio-grid"),
    "Hello Insta✨🔥_Social media fliers for….jpg": ("Marketing Analytics Hub", "SaaS Platform", "marketing-hub"),
    "Looking for the best dropshipping products to sell….jpg": ("Dropshipping Merchant Dashboard", "Web Application", "dropshipping"),
    "Powerful Workflow Automation Software & Tools….jpg": ("GianTecH Automation Engine", "Product Platform", "automation-engine"),
    "Ready to build the future_  Start your AI company….jpg": ("AI Incubator Dashboard", "Frontend Web App", "ai-incubator"),
    "Royella – Resort and Hotel Booking HTML5 Template….jpg": ("Resort & Hotel Booking Portal", "Responsive Website", "hotel-booking"),
    "Social Media flyer design for Teegar's Gadget.jpg": ("Teegar Gadget Marketplace", "E-Commerce Frontend", "teegar-gadget"),
    "Somos un estudio de diseño gráfico en San Luis….jpg": ("Creative Design Studio Portal", "Visual Website", "design-studio"),
    "Top Direct Selling Software Provider.jpg": ("Enterprise ERP Software Portal", "Enterprise Application", "erp-portal"),
    "Web Design, Adobe Photoshop, Adobe Illustrator.jpg": ("Graphic Agency Agency Portal", "Branding Website", "graphics-agency"),
    "d20b5e2532a2b11f4c0d3c56e6f22c5b_360w.mp4": ("Dynamic Workflow Interactions", "Interactive Web Experience", "workflow-automation")
}

def generate_graphics_cards():
    files = sorted(os.listdir(graphics_dir))
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    
    # Split into normal scrolling cards and the last 3 stack cards
    scroll_files = image_files[:-3]
    stack_files = image_files[-3:]
    
    scroll_cards = []
    for f in scroll_files:
        meta = graphics_meta.get(f)
        title, category = meta if meta else (f, "Graphics Design")
        url_encoded_filename = urllib.parse.quote(f)
        card_html = f"""      <div class="portfolio-card-panel">
        <div class="portfolio-card">
          <div class="portfolio-card-image-wrap">
            <img src="./Assets/graphics/{url_encoded_filename}" alt="{title}" loading="lazy">
          </div>
          <div class="portfolio-card-caption">
            <h4>{title}</h4>
            <p>{category}</p>
          </div>
        </div>
      </div>"""
        scroll_cards.append(card_html)
        
    stack_cards = []
    for i, f in enumerate(stack_files):
        meta = graphics_meta.get(f)
        title, category = meta if meta else (f, "Graphics Design")
        url_encoded_filename = urllib.parse.quote(f)
        card_html = f"""        <div class="portfolio-card stack-card card-{i+1}">
          <div class="portfolio-card-image-wrap">
            <img src="./Assets/graphics/{url_encoded_filename}" alt="{title}" loading="lazy">
          </div>
          <div class="portfolio-card-caption">
            <h4>{title}</h4>
            <p>{category}</p>
          </div>
        </div>"""
        stack_cards.append(card_html)
        
    stack_panel = f"""      <div class="portfolio-stack-panel">
        <div class="portfolio-stack-container">
{chr(10).join(stack_cards)}
        </div>
      </div>"""
      
    scroll_cards.append(stack_panel)
    return "\n".join(scroll_cards)

def generate_website_cards():
    files = sorted(os.listdir(website_dir))
    assets = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.mp4'))]
    
    scroll_assets = assets[:-3]
    stack_assets = assets[-3:]
    
    scroll_cards = []
    for f in scroll_assets:
        meta = website_meta.get(f)
        title, category, slug = meta if meta else (f, "Website Design", "project")
        url_encoded_filename = urllib.parse.quote(f)
        is_video = f.lower().endswith(('.mp4'))
        content_html = f'<video src="./Assets/website/{url_encoded_filename}" loop muted playsinline></video>' if is_video else f'<img src="./Assets/website/{url_encoded_filename}" alt="{title}" loading="lazy">'
        
        card_html = f"""      <div class="portfolio-card-panel">
        <div class="portfolio-card">
          <div class="browser-mockup">
            <div class="browser-header">
              <div class="browser-dots">
                <div class="browser-dot red"></div>
                <div class="browser-dot yellow"></div>
                <div class="browser-dot green"></div>
              </div>
              <div class="browser-address-bar">
                <svg viewBox="0 0 24 24" style="width: 10px; height: 10px; fill: currentColor; margin-right: 4px;"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>
                giantech.app/{slug}
              </div>
            </div>
            <div class="browser-content">
              {content_html}
            </div>
          </div>
          <div class="portfolio-card-caption">
            <h4>{title}</h4>
            <p>{category}</p>
          </div>
        </div>
      </div>"""
        scroll_cards.append(card_html)
        
    stack_cards = []
    for i, f in enumerate(stack_assets):
        meta = website_meta.get(f)
        title, category, slug = meta if meta else (f, "Website Design", "project")
        url_encoded_filename = urllib.parse.quote(f)
        is_video = f.lower().endswith(('.mp4'))
        content_html = f'<video src="./Assets/website/{url_encoded_filename}" loop muted playsinline></video>' if is_video else f'<img src="./Assets/website/{url_encoded_filename}" alt="{title}" loading="lazy">'
        
        card_html = f"""        <div class="portfolio-card stack-card card-{i+1}">
          <div class="browser-mockup">
            <div class="browser-header">
              <div class="browser-dots">
                <div class="browser-dot red"></div>
                <div class="browser-dot yellow"></div>
                <div class="browser-dot green"></div>
              </div>
              <div class="browser-address-bar">
                <svg viewBox="0 0 24 24" style="width: 10px; height: 10px; fill: currentColor; margin-right: 4px;"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>
                giantech.app/{slug}
              </div>
            </div>
            <div class="browser-content">
              {content_html}
            </div>
          </div>
          <div class="portfolio-card-caption">
            <h4>{title}</h4>
            <p>{category}</p>
          </div>
        </div>"""
        stack_cards.append(card_html)
        
    stack_panel = f"""      <div class="portfolio-stack-panel">
        <div class="portfolio-stack-container">
{chr(10).join(stack_cards)}
        </div>
      </div>"""
      
    scroll_cards.append(stack_panel)
    return "\n".join(scroll_cards)

def main():
    print("Reading index.html...")
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Strip any previous portfolio showcase blocks
    content = re.sub(
        r'<!-- START PORTFOLIO SHOWCASE -->.*?<!-- END PORTFOLIO SHOWCASE -->', 
        '', 
        content, 
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- START WEBSITE PORTFOLIO SHOWCASE -->.*?<!-- END WEBSITE PORTFOLIO SHOWCASE -->', 
        '', 
        content, 
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- START GRAPHICS PORTFOLIO SHOWCASE -->.*?<!-- END GRAPHICS PORTFOLIO SHOWCASE -->', 
        '', 
        content, 
        flags=re.DOTALL
    )
    
    # Strip styles/script links if present to avoid duplicating them
    content = content.replace('  <link rel="stylesheet" href="./Assets/portfolio.css">\n', '')
    content = content.replace('  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>\n', '')
    content = content.replace('  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>\n', '')
    content = content.replace('  <script src="./Assets/portfolio.js" defer></script>\n', '')

    print("Generating cards...")
    graphics_cards_html = generate_graphics_cards()
    website_cards_html = generate_website_cards()
    
    graphics_html = f"""<!-- START GRAPHICS PORTFOLIO SHOWCASE -->
<div class="Spacer_root__uoSvA" style="--height:120px"></div>

<!-- Graphics Design Portfolio Section -->
<div class="portfolio-scroll-wrapper" id="portfolio-graphics-wrapper">
  <div class="portfolio-sticky-container">
    <div class="portfolio-horizontal-track" id="portfolio-graphics-track">
      <!-- Title & Info Panel -->
      <div class="portfolio-intro-panel">
        <div class="portfolio-tag" id="portfolio-graphics-tag">Graphic Design</div>
        <h2 class="portfolio-title-reveal" id="portfolio-graphics-lines">
          <span>Design that captures attention,</span>
          <span>communicates value,</span>
          <span>and drives action.</span>
        </h2>
      </div>
      {graphics_cards_html}
    </div>
  </div>
</div>
<!-- END GRAPHICS PORTFOLIO SHOWCASE -->"""

    website_html = f"""<!-- START WEBSITE PORTFOLIO SHOWCASE -->
<div class="Spacer_root__uoSvA" style="--height:120px"></div>

<!-- Website & Digital Product Portfolio Section -->
<div class="portfolio-scroll-wrapper" id="portfolio-websites-wrapper">
  <div class="portfolio-sticky-container">
    <div class="portfolio-horizontal-track" id="portfolio-websites-track">
      <!-- Title & Info Panel -->
      <div class="portfolio-intro-panel">
        <div class="portfolio-tag" id="portfolio-websites-tag">Client Work</div>
        <h2 class="portfolio-title-reveal" id="portfolio-websites-lines">
          <span>Built for real businesses</span>
        </h2>
      </div>
      {website_cards_html}
    </div>
  </div>
</div>
<!-- END WEBSITE PORTFOLIO SHOWCASE -->"""

    print("Injecting links into the head of index.html...")
    head_tag = "</head>"
    if head_tag in content:
        assets_links = """  <link rel="stylesheet" href="./Assets/portfolio.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
  <script src="./Assets/portfolio.js" defer></script>\n</head>"""
        content = content.replace(head_tag, assets_links, 1)
    else:
        print("ERROR: </head> tag not found!")
        return
        
    print("Injecting Website Portfolio right after the Hero app mockup...")
    # Find the spacer preceding the features heading
    features_marker = '<div class="hide-desktop Spacer_root__uoSvA" style="--height:96px"></div><div class="show-desktop Spacer_root__uoSvA" style="--height:40px"></div><h2 id="features"'
    if features_marker in content:
        content = content.replace(features_marker, f"{website_html}\n\n{features_marker}", 1)
        print("SUCCESS: Website Portfolio injected after Hero mockup!")
    else:
        print("ERROR: Features marker not found in index.html!")
        return

    print("Injecting Graphics Portfolio before CTA section...")
    cta_marker = '<section class="CTA_homepagePrefooter__FWdih">'
    if cta_marker in content:
        content = content.replace(cta_marker, f"{graphics_html}\n\n{cta_marker}", 1)
        print("SUCCESS: Graphics Portfolio injected before CTA prefooter!")
    else:
        print("ERROR: CTA marker not found in index.html!")
        return
        
    print("Writing modified index.html...")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Patch complete!")

if __name__ == "__main__":
    main()
