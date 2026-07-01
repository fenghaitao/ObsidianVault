---
title: "Agent Review Bundles"
type: concept
tags: [agents, code-review, visualization, evidence, agent-craft]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon.md"]
last_updated: 2026-06-29
---

## Definition
Agent Review Bundles are PR review packages in AgentCraft that include not just code diffs but also visual evidence — screenshots and videos — showing what the agent did, why it made decisions, and what the result looks like, enabling faster human review with less cognitive investment.

## Key Information
- **Beyond code diffs**: Includes screenshots and videos of the agent's work, not just the code changes
- **Task-level context**: Shows what tasks the agent was working on and why it made specific decisions
- **Visual evidence**: Screenshots show UI changes; videos show interactive behavior and workflows
- **Reduced review time**: Humans can understand agent work through visual evidence without deep-diving into every code change
- **Multiple PRs at once**: When channels or campaigns produce many PRs, review bundles make it feasible to review them all
- Enables the shift from planning-heavy to review-heavy workflows: if agents can produce 10 variations, the human picks the best one with minimal effort
- Part of AgentCraft's progressive autonomy ladder: as agents do more work autonomously, review bundles make the human review step efficient

## Related
- [[summary-20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon]] — source transcript
- [[AgentCraft]] — the orchestrator implementing review bundles
- [[Agent Channels]] — source of many PRs needing review
- [[Agent Campaigns]] — source of PRs needing review
- [[AgentHuman Collaboration]] — the review step in collaboration
- [[CodeReviewAmplification]] — related concept
- [[Verification in Agentic Loops]] — related verification concept
