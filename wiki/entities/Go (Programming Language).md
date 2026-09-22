---
title: "Go (Programming Language)"
type: entity
tags: [language, systems-programming, concurrency, Dropbox]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md"]
last_updated: 2026-09-22
---
## Definition
Go is a systems programming language Dropbox used to build most of its Magic Pocket storage system, chosen for its concurrency and proxy/server design strengths.
## Key Information
- Cowling describes Go as "a great language for concurrency, a great language for proxies," well designed for servers that move data between places.
- Magic Pocket was built in Go before Go reached general availability.
- Downside in Dropbox's storage context: the garbage-collected runtime made memory usage unpredictable, and an out-of-memory error on a storage node looks like a disk failure — a batch of OOMs could trigger cascading re-replication and congestion collapse.
- The storage nodes were eventually rewritten in Rust to eliminate that unpredictability.
- Charlie Marsh lists Go alongside Zig and Rust as a language he sees "a ton of success" in, and notes the native JS tooling that inspired Python tooling began with esbuild (written in Go).
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Dropbox]] — used Go for Magic Pocket
- [[Magic Pocket]] — the system written in Go
- [[Rust]] — the language that replaced it on storage nodes
- [[Python]] — the earlier prototype language
- [[Congestion Collapse]] — the failure mode its runtime contributed to
- [[Zig]] — another systems language Charlie compares
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
