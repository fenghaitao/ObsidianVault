---
title: "ESQL"
type: concept
tags: [elasticsearch, query-language, database, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md"]
last_updated: 2026-06-29
---

## Definition

ESQL (Elasticsearch Query Language) is a pipe query language for filtering, transforming, and analyzing data in Elasticsearch. It is similar to SQL but with different syntax and capabilities. When used as an agent tool parameter, ESQL is a complex parameter type that agents can struggle with — requiring agent skills or detailed documentation to generate correctly.

## Key Information

- **Pipe query language**: Uses pipes for chaining operations — filtering, transforming, and analyzing data
- **Similar to SQL**: Reminiscent of SQL but with different syntax and capabilities
- **Wildcard characters**: Uses `*` (asterisk) as wildcard, not `%` (percent sign) — a common agent mistake when coming from SQL background
- **String literals**: Uses double quotes for string literals
- **Agent challenges**: Agents often use SQL wildcards (`%`) instead of ESQL wildcards (`*`), resulting in zero search results
- **Agent skills fix**: Official Elasticsearch agent skills provide ESQL syntax documentation loaded on demand via progressive disclosure
- **Capabilities**: Supports filtering, aggregations, counting — allows agents to outsource calculations to the database rather than doing them in the LLM (which is bad at counting)
- **Zero results**: Important to consider whether zero search results is a valid response or a failure mode

## Related

- [[summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic]] — source transcript
- [[Elastic]] — company behind Elasticsearch and ESQL
- [[Agent Skills]] — mechanism for providing ESQL documentation to agents
- [[Agentic Search]] — context where ESQL is used as a search tool
- [[Tool Description]] — critical for ESQL tools due to parameter complexity
