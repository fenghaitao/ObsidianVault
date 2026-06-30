---
title: "Gina"
type: entity
category: tool
tags: [semantic-search, cli, grep, local-files, embeddings]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md"]
last_updated: 2026-06-29
---

## Definition

Gina is a CLI tool that provides semantic search capabilities over local file systems. Its `gina-grap` command offers semantic search as an alternative to grep, which only supports exact matches. It is designed to be used by agents via the shell/bash tool for fuzzy or semantic queries over local files.

## Key Information

- **gina-grap**: Semantic search command — alternative to grep for fuzzy/semantic queries
- **Multiple modes**: Supports classification, re-ranking, and semantic search
- **Multi-vector embeddings**: Uses multi-vector embeddings for semantic search (similar to ColGrap by LightOn)
- **Agent integration**: Agents can use Gina Grap via the shell tool by running `gina-grap` commands
- **Usage guidance**: Use grep for exact matches, Gina Grap for semantic/fuzzy queries
- **Top K**: Supports configurable top-K results (e.g., return top 10)

## Related

- [[summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic]] — source transcript
- [[Gina Grap]] — the semantic search command
- [[Shell Tool]] — mechanism for agents to invoke Gina
- [[Semantic Search]] — the underlying technique
