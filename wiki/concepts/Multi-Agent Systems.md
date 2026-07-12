---
title: "Multi-Agent Systems"
type: concept
tags: [AI, agent, architecture, multi-agent]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md"]
last_updated: 2026-07-11
---

## Definition

Multi-agent systems are AI architectures where multiple agents work together to solve problems. According to Kiti Bottom, these systems are misunderstood — the common approach of dividing responsibilities by functionality and expecting agents to coordinate via peer-to-peer protocols is extremely hard to control. Supervisor-sub-agent patterns are more successful.

## Key Information

- **The misunderstood approach**: "I have this incredibly complex problem. Now I'm going to break it down into: hey you are this agent, take care of this. You're this agent, take care of this. And now if I somehow connect all of these agents, they think they're the agent utopia." — This is not how it works.
- **The problem**: Peer-to-peer agent coordination (like a gossip protocol) is incredibly hard to control — especially in customer-facing use cases where you need to manage which agent replies to the customer and shift guardrails everywhere.
- **What works better**: Supervisor-agent patterns — one supervisor agent with sub-agents that do the actual work. This limits the ways the system can go off track.
- **Current model capabilities**: "I don't think current ways of building and current model capabilities are right there" for peer-to-peer multi-agent coordination.
- **Alternatively**: Use a single larger agent that orchestrates everything, or have humans orchestrate individual agents for specific tasks.
- **Coding agents**: A different case — coding agents are built for customizability and integration, not for solving fixed workflows. This makes multi-agent patterns more natural in the coding domain.

## Related

- [[Agent Orchestration]] — related concept for managing agents
- [[Agency-Control Trade-off]] — why controlling multi-agent systems is hard
- [[Kiti Bottom]] — who identified this as misunderstood
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
