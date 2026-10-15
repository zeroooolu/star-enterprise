# Design QA — 首页首屏右侧专辑工作台

- Source visual truth: `/var/folders/c4/j08jzybj5xvfmh812c5w18p80000gp/T/codex-clipboard-c359b561-8bb0-4d63-9cd8-7ca8feb5138b.png`, `/var/folders/c4/j08jzybj5xvfmh812c5w18p80000gp/T/codex-clipboard-e507d7ad-4363-4e6a-8db9-e45b8c20b41d.png`, `/var/folders/c4/j08jzybj5xvfmh812c5w18p80000gp/T/codex-clipboard-aafea1a4-89f5-4f55-81cc-be524508c41f.png`, `/var/folders/c4/j08jzybj5xvfmh812c5w18p80000gp/T/codex-clipboard-36e9bb66-37e7-4e13-8af0-3f5f3613f4fc.png`, and `/var/folders/c4/j08jzybj5xvfmh812c5w18p80000gp/T/codex-clipboard-cb94f373-dec2-4a2e-b5b5-0c1e225e1a67.png`
- Implementation: `http://127.0.0.1:4173/prototype-v4/index.html`
- Desktop implementation screenshot: `design-qa-assets/home-hero-desktop.png`
- Mobile implementation screenshot: `design-qa-assets/home-hero-mobile.png`
- Product-mode cards screenshot: `design-qa-assets/use-modes-desktop.png`
- Combined comparison evidence: `design-qa-assets/reference-implementation-comparison.jpg`
- Reference dimensions: 1274 × 679 px and 185 × 116 px
- Browser CSS viewport: 1440 × 1000 px, device scale factor 1; responsive check at 390 × 844 px
- Desktop screen capture: 3024 × 1964 px at host Retina density; browser layout geometry independently confirmed at 1440 CSS px with document scroll width 1440 px
- State: homepage, initial hero state

## Findings

- No actionable P0/P1/P2 findings.
- The source images are stylistic product references rather than a pixel-identical hero mockup. The implementation intentionally reduces the source's filters, utilities, and large catalog density to a compact three-album evidence panel suitable for the homepage hero.
- Fonts and typography: the existing product font stack and blue hierarchy are preserved; the mock UI uses smaller optical sizes without visible clipping at desktop or mobile breakpoints.
- Spacing and layout rhythm: sidebar, title bar, album grid, and status row align to a consistent compact grid. The desktop document has no horizontal overflow, and the mobile layout reduces to two visible album cards.
- Colors and visual tokens: neutral whites and cool grays follow the source, with the existing enterprise blue retained for selected navigation, actions, and review state.
- Image quality and asset fidelity: all three visible album covers are original raster assets sized and cropped for their square slots. No placeholder, CSS-drawn album art, or stretched source screenshot is used.
- Cross-section content consistency: the WHAT IT DOES catalog card now reuses the hero's Night Drive, After Rain, and Northern Lights covers, titles, and artist names. The status card uses the same locally stored platform-logo set as the global distribution area.
- Responsive title treatment: WHO IT IS FOR uses two intentional, non-breaking title lines. At 1440 px the line widths are 463 px and 417 px within an 821 px title area; at 390 px they are 327 px and 295 px within 350 px, with no document overflow.
- Distribution channel accuracy: the homepage marquee and product distribution grid use the same 14-channel whitelist, including Spotify. Every item now uses a real locally stored logo sourced from the user-provided Star preset; Facebook and Instagram intentionally reuse the preset's shared Meta logo. Browser verification reported zero broken images across the document.
- Pricing consistency: the homepage, pricing page, API commercial modules, admin usage packages, and business baseline now use ¥0.8 / 首 / 渠道. The pricing example correctly resolves 60 uses to ¥48.
- Copy and content: fictional album and artist data is clearly separated from the user's reference data while still demonstrating album count, track count, and release state.
- Navigation fidelity: the workspace menu now contains the four specified groups and all eleven requested items in the supplied order. Each item uses a consistent local outline icon asset; all icon files loaded successfully at their intrinsic 24 px size.
- Accessibility: all covers include descriptive alt text; decorative menu icons have empty alt text and are hidden from assistive technology, while the example workspace and menu retain descriptive labels. The synchronization dot does not carry unique meaning without its adjacent text.

## Full-view comparison evidence

`design-qa-assets/reference-implementation-comparison.jpg` places the provided catalog/menu references and the rendered desktop hero in one comparison image. The implementation carries over the source's white/gray frame, slim menu, blue selection state, album-cover emphasis, and restrained enterprise density while remaining legible at hero scale.

## Focused region comparison evidence

