import os
import sys
import math
from PIL import Image, ImageFilter

IMAGES_DIR = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\images"
img_path = os.path.join(IMAGES_DIR, "first_banner.webp")
backup_path = os.path.join(IMAGES_DIR, "first_banner_original.webp")

if not os.path.exists(img_path):
    print(f"[ERROR] Image not found at {img_path}")
    sys.exit(1)

# Create a backup of the original if it doesn't exist yet
if not os.path.exists(backup_path):
    import shutil
    shutil.copy(img_path, backup_path)
    print(f"[OK] Backed up original image to {backup_path}")

# Load image
img = Image.open(backup_path).convert("RGBA")
width, height = img.size
print(f"Loaded image: {width}x{height}")

# Sample background pixels from borders to get the wall color
bg_pixels = []
# Sample top 8% of the image
for y in range(0, int(height * 0.08)):
    for x in range(0, width, 5):
        bg_pixels.append(img.getpixel((x, y)))

# Sample left 5% and right 5% of the image
for y in range(0, height, 5):
    for x in list(range(0, int(width * 0.05))) + list(range(int(width * 0.95), width)):
        bg_pixels.append(img.getpixel((x, y)))

# Calculate average background RGB
r_vals = [p[0] for p in bg_pixels]
g_vals = [p[1] for p in bg_pixels]
b_vals = [p[2] for p in bg_pixels]

bg_r = sum(r_vals) / len(r_vals)
bg_g = sum(g_vals) / len(g_vals)
bg_b = sum(b_vals) / len(b_vals)
print(f"Estimated Background Wall Color: R={bg_r:.1f}, G={bg_g:.1f}, B={bg_b:.1f}")

# We will apply soft thresholding based on Euclidean distance in RGB space
# If distance < threshold_low -> alpha = 0 (completely transparent background)
# If distance > threshold_high -> alpha = 255 (completely opaque foreground)
# In between -> linear interpolation of alpha
threshold_low = 45.0
threshold_high = 75.0

# Grayscale conversion and background keying
pixels = img.load()
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        
        # Calculate distance to background color
        dist = math.sqrt((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)
        
        # Calculate alpha
        if dist < threshold_low:
            new_a = 0
        elif dist > threshold_high:
            new_a = a
        else:
            factor = (dist - threshold_low) / (threshold_high - threshold_low)
            new_a = int(a * factor)
            
        # Convert to high-contrast grayscale
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        
        # Boost contrast slightly
        gray = int((gray - 128) * 1.15 + 128)
        gray = max(0, min(255, gray))
        
        pixels[x, y] = (gray, gray, gray, new_a)

# Apply a very slight blur to the alpha channel to smooth edges (feathering)
# We can do this by separating the alpha channel, blurring it, and putting it back
r, g, b, alpha = img.split()
alpha = alpha.filter(ImageFilter.GaussianBlur(1.0))
img = Image.merge("RGBA", (r, g, b, alpha))

# Save the processed image back as webp
img.save(img_path, "WEBP", quality=90)
print(f"[OK] Processed and saved keyed black-and-white hero image to {img_path}")
