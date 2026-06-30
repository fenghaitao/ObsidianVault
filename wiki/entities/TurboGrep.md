---
title: "TurboGrep"
type: entity
tags: [tool, cli, vector-search, semantic-search, code-indexing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer.md"]
last_updated: 2026-06-30
---

## Definition
TurboGrep is a CLI tool built by Turbopuffer that parses, chunks, embeds, and indexes codebases into the Turbopuffer vector database. It enables Claude Code (or any agent) to perform semantic code search by adding a "T Puffer search" tool to the agent's tool set.

## Key Information
- Built by Kuba Rogut at Turbopuffer
- Uses a tree-splitter library to parse and chunk codebases
- Embeds code using the Voyage code model
- Uploads indexed code to Turbopuffer for semantic search
- V1 version is open source; V2 is forthcoming
- Appears in Claude Code as a tool called "T Puffer search"
- Tested on the Django repository and ContextBench tasks
- Enables semantic (vector) code search alongside traditional grep-based search
- The approach is simple: a file system walk, chunk, embed, upload — no sophisticated preprocessing

## Related
- [[Turbopuffer]] — the vector database it indexes into
- [[KubaRogut]] — creator
- [[Voyage]] — embedding model used
- [[ClaudeCode]] — primary target agent
- [[SemanticCodeRetrieval]] — the capability it enables
- [[summary-20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer]] — source
