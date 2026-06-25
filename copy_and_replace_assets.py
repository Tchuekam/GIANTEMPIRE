import os
import shutil
import re

PROJECT_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"
ASSETS_DIR = os.path.join(PROJECT_DIR, "Assets")
IMAGES_DIR = os.path.join(PROJECT_DIR, "images")

os.makedirs(IMAGES_DIR, exist_ok=True)

# 1. Map assets to copy and rename
ASSET_MAPPING = {
    "First banner image.webp": "first_banner.webp",
    "660131912_17892757893439160_2270575115490846085_n.webp": "life_profile.webp",
    "496388200_614022438363053_7529213229702848414_n.jpg": "photo_1.jpg",
    "507583228_639746049124025_5595317250276355036_n.jpg": "photo_2.jpg",
    "571204103_748006521631310_6979112779590083803_n.jpg": "photo_3.jpg",
    "580729196_764116126687016_5160884119000785673_n.jpg": "photo_4.jpg",
    "603803827_797675093331119_4004654107839110566_n.jpg": "photo_5.jpg",
    "649722577_860400493725245_6894370796500621651_n.jpg": "photo_6.jpg",
    "651406802_860965547002073_4752343642189619294_n.jpg": "photo_7.jpg",
    "AQNOrVsA_8OrwFgmws_chu5Xgzuxxunvr86Ze9UUpeEEkzGTzr1Lmvc6V7Oe9in53IgU1yL9sGx9Ib9Sn-d2bVvyfPYeo234EBhRIEk.mp4": "video_1.mp4",
    "AQPk39BNLH54oVEc_IV2Py3M0wVrEIKRWsZYMgDJ4ZpBNLIHDniLJGbMMOwavcPBCFtD_-hcD5mdcSSxWJJFoGrexFyl9aHQJ5jJWjI.mp4": "video_2.mp4"
}

# Copy and rename assets
print("--- Copying Assets ---")
for src_name, dest_name in ASSET_MAPPING.items():
    src_path = os.path.join(ASSETS_DIR, src_name)
    dest_path = os.path.join(IMAGES_DIR, dest_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"[OK] Copied {src_name} -> {dest_name}")
    else:
        print(f"[WARNING] Asset not found: {src_name}")

