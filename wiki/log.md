# Operation Log

Append-only chronological record of all wiki operations.

Format: `## [YYYY-MM-DD] <action> | <one-line summary>`

Grep-friendly: `grep "^## \[" log.md | tail -10` to see recent operations.

---

## [2026-07-11] ingest | Batch ingested all 43 Lenny's Podcast transcripts (episodes 02-44)
- **Summary**: All 43 transcripts from `raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/` processed
- **Created**: 43 source summaries in `wiki/sources/03-transcripts/Lenny's Podcast/Lenny's Podcast/`
- **Created**: 524 entity pages in `wiki/entities/`
- **Created**: 483 concept pages in `wiki/concepts/`
- **Updated**: [[index.md]]
- **Method**: Parallel workers + direct processing
- **Conflicts**: none

## [2026-07-11] lint | Fixed 87 dead links, rebuilt index, created 4 missing entity pages
- **Changes**: Rebuilt `index.md` (registered all 1,050 pages, removed 13 stale entries)
- **Fixed**: 87 dead wikilinks corrected (Agent Soul / Identity -> Agent Soul - Identity, typo fixes, summary-34/36 link corrections)
- **Created**: [[Square]], [[PayPal]], [[Khosla Ventures]], [[Fair]] entity pages
- **Remaining**: 105 dead links (mostly minor entities), 127 orphans (expected for fresh corpus)
- **Updated**: [[index.md]]
- **Method**: Parallel workers for episodes 44-25, direct processing for episodes 24-02
- **Conflicts**: none
