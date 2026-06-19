"""Download channel-feed transcripts that aren't in any known playlist.

For a YouTube channel with both playlist-organized videos and standalone
uploads, this fetches just the standalone ones — the videos appearing in
the channel's /videos feed but not in any known playlist.

Usage:
    python3 download_channel_extras.py <author> <channel_url> [cookies_path]

Reuses the PLAYLISTS dict from download_playlists.py to know what's already
covered. Downloads VTTs to raw/05-vtts/<author>/Channel Only/ and clean
markdown to raw/03-transcripts/<author>/Channel Only/.
"""

import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vtt_to_md import sanitize_filename, vtt_to_markdown  # noqa: E402
from download_playlists import PLAYLISTS  # noqa: E402

VAULT_ROOT = Path(__file__).resolve().parent.parent
FOLDER_NAME = "Channel Only"


def enumerate_playlist_ids(playlist_id: str) -> list[str]:
    """Return all video IDs in a playlist (no metadata download)."""
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--flat-playlist",
        "--print", "id",
        f"https://www.youtube.com/playlist?list={playlist_id}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def build_seed_archive(playlists: dict[str, str], archive_path: Path) -> int:
    """Write a yt-dlp --download-archive file seeded with all playlist video IDs.

    Format per line: 'youtube <video_id>'. yt-dlp will skip any video whose
    'youtube <id>' line already exists in this file.
    """
    seen: set[str] = set()
    for name, plid in playlists.items():
        ids = enumerate_playlist_ids(plid)
        seen.update(ids)
        print(f"  {name}: {len(ids)} videos")
    archive_path.write_text(
        "\n".join(f"youtube {vid}" for vid in sorted(seen)) + "\n",
        encoding="utf-8",
    )
    return len(seen)


def download_channel_extras(
    author: str, channel_url: str, cookies_path: str | None
) -> int:
    """Download VTTs for channel videos not in any known playlist; clean to MD."""
    a_safe = sanitize_filename(author)
    p_safe = sanitize_filename(FOLDER_NAME)
    vtt_dir = VAULT_ROOT / "raw" / "05-vtts" / a_safe / p_safe
    md_dir = VAULT_ROOT / "raw" / "03-transcripts" / a_safe / p_safe

    if md_dir.exists() and any(md_dir.glob("*.md")):
        existing = len(list(md_dir.glob("*.md")))
        print(f"\n[skip] {FOLDER_NAME}: already has {existing} md files")
        return 0

    vtt_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)

    archive = vtt_dir / ".download_archive.txt"
    print("\nSeeding download archive from known playlists:")
    seed_count = build_seed_archive(PLAYLISTS, archive)
    print(f"  -> {seed_count} unique video IDs in archive")

    # NB: no playlist_index for channel feeds — use upload_date for ordering.
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--write-auto-sub",
        "--sub-lang", "en",
        "--skip-download",
        "--sub-format", "vtt",
        "--ignore-errors",
        "--download-archive", str(archive),
        "--extractor-args", "youtube:player_client=android_vr,web_safari",
        "-o", os.path.join(str(vtt_dir), "%(upload_date)s - %(title)s.%(ext)s"),
    ]
    if cookies_path:
        cmd.extend(["--cookies", cookies_path])
    cmd.append(channel_url)

    print(f"\nDownloading channel extras to {vtt_dir.relative_to(VAULT_ROOT)}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        err_tail = result.stderr.strip().splitlines()[-5:]
        print(f"[warn] yt-dlp returned {result.returncode}: {'; '.join(err_tail)}")

    vtt_files = sorted(vtt_dir.glob("*.vtt"))
    if not vtt_files:
        print(f"[note] No new VTTs — channel may be fully covered by playlists.")
        return 0

    print(f"\nCleaning {len(vtt_files)} VTTs to markdown...")
    for vtt in vtt_files:
        out_stem, md = vtt_to_markdown(vtt, FOLDER_NAME, author)
        (md_dir / f"{out_stem}.md").write_text(md, encoding="utf-8")
    print(f"-> {len(vtt_files)} files in {md_dir.relative_to(VAULT_ROOT)}")
    return len(vtt_files)


def main() -> None:
    if len(sys.argv) < 3:
        print(
            "Usage: python3 download_channel_extras.py "
            "<author> <channel_url> [cookies_path]"
        )
        sys.exit(1)

    author = sys.argv[1]
    channel_url = sys.argv[2]
    cookies_path = sys.argv[3] if len(sys.argv) > 3 else None

    if cookies_path and not Path(cookies_path).exists():
        print(f"Cookies file not found: {cookies_path}")
        sys.exit(1)

    print(f"Author:      {author}")
    print(f"Channel URL: {channel_url}")
    print(f"Cookies:     {cookies_path or '(none — public access)'}")
    print(f"Vault:       {VAULT_ROOT}")
    print(f"Known playlists to dedup against: {len(PLAYLISTS)}")

    n = download_channel_extras(author, channel_url, cookies_path)
    print(f"\nDone. {n} new transcript(s) downloaded.")


if __name__ == "__main__":
    main()
