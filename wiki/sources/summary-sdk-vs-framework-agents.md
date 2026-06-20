---
title: "summary-sdk-vs-framework-agents"
type: source
tags: [source, original-material, claude-agent-sdk, frameworks, rag, decision]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260326 - Everything You Thought About Building AI Agents is Wrong.md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] cuts through the "frameworks are dead, just build on the Claude Agent SDK" narrative with a nuanced decision framework: **coding-agent SDKs** ([[ClaudeAgentSDK]], Codex SDK) are batteries-included and great when *you* are the only user and some latency is fine; **frameworks** ([[PydanticAI]], [[LangGraph]]) are still the right choice for production agents that must be fast, cheap, scalable, and fully controllable. He also clarifies the RAG picture: not dead, but evolved to **agentic RAG**.

## Key Points

- **The "old way" (2024–2025)**: pick a framework → define tools → add [[RetrievalAugmentedGeneration|RAG]] (chunking/embedding/retrieval) → wire the agent loop yourself (state, memory, conversation history in your own DB, e.g. [[Neon]]). Powerful but lots of glue code.
- **The "new way"**: build *non-coding* agents on top of a coding-agent SDK. The [[ClaudeAgentSDK]] gives you, out of the box, built-in prompting + tools, **managed conversation history** (no DB needed), [[SubAgent]]s, [[ClaudeSkills]], [[ModelContextProtocol|MCP]], hooks, permissions, and **file search** (so often no RAG pipeline). Cole's whole Second-Brain heartbeat is one TypeScript file on the SDK.
- **Three SDK limitations**: (1) **slower** — reasoning overhead from all the built-in machinery; (2) **token-heavy/bloated** — goes hand-in-hand with the speed cost; (3) **less deterministic** — you don't control exactly how it operates. Plus the big one:
- **Cost / ToS limitation**: SDKs are token-heavy, so you typically run them on your *subscription* — but subscriptions are only licensed when **you alone** use the agent. Multi-user production requires an **API key** (expensive). This pushes most production agents back to frameworks.
- **Frameworks keep modern techniques**: you can add [[ClaudeSkills|skills]] and MCP to a [[PydanticAI]] agent yourself (Cole's skills-agent: dynamic system prompt + a skills directory; responds near-instantly vs ~10s on the SDK). More setup, but sub-second responses, full control over message history, and scale.
- **The decision framework — two questions**: *Who uses the agent?* and *What's your tolerance for latency/scale?*
  - Just you + delay OK + no scale → **SDK** (Claude Agent SDK / Codex SDK).
  - Many users + production + must be fast/scalable → **framework** (PydanticAI / LangGraph).
  - Start simplest; sometimes prototype tooling on the SDK, then migrate to a framework when you need to scale.
- **What happened to RAG** (broader than the coding-only take): 2024 = RAG everywhere; 2025 = file search rose (coding agents dropped vector DBs for grep), and a **LlamaIndex** study showed **file search beats RAG for *small* corpuses**; but for **large** knowledge bases (thousands of docs) semantic search is still more accurate *and* cheaper. 2026 = the middle ground, **agentic RAG** (give the agent semantic + grep + keyword and let it choose), with **Graph RAG** popular for massive/multi-codebase work. RAG is still needed for most non-coding agents and enterprise coding — Cole still spends real time on RAG strategies, even adding semantic search to SDK agents via skills/MCP.

## Related

- [[AgentSDKvsFramework]] — the decision framework distilled
- [[ClaudeAgentSDK]] — the batteries-included SDK side (+ its limitations)
- [[PydanticAI]] — the framework side (speed/scale/control)
- [[RetrievalAugmentedGeneration]] — the agentic-RAG middle ground
- [[SecondBrain]] — built on the SDK with custom RAG added
- [[Codex]] — its SDK is the other batteries-included option