The hero workbench itself is the focused comparison region. Its menu labels, breadcrumb, action placement, three-column album grid, metadata, and status chips were reviewed against the corresponding regions in the reference screenshots. No additional crop was needed because those details remain readable in the combined board.

## Primary interactions and runtime checks

- Verified the “查看版本与价格” entry routes to `/enterprise/pricing` and browser back restores the homepage.
- Verified the responsive hero at 390 × 844 CSS px.
- Browser console warnings/errors checked: none.

## Comparison history

- Pass 1: no actionable P0/P1/P2 differences. The simplified density is intentional and appropriate to the homepage context.
- Pass 2: updated the menu to the specified content assets, distribution and licensing, reporting and split, and settings groups; added eleven consistent outline icons; removed the extra Home, DDEX, and DSP items. Rechecked at 1440 × 1000 and 390 × 844 CSS px. All icons loaded, document scroll width equals viewport width, and no console warnings or errors were present.
- Pass 3: replaced the fictional NOVA / Music Distribution title with the fully visible “LOGO / 自有品牌” lockup, removed the synchronization status row and CATALOG WORKSPACE label, and replaced them with a clipped next-row preview using three new original album-cover assets. Rechecked desktop and mobile rendering; all three images loaded at 360 px intrinsic width, mobile document width remained 390 px, and no console warnings or errors were present.
- Pass 4: replaced the left “TWO WAYS TO USE” card's legacy pseudo-element mockup with a structured brand-portal preview. Reset inherited badge styles inside the component so the brand name and metric values no longer become unintended blue pills. Rechecked at 1440 × 1000 and 390 × 844 CSS px; the mobile card fits from x=37 to x=353 within the 390 px viewport, document width remains 390 px, and no console warnings or errors were present.
- Pass 5: aligned the WHAT IT DOES catalog preview with the hero albums, added local QQ Music / NetEase Cloud Music / Apple Music marks to the channel-status preview, changed WHO IT IS FOR to a deliberate two-line title, localized all nine global-distribution logos, and unified the release usage fee at ¥0.8. Rechecked at 1440 × 1000 and 390 × 844 CSS px; all images loaded, both title lines fit, the pricing example equals ¥48, and browser console warnings/errors remain empty.
- Pass 6: replaced the previous DSP set with the user-specified 13-channel whitelist across the homepage marquee, product distribution grid, supporting counts, and API examples. Confirmed 26 marquee items (two identical 13-item loops), 13 product-grid items, four real local logos, nine neutral placeholders, zero legacy channel names in the homepage, no horizontal overflow at 390 px, and no console warnings or errors.
- Pass 7: added Spotify and replaced every remaining neutral DSP placeholder with the matching real asset from the supplied Star preset. Confirmed 28 marquee images (two identical 14-item loops), 14 product-grid images, zero placeholders, zero broken images, no horizontal overflow at 390 px, and no browser console warnings or errors.
- Pass 8: synchronized the homepage pricing cards with the pricing page yearly values (¥9,999 / ¥99,999 / ¥299,999), replaced the homepage API illustration with five real Open API V1 endpoints and the production integration capabilities, and converted the global footer to a white theme with the requested copyright and filing records. Rechecked at 1440 × 1000 and 390 × 844 CSS px; the home and pricing-page values match exactly, both MIIT links resolve to the supplied filing URL, the longest API path wraps inside its card, the footer remains readable without horizontal overflow, all images load, and browser console warnings/errors remain empty.
- Pass 9: synchronized public brand information with the current kanjian.com website. Added the official 32 px favicon and official Open Graph image as local assets, added current brand metadata, and expanded the footer with the official 2012 founding statement, public scale figures, global-office regions, official website/contact links, and verified social profiles. Rechecked at desktop and 390 × 844 CSS px; favicon and social links resolve, no image is broken, and the expanded footer has no horizontal overflow.
- Pass 10: replaced the product-page hero mockup shell with the homepage's same LOGO / 自有品牌 title bar, enterprise-admin label, four menu groups, eleven menu items, and local outline icon set. The product page correctly highlights 发行 while preserving its existing 发行工作台 / 今日待处理 metrics and task list. Rechecked at 1440 × 1000 and 390 × 844 CSS px; all eleven icons load, the mobile shell remains within its 350 px card, every task row fits without overflow, and the document scroll width equals the viewport width.
- Pass 11: replaced the product page YOUR BRAND illustration with a simplified client-portal dashboard grounded in the supplied real portal screenshot. Preserved the reference hierarchy through a branded left navigation, four release-guide actions, a four-metric data overview, and a three-album preview using the existing real cover assets. Removed the reference's account-specific utility details and chat widget as requested by the simplified homepage context. Rechecked at 1440 × 1000 and 390 × 844 CSS px; all local icons and covers load, guide rows stay within their cards, the portal fits the 350 px mobile column, and the document has no horizontal overflow.
- Pass 12: vertically centered the three YOUR BRAND capability rows. Each row now has the same 64 px desktop height, with its check icon, title, and description sharing the exact row center; the mobile rows also remain equal-height with centered check icons and no horizontal overflow.
- Pass 13: replaced the CLIENT PORTAL + OPERATIONS customer-side placeholder with a compact album-list workspace derived from the supplied real portal reference. The illustration now uses the same Night Drive, After Rain, and Northern Lights covers as the homepage, plus realistic UPC, artist, label, release date, authorization, live, processing, and exception states. Rechecked the client/admin tab switch and all three local covers at the desktop viewport; reflowed filters and album rows at 390 × 844 CSS px, where the document width remains 390 px with no horizontal overflow.
- Pass 14: replaced the CLIENT PORTAL + OPERATIONS team-side placeholder with a simplified release-status view derived from the supplied 1685 × 887 px operations screenshot. Preserved its core hierarchy through an album summary, UPC and review state, three platform totals, and five DSP task rows. Spotify, Apple Music, QQ Music, NetEase Cloud Music, and YouTube Music all use the agreed local channel assets; every logo loaded successfully. Rechecked the admin tab at the 878 px desktop viewport and 390 × 844 mobile viewport: the five rows remain legible, the mobile table becomes a compact two-column list, document width equals viewport width, and browser console warnings/errors remain empty. No actionable P0/P1/P2 differences remain; reduced table density is intentional for the website illustration context.

