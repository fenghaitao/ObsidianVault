---
title: "ContextBench"
type: entity
tags: [benchmark, code-retrieval, evaluation, research]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer.md"]
last_updated: 2026-06-30
---

## Definition
ContextBench is a public benchmark for evaluating code retrieval in coding agents. Unlike end-to-end benchmarks (did the agent solve the task?), ContextBench evaluates the retrieval process: did the agent find the correct files, lines, and symbols while solving the task?

## Key Information
- Public paper and benchmark for code retrieval evaluation
- Human-labeled dataset: for each task, annotators specify which files, lines, and symbols the agent should have found
- Measures three precision/recall dimensions: file-level, line-level, and symbol-level
- Used by Kuba Rogut to benchmark Claude Code with and without semantic search (50 tasks)
- Thesis: the process of how agents find context matters, not just the end result
- Cursor has their own internal version of a similar benchmark
- Precision measures: of all files read, how many were actually needed (golden files)?
- Recall measures: of all needed files, how many did the agent find?

## Related
- [[SemanticCodeRetrieval]] — capability evaluated by ContextBench
- [[CodeRetrievalBenchmarking]] — broader methodology
- [[KubaRogut]] — used ContextBench for his experiments
- [[summary-20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer]] — source
