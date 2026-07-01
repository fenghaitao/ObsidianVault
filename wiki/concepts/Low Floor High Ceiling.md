---
title: "Low Floor High Ceiling"
type: concept
tags: [agents, search-tools, tool-design, curation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md"]
last_updated: 2026-06-29
---

## Definition

Low Floor High Ceiling is a tool curation strategy for AI agents, borrowed from user experience design. It means providing a balanced set of search tools: specialized tools with simple parameters that agents can use out of the box with few mistakes (low floor), combined with general-purpose tools that can handle unexpected or complex queries (high ceiling).

## Key Information

- **Low Floor**: Specialized tools with simple parameters — agent doesn't make many mistakes, efficient (fewer tool calls), examples include semantic search tools, get-customer-by-ID
- **High Ceiling**: General-purpose tools for unexpected queries and complex questions — shell tool, query execution tools (ESQL, SQL) — agent may need more iterations but can handle anything
- **Trade-off**: General-purpose tools are versatile but require more powerful models and more iterations; specialized tools are efficient but limited in scope
- **Start with general-purpose** if you don't know agent query behavior yet, then log behavior and create specialized tools for common patterns
- **Indicator for specialization**: If agent takes 4-5 tool calls per question, the tool is too difficult — scope out something more specialized
- **Origin**: Concept from user experience design, applied to agent tool design by Elastic

## Related

- [[summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic]] — source transcript
- [[Agentic Search]] — the context where this strategy applies
- [[ToolCuration]] — related practice of selecting the right tools
- [[Tool Description]] — critical for making tools accessible (low floor)
- [[Shell Tool]] — the quintessential high-ceiling tool
- [[Elastic]] — organization advocating this approach
