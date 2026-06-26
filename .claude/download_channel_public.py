"""Download a YouTube channel's English subtitles (public / no-cookie path).

Uses the android_vr player client, which bypasses the n-challenge and PO-token
requirements without cookies or a JS runtime — but cannot use cookies. Per-video
iteration with a fixed delay keeps it under YouTube's rate limit. The shared core
handles the self-managed ID archive and date-floored incremental fetch, identical
to download_channel_authed.py; only the client config differs.

Usage:
    python3 download_channel_public.py <author> <channel_url>
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _channel_core as core  # noqa: E402

# Optional hard floor (YYYYMMDD). If 0, the cutoff is derived from the newest
# upload_date already on disk. Set this to backfill from a fixed date.
MIN_DATE = 20260101

# android_vr bypasses the n-challenge/PO-token; no cookies, no JS runtime needed.
CLIENT_OPTS = {
    "extractor_args": {"youtube": {"player_client": ["android_vr", "web_safari"]}},
}


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python3 download_channel_public.py <author> <channel_url>")
        sys.exit(1)
    author, channel_url = sys.argv[1], sys.argv[2]
    core.run(author, channel_url, client_opts=CLIENT_OPTS, min_date=MIN_DATE)


if __name__ == "__main__":
    main()
