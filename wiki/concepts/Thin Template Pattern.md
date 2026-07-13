---
title: "Thin Template Pattern"
type: concept
tags: [software-engineering, ai, agentic-engineering]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

[[Simon Willison]]'s practice of starting every new coding-agent project from a minimal, personally-styled project skeleton (e.g., a single passing test asserting 1+1=2, laid out exactly how he prefers) rather than a long written instructions file (like an extensive CLAUDE.md).

## Key Information

- Rationale: coding agents are extremely good at picking up and continuing existing patterns in a codebase — even a single example test or a specific indentation/formatting style is enough for an agent to notice and replicate going forward, without needing it spelled out in prose.
- Preferred by Willison over verbose written style guides because it's simpler to maintain and, in his experience, more reliably followed — the agent learns "how Simon likes code written" by imitation rather than instruction.
- He maintains several such templates on GitHub (one for a Python library, one for a dataset plugin, one for a command-line tool), each just a thin, pre-styled starting skeleton.

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[Simon Willison]] — practices and recommends this pattern
- [[Agentic Engineering]] — broader discipline this technique supports
