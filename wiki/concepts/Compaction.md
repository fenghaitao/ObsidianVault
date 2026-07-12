---
title: "Compaction"
type: concept
tags: [AI, context-window, agent, technical]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue.md"]
last_updated: 2026-07-10
---

## Definition

Compaction is a technique that enables AI models to run continuously for extended periods (24+ hours) by managing context windows. When a model approaches its context window limit, compaction prepares it to be run in a new context window, preserving the essential state of its work.

## Key Information

- A critical feature for Codex that enables multi-hour and overnight coding sessions
- Requires coordination across all three layers of the agent stack: the model (must understand compaction and prepare for it), the API (must have an endpoint for the transition), and the harness (must prepare the payload)
- Without compaction, models would be limited by their context window size for long-running tasks
- Shipping compaction required working across the model, API, and harness teams simultaneously
- This feature is an example of why OpenAI's tightly integrated product and research team structure is advantageous — all three layers must be optimized together

## Related

- [[Codex]] — product that uses compaction
- [[Agent Harness]] — the stack layer that prepares compaction payloads
- [[summary-39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue]] — source summary
