---
title: "Agent Orchestration"
type: concept
tags: [AI, agents, architecture, product-development]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/41 - Why AI is disrupting traditional product management ｜ Tomer Cohen (LinkedIn CPO).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/35 - We replaced our sales team with 20 AI agents—here's what happened next ｜ Jason Lemkin (SaaStr).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-10
---

## Definition

Agent orchestration is the architectural approach of coordinating multiple specialized AI agents to work together fluidly rather than sequentially, where agents can call upon each other (e.g., a trust agent working with a growth agent) to handle complex product development tasks.

## Key Information

- LinkedIn is building an orchestrator layer that coordinates its specialized agents (trust, growth, research, analyst, etc.).
- The goal is to eventually mask the individual agents behind a unified interface (e.g., a "product jammer agent" that internally orchestrates all other agents).
- Currently, agents are being built as standalone building blocks before the orchestrating layer is completed.
- The trust agent and growth agent are designed to work in a back-and-forth rather than sequentially.
- LinkedIn intentionally built separate agents (rather than one super-intelligent agent) to be able to rate and grade each agent's performance independently.
- This approach allows domain experts (e.g., head of trust) to build and own their specific agent.
- In the GTM/sales context at SaaStr: Amelia (chief AI officer) spends 20% of her time (~10-15 hours/week) orchestrating 20 AI agents, segmenting customer bases, and reviewing outputs to prevent agent conflicts.
- SaaStr hit "agent fatigue" at 20 agents — may not be able to add a 21st because the human orchestration burden is too high.
- There are no "master agents that can manage agents that can manage agents" yet in production — human oversight is still required for multi-agent environments.
- Running multiple agents requires careful base segmentation to prevent agents from conflicting with each other.
- [[Kiti Bottom]] warns that multi-agent systems are widely misunderstood: the common approach of dividing responsibilities by functionality and expecting agents to coordinate via peer-to-peer protocols (like a "gossip protocol") is extremely hard to control — especially in customer-facing use cases
- Supervisor-sub-agent patterns are more successful than peer-to-peer coordination, as they limit the ways the system can go off track
- For agentic coding, multi-agent patterns are more natural because coding agents are built for customizability and integration, not for solving fixed workflows

## Related

- [[summary-41 - Why AI is disrupting traditional product management ｜ Tomer Cohen (LinkedIn CPO)]] — source summary
- [[summary-35 - We replaced our sales team with 20 AI agents—here's what happened next ｜ Jason Lemkin (SaaStr)]] — source summary
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — additional source
- [[Trust Agent]] — orchestrated agent
- [[Growth Agent]] — orchestrated agent
- [[Research Agent]] — orchestrated agent
- [[Analyst Agent]] — orchestrated agent
- [[Full-Stack Builder Model]] — parent concept
- [[Agent Fatigue]] — consequence of multi-agent orchestration
- [[AI Sales Agents]] — GTM application of agent orchestration
- [[Multi-Agent Systems]] — the broader concept; peer-to-peer coordination is often misunderstood
