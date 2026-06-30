---
title: "Pattern Files (AI)"
type: concept
tags: [ai, agents, coding, context, best-practices, prompt-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md"]
last_updated: 2026-06-29
---

## Definition

Pattern files are AI-generated markdown documents that capture best practices for using a specific library or framework. They are created by having an AI coding agent explore a library's source code repository, extract patterns, and document them. Pattern files serve as persistent context that future agent sessions can reference, avoiding the need to re-explore the codebase each time.

## Key Information

- Created by asking the model: "Explore the effect repo for patterns on how to do X. Save your research into patterns/X.md"
- Pattern files are self-selecting — you only generate them for features you actually want to use, avoiding context pollution from unused library features
- Each pattern file captures: general approach, relevant upstream files (with links), testing patterns, common pitfalls
- Examples from the workshop: `patterns/http-api.md` (shared HTTP API pattern, OpenAPI derivation), `patterns/sql.md` (Effect SQL + SQLite with migrations), `patterns/testing.md` (use `EffectTest`, `itLayer`, avoid custom wrappers)
- Pattern files should be referenced in `agents.md` so agents know they exist
- Michael Arnaldi advocates generating patterns per-model because GPT and Claude respond differently to prompting styles
- For brownfield projects: clone the main libraries, ask the model to generate pattern files, then the model operates much more efficiently
- Pattern files can include very specific rules born from experience: "Avoid custom wrappers that call `Layer.build`" exists because the model did that
- Effectful is considering a CLI to prefetch patterns optimized per model family

## Related

- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source
- [[Michael Arnaldi]] — developed the approach
- [[Clone the Repo Pattern]] — prerequisite step
- [[AgentsDotMd]] — where pattern files are referenced
- [[Model Prompting Styles]] — why per-model patterns matter
- [[Vibe Engineering]] — the parent methodology
- [[ContextEngineering]] — the broader practice
