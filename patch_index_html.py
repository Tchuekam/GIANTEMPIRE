import re

html_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

replaces = []

# 1. Replace the header logo link href="#" with href="index.html"
logo_old = '<a aria-label="Navigate to home" data-radix-collection-item="" class="Header_logoLink__Sgfy4 Link_root__cNtak" rel="noopener" href="#">'
logo_new = '<a aria-label="Navigate to home" data-radix-collection-item="" class="Header_logoLink__Sgfy4 Link_root__cNtak" rel="noopener" href="index.html">'
replaces.append((logo_old, logo_new, "Header Logo Link"))

# 2. Replace Product trigger button in navbar with anchor tag to products.html
prod_old = '<li class="hide-tablet Header_item__a2E_K"><button id="radix-_R_ninpfcqlb_-trigger-product" data-state="closed" aria-expanded="false" aria-controls="radix-_R_ninpfcqlb_-content-product" class="Header_anchor__CTwdv Header_trigger__xKGQe reset_reset-button__5vBZ4" data-radix-collection-item="">Product</button></li>'
prod_new = '<li class="hide-tablet Header_item__a2E_K"><a data-radix-collection-item="" class="Header_anchor__CTwdv Link_root__cNtak" href="products.html">Product</a></li>'
replaces.append((prod_old, prod_new, "Navbar Product Button"))

# 3. Replace the footer logo link href="#" with href="index.html"
footer_logo_old = '<a class="Footer_logoWrapper__9IJLI Link_root__cNtak Link_variant-fade__U2YWc" rel="noopener" href="#"><img src="./giantech_files/logo.png"'
footer_logo_new = '<a class="Footer_logoWrapper__9IJLI Link_root__cNtak Link_variant-fade__U2YWc" rel="noopener" href="index.html"><img src="./giantech_files/logo.png"'
replaces.append((footer_logo_old, footer_logo_new, "Footer Logo Link"))

# 4. Replace footer "Intake" link with "Product Suite" linking to products.html
intake_old = '<li class="Footer_sectionItem__lDqAK"><a class="Footer_sectionLink__yuXh6 Link_root__cNtak Link_variant-dimmed__kvcr0" rel="noopener" href="#">Intake</a></li>'
intake_new = '<li class="Footer_sectionItem__lDqAK"><a class="Footer_sectionLink__yuXh6 Link_root__cNtak Link_variant-dimmed__kvcr0" rel="noopener" href="products.html">Product Suite</a></li>'
replaces.append((intake_old, intake_new, "Footer Intake to Product Suite Link"))

# 5. Add id="features" to the main features header tag
features_old = '<h2 style="max-width:1250px" class="sc-d5151d0-0 exSLMF utils_inset__Xhl3T utils_insetLarge__6UCke"><strong class="sc-d5151d0-0 bWWlPr">A new species of product tool.</strong>'
features_new = '<h2 id="features" style="max-width:1250px" class="sc-d5151d0-0 exSLMF utils_inset__Xhl3T utils_insetLarge__6UCke"><strong class="sc-d5151d0-0 bWWlPr">A new species of product tool.</strong>'
replaces.append((features_old, features_new, "Features Section ID"))

# 6. Add id="changelog" to the Changelog header tag
changelog_old = '<h2 class="sc-d5151d0-0 kkJAGU">Changelog</h2>'
changelog_new = '<h2 id="changelog" class="sc-d5151d0-0 kkJAGU">Changelog</h2>'
replaces.append((changelog_old, changelog_new, "Changelog Section ID"))

# 7. Replace footer "Changelog" link href="#" with href="#changelog"
# We'll do this carefully by finding the context:
# class="Footer_sectionLink__yuXh6 Link_root__cNtak Link_variant-dimmed__kvcr0" rel="noopener" href="#">Changelog</a>
footer_changelog_old = 'class="Footer_sectionLink__yuXh6 Link_root__cNtak Link_variant-dimmed__kvcr0" rel="noopener" href="#">Changelog</a>'
footer_changelog_new = 'class="Footer_sectionLink__yuXh6 Link_root__cNtak Link_variant-dimmed__kvcr0" rel="noopener" href="#changelog">Changelog</a>'
replaces.append((footer_changelog_old, footer_changelog_new, "Footer Changelog Link"))

