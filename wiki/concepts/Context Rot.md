---
title: "Context Rot"
type: concept
tags: [agents, context-management, failure-mode, long-running]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md"]
last_updated: 2026-06-26
---

## Definition
Context rot is a failure mode in long-running AI agents where the context window becomes degraded after extended operation — typically signaled by "compaction" events — causing the agent to forget earlier context and produce unreliable results. It is a primary reason why chat is a poor interface for complex agent work.

## Key Information
- Manifests in long-running complex agents that do extensive research, spawn sub-agents, perform web searches, and write files over extended periods (e.g., 30+ minutes)
- Often signaled by a "compaction" event in the agent's trace — a known indicator that the agent is about to lose context
- When context rot occurs, the agent forgets earlier instructions and context, making subsequent interactions unreliable
- Example: after 30 minutes of work, a user asks the agent to fix clause three of a contract — compaction occurs, the agent forgets everything, and the resulting contract may have unintended changes beyond clause three
- Related to but distinct from context exhaustion (where the window fills up before work is done)
- Context rot is exacerbated by chat interfaces because chat is linear and cannot effectively represent the tree/DAG structure of complex work
- High-bandwidth artifacts help mitigate context rot by providing persistent, structured interfaces that don't depend on maintaining all context in a single linear thread

## Related
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source
- [[ContextExhaustion]] — related failure mode (window fills before work completes)
- [[Context Management]] — broader practice
- [[High-Bandwidth Artifacts]] — mitigation through persistent interfaces
- [[Agent-Human Collaboration]] — framework for avoiding context rot
- [[JacobLauritzen]] — described this failure mode
