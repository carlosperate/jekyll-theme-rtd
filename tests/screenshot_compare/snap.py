#!/usr/bin/env python3
"""
Screenshot comparison tool for jekyll-theme-rtd.

Usage:
    python tests/screenshot_compare/snap.py            # from repo root
    python tests/screenshot_compare/snap.py --no-open  # skip opening browser
    python snap.py                                      # from tests/screenshot_compare/

Steps:
  1. Builds the Docker image (docker build -t jekyll-theme-rtd .)
  2. Runs a Jekyll build inside the container to generate _site/
  3. Finds all HTML pages produced in _site/
  4. Archives any existing screenshots to tests/screenshots/old/
  5. Serves _site/ over a local HTTP server
  6. Takes a full-page screenshot of every page with Playwright
  7. Writes tests/screenshots/screenshots-data.js for compare.html

Requirements:
    pip install -r tests/requirements.txt
    playwright install chromium
"""

import argparse
import json
import shutil
import subprocess
import threading
import time
import webbrowser
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

from playwright.sync_api import sync_playwright

# ---------------------------------------------------------------------------
# Paths & config
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent.parent.resolve()
SITE_DIR = REPO_ROOT / "_site"
SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"
OLD_DIR = SCREENSHOTS_DIR / "old"
DATA_JS = SCREENSHOTS_DIR / "screenshots-data.js"

SERVER_PORT = 8765
BASE_URL = f"http://localhost:{SERVER_PORT}"
VIEWPORT = {"width": 1280, "height": 900}


# ---------------------------------------------------------------------------
# 1. Build steps
# ---------------------------------------------------------------------------

def build_docker_image():
    print("\n==> Building Docker image...")
    subprocess.run(
        ["docker", "build", "-t", "jekyll-theme-rtd", "."],
        cwd=REPO_ROOT,
        check=True,
    )


def build_jekyll_site():
    print("\n==> Building Jekyll site...")
    subprocess.run(
        [
            "docker", "run", "--rm",
            "-v", f"{REPO_ROOT}:/srv/jekyll",
            "jekyll-theme-rtd", "build",
        ],
        cwd=REPO_ROOT,
        check=True,
    )


# ---------------------------------------------------------------------------
# 2. Page discovery
# ---------------------------------------------------------------------------

def find_html_pages():
    """Return sorted URL paths for all HTML files inside _site/."""
    pages = []
    for html_file in sorted(SITE_DIR.rglob("*.html")):
        url_path = "/" + html_file.relative_to(SITE_DIR).as_posix()
        pages.append(url_path)
    return pages


def page_to_slug(url_path):
    """Convert a URL path to a safe, flat filename stem.

    /index.html                                       -> index
    /docs/dev.html                                    -> docs__dev
    /docs/demo-pages/deepersection/test-page.html     -> docs__demo-pages__deepersection__test-page
    """
    slug = url_path.lstrip("/").removesuffix(".html")
    return slug.replace("/", "__")


# ---------------------------------------------------------------------------
# 3. Archive old screenshots
# ---------------------------------------------------------------------------

def archive_old_screenshots():
    """Move existing PNGs into old/ and return True if any were found."""
    existing = list(SCREENSHOTS_DIR.glob("*.png"))
    if not existing:
        return False

    print(f"\n==> Archiving {len(existing)} old screenshot(s) -> {OLD_DIR.relative_to(REPO_ROOT)}/")
    if OLD_DIR.exists():
        shutil.rmtree(OLD_DIR)
    OLD_DIR.mkdir(parents=True)

    for png in existing:
        shutil.move(str(png), OLD_DIR / png.name)
    return True


# ---------------------------------------------------------------------------
# 4. Local HTTP server
# ---------------------------------------------------------------------------

def start_server():
    """Serve _site/ on SERVER_PORT in a background daemon thread."""
    handler = partial(SimpleHTTPRequestHandler, directory=str(SITE_DIR))
    # Suppress per-request log lines
    handler.log_message = lambda *_: None
    server = HTTPServer(("localhost", SERVER_PORT), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    time.sleep(0.5)  # give the socket time to bind
    print(f"\n==> Serving _site/ at {BASE_URL}")
    return server


# ---------------------------------------------------------------------------
# 5. Take screenshots
# ---------------------------------------------------------------------------

def take_screenshots(pages):
    """Screenshot every page with Playwright and return the list of slugs."""
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    slugs = []

    print(f"\n==> Screenshotting {len(pages)} page(s)...")
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        tab = browser.new_page(viewport=VIEWPORT)
        for url_path in pages:
            slug = page_to_slug(url_path)
            out = SCREENSHOTS_DIR / f"{slug}.png"
            print(f"    {url_path}  ->  {out.name}")
            tab.goto(f"{BASE_URL}{url_path}", wait_until="networkidle")
            tab.screenshot(path=str(out), full_page=True)
            slugs.append(slug)
        browser.close()

    return slugs


# ---------------------------------------------------------------------------
# 6. Write comparison manifest
# ---------------------------------------------------------------------------

def write_data_js(pages, slugs, has_old):
    """Write screenshots-data.js consumed by compare.html."""
    entries = []
    for url_path, slug in zip(pages, slugs):
        old_exists = has_old and (OLD_DIR / f"{slug}.png").exists()
        entries.append({"name": url_path, "slug": slug, "hasOld": old_exists})

    lines = [
        "// This file is generated by snap.py.  Do not edit.",
        "window.SCREENSHOTS = ["
    ]
    for e in entries:
        lines.append(
            f'  {{ name: {json.dumps(e["name"])}, '
            f'slug: {json.dumps(e["slug"])}, '
            f'hasOld: {"true" if e["hasOld"] else "false"} }},'
        )
    lines.append("];\n")

    DATA_JS.write_text("\n".join(lines))
    print(f"\n==> Written {DATA_JS.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Build Jekyll site and take screenshots.")
    parser.add_argument("--no-open", action="store_true", help="Skip opening compare.html in the browser")
    args = parser.parse_args()
    build_docker_image()
    build_jekyll_site()

    pages = find_html_pages()
    print(f"\n==> Found {len(pages)} HTML page(s) in _site/")

    has_old = archive_old_screenshots()
    server = start_server()

    try:
        slugs = take_screenshots(pages)
    finally:
        server.shutdown()

    write_data_js(pages, slugs, has_old)

    compare_html = Path(__file__).parent / 'compare.html'
    print(f"\n✓ Done!  Open the comparison page:")
    print(f"  {compare_html}\n")

    if not args.no_open:
        webbrowser.open(compare_html.as_uri())


if __name__ == "__main__":
    main()
