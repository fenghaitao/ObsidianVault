---
title: "Vibe Engineering"
type: concept
tags: [ai, coding, development-methodology, vibe-coding, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md"]
last_updated: 2026-06-29
---

## Definition

Vibe Engineering is Michael Arnaldi's term for AI-assisted development done authentically from scratch — starting with an empty repository, no preparation, and building a complete application through iterative AI collaboration. It extends vibe coding with deliberate engineering practices: pattern files, back pressure loops, spec-driven planning, and Ralph loops.

## Key Information

- Coined by Michael Arnaldi during his aiDotEngineer workshop where he built a full-stack Effect application from scratch with no preparation
- Distinguished from pure "vibe coding" by its structured methodology: clone the repo, generate pattern files, spec-driven planning, ESLint back pressure, Ralph loops
- Key practices: (1) clone library repos as git subtrees, (2) generate pattern files by having AI explore the codebase, (3) create specs as markdown plans, (4) use ESLint custom rules to prevent AI shortcuts, (5) run Ralph loops for iterative implementation, (6) restart sessions frequently to avoid context pollution
- The goal is to set up repositories so models can operate effectively at scale — "our job as programmers should be to set up repositories in ways that models can act good on it"
- Contrasts with naive vibe coding where the developer relies on the model getting things right without guardrails
- Uses spec-driven development: discuss a plan with the model, persist as markdown, then implement

## Related

- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source
- [[Michael Arnaldi]] — coined the term
- [[VibeCoding]] — the broader, less structured approach
- [[Clone the Repo Pattern]] — core technique
- [[Back Pressure Loop]] — ESLint-based guardrail
- [[Pattern Files (AI)]] — AI-generated best practices
- [[SpecificationDrivenDevelopment]] — planning methodology used
- [[Ralph Loop]] — iterative implementation pattern
