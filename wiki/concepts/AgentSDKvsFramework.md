---
title: "AgentSDKvsFramework"
type: concept
tags: [concept, agents, claude-agent-sdk, frameworks, decision, architecture]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260326 - Everything You Thought About Building AI Agents is Wrong.md"
last_updated: 2026-06-20
---

## Definition

A decision framework from [[ColeMedin]] for *how* to build an AI agent: on a **batteries-included coding-agent SDK** ([[ClaudeAgentSDK]], Codex SDK) versus a **from-the-ground-up framework** ([[PydanticAI]], [[LangGraph]], etc.). Neither is universally right — the choice follows from who uses the agent and how much latency/scale/cost control you need.

## Key Information

### The two approaches

| | Coding-agent SDK | Framework |
|---|---|---|
| Examples | [[ClaudeAgentSDK]], Codex SDK | [[PydanticAI]], [[LangGraph]], n8n, OpenAI Agents SDK |
| Out of the box | prompting, tools, **managed conversation history**, [[SubAgent]]s, [[ClaudeSkills]], MCP, hooks, file search | you wire tools, memory, RAG, the agent loop yourself |
| Code | very little (one file) | more glue code |
| Speed | slower (reasoning overhead) | sub-second possible |
| Tokens | heavy / bloated | lean |
| Determinism / control | less | full control |
| Cost & ToS | subscription only when *you* are the sole user; multi-user → API key (expensive) | API billing scales economically |

### The decision (two questions)

1. **Who uses the agent?** Just you → SDK is fine. Many users / production → framework.
2. **Tolerance for latency & scale?** Some delay OK, no scaling → SDK. Must be fast and scale → framework.

Heuristic: **start with the simplest implementation.** Sometimes prototype tooling (skills/MCP) on the SDK, then migrate to a framework once you need scale. Most use cases make the choice obvious immediately.

### Frameworks aren't "behind"

You can add the modern niceties (skills, MCP) to a framework yourself — Cole's [[PydanticAI]] skills agent reimplements [[ProgressiveDisclosure]] and responds near-instantly versus ~10s on the bloated SDK. The framework route is more setup but yields speed, cost-efficiency, scale, and control (e.g. owning your own message history for [[AgentObservability]]).

### Why production usually means a framework

Two forces push deployed, multi-user agents to frameworks: **cost** (SDK token-heaviness + subscription-single-user ToS → expensive API usage at scale) and **performance/control** (sub-second latency, deterministic behavior, self-managed memory).

## Related

- [[ClaudeAgentSDK]] — the batteries-included option
- [[PydanticAI]] — the framework option Cole favors
- [[LangGraph]] — framework option for orchestration
- [[Codex]] — its SDK is the other batteries-included choice
- [[RetrievalAugmentedGeneration]] — the RAG decision that accompanies this one
- [[ColeMedin]] — articulator
- [[summary-20260326 - Everything You Thought About Building AI Agents is Wrong]] — primary source
