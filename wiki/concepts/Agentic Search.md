---
title: "Agentic Search"
type: concept
tags: [agents, search, context-engineering, retrieval, rag]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md"]
last_updated: 2026-06-29
---

## Definition

Agentic search is the approach where an AI agent decides whether, when, and how to call search tools to retrieve context, rather than following a fixed retrieval pipeline. It is the core mechanism of context engineering — the search tools that decide what goes from context sources into the context window. Leonie Monigatti argues that context engineering is about 80% agentic search.

## Key Information

- **Contrast with fixed RAG**: In fixed RAG, the user message is used verbatim as a search query in a predetermined pipeline. In agentic search, the agent decides whether to retrieve at all, which tool to use, and can rewrite queries or retrieve multiple times
- **Multi-source retrieval**: Agentic search spans local files, databases, web, memory, and agent skills — each with native search tools
- **Tool landscape**: Includes semantic search tools, general-purpose query execution tools (ESQL, SQL), shell/bash tools, web search tools, memory tools, and custom CLIs
- **Three common failure modes**: (1) Agent doesn't call any tool (thinks parametric knowledge is sufficient), (2) Agent calls the wrong tool, (3) Agent generates wrong search parameters
- **Tool descriptions are critical**: Start with core purpose; add trigger conditions, relationships, and system prompt reinforcement if agent struggles
- **Error handling**: Tools should return errors to the agent so it can self-correct rather than crashing
- **Low floor, high ceiling**: Curate a balanced set of specialized tools (simple parameters, few mistakes) and general-purpose tools (handle unexpected queries)
- **Start general, then specialize**: If you don't know agent query behavior, start with general-purpose tools, log behavior, then create specialized tools for common patterns
- **Model strength matters**: Stronger models reduce parameter error rates for general-purpose tools but don't eliminate errors
- **Combining tools**: Hybrid agents using both database tools and shell tools can achieve higher accuracy by cross-verifying results

## Related

- [[summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic]] — source transcript
- [[Agentic RAG]] — the RAG-specific form
- [[ContextEngineering]] — the parent paradigm
- [[Shell Tool]] — universal adapter for agentic search
- [[Tool Description]] — critical for agentic search success
- [[Low Floor High Ceiling]] — tool curation strategy
- [[Agent Skills]] — progressive disclosure for complex parameters
- [[AgenticSearchInterface]] — related design pattern for search interfaces
- [[RAG]] — the earlier fixed-pipeline paradigm
- [[Leonie Monigatti]] — speaker
