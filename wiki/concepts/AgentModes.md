---
title: "AgentModes"
type: concept
tags: [ai, agents, configuration, workflow]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md"]
last_updated: 2026-06-26
---

## Definition
Agent modes are role-based configurations for AI coding agents that specialize behavior for different phases of development. The three primary modes promoted by Kilo Code are: ask (research-only, cannot write files), code (implementation), and architect (planning). Modes enforce task separation and prevent the agent from jumping to implementation prematurely.

## Key Information
- **Ask mode**: Research-only — can chat and optionally read files, but cannot write files or start coding. Designed for understanding the system, exploring the codebase, and brainstorming edge cases.
- **Code mode**: Implementation — can write files, run tests, and make changes. Used only after research and planning are complete.
- **Architect mode**: Planning — specialized for creating detailed implementation plans with step-by-step instructions.
- Modes are part of a three-bucket agent configuration system: modes (role-based behavior), agents.md (always-on project rules), and skills (on-demand reusable playbooks)
- The mode paradigm prevents the common anti-pattern of jumping straight to code generation with insufficient context
- Modes can be tuned: what tools the agent can use independently, what requires human approval, file read/write permissions inside/outside the workspace
- Configuration should evolve as the user learns: start conservative, then adjust as comfort and understanding grow

## Related
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source transcript
- [[KiloCode]] — the tool that implements these modes
- [[ResearchPlanImplement]] — the workflow enabled by mode separation
- [[AgenticEngineering]] — the parent paradigm
- [[AgentsDotMd]] — complementary always-on configuration
- [[Skills]] — complementary on-demand configuration
