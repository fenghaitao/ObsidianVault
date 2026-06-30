---
title: "Gina Grap"
type: concept
tags: [semantic-search, cli, local-files, grep, embeddings]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md"]
last_updated: 2026-06-29
---

## Definition

Gina Grap is a CLI command from the Gina tool that provides semantic search over local file systems. It serves as a semantic alternative to grep, which only supports exact/pattern matches. Agents can invoke Gina Grap via the shell/bash tool to perform fuzzy or semantic queries over local files.

## Key Information

- **Semantic alternative to grep**: Grep works on exact matches; Gina Grap handles fuzzy/semantic queries
- **Multi-vector embeddings**: Uses multi-vector embeddings for semantic search
- **Multiple modes**: Supports classification, re-ranking, and semantic search
- **Agent integration**: Agents invoke it via shell tool — e.g., `gina-grap "regulatory constraints" --top-k 10`
- **Usage guidance**: Use grep for exact matches, Gina Grap for semantic/fuzzy queries
- **Efficiency**: Much more efficient than agents chaining grep with synonyms to approximate semantic search
- **Similar tools**: ColGrap by LightOn (multi-vector embeddings), Sam Tools by LlamaIndex
- **First-try success**: In demos, agents correctly used Gina Grap on the first attempt for semantic queries

## Related

- [[summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic]] — source transcript
- [[Gina]] — the parent CLI tool
- [[Shell Tool]] — mechanism for agents to invoke Gina Grap
- [[Semantic Search]] — the underlying technique
- [[Agentic Search]] — the broader context
