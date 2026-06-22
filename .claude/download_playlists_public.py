"""Batch download YouTube playlist subtitles (public / no-cookie path).

Uses the android_vr player client, which bypasses the n-challenge and PO-token
requirements without cookies or a JS runtime -- but cannot use cookies. For
private/members-only videos, use download_playlists_auth.py instead.

Usage:
    python3 download_playlists_public.py <author>

For each playlist in PLAYLISTS:
  1. Download English auto-subs as VTT into  raw/05-vtts/<author>/<playlist>/
     (these are the immutable source files and are kept).
  2. Clean each VTT to markdown into        raw/03-transcripts/<author>/<playlist>/

Cleaning logic lives in vtt_to_md.py (imported, not duplicated). The shared
download_and_clean()/PLAYLISTS/run() machinery here is reused by the authed
variant (download_playlists_auth.py); only the yt-dlp client flags differ.
"""

import os
import subprocess
import sys
from pathlib import Path

# Import the shared cleaning/conversion logic (same directory).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from vtt_to_md import sanitize_filename, vtt_to_markdown  # noqa: E402

# @claude channel playlists.
PLAYLISTS = {
    "Code with Claude 2026 - Japan": "PLmWCw1CzcFinrtcyN6EMIp6KqrDj8sxD7",
    "The Problem Solvers": "PLmWCw1CzcFikJTGCza0osIfmN9jAyH_5X",
    "Code with Claude 2026 - London Day 2": "PLmWCw1CzcFinm44PAkEoR2glf-iNPhulP",
    "Code with Claude 2026 - London": "PLmWCw1CzcFilPJdvw6scjHjbBripZWFps",
    "How Anthropic uses Claude Cowork": "PLmWCw1CzcFikMO-6XqFrhO0GE_OOwmHsv",
    "Code with Claude 2026 - San Francisco": "PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR",
    "How teams use Claude": "PLmWCw1CzcFimZNJTcPVEzACE9Vj2KjUal",
    "Claude Code 101": "PLmWCw1CzcFilebjK89WLb5cAvM8K0cLB3",
    "Claude Code subagents": "PLmWCw1CzcFilWIFAY4hapAgFtGB7UlvVQ",
    "Claude Code Skills": "PLmWCw1CzcFim_hkruZSlABOUOAAQ5JMyo",
    "Product Launches": "PLmWCw1CzcFilOIgUYuMIJ2iZMo09Ho0va",
    "How Anthropic uses Claude": "PLmWCw1CzcFinE9w1AEkweLcGasG_IRiyW",
}

# Public-path client flags: android_vr bypasses the n-challenge without cookies
# or a JS runtime. The authed variant swaps these out (see download_playlists_auth.py).
PUBLIC_CLIENT_ARGS = [
    "--extractor-args", "youtube:player_client=android_vr,web_safari",
]

VAULT_ROOT = Path(__file__).resolve().parent.parent  # .claude/ -> vault root


def download_and_clean(
    author: str,
    playlist_name: str,
    playlist_id: str,
    client_args: list[str],
    cookies_path: str | None = None,
    skip_if_done: bool = True,
) -> int:
    """Download a playlist's VTTs (kept) and clean them to markdown.

    `client_args` are the per-variant yt-dlp client flags (android_vr for public,
    web + node for authed). `skip_if_done` short-circuits when the md dir already
    has files -- the authed path disables this so it can backfill newly-granted
    private videos into an already-processed playlist.
    """
    a_safe = sanitize_filename(author)
    p_safe = sanitize_filename(playlist_name)
    vtt_dir = VAULT_ROOT / "raw" / "05-vtts" / a_safe / p_safe
    md_dir = VAULT_ROOT / "raw" / "03-transcripts" / a_safe / p_safe

    if skip_if_done and md_dir.exists() and any(md_dir.glob("*.md")):
        existing = len(list(md_dir.glob("*.md")))
        print(f"  [skip] {playlist_name}: already has {existing} md files")
        return 0

    vtt_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)

    before = {p.name for p in vtt_dir.glob("*.vtt")}

    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--write-auto-sub",
        "--sub-lang", "en",
        "--skip-download",
        "--sub-format", "vtt",
        "--ignore-errors",
        # Rate-limit safety margin: pace metadata requests and subtitle fetches.
        "--sleep-requests", "1.5",
        "--sleep-subtitles", "2",
        *client_args,
        "-o", os.path.join(str(vtt_dir), "%(playlist_index)02d - %(title)s.%(ext)s"),
    ]
    if cookies_path:
        cmd.extend(["--cookies", cookies_path])
    cmd.append(f"https://www.youtube.com/playlist?list={playlist_id}")

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        err_tail = result.stderr.strip().splitlines()[-5:]
        print(f"  [warn] yt-dlp returned {result.returncode}: {'; '.join(err_tail)}")

    vtt_files = sorted(vtt_dir.glob("*.vtt"))
    if not vtt_files:
        print(f"  [error] No VTTs downloaded for {playlist_name}")
        return 0

    new_vtts = [v for v in vtt_files if v.name not in before]
    for vtt in vtt_files:
        out_stem, md = vtt_to_markdown(vtt, playlist_name, author)
        (md_dir / f"{out_stem}.md").write_text(md, encoding="utf-8")

    print(
        f"  -> {len(vtt_files)} VTTs ({len(new_vtts)} new) in "
        f"{vtt_dir.relative_to(VAULT_ROOT)}, md in {md_dir.relative_to(VAULT_ROOT)}"
    )
    return len(new_vtts)


def run(
    author: str,
    *,
    client_args: list[str],
    cookies_path: str | None = None,
    skip_if_done: bool = True,
    name_filter: str | None = None,
) -> int:
    """Iterate PLAYLISTS, downloading + cleaning each. Returns new transcript count."""
    items = [
        (n, p) for n, p in PLAYLISTS.items()
        if not name_filter or name_filter.lower() in n.lower()
    ]
    if not items:
        print(f"No playlist matches filter {name_filter!r}.")
        return 0

    print(f"Author: {author}")
    print(f"Cookies: {cookies_path or '(none - public access)'}")
    print(f"Vault: {VAULT_ROOT}")
    print(f"Playlists: {len(items)}" + (f" (filter: {name_filter!r})" if name_filter else "") + "\n")

    total = 0
    for i, (name, plid) in enumerate(items, 1):
        print(f"[{i}/{len(items)}] {name}")
        total += download_and_clean(
            author, name, plid, client_args,
            cookies_path=cookies_path, skip_if_done=skip_if_done,
        )
        print()

    print(f"Done. {total} new transcripts downloaded.")
    return total


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 download_playlists_public.py <author>")
        sys.exit(1)
    run(sys.argv[1], client_args=PUBLIC_CLIENT_ARGS, skip_if_done=True)


if __name__ == "__main__":
    main()
