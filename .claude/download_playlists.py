"""Batch download YouTube playlist subtitles, save the VTTs, clean to markdown.

Usage:
    python3 download_playlists.py <author> [cookies_path]

For each playlist in PLAYLISTS:
  1. Download English auto-subs as VTT into  raw/05-vtts/<author>/<playlist>/
     (these are the immutable source files and are kept).
  2. Clean each VTT to markdown into        raw/03-transcripts/<author>/<playlist>/

Cleaning logic lives in vtt_to_md.py (imported, not duplicated).
"""

import os
import subprocess
import sys
from pathlib import Path

# Import the shared cleaning/conversion logic (same directory).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from vtt_to_md import sanitize_filename, vtt_to_markdown  # noqa: E402

# Cole Medin's playlists.
PLAYLISTS = {
    "AI Agents Masterclass": "PLyrg3m7Ei-MpsdEA6eKN1k2gJpuhllNTi",
    "n8n RAG Template": "PLyrg3m7Ei-Mo1t_H9KHoeqXkg0pnfkX-S",
    "Archon - The AI Agent Builder": "PLyrg3m7Ei-Mr_FkLdJFx2DCnEOiek4yqa",
    "Guide to Building AI Agents": "PLyrg3m7Ei-MrSXWv90oXXbuSsbdOP9j2n",
    "bolt.diy": "PLyrg3m7Ei-MpOPKdenkQNcx8ueI36RNrA",
    "AI Platform Showcases": "PLyrg3m7Ei-MoBc8dipiPpoiRleGKMquoJ",
    "LangChain": "PLyrg3m7Ei-MpiX11VkL5NzH4cDoRtuxno",
    "No Code AI with n8n": "PLyrg3m7Ei-MrYaMyxC_vZ0x-OUdTQN6RS",
    "Local AI (LLMs, RAG, more)": "PLyrg3m7Ei-MqNM-au_lfjzTsuVVTTx0ke",
}

VAULT_ROOT = Path(__file__).resolve().parent.parent  # .claude/ -> vault root


def download_and_clean(
    author: str, playlist_name: str, playlist_id: str, cookies_path: str | None
) -> int:
    """Download a playlist's VTTs (kept) and clean them to markdown."""
    a_safe = sanitize_filename(author)
    p_safe = sanitize_filename(playlist_name)
    vtt_dir = VAULT_ROOT / "raw" / "05-vtts" / a_safe / p_safe
    md_dir = VAULT_ROOT / "raw" / "03-transcripts" / a_safe / p_safe

    if md_dir.exists() and any(md_dir.glob("*.md")):
        existing = len(list(md_dir.glob("*.md")))
        print(f"  [skip] {playlist_name}: already has {existing} md files")
        return 0

    vtt_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--write-auto-sub",
        "--sub-lang", "en",
        "--skip-download",
        "--sub-format", "vtt",
        "--ignore-errors",
        # android_vr player bypasses the n-challenge (no JS decoding needed).
        "--extractor-args", "youtube:player_client=android_vr,web_safari",
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

    for vtt in vtt_files:
        out_stem, md = vtt_to_markdown(vtt, playlist_name, author)
        (md_dir / f"{out_stem}.md").write_text(md, encoding="utf-8")

    print(
        f"  -> {len(vtt_files)} VTTs in {vtt_dir.relative_to(VAULT_ROOT)}, "
        f"md in {md_dir.relative_to(VAULT_ROOT)}"
    )
    return len(vtt_files)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 download_playlists.py <author> [cookies_path]")
        print("       (cookies_path is optional; omit to download without auth)")
        sys.exit(1)
    author = sys.argv[1]
    cookies_path = sys.argv[2] if len(sys.argv) > 2 else None

    if cookies_path and not Path(cookies_path).exists():
        print(f"Cookies file not found: {cookies_path}")
        sys.exit(1)

    print(f"Author: {author}")
    print(f"Cookies: {cookies_path or '(none - public access)'}")
    print(f"Vault: {VAULT_ROOT}")
    print(f"Playlists: {len(PLAYLISTS)}\n")

    total = 0
    for i, (name, plid) in enumerate(PLAYLISTS.items(), 1):
        print(f"[{i}/{len(PLAYLISTS)}] {name}")
        total += download_and_clean(author, name, plid, cookies_path)
        print()

    print(f"Done. {total} new transcripts downloaded.")


if __name__ == "__main__":
    main()
