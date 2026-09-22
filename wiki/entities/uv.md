---
title: "uv"
type: entity
tags: [tool, package-manager, Python, Rust, open-source]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md"]
last_updated: 2026-09-22
---
## Definition
uv is Astral's fast Python package and project manager, written in Rust.

## Key Information
- uv is mostly an IO-bound workload (downloading, unzipping, writing files), so its speed combines Rust with architectural innovation — especially an intentional cache design that makes repeated installs of the same package near-instant in time and disk space.
- A notable optimization by Andrew Gallant (burntsushi) represents roughly 90%+ of version numbers as a single u64 integer, avoiding expensive per-version allocations during resolution.
- Relied on by millions of engineers; Charlie treats uv with far more care than internal/personal tools when using agents — shipping standards scale with user responsibility.
- Astral's commercial counterpart is a hosted private package registry with first-class uv support.
- uv's test suite is largely snapshot-based: most tests run uv and verify its output, embedding snapshots in Rust source (e.g., a very long `lock.rs`).

## Related
- [[Charlie Marsh]] — creator
- [[Astral]] — the company
- [[Rust]] — implementation language
- [[Python]] — target ecosystem
- [[Andrew Gallant]] — author of the u64 version optimization
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
