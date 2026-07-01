---
title: "Slack-based Agent Interface"
type: concept
tags: [ai, agents, slack, interface, messaging, async]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski.md"]
last_updated: 2026-06-29
---

## Definition
A Slack-based Agent Interface is an interaction paradigm where an AI agent lives entirely within Slack, using DMs, channels, threads, emoji reactions, and message edits as its input and output surface — without a separate web application. This contrasts with single-thread web app agents by embracing Slack's multi-modal, async communication patterns.

## Key Information
- Fryderyk Wiatrowski chose Slack as Viktor's sole interface for two reasons:
  1. **Human-employee feel**: "You don't interact with human employees in web apps. You interact with them in Slack, just as your teammates."
  2. **Async latency tolerance**: Long-running agent tasks (10+ minutes) feel acceptable in Slack because the comparison point is human response time — "if you ping someone on Slack and tell them to build an app and get an answer in 10 minutes, you are shocked." In a web app, waiting 10 minutes for an answer feels frustrating because users expect instant ChatGPT-like responses
- **What breaks in Slack**: Slack's multiple interaction modes complicate agent design:
  - DMs, public channels, threads, emoji reactions, message edits, and deletions all serve as inputs
  - All of these must fit into a linear context window somehow
  - Message deletions should signal task cancellation
  - Message edits require updated responses
  - Users frequently abandon threads and start new DMs to the same person — the agent must roll over context from previous conversations
- **Interaction modes as input**: Unlike web apps with a single thread, Slack agents must handle a fundamentally multi-modal input surface
- **Advantages over web apps**: No context switching (agent is where work already happens), no separate tool to learn, agent feels like part of the team
- The approach positions the agent as a team member rather than an external service you visit

## Related
- [[Viktor]] — the platform using this interface paradigm
- [[Slack]] — the messaging platform serving as agent interface
- [[AI Employee]] — the role that naturally fits Slack-based interaction
- [[Company Agent]] — agent type using Slack as its living environment
- [[AgentHuman Collaboration]] — Slack as the collaboration surface
- [[Agent Channels]] — related concept about channel-based agent organization
- [[AgentSocialContext]] — understanding social dynamics in Slack
- [[summary-20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski]] — source