# 2. Localize replacements in HTML files
def localize_page_media(filename):
    path = os.path.join(PROJECT_DIR, filename)
    if not os.path.exists(path):
        return
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # A. Replace Hero Fallback Image
    # Original: hero-alpha.webp or the raw webflow URL
    # Replace src="https://cdn.prod.website-files.com/..._hero-alpha.webp" or src="...hero-alpha.webp"
    content = re.sub(
        r'src="[^"]*hero-alpha[^"]*\.webp"',
        'src="images/first_banner.webp"',
        content
    )
    
    # Also clean up any srcset attribute on the hero fallback image so browser is forced to load first_banner
    # (Since responsive srcset links point to webflow CDN which we don't want)
    content = re.sub(
        r'srcset="[^"]*hero-alpha[^"]*\.webp[^"]*"',
        'srcset="images/first_banner.webp 1x"',
        content
    )

    # B. Replace other specific Webflow site layout images
    # 1. Chall 02 (home page challenger section image 1)
    content = re.sub(r'src="[^"]*Chall%2002[^"]*\.webp"', 'src="images/photo_1.jpg"', content)
    content = re.sub(r'srcset="[^"]*Chall%2002[^"]*\.webp[^"]*"', 'srcset="images/photo_1.jpg 1x"', content)
    
    # 2. Chall 03 (home page challenger section image 2)
    content = re.sub(r'src="[^"]*Chall%2003[^"]*\.webp"', 'src="images/photo_2.jpg"', content)
    content = re.sub(r'srcset="[^"]*Chall%2003[^"]*\.webp[^"]*"', 'srcset="images/photo_2.jpg 1x"', content)
    
    # 3. img popup01 (beliefs page pop-up hover)
    content = re.sub(r'src="[^"]*img%20popup01[^"]*\.webp"', 'src="images/photo_3.jpg"', content)
    content = re.sub(r'srcset="[^"]*img%20popup01[^"]*\.webp[^"]*"', 'srcset="images/photo_3.jpg 1x"', content)

    # 4. motorcycle_2x (loves motorcycle hover image)
    content = re.sub(r'src="[^"]*motorcycle_2x[^"]*\.webp"', 'src="images/photo_4.jpg"', content)
    content = re.sub(r'srcset="[^"]*motorcycle_2x[^"]*\.webp[^"]*"', 'srcset="images/photo_4.jpg 1x"', content)
    
    # 5. Loader Img01, Img02, Img03 in index.html and other files (replace with logo or specific photos if desired)
    # Let's keep them pointing to logo.png or swap them with different photos
    content = re.sub(r'src="[^"]*Loader%20Img01[^"]*\.webp"', 'src="images/logo.png"', content)
    content = re.sub(r'srcset="[^"]*Loader%20Img01[^"]*\.webp[^"]*"', 'srcset="images/logo.png 1x"', content)
    
    content = re.sub(r'src="[^"]*Loader%20Img02[^"]*\.webp"', 'src="images/logo.png"', content)
    content = re.sub(r'srcset="[^"]*Loader%20Img02[^"]*\.webp[^"]*"', 'srcset="images/logo.png 1x"', content)

    content = re.sub(r'src="[^"]*Loader%20Img03[^"]*\.webp"', 'src="images/logo.png"', content)
    content = re.sub(r'srcset="[^"]*Loader%20Img03[^"]*\.webp[^"]*"', 'srcset="images/logo.png 1x"', content)

    # C. Replace Video Source files
    # The home page uses background videos on binsta.dev
    # We will replace them with local video files
    content = re.sub(
        r'src="https://binsta\.dev/api/v1/files/tm-dkkuil7/transform[^"]*"',
        'src="images/video_1.mp4"',
        content
    )
    content = re.sub(
        r'src="https://binsta\.dev/api/v1/files/27NbTVo1wj/transform[^"]*"',
        'src="images/video_2.mp4"',
        content
    )
    
    # Other videos
    content = re.sub(
        r'src="https://binsta\.dev/api/v1/files/[^"]*"',
        'src="images/video_1.mp4"',
        content
    )

    # D. Replace life.html main profile image
    # Original: hero-life.webp or similar
    content = re.sub(
        r'src="[^"]*hero-life[^"]*\.webp"',
        'src="images/life_profile.webp"',
        content
    )
    content = re.sub(
        r'srcset="[^"]*hero-life[^"]*\.webp[^"]*"',
        'srcset="images/life_profile.webp 1x"',
        content
    )
    
    # Replace other site-specific images on life.html (like maps or groups) with user photos
    content = re.sub(r'src="[^"]*Group\.svg[^"]*"', 'src="images/logo.png"', content)
    content = re.sub(r'src="[^"]*Career%20Img[^"]*\.webp"', 'src="images/photo_5.jpg"', content)
    content = re.sub(r'srcset="[^"]*Career%20Img[^"]*\.webp[^"]*"', 'srcset="images/photo_5.jpg 1x"', content)
    content = re.sub(r'src="[^"]*Career%20Design%2001[^"]*\.webp"', 'src="images/photo_6.jpg"', content)
    content = re.sub(r'srcset="[^"]*Career%20Design%2001[^"]*\.webp[^"]*"', 'srcset="images/photo_6.jpg 1x"', content)
    content = re.sub(r'src="[^"]*Career%20Design%2002[^"]*\.webp"', 'src="images/photo_7.jpg"', content)
    content = re.sub(r'srcset="[^"]*Career%20Design%2002[^"]*\.webp[^"]*"', 'srcset="images/photo_7.jpg 1x"', content)

    # E. Replace loves.html elements (cats / goldie)
    # Loves page has pets images (cat-1, cat-2, goldie)
    content = re.sub(r'src="[^"]*cat-1[^"]*\.webp"', 'src="images/photo_1.jpg"', content)
    content = re.sub(r'srcset="[^"]*cat-1[^"]*\.webp[^"]*"', 'srcset="images/photo_1.jpg 1x"', content)
    content = re.sub(r'src="[^"]*cat-2[^"]*\.webp"', 'src="images/photo_2.jpg"', content)
    content = re.sub(r'srcset="[^"]*cat-2[^"]*\.webp[^"]*"', 'srcset="images/photo_2.jpg 1x"', content)
    content = re.sub(r'src="[^"]*goldie[^"]*\.webp"', 'src="images/photo_3.jpg"', content)
    content = re.sub(r'srcset="[^"]*goldie[^"]*\.webp[^"]*"', 'srcset="images/photo_3.jpg 1x"', content)

    # F. Replace work.html elements (project icons/slides)
    content = re.sub(r'src="[^"]*hero%20work[^"]*\.webp"', 'src="images/first_banner.webp"', content)
    content = re.sub(r'srcset="[^"]*hero%20work[^"]*\.webp[^"]*"', 'srcset="images/first_banner.webp 1x"', content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] Localized media paths in {filename}")

print("\n--- Replacing Paths in HTML Files ---")
for page in ["index.html", "life.html", "loves.html", "work.html", "contact.html"]:
    localize_page_media(page)

print("\nAssets replacement script finished!")
