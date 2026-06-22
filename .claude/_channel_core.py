"""Shared core for the channel subtitle downloaders.

Both download_channel_authed.py (cookies + Node JS runtime) and
download_channel_public.py (no cookies, android_vr client) use the same
per-video pipeline; only the yt-dlp client config differs. That common
machinery lives here:

  - flat-enumerate a channel /videos feed (newest first),
  - skip already-done videos via a self-managed .processed_ids.txt archive
    (yt-dlp's --download-archive is NOT written for subtitle-only runs),
  - bound by a date floor: since the feed is newest-first, once a video older
    than the cutoff is reached, it and every remaining older video are retired
    without download (keeps the ancient backlog out, pulls only new uploads),
  - download en auto-subs as VTT, then clean each to markdown.
"""

import re
import time
from pathlib import Path

import yt_dlp

VAULT_ROOT = Path(__file__).resolve().parent.parent
FOLDER_NAME = "Channel Only"
SLEEP_BETWEEN = 2  # seconds between per-video requests

_DATE_PREFIX = re.compile(r"^(\d{8}) - ")


def enumerate_channel(channel_url: str) -> list[tuple[str, str]]:
    """Return (video_id, watch_url) for every video in a channel feed (flat)."""
    with yt_dlp.YoutubeDL({"extract_flat": True, "quiet": True}) as ydl:
        info = ydl.extract_info(channel_url, download=False)
    return [
        (e["id"], e["url"])
        for e in info.get("entries", [])
        if e.get("id") and e.get("url")
    ]


def load_processed(path: Path) -> set[str]:
    """Read the self-managed archive of already-downloaded video IDs."""
    if not path.exists():
        return set()
    return {ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()}


def latest_existing_date(vtt_dir: Path) -> int:
    """Newest upload_date (YYYYMMDD int) among existing VTTs; 0 if none.

    VTT filenames are '%(upload_date)s - %(title)s.en.vtt', so the date is the
    8-digit prefix. Used as the cutoff so only newer videos are fetched.
    """
    dates = [
        int(m.group(1))
        for vtt in vtt_dir.glob("*.vtt")
        if (m := _DATE_PREFIX.match(vtt.name))
    ]
    return max(dates) if dates else 0


def run(
    author: str,
    channel_url: str,
    *,
    client_opts: dict,
    cookies_path: str | None = None,
    min_date: int = 0,
) -> int:
    """Download a channel's new en subtitles and clean them to markdown.

    `client_opts` carries the per-variant yt-dlp config (e.g. js_runtimes for
    the authed client, or extractor_args for the public android_vr client).
    `min_date` (YYYYMMDD) is a hard floor; if 0, the cutoff is the newest
    upload_date already on disk. Returns the number of new videos downloaded.
    """
    # Local import keeps the core importable even if run from another cwd.
    from vtt_to_md import sanitize_filename, vtt_to_markdown

    a_safe = sanitize_filename(author)
    p_safe = sanitize_filename(FOLDER_NAME)
    vtt_dir = VAULT_ROOT / "raw" / "05-vtts" / a_safe / p_safe
    md_dir = VAULT_ROOT / "raw" / "03-transcripts" / a_safe / p_safe
    vtt_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)
    archive = vtt_dir / ".processed_ids.txt"

    cutoff = min_date or latest_existing_date(vtt_dir)
    print(f"Enumerating {channel_url} ...")
    videos = enumerate_channel(channel_url)  # newest first
    processed = load_processed(archive)
    print(
        f"  -> {len(videos)} in feed, {len(processed)} already done, "
        f"cutoff date {cutoff or '(none)'}"
    )

    opts = {
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en"],
        "subtitlesformat": "vtt",
        "skip_download": True,
        "ignoreerrors": True,
        "quiet": True,
        "no_warnings": True,
        "outtmpl": str(vtt_dir / "%(upload_date)s - %(title)s.%(ext)s"),
        "writedescription": False,
        "writeinfojson": False,
        "writethumbnail": False,
        **client_opts,
    }
    if cookies_path:
        opts["cookiefile"] = cookies_path

    def record(vids: list[str]) -> None:
        if vids:
            with archive.open("a", encoding="utf-8") as f:
                f.write("".join(f"{v}\n" for v in vids))

    new = 0
    with yt_dlp.YoutubeDL(opts) as ydl:
        for idx, (vid, url) in enumerate(videos):
            if vid in processed:
                continue
            info = ydl.extract_info(url, download=False)
            udate = (info or {}).get("upload_date")
            if cutoff and udate and int(udate) < cutoff:
                # Newest-first: this and all remaining are older -> retire & stop.
                older = [v for v, _ in videos[idx:] if v not in processed]
                record(older)
                print(f"  reached cutoff at {udate}; retired {len(older)} older video(s)")
                break
            try:
                ret = ydl.download([url])
            except Exception as e:  # noqa: BLE001
                print(f"  [warn] {e}")
                ret = 1
            if ret == 0:
                record([vid])
                new += 1
                print(f"  [{new}] {udate} {url}")
            time.sleep(SLEEP_BETWEEN)
    print(f"Downloaded {new} new video(s).")

    vtt_files = sorted(vtt_dir.glob("*.vtt"))
    print(f"\nCleaning {len(vtt_files)} VTTs to markdown...")
    n = 0
    for vtt in vtt_files:
        stem, md = vtt_to_markdown(vtt, FOLDER_NAME, author)
        out = md_dir / f"{stem}.md"
        if not out.exists():
            out.write_text(md, encoding="utf-8")
            n += 1
    print(f"-> {len(vtt_files)} VTTs, {n} new md in {md_dir.relative_to(VAULT_ROOT)}")
    return new
