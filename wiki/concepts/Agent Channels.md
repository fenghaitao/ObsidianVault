---
title: "Agent Channels"
type: concept
tags: [agents, automation, cron, autonomy, agent-craft]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon.md"]
last_updated: 2026-06-29
---

## Definition
Agent Channels are cron-based autonomous agent execution pipelines in AgentCraft where agents run on a schedule — for example, scanning Twitter daily for interesting ideas and implementing them — with the human only deciding what they want and reviewing the resulting PRs.

## Key Information
- **Cron-based execution**: Agents run on a schedule without human triggering
- **External input scanning**: Channels can pull ideas from external sources (Twitter, RSS, APIs) as input for agent work
- **End-to-end autonomy**: From idea discovery to implementation to PR creation — fully automated
- **Human role**: Decide what kind of work to automate, review the resulting PRs via review bundles
- **Example**: "Go to Twitter every day, scan cool ideas, and just implement them"
- Represents the highest level of AgentCraft's autonomy ladder: direct prompting → quests → campaigns → channels
- Ido Salomon implemented channels "pretty quickly" using AgentCraft itself, demonstrating the tool's self-hosting capability
- Produces multiple PRs that are reviewed efficiently using review bundles with visual evidence

## Related
- [[summary-20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon]] — source transcript
- [[AgentCraft]] — the orchestrator implementing channels
- [[Agent Review Bundles]] — how channel PRs are reviewed
- [[Agent Campaigns]] — one level below in the autonomy ladder
- [[RTS-Inspired Agent Orchestration]] — the broader paradigm
- [[Agent Orchestration]] — broader orchestration concept