## Follow-up polish

- P3: if future real enterprise catalog data becomes available, the fictional titles can be swapped without changing the layout.

final result: passed

---

# Design QA — 定价页订阅周期切换器（2026-10-15）

- Source visual truth: `/var/folders/c4/j08jzybj5xvfmh812c5w18p80000gp/T/codex-clipboard-f5b3f19a-9244-46d8-bd59-7d47e3d76f81.png` (522 × 146 px).
- Implementation: `http://localhost:3001/pricing`; full-view capture: `design-qa-assets/pricing-toggle-yearly-full.png` (1280 × 720 px); focused capture: `design-qa-assets/pricing-toggle-yearly-focus.png` (320 × 78 px).
- Viewport and normalization: 1280 × 720 CSS px, browser capture at 1×. The reference is an enlarged component crop, so the source and focused implementation were compared by relative proportions and state, not as pixel-identical page captures. Responsive checks used 390 × 844 and 320 × 700 CSS px.
- State: yearly selected for the saved captures; monthly selected was also checked interactively.

## Findings

- No actionable P0/P1/P2 mismatch. The longer existing annual-offer label makes the implementation wider than the reference, as expected from the requirement to preserve all copy.
- Fonts and typography: existing site font, sizes, weights, and all four labels remain unchanged and readable. The selected label uses the brand blue; the inactive label uses muted gray.
- Spacing and layout rhythm: a subtly bordered pale-gray frame contains the two choices, and the selected choice is a rounded white raised segment. The badges stay aligned with their labels at desktop and 390 px; they stack within each choice at 320 px to prevent clipping.
- Colors and tokens: the only blue accent is the existing brand token. Both badges use a pale tint of that token; the selected state no longer uses a solid-blue fill.
- Image quality and assets: the source has no imagery or external assets, so no image substitution is involved.
- Copy and content: “月付”, “3 个月起订”, “年付”, and “省约 17% · 免部署费” are unchanged. Monthly and yearly selection still update `aria-pressed` and the prices.

## Comparison evidence

- Full view: `design-qa-assets/pricing-toggle-yearly-full.png` shows the revised switch centered beneath the existing heading without changing card layout.
- Focused region: the source crop and `design-qa-assets/pricing-toggle-yearly-focus.png` were opened together in one visual comparison. Both show a pale-gray frame, inactive gray option, white elevated selected option, and blue tinted badges. The width difference follows the longer preserved annual badge text.

## Interaction and runtime checks

- Monthly and yearly buttons were both clicked; selected state and prices updated in each direction.
- Captures at 390 px and 320 px showed no cut-off switch labels.
- Browser console errors: none. Brand color validation and `git diff --check` passed.

## Comparison history

- Pass 1: after the CSS change, the rendered yearly component was compared with the reference. No actionable P0/P1/P2 differences remained; no further visual fix was needed.

## Open questions and follow-up polish

- None required for this scoped style change.

final result: passed
