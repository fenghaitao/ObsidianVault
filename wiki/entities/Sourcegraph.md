---
title: "Sourcegraph"
type: entity
tags: [company, coding-agent, developer-tools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md"]
last_updated: 2026-06-25
---

## Definition
Sourcegraph is the company behind Amp Code (AMP), a coding agent with a free tier supported by ads. Their vision focuses on building agents that work with agent-friendly environments, emphasizing the feedback loop between coding agents and testable codebases.

## Key Information
- Creator of Amp Code, a coding agent with a free tier
- Uses an ad-sponsored inference model to subsidize costs for the free tier
- Amp Code does not have a model selector — this helps them move faster by reducing user expectations about specific model outputs
- Vision: build not just the best agent, but the agent that works with the most agent-friendly environments
- Focuses on hermetically sealed coding repos where agents can run tests autonomously
- Believes the feedback loop (agent writes code, runs tests, sees results) is the holy grail for autonomous agents
- Introduced "handoff" technique as an alternative to context compaction
- Uses reasoning knobs: fast, smart, and Oracle model tiers
- Willing to switch what model serves as "Oracle" without telling users

## Related
- [[AmpCode]] — their coding agent product
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[AdSponsoredInference]] — economic model used for free tier
- [[Handoff]] — context management technique they pioneered
- [[AgentOrientedArchitecture]] — design philosophy
