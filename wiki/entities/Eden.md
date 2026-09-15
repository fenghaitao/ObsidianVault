---
title: "Eden"
type: entity
tags: [tool, virtual-file-system, Meta]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin.md"]
last_updated: 2026-09-14
---

## Definition

Eden (originally the name of the virtual file system) is Meta's virtual file system that let engineers work on the monorepo without materializing every file on disk, a project Michael Bolin worked on to preempt repo-scaling problems.

## Key Information

- The repo keeps growing; Bolin's manager Brian O'Sullivan gathered engineers (Bolin, Adam Simpkins, Wes Furlong) to work on a virtual file system.
- The idea: design tooling so cloning/updating doesn't require writing every file to disk; the VFS fetches file contents on demand as the OS asks.
- Bolin's contribution focused on the second part — changing toolchain and development flow to be VFS-aware, because tools that just "read everything" would materialize files and undo the benefit.
- Anticipating the file search problem led to the Miles index (which solved Eden's file-search need before Eden itself was ready).

## Related

- [[summary-20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin]] — source summary
- [[Michael Bolin]] — who worked on Eden
- [[Miles]] — the file-search index built to serve Eden
- [[Monorepo]] — the scaling problem Eden addressed
- [[Brian O'Sullivan]] — the manager who convened the project
- [[Adam Simpkins]] — engineer on the project
- [[Wes Furlong]] — engineer on the project
