---
title: "Go (Programming Language)"
type: entity
tags: [language, systems-programming, concurrency, Dropbox]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---
## Definition
Go is a systems programming language Dropbox used to build most of its Magic Pocket storage system, chosen for its concurrency and proxy/server design strengths.
## Key Information
- Cowling describes Go as "a great language for concurrency, a great language for proxies," well designed for servers that move data between places.
- Magic Pocket was built in Go before Go reached general availability.
- Downside in Dropbox's storage context: the garbage-collected runtime made memory usage unpredictable, and an out-of-memory error on a storage node looks like a disk failure — a batch of OOMs could trigger cascading re-replication and congestion collapse.
- The storage nodes were eventually rewritten in Rust to eliminate that unpredictability.
- Charlie Marsh lists Go alongside Zig and Rust as a language he sees "a ton of success" in, and notes the native JS tooling that inspired Python tooling began with esbuild (written in Go).
### Anders Hejlsberg on choosing Go for TypeScript 7

- Chose Go for the native TypeScript compiler port because it offered robust, mature native code generation on all major platforms, garbage collection, and excellent shared-memory concurrency — the "high-order bits" the team needed.
- Go won over Rust because Rust has no garbage collection (manual, via the borrow checker) and the borrow checker disallows circular data structures — trees with parent pointers, recursive types, symbols that reference each other — which the compiler is "chalk full" of.
- Go is type-safe and memory-safe, with garbage collection engineered into the language, avoiding the unsafe escape hatches that manual memory strategies require.
- The codebase's existing assumptions (garbage collection and first-class functions) made Go the language that "checked the most boxes."
- The decision process was "pretty structured": the team evaluated languages against those constraints and found every alternative had something that "worked against" them — Go was the right choice for this particular workload.
- Odersky: Go is not a "nuts-and-bolts" systems language but one for application servers, middleware, and cloud infrastructure — not embedded, which Rust covers; in their domains, both are the leaders he takes seriously.
- Go was intentionally designed very small, "the standards of the languages in the '90s"; generics were a late, big step forward but the language is still limited — that limitation forces a uniform style that makes others' code easy to read and jump into.

## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Dropbox]] — used Go for Magic Pocket
- [[Magic Pocket]] — the system written in Go
- [[Rust]] — the language that replaced it on storage nodes
- [[Python]] — the earlier prototype language
- [[Congestion Collapse]] — the failure mode its runtime contributed to
- [[Zig]] — another systems language Charlie compares
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
- [[TypeScript]] — compiler ported to Go
- [[Anders Hejlsberg]] — led the TypeScript 7 port
- [[Garbage Collection]] — a deciding factor
- [[Porting vs Rewriting]] — the port decision
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[Martin Odersky]] — on Go's smallness as uniformity
- [[Rust]] — the systems-level contrast
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg]] — source summary
