---
title: "Red-knot"
type: entity
tags: [tool, type-checker, Python, Rust, language-server]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md"]
last_updated: 2026-09-22
---
## Definition
Red-knot is Astral's Python type checker and language server, built on the Salsa incremental-computation framework. The episode title's "ty" and the transcript's "TY" are garbled references to it.

## Key Information
- The transcript repeatedly refers to it as "TY": "TY is our type checker. Probably [the] hardest project I've worked on technically."
- Designed to be both a type checker and a language server with a highly incremental, lazy architecture — open one file and get analysis without type-checking the whole project, and recompute only what changed.
- Built on Salsa, the same framework used by Rust Analyzer (the popular Rust language server); Astral has become a large contributor to Salsa.
- Performance work targets both speed and memory, so running the language server on a very large project stays efficient rather than consuming many gigabytes.
- A plausible agent-generated PR to the type checker "might take them two minutes and then it could take us an hour to understand it."

## Related
- [[Astral]] — the company
- [[Ruff]] — the linter it complements
- [[Salsa (Framework)]] — the underlying incremental-computation framework
- [[Rust Analyzer]] — also built on Salsa
- [[Python]] — target language
- [[Charlie Marsh]] — calls it the hardest project
- [[mypy]] — earlier Python type-checking ecosystem
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
