---
title: "Semantic Summaries"
type: concept
tags: [agents, data-engineering, context-management, agent-interface]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Semantic Summaries are condensed, structured representations of complex data (returned as markdown or other structured formats) designed to fit within an agent's context window. Instead of forcing agents to process raw data (e.g., 50K lines of JSON trace files), semantic summaries point them at the relevant information.

## Key Information
- Technique used by Chrome DevTools MCP to avoid blowing through agent context windows
- Raw trace files contain multiple megabytes of JSON data — agents cannot reason about this volume
- Instead, performance tracing endpoints return markdown and semantic summaries with key metrics (LCP, INP, CLS)
- Analogy: "Don't force the agent to read the entire book — point it at the right sentence"
- Can still return raw data for post-processing with other tools (e.g., CLI chaining)
- Part of the broader pattern of designing agent-appropriate data formats
- Addresses the core problem that coding agents were "flying blind" — could generate code but not validate it

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Agents As Different User Class]] — why this technique is necessary
- [[Chrome DevTools MCP]] — practical implementation
- [[Context Management]] — broader category
- [[CLI For Agents]] — complementary technique for raw data post-processing
