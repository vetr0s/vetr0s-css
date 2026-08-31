from pathlib import Path


root = Path(__file__).parent.parent

fonts = (
    "font/et-book-roman-line-figures.woff2",
    "font/et-book-display-italic-old-style-figures.woff2",
    "font/et-book-bold-line-figures.woff2",
)

icons = (
    "favicon.ico",
    "favicon-16x16.png",
    "favicon-32x32.png",
    "apple-touch-icon.png",
    "android-chrome-192x192.png",
    "android-chrome-512x512.png",
    "site.webmanifest",
)

required = (
    "index.html",
    "css/reset.css",
    "css/style.css",
    "js/theme.js",
    "CNAME",
    "font/LICENSE-et-book.txt",
    *icons,
    *fonts,
)

missing = [path for path in required if not (root / path).is_file()]
if missing:
    raise SystemExit("missing files: " + ", ".join(missing))

style = (root / "css/style.css").read_text()
for font in fonts:
    url = f'url("/{font}")'
    if url not in style:
        raise SystemExit(f"style.css does not reference {url}")

fixture = (root / "index.html").read_text()
loaded = (
    "/css/reset.css",
    "/css/style.css",
    "/js/theme.js",
    "/favicon.ico",
    "/site.webmanifest",
)
for asset in loaded:
    if asset not in fixture:
        raise SystemExit(f"index.html does not load {asset}")

domain = "css.vetr0s.dev"
if (root / "CNAME").read_text().strip() != domain:
    raise SystemExit(f"CNAME does not hold {domain}")

print("checked standalone assets, fixture, and CNAME")
