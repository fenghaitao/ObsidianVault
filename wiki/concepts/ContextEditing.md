---
title: "ContextEditing"
type: concept
tags: [context, agents, token-management, performance, agentic]
sources: ["raw/01-articles/claude/2025-09-29 - Managing context on the Claude Developer Platform.md"]
last_updated: 2026-06-28
---

## Definition

Context editing is an automatic context management mechanism that removes stale tool calls and their results from within the context window when an agent is approaching token limits. It preserves conversation flow while discarding accumulated tool output that is no longer needed, effectively extending how long an agent can operate without manual intervention.

## Key Information

- **Trigger**: Activates automatically when the agent approaches the context window token limit.
- **Behavior**: Removes stale tool call/result pairs while preserving the surrounding conversation structure.
- **Effect on performance**: Keeps only relevant context in-window, which increases effective model performance because Claude focuses on current, pertinent information.
- **Compared to manual truncation**: Developers previously had to choose between cutting agent transcripts (losing information) or accepting degraded performance; context editing automates this trade-off.

## Measured Results

- **29% performance improvement** over baseline (alone) on an internal agentic search evaluation.
- **39% performance improvement** when combined with the memory tool.
- **84% reduction in token consumption** in a 100-turn web search evaluation, while still enabling agents to complete workflows that would otherwise fail due to context exhaustion.

## Availability

- Public beta on the [[Anthropic]] Claude Developer Platform (released September 2025).
- Also available natively via [[AmazonBedrock]] and [[VertexAI|Google Cloud Vertex AI]].
- Works with [[Claude4.5Sonnet]], which has built-in context awareness to track available tokens.

## Related

- [[ContextWindow]] — the fundamental resource that context editing manages
- [[AgenticMemory]] — complementary capability; memory tool stores information outside the context window
- [[AIAgent]] — the primary consumer of context editing; enables longer-running agentic workflows
- [[Claude4.5Sonnet]] — the model with built-in context awareness that powers this feature
- [[AmazonBedrock]] — cloud platform where context editing is available
- [[VertexAI]] — cloud platform where context editing is available
- [[Anthropic]] — introduced context editing in September 2025
- [[summary-2025-09-29 - Managing context on the Claude Developer Platform]] — source article
