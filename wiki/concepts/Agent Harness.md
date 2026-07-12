---
title: "Agent Harness"
type: concept
tags: [AI, agent, architecture, coding]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue.md"]
last_updated: 2026-07-10
---

## Definition

The agent harness is the middleware layer in the AI agent stack that sits between the model API and the user, managing tool execution, environment configuration, sandboxing, and UI. It is one of three layers that must be optimized together for effective AI agents.

## Key Information

- The agent stack has three layers: the reasoning model, the API, and the harness
- The harness is where opinions about how the agent should work are expressed — e.g., whether it uses semantic search, specific tools, or the shell
- OpenAI's Codex harness is opinionated: the model uses the shell and operates in a sandbox for safety
- Different coding products have very different harnesses with different opinions, and training a model to be good at all of them is harder than optimizing for one
- The harness is responsible for preparing compaction payloads, managing the sandbox, and rendering results (e.g., diff vs image preview)
- The harness also handles the UX question of what to show first: the diff of code changes or the preview of what the code produced
- A tightly integrated product and research team can iterate on the model and harness together, which is a competitive advantage
- The harness is where "mixed initiative" interactions happen — surfacing contextual help at the right moment

## Related

- [[Codex]] — product with a tightly integrated harness
- [[Compaction]] — feature that spans all three layers
- [[summary-39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue]] — source summary
