---
title: "Model Tiering"
type: concept
tags: [model-selection, cost-optimization, agent-systems]
sources: ["raw/01-articles/claude/2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system.md"]
last_updated: 2026-07-07
---

## Definition

Model tiering is the practice of matching AI model tiers (differing in capability, cost, and latency) to specific task complexity within an agent system — using stronger models for strategic reasoning and orchestration, mid-tier models for structured planning and sequencing, and smaller models for narrowly scoped, well-defined operations.

## Key Information

### CodeRabbit's Tiered Approach

[[CodeRabbit]]'s [[AgentOrchestration|agent orchestration system]] matches each [[Claude]] model tier to task complexity to optimize for cost and latency:

- **Opus** drives the orchestration loop and higher-level strategic work: understanding the problem and setting overall direction.
- **Sonnet** takes Opus's output and sequences it into structured planning steps.
- **Haiku** handles narrowly scoped operations like context distillation and targeted tool use, where the question is specific enough that a smaller model can answer it well.

### Decision Framework

The assignment of model to task is guided by evaluation data rather than intuition. As [[CodeRabbit]] VP of AI David Loker states: "If Haiku does as well as Sonnet on a given task, we use Haiku. If the evaluation harness tells us the plan quality improves when we give Opus more room, we give it more room. We don't guess."

### Benefits

- **Cost optimization**: using smaller, cheaper models for tasks they can handle well reduces overall system cost.
- **Latency optimization**: smaller models respond faster for narrowly scoped operations.
- **Capability matching**: reserving the most capable models for the hardest problems ensures quality where it matters most.

## Related

- [[summary-2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system]] — source summary
- [[AgentOrchestration]] — the orchestration pattern model tiering supports
- [[CodeRabbit]] — company that implements this pattern
- [[Claude]] — the model family being tiered
- [[TokenOptimization]] — related concern in agent system design
