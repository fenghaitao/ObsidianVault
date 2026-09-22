---
title: "Incremental Computation"
type: concept
tags: [compilers, performance, architecture, type-checking]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md"]
last_updated: 2026-09-22
---
## Definition
Incremental computation recomputes only the parts of a result affected by a change, rather than recomputing everything from scratch.

## Key Information
- Astral's Red-knot type checker/language server is "highly incremental": opening one file should not require type-checking the entire project, and editing one file should recompute only what changed.
- Implemented via a dependency graph that models what's happening in the code, so changed data flows back through only the affected pieces.
- Built on Salsa, the same framework behind Rust Analyzer, and requires care to be both lazy and memory-efficient on very large projects.

## Related
- [[Salsa (Framework)]] — the framework that implements it
- [[Rust Analyzer]] — a language server built this way
- [[Red-knot]] — Astral's incremental type checker
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
