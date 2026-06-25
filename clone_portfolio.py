import os
import urllib.request
import re

# Set directories
TARGET_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"
CSS_DIR = os.path.join(TARGET_DIR, "css")
JS_DIR = os.path.join(TARGET_DIR, "js")

# Create folders if not exist
os.makedirs(CSS_DIR, exist_ok=True)
os.makedirs(JS_DIR, exist_ok=True)

# User-Agent header to avoid bot blocking
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Define resources to download
PAGES = {
    "index.html": "https://www.wonjyou.com/",
    "life.html": "https://www.wonjyou.com/life",
    "loves.html": "https://www.wonjyou.com/loves",
    "work.html": "https://www.wonjyou.com/work",
    "thoughts.html": "https://www.wonjyou.com/thoughts",
    "contact.html": "https://www.wonjyou.com/contact"
}

ASSETS = {
    os.path.join(CSS_DIR, "styles.css"): "https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/css/won-j-you.webflow.abc89deb1.css",
    os.path.join(JS_DIR, "main.js"): "https://wonjyou.vercel.app/main.js",
    os.path.join(JS_DIR, "webflow.js"): "https://cdn.prod.website-files.com/644918964e907d2eeb9e57a0/js/webflow.7e939bc70.js",
    os.path.join(JS_DIR, "jquery.js"): "https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js"
}

def download_file(url, target_path):
    print(f"Downloading {url} to {target_path}...")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req) as response:
            content = response.read()
            with open(target_path, "wb") as f:
                f.write(content)
        print(f"[OK] Successfully downloaded {target_path}")
    except Exception as e:
        print(f"[ERROR] Error downloading {url}: {e}")

def process_html(file_path):
    print(f"Processing HTML paths in {file_path}...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()

        # 1. Rewrite subpage links
        # href="/" or href=""
        html = html.replace('href="/"', 'href="index.html"')
        html = html.replace('href="/life"', 'href="life.html"')
        html = html.replace('href="/loves"', 'href="loves.html"')
        html = html.replace('href="/work"', 'href="work.html"')
        html = html.replace('href="/thoughts"', 'href="thoughts.html"')
        html = html.replace('href="/contact"', 'href="contact.html"')

        # 2. Rewrite CSS link
        # Look for the specific webflow css link or any website-files.com css link and replace it
        html = re.sub(
            r'href="https://cdn\.prod\.website-files\.com/[^"]+/css/won-j-you\.webflow\.[^"]+\.css"',
            'href="css/styles.css"',
            html
        )

        # 3. Rewrite main JS link
        html = html.replace('src="https://wonjyou.vercel.app/main.js"', 'src="js/main.js"')

        # 4. Rewrite jQuery and Webflow JS links
        html = re.sub(
            r'src="https://d3e54v103j8qbb\.cloudfront\.net/js/jquery-[^"]+\.js(?:\?[^"]+)?"',
            'src="js/jquery.js"',
            html
        )
        html = re.sub(
            r'src="https://cdn\.prod\.website-files\.com/[^"]+/js/webflow\.[^"]+\.js"',
            'src="js/webflow.js"',
            html
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[OK] Successfully processed {file_path}")
    except Exception as e:
        print(f"[ERROR] Error processing {file_path}: {e}")

def main():
    # Download HTML pages
    for filename, url in PAGES.items():
        dest = os.path.join(TARGET_DIR, filename)
        download_file(url, dest)
        process_html(dest)

    # Download JS and CSS Assets
    for dest, url in ASSETS.items():
        download_file(url, dest)

    print("\nClone process completed!")

if __name__ == "__main__":
    main()
