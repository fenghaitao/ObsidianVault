---
title: "Salsa (Framework)"
type: entity
tags: [framework, Rust, incremental-computation, tooling]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md"]
last_updated: 2026-09-22
---
## Definition
Salsa is a Rust framework for incremental, on-demand computation, used by Rust Analyzer and by Astral's Red-knot type checker.

## Key Information
- Red-knot is built on Salsa, the same framework behind Rust Analyzer (the popular Rust language server).
- Salsa enables the "lazy" recomputation model: model a dependency graph of what's happening in the code, then flow changed data back only through the affected pieces.
- Astral has become a large contributor to Salsa, intentionally or inadvertently, through its type-checker work.
- Charlie spends time optimizing Salsa memory usage (e.g., reducing Salsa memory by ~1% on a project) using agents for micro-optimizations.

## Related
- [[Rust Analyzer]] — built on the same framework
- [[Red-knot]] — Astral's type checker using it
- [[Rust]] — the language ecosystem
- [[Incremental Computation]] — the design principle it implements
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
