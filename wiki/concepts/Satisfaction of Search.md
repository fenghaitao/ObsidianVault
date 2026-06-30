---
title: "Satisfaction of Search"
type: concept
tags: [agent-failure, context-engineering, retrieval, cognitive-bias]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked.md"]
last_updated: 2026-06-30
---

## Definition

Satisfaction of search is a cognitive phenomenon, originally identified in radiology, where an observer stops searching after finding the first plausible answer, missing additional important findings. In AI agent context retrieval, it describes the failure mode where an agent calls an MCP tool, finds the first piece of matching data, assumes it has found the correct pattern, and stops looking — missing the actual root cause or best approach.

## Key Information

- Originally a radiology phenomenon: a radiologist finds one anomaly on an X-ray and stops scanning, missing other critical findings
- In agent context retrieval: when asked "make a Zendesk integration," the agent finds one pattern and stops — without exhaustive search, it may miss the correct pattern or alternative approaches
- This is why naive RAG fails as a context engine: it retrieves some relevant chunks but the agent latches onto the first result without exhaustive coverage
- The antidote is exhaustive retrieval: a context engine must reason across all data sources and run exhaustively to find everything important before sending a token-optimized response
- Results in agents producing code that compiles but is architecturally wrong — a senior engineer would reject it

## Related

- [[summary-20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked]] — source
- [[ContextEngine]] — solves this problem through exhaustive retrieval
- [[DoomLoop]] — related failure mode from insufficient context
- [[Brandon Waselnuk]] — speaker who identified this in agent context
