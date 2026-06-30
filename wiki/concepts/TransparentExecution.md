---
type: concept
tags: [agents, design-pattern, UX, trust]
---

# Transparent Execution

## Definition

Transparent Execution is a design pattern for AI agents where the agent's thinking, tool calls, assumptions, and progress are made fully visible to the user. The core goal is to shift the dynamic from delegation (agent produces a result) to collaboration (user is part of the process). This builds trust in outputs and enables early user intervention if the agent goes wrong.

## Key Information

- **Origin:** Identified by [[MarduSwanepoel]] ([[FlinnAI]]) in his aiDotEngineer talk "What the Best Agents Share" (2026-05-26).
- **Exemplars:**
  - **[[ClaudeCode]]:** Shows a progress/to-do list of completed and pending steps, context being used, skills drawn from, and all tool call inputs/outputs.
  - **[[Manifold]]:** Shows task progress — completed and pending tasks, what it examined, and its interpretation.
- **Benefits:**
  - **Trust:** Sharing the process, thoughts, assumptions, and uncertainties builds trust in the outcome.
  - **Reduced waste:** Users can intervene early (e.g., at step 2) if the agent reads the wrong sources or takes the wrong approach.
- **Key Insight:** Shifts from delegation to collaboration — the user is part of the process, not just a recipient of the result.

## Related

- [[MarduSwanepoel]] — Speaker who identified this pattern.
- [[ClaudeCode]] — Exemplar agent with progress lists and visible tool calls.
- [[Manifold]] — Exemplar agent with transparent task progress.
- [[FocusModes]] — Companion pattern: constraining action space per mode.
- [[AgentPersonalization]] — Companion pattern: encoding user principles.
- [[Reversibility]] — Companion pattern: undo capabilities.
- [[AgentObservability]] — Related concept: built-in inspection of agent runs and steps.
