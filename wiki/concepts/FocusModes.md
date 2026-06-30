---
type: concept
tags: [agents, design-pattern, UX, agent-architecture]
---

# Focus Modes

## Definition

Focus Modes is a design pattern for AI agents where the agent is put into a specific mode that constrains its action space and input space. Examples include planning mode, debug mode, and research mode. By limiting what the agent can do in each mode, the output quality improves on the smaller constrained surface, and user expectations are aligned with what the mode is designed to deliver.

## Key Information

- **Origin:** Identified by [[MarduSwanepoel]] ([[FlinnAI]]) in his aiDotEngineer talk "What the Best Agents Share" (2026-05-26).
- **Exemplar:** [[Cursor]] — offers a drop-down mode selector with distinct behaviors per mode.
- **Cursor's Modes:** Planning mode (no code, asks questions, produces a plan); Debug mode (hypothesis-driven, spins up a debug server, inspects logs).
- **Benefits:**
  - **For engineers:** Ability to refine the system prompt, drop tools, and optimize evals on a smaller, constrained space before expanding.
  - **For users:** Aligned expectations — users know what the agent will and won't do, and tailor their inputs accordingly.
- **Related Patterns:** Contrasts with "do anything" agent UIs where users don't know how to get the best result and have inflated expectations.

## Related

- [[MarduSwanepoel]] — Speaker who identified this pattern.
- [[Cursor]] — Exemplar agent implementing focus modes.
- [[TransparentExecution]] — Companion pattern: making agent actions visible.
- [[AgentPersonalization]] — Companion pattern: encoding user principles.
- [[Reversibility]] — Companion pattern: undo capabilities.
- [[AgentModes]] — Related concept: role-based agent configurations (ask, code, architect).
