import os
import re

PROJECT_DIR = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

# Helper function to do replacements in a file
def replace_in_file(filename, replacements):
    path = os.path.join(PROJECT_DIR, filename)
    if not os.path.exists(path):
        print(f"[ERROR] File not found: {path}")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] Replaced in {filename}")

def main():
    # 1. life.html replacements
    # Replace skydiving.webp with life_profile.webp and fix aspect ratio to 1.00000
    life_reps = [
        ('src="https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64aa81360b9982d5e08de2ba_skydiving.webp"', 'src="images/life_profile.webp"'),
        ('srcset="https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64aa81360b9982d5e08de2ba_skydiving-p-500.webp 500w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64aa81360b9982d5e08de2ba_skydiving-p-800.webp 800w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64aa81360b9982d5e08de2ba_skydiving-p-1080.webp 1080w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64aa81360b9982d5e08de2ba_skydiving-p-1600.webp 1600w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64aa81360b9982d5e08de2ba_skydiving-p-2000.webp 2000w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64aa81360b9982d5e08de2ba_skydiving-p-2600.webp 2600w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64aa81360b9982d5e08de2ba_skydiving-p-3200.webp 3200w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64aa81360b9982d5e08de2ba_skydiving.webp 3898w"', 'srcset="images/life_profile.webp 1x"'),
        ('aspect="1.5781376518"', 'aspect="1.00000"')
    ]
    replace_in_file("life.html", life_reps)
    
    # 2. loves.html replacements
    # Replace hero-3.webp with photo_5.jpg and fix aspect ratio to 0.75000
    loves_reps = [
        ('src="https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/6465ea92dcb0a00eb02c61e6_hero-3.webp"', 'src="images/photo_5.jpg"'),
        ('srcset="https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/6465ea92dcb0a00eb02c61e6_hero-3-p-500.webp 500w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/6465ea92dcb0a00eb02c61e6_hero-3-p-800.webp 800w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/6465ea92dcb0a00eb02c61e6_hero-3-p-1080.webp 1080w, https://cdn.prod.website-files.com/6465ea92dcb0a00eb02c61e6_hero-3-p-1600.webp 1600w, https://cdn.prod.website-files.com/6465ea92dcb0a00eb02c61e6_hero-3-p-2000.webp 2000w, https://cdn.prod.website-files.com/6465ea92dcb0a00eb02c61e6_hero-3-p-2600.webp 2600w, https://cdn.prod.website-files.com/6465ea92dcb0a00eb02c61e6_hero-3-p-3200.webp 3200w, https://cdn.prod.website-files.com/6465ea92dcb0a00eb02c61e6_hero-3.webp 3898w"', 'srcset="images/photo_5.jpg 1x"'),
        ('aspect="1.5781376518"', 'aspect="0.75000"')
    ]
    replace_in_file("loves.html", loves_reps)
    
    # 3. thoughts.html replacements
    # Replace Hero.webp with photo_6.jpg and fix aspect ratio to 0.75299
    thoughts_reps = [
        ('src="https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64787d6faf69e9b944e2f34a_Hero.webp"', 'src="images/photo_6.jpg"'),
        ('srcset="https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64787d6faf69e9b944e2f34a_Hero-p-500.webp 500w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64787d6faf69e9b944e2f34a_Hero-p-800.webp 800w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64787d6faf69e9b944e2f34a_Hero-p-1080.webp 1080w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64787d6faf69e9b944e2f34a_Hero-p-1600.webp 1600w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64787d6faf69e9b944e2f34a_Hero-p-2000.webp 2000w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64787d6faf69e9b944e2f34a_Hero-p-2600.webp 2600w, https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/64787d6faf69e9b944e2f34a_Hero-p-3200.webp 3200w, https://cdn.prod.website-files.com/64787d6faf69e9b944e2f34a_Hero.webp 3898w"', 'srcset="images/photo_6.jpg 1x"'),
        ('aspect="1.5781376518"', 'aspect="0.75299"')
    ]
    replace_in_file("thoughts.html", thoughts_reps)
    
    # 4. work.html replacements
    # Fix aspect ratio to 0.75292
    work_reps = [
        ('aspect="1.5781376518"', 'aspect="0.75292"')
    ]
    replace_in_file("work.html", work_reps)
    
    # 5. index.html replacements
    # Fix aspect ratio to 0.75292
    index_reps = [
        ('aspect="1.5781376518"', 'aspect="0.75292"')
    ]
    replace_in_file("index.html", index_reps)

if __name__ == "__main__":
    main()
