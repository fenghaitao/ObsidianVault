---
title: "PromptCaching"
type: concept
tags: [performance, llm, optimization, context]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Prompt caching is a technique that caches repeated prompt prefixes to avoid re-sending them to the LLM on every turn. Amazon Kiro achieves 90-95% cache token usage, making agent interactions significantly faster than sending full context cold each time.

## Key Information
- Kiro achieves 90-95% cache hit rate in typical usage
- This is the primary reason Kiro has not invested heavily in incremental summarization: cached interactions are already fast
- Without caching, each turn would send ~160k tokens to the model cold
- Changing MCP configuration or tools mid-session is a cache-invalidating operation that can dramatically slow down deep sessions
- Kiro's focus on caching over summarization is a deliberate engineering trade-off

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[AmazonKiro]] — IDE using this technique
- [[Context Management]] — broader context optimization category
- [[ContextCompression]] — alternative approach to context management
