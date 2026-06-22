"""Batch download YouTube playlist subtitles (authenticated / cookie path).

Uses the cookie-aware `web` player client plus a Node JS runtime to solve the
n-challenge. Unlike download_playlists_public.py (android_vr, which silently
ignores cookies), this path actually authenticates -- required for private or
members-only videos that appear in a playlist as placeholders.

It reuses the shared PLAYLISTS/run() machinery from download_playlists_public.py;
only the yt-dlp client flags differ, and skip-if-done is disabled so an
already-processed playlist is re-scanned to backfill newly-accessible videos.

Requirements:
  - A cookies.txt exported while logged into an account *granted access* to the
    target video. A valid cookie alone is not enough -- the account must be on
    the video's allow-list.
  - Node.js on PATH (yt-dlp's JS runtime for the n-challenge).

Usage:
    python3 download_playlists_auth.py <author> <cookies_path> [playlist_name_filter]

    playlist_name_filter (optional): case-insensitive substring; limits the run
    to matching playlists (e.g. "How Anthropic uses Claude") so you don't
    re-download all 12 just to grab one private video.
"""

import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from download_playlists_public import run  # noqa: E402

# Authed client flags: web client honors cookies; node solves the n-challenge.
AUTH_CLIENT_ARGS = [
    "--js-runtimes", "node",
    "--extractor-args", "youtube:player_client=web,web_safari",
]


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python3 download_playlists_auth.py <author> <cookies_path> [playlist_name_filter]")
        sys.exit(1)
    author = sys.argv[1]
    cookies_path = sys.argv[2]
    name_filter = sys.argv[3] if len(sys.argv) > 3 else None

    if not Path(cookies_path).exists():
        print(f"Cookies file not found: {cookies_path}")
        sys.exit(1)
    if shutil.which("node") is None:
        print(
            "Node.js not found on PATH. yt-dlp needs a JS runtime to solve the "
            "n-challenge on the authed path.\n"
            "  - Install Node, or ensure your nvm/node bin dir is on PATH, then retry."
        )
        sys.exit(1)

    run(
        author,
        client_args=AUTH_CLIENT_ARGS,
        cookies_path=cookies_path,
        skip_if_done=False,  # backfill newly-granted private videos
        name_filter=name_filter,
    )


if __name__ == "__main__":
    main()
