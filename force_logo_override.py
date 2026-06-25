import re

html_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Inject a post-hydration script that forcefully replaces the navbar logo
# This runs AFTER React hydration, so it always wins
override_script = """
<script>
// Force-replace the navbar logo after React hydration
(function() {
  function replaceLogo() {
    // Find all SVGs with the Linear/GianTecH logo path
    var allSvgs = document.querySelectorAll('svg[aria-label]');
    allSvgs.forEach(function(svg) {
      var label = (svg.getAttribute('aria-label') || '').toLowerCase();
      if (label.includes('logo')) {
        var img = document.createElement('img');
        img.src = './giantech_files/logo.png';
        img.alt = 'GianTecH Empire Logo';
        img.style.height = svg.getAttribute('height') ? svg.getAttribute('height') + 'px' : '20px';
        img.style.width = 'auto';
        img.style.objectFit = 'contain';
        img.style.verticalAlign = 'middle';
        svg.parentNode.replaceChild(img, svg);
      }
    });

    // Also find the "Linear" or "GianTecH Empire" text next to the logo in the navbar
    var navLinks = document.querySelectorAll('a[href], div');
    navLinks.forEach(function(el) {
      // Look for elements that have direct text "Linear" as a child span
      var spans = el.querySelectorAll('span');
      spans.forEach(function(span) {
        if (span.textContent.trim() === 'Linear') {
          span.textContent = 'GianTecH Empire';
        }
      });
    });
  }

  // Run immediately
  replaceLogo();
  // Run again after a delay to catch late hydration
  setTimeout(replaceLogo, 500);
  setTimeout(replaceLogo, 1500);
  setTimeout(replaceLogo, 3000);

  // Also use MutationObserver to catch any future re-renders
  var observer = new MutationObserver(function() {
    replaceLogo();
  });
  observer.observe(document.body, { childList: true, subtree: true });

  // Stop observing after 5 seconds to avoid performance issues
  setTimeout(function() { observer.disconnect(); }, 5000);
})();
</script>
"""

# Inject right before </body>
content = content.replace("</body>", override_script + "</body>")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected post-hydration logo override script.")
