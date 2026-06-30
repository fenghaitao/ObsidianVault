---
type: concept
tags: [agents, design-pattern, personalization, memory]
---

# Agent Personalization

## Definition

Agent Personalization is a design pattern where the agent is given the thoughts, systems, knowledge, principles, and patterns that the user would have used if they were doing the task themselves. The fundamental goal is to optimize for speed-to-understanding (not just speed-to-outcome): the agent must grasp the nuances and implicit preferences of the user to do the right thing, not just something.

## Key Information

- **Origin:** Identified by [[MarduSwanepoel]] ([[FlinnAI]]) in his aiDotEngineer talk "What the Best Agents Share" (2026-05-26).
- **Core Problem Addressed:** Many agents optimize for speed-to-outcome but not speed-to-understanding — they generate output quickly, but if it doesn't align with how the user would have done it, it's useless.
- **Exemplars:**
  - **[[Harvey]]:** Uses playbooks (legal firm methods and principles for tasks like contract review) and memory (persisting learnings across interactions).
  - **[[ClaudeCode]]:** Uses skills, connectors, and systems to increase the knowledge base and personalize the agent.
- **Key Insight:** Personalization enables a quicker speed-to-understanding, helping the agent do the right thing rather than just something.

## Related

- [[MarduSwanepoel]] — Speaker who identified this pattern.
- [[Harvey]] — Exemplar agent with playbooks and memory.
- [[ClaudeCode]] — Exemplar agent with skills and connectors.
- [[FocusModes]] — Companion pattern: constraining action space per mode.
- [[TransparentExecution]] — Companion pattern: making agent actions visible.
- [[Reversibility]] — Companion pattern: undo capabilities.
- [[ContextEngineering]] — Related concept: curating what goes into an agent's context window.
