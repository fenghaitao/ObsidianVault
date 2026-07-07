---
title: "ContextAnxiety"
type: concept
tags: [model-behavior, context-window, harness-design, claude]
sources: ["raw/01-articles/claude/2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents.md"]
last_updated: 2026-07-07
---

## Definition

Context anxiety is a model behavior pattern where an AI agent rushes to finish its work as it nears the end of its context window, cutting work short rather than using the remaining room it has left. It was observed on [[Claude4.5Sonnet|Claude Sonnet 4.5]] and motivated a harness-level fix (context resets), but the behavior disappeared on [[Claude4.7Opus|Claude Opus 4.5]], turning the fix into overhead.

## Key Information

- **Observed on**: Claude Sonnet 4.5 — the model would prematurely wrap up tasks when approaching its context limit, even when it still had capacity remaining.
- **Initial fix**: Anthropic added context resets to the harness, baking in the assumption that Claude needed help staying coherent near the context limit.
- **Model evolution invalidated the fix**: On Claude Opus 4.5, the anxiety behavior was gone. The context resets that had been added to compensate became pure overhead with no benefit.
- **Implication for harness design**: This pattern illustrates why agent harnesses must evolve alongside model intelligence. A fix that improves behavior on one model generation can become a performance drag on the next. This is a key argument for managed agent platforms like [[ClaudeManagedAgents]], where the harness evolves with the model without requiring developer intervention.
- **Broader significance**: Context anxiety is an example of a deeper principle — harness assumptions are model-specific and decay over time. What helps one model may harm another, and maintaining a homegrown harness means constantly re-tuning for each model release.

## Related

- [[summary-2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents]] — source article
- [[Claude4.5Sonnet]] — the model that exhibited context anxiety
- [[Claude4.7Opus]] — the model on which the behavior disappeared
- [[ClaudeManagedAgents]] — the managed platform where harness evolution is handled automatically
- [[AgenticSurfaces]] — the broader evolution of agent-building interfaces
- [[ContextWindow]] — the underlying resource constraint that triggers the behavior
- [[AgenticLoop]] — the core pattern affected by context management
