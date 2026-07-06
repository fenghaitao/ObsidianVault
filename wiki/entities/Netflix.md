---
title: "Netflix"
type: entity
tags: [enterprise, streaming, media, ai-adopter, software-development]
sources: ["raw/01-articles/claude/2025-10-01 - How enterprises are driving AI transformation with Claude.md", "raw/01-articles/claude/2026-04-23 - Built-in memory for Claude Managed Agents.md", "raw/01-articles/claude/2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration.md"]
last_updated: 2026-07-05
---

## Definition

Netflix is a streaming entertainment company cited by Anthropic as an example of developers using Claude Sonnet 4.5 to tackle complex, codebase-spanning tasks with unprecedented accuracy.

## Key Information

- Developers at Netflix are cited (alongside [[GitHub]]) as benefiting from Claude Sonnet 4.5's ability to handle complex, codebase-spanning development tasks accurately.
- Cited (April 2026) as a [[ClaudeManagedAgents]] memory customer: Netflix's agents carry context across sessions — including insights that took multiple turns to uncover and corrections a human made mid-conversation — instead of the team manually updating prompts and skills.
- **Multiagent orchestration customer (May 19, 2026)**: Netflix's platform team built an analysis agent that processes logs from hundreds of builds across different sources. Since changes affect thousands of applications, what matters is finding issues that recur across many of them; multiagent orchestration lets the agent analyze batches in parallel and surface only the patterns worth acting on. See [[MultiAgentSystem]] and [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]].

## Related

- [[Claude4.5Sonnet]] — the model credited with this result
- [[GitHub]] — cited alongside Netflix for the same capability
- [[Anthropic]] — model provider
- [[summary-2025-10-01 - How enterprises are driving AI transformation with Claude]] — source article
- [[ClaudeManagedAgents]] — memory and multiagent orchestration customer
- [[summary-2026-04-23 - Built-in memory for Claude Managed Agents]] — source citing Netflix's memory use case
- [[MultiAgentSystem]] — coordination pattern behind Netflix's parallel log-analysis agent
- [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]] — source citing Netflix's multiagent orchestration use case
