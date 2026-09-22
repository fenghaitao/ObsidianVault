---
title: "Ruff"
type: entity
tags: [tool, linter, Python, Rust, open-source]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md"]
last_updated: 2026-09-22
---
## Definition
Ruff is a fast Python linter (and formatter) written in Rust, created by Charlie Marsh as Astral's first product. The transcript frequently garbles it as "Rough".

## Key Information
- Began as a prototype to test the hypothesis "Python tooling could be much, much faster"; the announcement post followed an earlier type-checking-at-scale post by roughly nine days.
- The linter was chosen as the first form factor because it has a simple core plus many rules, so value ships incrementally — unlike a 75%-done type checker or package manager, which isn't very useful.
- Its benchmark graph became a "priceless" viral visual hook; Charlie stresses honest benchmarks (no non-zeroed "chart crimes") while acknowledging performance is nuanced (caching, workload, out-of-band C++ builds).
- Early momentum tactics: aggressively acknowledge and fix issues within a day, and win specific high-profile adopters such as Sebastian Ramirez (FastAPI).
- Much of Ruff's speed comes from Rust, with additional gains from deep performance and design thinking over time.

## Related
- [[Charlie Marsh]] — creator
- [[Astral]] — the company
- [[Rust]] — implementation language
- [[Python]] — target language
- [[mypy]] — the type checking it was initially contrasted with
- [[Red-knot]] — Astral's type checker
- [[Sebastian Ramirez]] — early influential adopter
- [[FastAPI]] — Ramirez's project
- [[Developer Marketing]] — the benchmark-graph strategy
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
