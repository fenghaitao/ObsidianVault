"""Download a YouTube channel's English subtitles (authenticated path).

Uses yt-dlp's default client with cookies and a Node JS runtime to solve the
n-challenge. Per-video iteration spaces requests; the shared core handles the
self-managed ID archive and date-floored incremental fetch. Unlike
download_channel_public.py, this can use cookies (the android_vr client there
cannot) at the cost of needing a JS runtime.

Usage:
    python3 download_channel_authed.py <author> <channel_url> [cookies_path]
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _channel_core as core  # noqa: E402

# Optional hard floor (YYYYMMDD). If 0, the cutoff is derived from the newest
# upload_date already on disk. Set this to backfill from a fixed date.
MIN_DATE = 0

# Default client: cookies are wired in by core; Node solves the n-challenge.
CLIENT_OPTS = {"js_runtimes": {"node": {}}}


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python3 download_channel_authed.py <author> <channel_url> [cookies_path]")
        sys.exit(1)
    author, channel_url = sys.argv[1], sys.argv[2]
    cookies_path = sys.argv[3] if len(sys.argv) > 3 else None
    if cookies_path and not Path(cookies_path).exists():
        print(f"Cookies file not found: {cookies_path}")
        sys.exit(1)
    core.run(
        author, channel_url,
        client_opts=CLIENT_OPTS, cookies_path=cookies_path, min_date=MIN_DATE,
    )


if __name__ == "__main__":
    main()
