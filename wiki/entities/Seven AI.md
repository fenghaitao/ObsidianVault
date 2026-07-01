---
title: "Seven AI"
type: entity
tags: [company, startup, agents, europe, coding-agents, openclaw, pi]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon.md"]
last_updated: 2026-06-29
---

## Definition
Seven AI is a small European startup founded by Matthias Luebken that builds AI agents for organizations. They focus on embedding coding agents into business products, demonstrated through a sales RFP processing system built on Pi and OpenClaw.

## Key Information
- Small startup based in Europe
- Focus: building agents for organizations — embedding coding agents into business workflows
- Built a production system for sales RFP processing: monitors email inboxes, routes requests to per-customer agents, generates draft email responses
- Architecture uses Pi's agent core and coding agent as the foundation, with OpenClaw for multi-channel orchestration
- Key patterns in their system:
  - One agent per customer, each with agent.md (general harness) and customer.md (customer-specific context)
  - Session reuse for context continuity per case
  - Backend systems (CRM, ERP) exposed as CLIs for agent consumption
  - Draft email generation as the output — users stay in their email workflow
- Exploring Nvidia's NeMo Claw for sandboxing and security

## Related
- [[Matthias Luebken]] — founder
- [[summary-20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon]] — source
- [[Pi (coding agent)]] — core agent framework
- [[OpenClaw]] — multi-channel agent platform
- [[Coding Agents as Building Blocks]] — core thesis
- [[Agent Session Reuse]] — key pattern
- [[AgentSpecific MD Files]] — agent.md/customer.md pattern
- [[MultiChannel Agent Routing]] — email routing pattern
- [[Nvidia]] — NeMo Claw sandboxing
