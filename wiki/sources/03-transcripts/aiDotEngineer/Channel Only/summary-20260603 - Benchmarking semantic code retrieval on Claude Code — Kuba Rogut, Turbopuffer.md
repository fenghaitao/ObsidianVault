---
title: "summary-20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer"
type: source
tags: [source, transcript, semantic-search, code-retrieval, benchmarking]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer.md"]
last_updated: 2026-06-30
---

## Core Summary

Kuba Rogut from Turbopuffer benchmarks semantic code retrieval on Claude Code, comparing raw agentic search (grep) against windowed grep and Turbo Grep semantic search. Results show semantic search boosts file precision from 65% to 87% but recall varies by task type. Semantic search acts as "cached compute" — upfront indexing cost saves tokens across sessions.

## Key Points

- Claude Code defaults to agentic search (grep), not semantic search. Cursor uses semantic search and sees 24% relative improvement in answer accuracy.
- Turbo Grep: CLI tool that chunks, embeds (Voyage code model), and indexes codebases into Turbopuffer for Claude Code tool calling.
- Benchmark: precision (how many files read were relevant) went from 65% (raw) → 87% (semantic). Recall varies — grep wins on import tracing, semantic wins on behavior-adjacent files.
- Semantic search as "cached compute": upfront indexing cost amortized across all sessions/agents, saving tokens long-term.
- Claude Code not optimized for semantic search (added as extra tool); Cursor's built-in integration yields better results.
- Long-term winners will provide lightweight tools to shrink billion-token context windows into the right million tokens.

## Related

- [[KubaRogut]] — speaker, Turbopuffer
- [[Turbopuffer]] — serverless full-text and vector search database
- [[SemanticCodeRetrieval]] — concept
- [[ClaudeCode]] — coding agent benchmarked
- [[Cursor]] — comparison point
- [[Agentic Search]] — grep-based approach
