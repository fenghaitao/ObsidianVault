---
title: "Monorepo"
type: concept
tags: [engineering, version-control, infrastructure, Meta]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin.md"]
last_updated: 2026-09-14
---

## Definition

Monorepo is the practice of putting all a company's code in one repository. Its scaling problem — the repo keeps growing — is what prompted Meta's Eden virtual file system and Miles file-search index.

## Key Information

- "If you have bought into the monorepo philosophy, put all the code in one repo" — most work needs only a subset of the files at any time.
- The naive approach materializes every file on disk on every clone/update, which grows proportionally with repo size and eventually makes developers "very sad."
- The virtual file system (Eden) answers this by fetching file contents on demand, but only works if the toolchain is redesigned to be VFS-aware (tools that "just read everything" undo the benefit).
- Miles solved file search within the monorepo by indexing file names (not contents) per commit and supporting fuzzy camelCase matching.
- Facebook always had "the biggest app" and hit these scaling limits before everyone else, solving problems no one had solved before.

## Related

- [[summary-20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin]] — source summary
- [[Michael Bolin]] — who worked on the VFS and search
- [[Eden]] — the virtual file system for the monorepo
- [[Miles]] — the file-search index for the monorepo
- [[Facebook]] — where the monorepo scaling problem was lived
- [[Code Search]] — the broader capability Miles advanced
