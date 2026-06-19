"""Clean VTT subtitle files into plain markdown transcripts.

This module is the single source of truth for VTT cleaning. `download_playlists.py`
imports from here rather than duplicating the logic.

Strips:
- WEBVTT header, Kind:/Language: metadata
- NOTE comment blocks
- Bare cue-identifier lines (numbers)
- Cue timing lines (00:00:00.000 --> 00:00:00.000 ...)
- Inline word-timing tags (<00:00:00.800><c>...</c>) and any HTML-ish tags
- Rolling/overlapping duplication produced by YouTube auto-subs

Output: clean, paragraph-formatted text suitable for LLM ingestion.

CLI:
    python3 vtt_to_md.py <vtt_dir> <out_dir> <playlist_name> [author]
"""

import re
import sys
from pathlib import Path

DEFAULT_AUTHOR = "Cole Medin"

_TS_LINE = re.compile(r"^\d{2}:\d{2}:\d{2}[.,]\d{3}\s+-->")
_WORD_TS = re.compile(r"<\d{2}:\d{2}:\d{2}[.,]\d{3}>")
_C_TAG = re.compile(r"</?c[^>]*>")
_ANY_TAG = re.compile(r"<[^>]+>")
_CUE_NUMBER = re.compile(r"^\d+$")
_INDEX_PREFIX = re.compile(r"^\d{2,}\s*-\s*")
_ILLEGAL_FS = re.compile(r'[<>:"/\\|?*\x00-\x1f…]')


def sanitize_filename(name: str) -> str:
    """Make a string safe for use as a filename on Windows and POSIX."""
    name = _ILLEGAL_FS.sub("", name)
    name = re.sub(r"\s+", " ", name).strip()
    # Windows disallows trailing dots/spaces
    return name.rstrip(". ")


def _yaml_escape(value: str) -> str:
    """Escape a string for use inside a double-quoted YAML scalar."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _extract_text_lines(vtt_text: str) -> list[str]:
    """Return spoken-text lines only: drop headers, NOTE blocks, cues, timings, tags."""
    out: list[str] = []
    in_note = False
    for raw in vtt_text.splitlines():
        line = raw.strip()

        # NOTE blocks run until the next blank line.
        if in_note:
            if not line:
                in_note = False
            continue
        if line.startswith("NOTE"):
            in_note = True
            continue

        if not line:
            continue
        if line == "WEBVTT" or line.startswith("WEBVTT"):
            continue
        if line.startswith(("Kind:", "Language:")):
            continue
        if _TS_LINE.match(line):
            continue
        if _CUE_NUMBER.match(line):  # bare cue identifier
            continue

        # Strip inline timing/markup tags.
        line = _WORD_TS.sub("", line)
        line = _C_TAG.sub("", line)
        line = _ANY_TAG.sub("", line)
        line = line.strip()
        if line:
            out.append(line)
    return out


def _dedupe_rolling(lines: list[str]) -> list[str]:
    """Collapse YouTube's rolling captions.

    Auto-subs repeat the previous caption plus a new word ("a", "a b", "a b c"),
    and also emit exact duplicates. Both are handled by merging each line into a
    running word list, skipping the longest leading run of words that already
    appears as the tail of what we've accumulated.
    """
    words: list[str] = []
    for line in lines:
        new = line.split()
        if not new:
            continue
        max_k = min(len(words), len(new))
        overlap = 0
        for k in range(max_k, 0, -1):
            if words[-k:] == new[:k]:
                overlap = k
                break
        words.extend(new[overlap:])
    return words


def clean_vtt(vtt_text: str) -> str:
    """Convert raw VTT text into clean, paragraph-formatted prose."""
    text_lines = _extract_text_lines(vtt_text)
    words = _dedupe_rolling(text_lines)

    text = re.sub(r"\s+", " ", " ".join(words)).strip()
    if not text:
        return ""

    # Group sentences into paragraphs (~6 sentences each).
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunk_size = 6
    paragraphs = [
        " ".join(sentences[i : i + chunk_size]).strip()
        for i in range(0, len(sentences), chunk_size)
    ]
    return "\n\n".join(p for p in paragraphs if p)


def _title_from_stem(vtt_path: Path) -> str:
    """Derive a human title: '01 - My Title.en.vtt' -> 'My Title'."""
    stem = vtt_path.stem
    if stem.endswith(".en"):
        stem = stem[:-3]
    title = _INDEX_PREFIX.sub("", stem)
    return title.replace("？", "?").strip()


def _file_stem_from_vtt(vtt_path: Path) -> str:
    """Filename stem WITH playlist index preserved: '01 - My Title.en.vtt' -> '01 - My Title'.

    Used for the markdown output filename so files sort by playlist position
    in Obsidian's file explorer. The YAML title and H1 use the index-stripped
    version from `_title_from_stem` for cleaner display.
    """
    stem = vtt_path.stem
    if stem.endswith(".en"):
        stem = stem[:-3]
    return stem.replace("？", "?").strip()


def vtt_to_markdown(
    vtt_path: Path, playlist: str, author: str = DEFAULT_AUTHOR
) -> tuple[str, str]:
    """Return (output_filename_stem, markdown_content) for a VTT file."""
    text = vtt_path.read_text(encoding="utf-8", errors="replace")
    body = clean_vtt(text)

    title = _title_from_stem(vtt_path)
    file_stem = _file_stem_from_vtt(vtt_path)
    out_stem = sanitize_filename(file_stem) or sanitize_filename(vtt_path.stem) or "untitled"

    md = (
        "---\n"
        f'title: "{_yaml_escape(title)}"\n'
        "type: transcript\n"
        "source: youtube\n"
        f'playlist: "{_yaml_escape(playlist)}"\n'
        f'author: "{_yaml_escape(author)}"\n'
        "---\n\n"
        f"# {title}\n\n"
        f"{body}\n"
    )
    return out_stem, md


def main() -> None:
    vtt_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/colemedin_vtt")
    out_dir = Path(sys.argv[2] if len(sys.argv) > 2 else "raw/03-transcripts")
    playlist = sys.argv[3] if len(sys.argv) > 3 else "Cole Medin - AI Agents Masterclass"
    author = sys.argv[4] if len(sys.argv) > 4 else DEFAULT_AUTHOR

    out_dir.mkdir(parents=True, exist_ok=True)

    vtt_files = sorted(vtt_dir.glob("*.vtt"))
    if not vtt_files:
        print(f"No .vtt files in {vtt_dir}")
        return

    print(f"Cleaning {len(vtt_files)} files -> {out_dir}")
    for vtt in vtt_files:
        out_stem, md = vtt_to_markdown(vtt, playlist, author)
        out_path = out_dir / f"{out_stem}.md"
        out_path.write_text(md, encoding="utf-8")
        size_kb = out_path.stat().st_size / 1024
        print(f"  {out_path.name}  ({size_kb:.1f} KB)")

    print(f"\nDone. {len(vtt_files)} markdown files in {out_dir}")


if __name__ == "__main__":
    main()
