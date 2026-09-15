---
title: "Miles"
type: entity
tags: [tool, file-search, Meta, index]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin.md"]
last_updated: 2026-09-14
---

## Definition

Miles ("my files") is the fuzzy file-search index Michael Bolin built with Hanson Wong at Meta to serve the Eden virtual file system, providing fast fuzzy camelCase file matching over a million files.

## Key Information

- Indexed file names (not contents) from every commit on trunk via a cron-like job, tracking which files were added or removed at each commit.
- Represented files seen over time with a 64-bit character mask (26 lowercase, 26 uppercase, 10 digits, and a few symbols), letting it exclude files quickly before matching.
- Used parallel arrays packed for cache-efficient linear reads, partitionable for parallelism.
- Achieved fuzzy matching over a million files in roughly 10–20 ms — faster than Xcode or VS Code's out-of-the-box file search.
- Exposed as an internal thrift service; by the time Bolin left, ~30 servers were running the index for uses well beyond personal file search.

## Related

- [[summary-20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin]] — source summary
- [[Michael Bolin]] — who built Miles
- [[Hanson Wong]] — who contributed the index-maintenance ideas
- [[Eden]] — the virtual file system Miles was built to serve
- [[Monorepo]] — the problem Miles helps navigate
