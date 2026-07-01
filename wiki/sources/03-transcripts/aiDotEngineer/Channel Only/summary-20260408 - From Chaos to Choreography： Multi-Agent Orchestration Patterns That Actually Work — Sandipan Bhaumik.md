---
title: "summary-20260408 - From Chaos to Choreography： Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik"
type: source
tags: [source, transcript, multi-agent, orchestration, distributed-systems]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - From Chaos to Choreography： Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik.md"]
last_updated: 2026-06-30
---

## Core Summary

Sandipan Bhaumik from Databricks presents production multi-agent orchestration patterns. Adding agents isn't like adding features — it's building a distributed system. He covers choreography vs orchestration, state management, failure recovery, and a real-world credit decisioning system where cache invalidation caused 20% incorrect risk ratings.

## Key Points

- One agent works beautifully. Five agents introduce coordination complexity that grows exponentially (5 agents = 10+ connections).
- Production war story: credit decisioning system with 5 agents. Cache invalidation failure caused risk agent to read stale credit scores, resulting in 20% wrong approvals.
- Choreography vs orchestration: decentralized event-driven vs centralized coordinator. Most teams pick one instinctively and regret it.
- Multi-agent is a distributed systems problem, not an AI problem. Most engineers didn't sign up for distributed systems.
- 18 years building distributed systems at AWS and Databricks inform these patterns.
- Coordination, state management, and failure recovery are the critical concerns, not model quality or prompts.

## Related

- [[SandipanBhaumik]] — speaker, Databricks
- [[Databricks]] — company
- [[MultiAgentOrchestration]] — core concept
- [[ChoreographyVsOrchestration]] — coordination patterns
- [[AgentStateManagement]] — state synchronization
- [[DistributedSystems]] — underlying discipline
