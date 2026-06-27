"""Download the Anthropic Claude blog (claude.com/blog) into raw/01-articles/claude.

The blog is server-rendered static HTML — no JS runtime needed. The landing page
only lists ~23 recent posts, but sitemap.xml exposes the full historical set, so
that is the enumeration source. Each post carries a JSON-LD (application/ld+json)
block with clean metadata (headline, description, dates); the body is extracted
from the page HTML with trafilatura and written as markdown.

Incremental by design: a self-managed .processed_urls.txt archive in the target
dir records done URLs (same dedup philosophy as the YouTube downloaders'
.processed_ids.txt), so re-runs only fetch new posts.

Usage:
    python3 download_blog.py [--limit N]
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

import trafilatura

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vtt_to_md import sanitize_filename  # noqa: E402

VAULT_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = VAULT_ROOT / "raw" / "01-articles" / "claude"
SITEMAP_URL = "https://claude.com/sitemap.xml"
USER_AGENT = "Mozilla/5.0 (compatible; LLMWikiBot/1.0)"
SLEEP_BETWEEN = 2  # seconds between per-post requests
AUTHOR = "Anthropic"

_LD_JSON = re.compile(
    r'<script type="application/ld\+json">(.*?)</script>', re.S
)
_TITLE_TAG = re.compile(r"<title>(.*?)</title>", re.S)
_LOC = re.compile(r"<loc>(https://claude\.com/blog/[^<]+)</loc>")


def fetch(url: str, *, retries: int = 3) -> str:
    """GET a URL as text, retrying transient errors with linear backoff."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8", "replace")
        except (urllib.error.URLError, TimeoutError) as e:  # noqa: PERF203
            last = e
            if attempt < retries:
                time.sleep(2 * attempt)
    raise last  # type: ignore[misc]


def enumerate_posts() -> list[str]:
    """Return every unique /blog/ post URL from the sitemap, sorted."""
    sitemap = fetch(SITEMAP_URL)
    return sorted(set(_LOC.findall(sitemap)))


def load_processed(path: Path) -> set[str]:
    """Read the self-managed archive of already-downloaded post URLs."""
    if not path.exists():
        return set()
    return {ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()}


def parse_metadata(html: str) -> dict:
    """Pull headline/description/dates from the post's JSON-LD block.

    Falls back to the <title> tag for the headline if JSON-LD is missing.
    """
    meta: dict = {}
    m = _LD_JSON.search(html)
    if m:
        try:
            data = json.loads(m.group(1))
            if isinstance(data, list):  # some pages wrap LD-JSON in an array
                data = next((d for d in data if isinstance(d, dict)), {})
            if isinstance(data, dict):
                meta = data
        except json.JSONDecodeError:
            pass
    if not meta.get("headline"):
        t = _TITLE_TAG.search(html)
        if t:
            # "<headline> | Claude by Anthropic" -> "<headline>"
            meta["headline"] = re.sub(r"\s*\|\s*Claude by Anthropic\s*$", "", t.group(1)).strip()
    return meta


def to_iso(date_str: str | None) -> str:
    """Best-effort parse of the JSON-LD date ('Jun 18, 2026') to ISO YYYY-MM-DD."""
    if not date_str:
        return ""
    for fmt in ("%b %d, %Y", "%B %d, %Y", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return ""


def _yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def clean_body(md: str) -> str:
    """Drop the duplicated subtitle line trafilatura emits twice on these posts."""
    lines = md.splitlines()
    out: list[str] = []
    for line in lines:
        if out and line.strip() and line == out[-1]:
            continue  # collapse an immediately-repeated line
        out.append(line)
    return "\n".join(out).strip()


def build_markdown(url: str, html: str) -> tuple[str, str]:
    """Return (filename_stem, markdown) for a blog post page."""
    meta = parse_metadata(html)
    headline = (meta.get("headline") or "").strip() or url.rstrip("/").rsplit("/", 1)[-1]
    description = (meta.get("description") or "").strip()
    published = to_iso(meta.get("datePublished"))
    modified = to_iso(meta.get("dateModified"))

    body = trafilatura.extract(
        html, output_format="markdown", include_links=True, include_images=True,
        with_metadata=False, favor_precision=True,
    ) or ""
    body = clean_body(body)

    fm = ["---", f'title: "{_yaml_escape(headline)}"', "type: article", f"source: {url}"]
    if description:
        fm.append(f'description: "{_yaml_escape(description)}"')
    fm.append(f'author: "{AUTHOR}"')
    if published:
        fm.append(f"published: {published}")
    if modified:
        fm.append(f"last_modified: {modified}")
    fm.append("---")

    md = "\n".join(fm) + "\n\n" + body + "\n"

    prefix = f"{published} - " if published else ""
    stem = sanitize_filename(f"{prefix}{headline}") or sanitize_filename(headline) or "untitled"
    return stem, md


def main() -> None:
    ap = argparse.ArgumentParser(description="Download the Claude blog into raw/01-articles/claude.")
    ap.add_argument("--limit", type=int, default=0, help="max new posts to fetch (0 = all)")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    archive = OUT_DIR / ".processed_urls.txt"

    print(f"Enumerating {SITEMAP_URL} ...")
    posts = enumerate_posts()
    processed = load_processed(archive)
    todo = [u for u in posts if u not in processed]
    print(f"  -> {len(posts)} posts in sitemap, {len(processed)} already done, {len(todo)} new")
    if args.limit:
        todo = todo[: args.limit]
        print(f"  (limited to {len(todo)})")

    new = 0
    with archive.open("a", encoding="utf-8") as arc:
        for i, url in enumerate(todo, 1):
            try:
                html = fetch(url)
                stem, md = build_markdown(url, html)
                out = OUT_DIR / f"{stem}.md"
                out.write_text(md, encoding="utf-8")
                arc.write(f"{url}\n")
                arc.flush()
                new += 1
                print(f"  [{new}/{len(todo)}] {out.name}")
            except Exception as e:  # noqa: BLE001
                print(f"  [warn] {url}: {e}")
            if i < len(todo):
                time.sleep(SLEEP_BETWEEN)

    print(f"\nDownloaded {new} new post(s) into {OUT_DIR.relative_to(VAULT_ROOT)}")


if __name__ == "__main__":
    main()