# 8. Check and replace to make sure header navigation buttons match products.html buttons
# We can replace the hide-login elements with the booking button, but wait, let's keep the original logic
# but add the Book Consultation button cleanly.
# Let's see: in products.html:
# <button type="button" class="Button_root__Stmhv Button_variant-invert__ECHZN Button_size-small__sjtMt Button_variant__1FJO9 Link_root__cNtak" id="navBookBtn">Book Consultation</button>
# Let's insert the Book Consultation button in the navbar right before Sign Up or instead of Login/Signup.
# Let's look at the Header buttons block:
# <ul class="Header_buttons__qwTPf"><li class="hide-mobile Header_buttonItem__crtcc Header_item__a2E_K" data-show="logged-in"><a data-radix-collection-item="" class="Header_anchor__CTwdv Link_root__cNtak" rel="noopener" href="#">Docs</a></li><li class="Header_buttonItem__crtcc Header_item__a2E_K" data-show="logged-in"><span id="header-tooltip-open-app"><a draggable="false" type="button" role="button" tabindex="0" class="Button_root__Stmhv Button_variant-invert__ECHZN Button_size-small__sjtMt Button_variant__1FJO9 Link_root__cNtak" rel="noopener" href="#">Open app</a></span></li><li class="Header_buttonItem__crtcc Header_item__a2E_K" data-hide="logged-in"><span id="header-tooltip-login"><a draggable="false" class="Header_anchor__CTwdv Link_root__cNtak" rel="noopener" href="#">Log in</a></span></li><li class="Header_buttonItem__crtcc Header_item__a2E_K" data-hide="logged-in"><a draggable="false" class="Button_root__Stmhv Button_variant-invert__ECHZN Button_size-small__sjtMt Button_variant__1FJO9 Link_root__cNtak" rel="noopener" href="#">Sign up</a></li></ul>
# Let's replace the whole Header_buttons block to have the "Book Consultation" button on desktop/mobile for guest users!
# But let's check if we should replace it.
buttons_old = '<ul class="Header_buttons__qwTPf"><li class="hide-mobile Header_buttonItem__crtcc Header_item__a2E_K" data-show="logged-in"><a data-radix-collection-item="" class="Header_anchor__CTwdv Link_root__cNtak" rel="noopener" href="#">Docs</a></li><li class="Header_buttonItem__crtcc Header_item__a2E_K" data-show="logged-in"><span id="header-tooltip-open-app"><a draggable="false" type="button" role="button" tabindex="0" class="Button_root__Stmhv Button_variant-invert__ECHZN Button_size-small__sjtMt Button_variant__1FJO9 Link_root__cNtak" rel="noopener" href="#">Open app</a></span></li><li class="Header_buttonItem__crtcc Header_item__a2E_K" data-hide="logged-in"><span id="header-tooltip-login"><a draggable="false" class="Header_anchor__CTwdv Link_root__cNtak" rel="noopener" href="#">Log in</a></span></li><li class="Header_buttonItem__crtcc Header_item__a2E_K" data-hide="logged-in"><a draggable="false" class="Button_root__Stmhv Button_variant-invert__ECHZN Button_size-small__sjtMt Button_variant__1FJO9 Link_root__cNtak" rel="noopener" href="#">Sign up</a></li></ul>'
buttons_new = '<ul class="Header_buttons__qwTPf"><li class="Header_buttonItem__crtcc Header_item__a2E_K"><button type="button" class="Button_root__Stmhv Button_variant-invert__ECHZN Button_size-small__sjtMt Button_variant__1FJO9 Link_root__cNtak" id="navBookBtn">Book Consultation</button></li></ul>'
replaces.append((buttons_old, buttons_new, "Navbar Consultation CTA"))

# Apply and verify replacements
modified_content = content
for old_str, new_str, name in replaces:
    count = modified_content.count(old_str)
    print(f"Replacement '{name}': {count} occurrences found.")
    if count > 0:
        modified_content = modified_content.replace(old_str, new_str)
    else:
        print(f"WARNING: '{name}' pattern NOT found!")

# Let's save index.html if modified
if modified_content != content:
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(modified_content)
    print("SUCCESS: index.html patched successfully!")
else:
    print("WARNING: No modifications were made to index.html!")
