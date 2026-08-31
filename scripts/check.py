from pathlib import Path


root = Path(__file__).parent.parent
required = (
    "index.html",
    "css/reset.css",
    "css/style.css",
    "font/et-book-roman-line-figures.woff2",
    "font/et-book-display-italic-old-style-figures.woff2",
    "font/et-book-bold-line-figures.woff2",
    "font/LICENSE-et-book.txt",
    "js/theme.js",
)

missing = [path for path in required if not (root / path).is_file()]
if missing:
    raise SystemExit("missing files: " + ", ".join(missing))

style = (root / "css/style.css").read_text()
for font in required[3:6]:
    url = f'url("/{font}")'
    if url not in style:
        raise SystemExit(f"style.css does not reference {url}")

fixture = (root / "index.html").read_text()
for asset in ("/css/reset.css", "/css/style.css", "/js/theme.js"):
    if asset not in fixture:
        raise SystemExit(f"index.html does not load {asset}")

print("checked standalone assets and fixture")
