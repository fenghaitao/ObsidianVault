---
title: "Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer.md"
author: "Kuba Rogut"
organization: "Turbopuffer"
date: 2026-06-03
tags: [semantic-code-search, code-retrieval, vector-search, claude-code, benchmarking, embeddings]
---

# Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer

## Core Thesis

Kuba Rogut from Turbopuffer presents benchmarking results showing that adding semantic (vector) code search to Claude Code significantly improves retrieval precision, though not necessarily recall. Semantic search and traditional grep-based search excel at different types of tasks: semantic search finds behaviorally-related files without shared keywords, while grep excels at tracing imports and keyword-matching tasks. The key insight is that embeddings act as "cached compute" — an upfront investment in chunking and embedding a codebase pays off by avoiding repeated exploratory grep-and-read cycles across sessions and agents. While Cursor sees ~24% improvement from built-in semantic search, Claude Code's add-on approach yields more modest gains because the agent was not designed to understand when to use semantic search.

## Key Points

1. **Claude Code's default approach**: Uses "agentic search" (grep-based file system exploration) rather than semantic search. Early versions tried a local vector DB but abandoned it in favor of simpler grep-based search.

2. **Embeddings as cached compute**: The core thesis — chunk, embed, and index the codebase upfront so that agents can query semantic meaning instead of repeatedly grepping and reading files. This amortizes the compute cost across sessions and agents.

3. **TurboGrep CLI tool**: A simple tool that uses a tree-splitter library to parse, chunk, embed (via Voyage code model), and upload codebases to Turbopuffer. A V1 open-source library exists; V2 is forthcoming.

4. **Benchmark methodology**: Tested Claude Code under three conditions on 50 tasks from ContextBench:
   - Raw Claude Code (baseline)
   - Claude Code with max 50-line reads (windowed grep)
   - Claude Code with windowed grep + TurboGrep semantic search tool

5. **Precision results**: Semantic search improved file precision from 65% (baseline) to 87%. In English: baseline Claude Code wastes 1 in 3 file reads; semantic search reduces waste to 1 in 8 files.

6. **Recall results**: Baseline Claude Code had the highest file recall due to its exploratory nature, but lower line and symbol recall because it read many files without golden context. Windowed grep and semantic search had similar recall overall.

7. **Task-dependent performance**: Breaking down results by task reveals stark differences — semantic search wins on tasks requiring behavioral adjacency (e.g., finding related ORM files across libraries), while grep wins on import-tracing and keyword-matching tasks.

8. **Cursor comparison**: Cursor sees ~24% relative improvement in answer accuracy with built-in semantic search because it knows when and how to use it. Claude Code's add-on tool approach is less effective because the agent does not have a true understanding of when to call semantic search.

9. **Cursor's A/B test results**: 2.6% increase in code retention on large codebases and 2.2% decrease in dissatisfied user requests — numbers that appear small because not all queries benefit from semantic search.

10. **What makes semantic search work best**: Codebases with good inline comments and documentation — comments above functions help the embedding model understand meaning, improving search quality.

11. **Vector databases for multi-modal and complex data**: Beyond code, vector DBs enable search across knowledge bases (Notion), multi-modal data (video, audio, images), and other data types that cannot be grepped.

12. **Long-term winners**: Those who provide lightweight tools to find the right context in various ways — shrinking billion-token context windows into the right million tokens — will win.

## Entities

- [[KubaRogut]] — Speaker, from Turbopuffer
- [[Turbopuffer]] — Serverless full-text and vector search database on object storage
- [[ClaudeCode]] — Anthropic's coding agent, tested with and without semantic search
- [[Cursor]] — AI code editor that uses Turbopuffer for built-in semantic code search
- [[Anthropic]] — Creator of Claude Code
- [[TurboGrep]] — CLI tool for chunking, embedding, and indexing codebases
- [[Voyage]] — Provider of the Voyage code embedding model used by TurboGrep
- [[ContextBench]] — Public benchmark for evaluating code retrieval in coding agents
- [[Boris Starkov]] — Referenced as "founding father of Claude Code" who tweeted about early semantic search experiments

## Concepts

- [[SemanticCodeRetrieval]] — Vector-based code search using embeddings
- [[CacheCompute]] — Embeddings as cached compute to amortize search costs
- [[AgenticSearch]] — Grep-based exploratory file system search used by Claude Code by default
- [[VectorDatabases]] — Infrastructure for embedding-based search
- [[Precision and Recall in Code Retrieval]] — Metrics for evaluating code search quality

## Related

- [[summary-20260428 - Building your own software factory — Eric Zakariasson, Cursor]] — Cursor's use of semantic search
- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — Cursor's approach to tooling
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — Claude Code architecture
