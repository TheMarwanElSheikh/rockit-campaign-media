# Website custom code (rockit-transport.com)

Site-wide code added through the Wix Custom Embeds API. Wix has no API for editing the site menu.

## Newsletter menu tab

| Field | Value |
|---|---|
| Wix custom embed | "Rockit – Newsletter menu tab", id `a65db1dc-e88e-4e6e-8f40-81bf6690f83f` |
| Placement | Body end, all pages, Essential, loads once |
| Source | `newsletter-menu-tab.html` (deployed revision 3, 15 Nov 2026) |
| Links to | https://www.rockit-transport.com/insights/categories/newsletter (blog category "The Rockit Manifest", id `23f3ec1c-cf6b-4d10-ad83-869b0e20376c`) |

**What it does**
- Adds a **Newsletter** tab before **Contact** in the desktop menu and in the mobile menu.
- Each tab is a copy of an existing plain tab, so it keeps the site's own font, colour and hover style.
- The label is translated per language: Arabic "النشرة", Spanish "Boletín", "Newsletter" otherwise.

**How it fits on narrow screens**
- The desktop menu has a fixed width. When the extra tab would overflow it, the script first narrows the gap between tabs (to no less than 4 px).
- If that is not enough, it trims the tab padding and letter-spacing.
- It re-checks whenever the menu changes size (fonts loading, window resize), so "Contact" is never clipped.

**Duplicates**
- If a Newsletter link is ever added directly in the Wix editor, the script does nothing, so no duplicate tab appears.
- You can then delete this embed (Wix dashboard → Settings → Custom Code), or call `DELETE /embeds/v1/custom-embeds/{id}`.

**Verified on the live site, 15 Nov 2026**
- Widths 1440, 1280, 1100 and 1024 px, plus mobile at 390 px.
- English and Arabic pages.
- The tab opens the newsletter page.
- No script errors.
- Screenshots: `newsletter-menu-tab_desktop.png`, `newsletter-menu-tab_mobile.png`.
