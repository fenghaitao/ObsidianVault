---
title: "Make it Easy for Agents"
type: concept
tags: [architecture, agents, cli, design-pattern, coding-agents, agent-embedding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon.md"]
last_updated: 2026-06-29
---

## Definition
Make it Easy for Agents is an architectural pattern for designing systems that coding agents can effectively interact with. Instead of building complex APIs or integrations, expose system functionality through simple, composable CLIs that agents can discover and use autonomously.

## Key Information
- Articulated by Matthias Luebken after a conversation with Evan at AIE Code Summit
- Core principle: think about what the coding agent is good at, and build your system so the agent can easily access it
- Agents are really good at using CLIs — expose backend systems (CRM, ERP) as CLIs rather than complex APIs
- Cohere's Excel skill exemplifies the pattern: instead of building a complex Excel integration, they wrapped existing CLI tools (Pandas, OpenPyXL, LibreOffice) into a skill
- Ken Thompson's Unix philosophy is the guiding principle: "Write programs that do one thing and do one thing well" — build small, focused tools that agents can compose
- In Seven AI's sales system, CRM and ERP data access is exposed as CLI tools that per-customer agents call
- Data security is maintained through sandboxing — the CLIs run in a controlled environment
- Contrasts with building monolithic integrations — the pattern is about making the system legible and composable for agents
- Related to the broader "don't try to be complex" philosophy: design for the agent's strengths (tool calling, shell access) rather than building abstractions that hide functionality

## Related
- [[summary-20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon]] — source
- [[Coding Agents as Building Blocks]] — the broader thesis this pattern enables
- [[CLI for Agents]] — the specific pattern of exposing tools as CLIs
- [[BashAsUniversalAdapter]] — related pattern for agent-tool interaction
- [[Ken Thompson]] — Unix philosophy as guiding principle
- [[Cohere]] — Excel skill as canonical example
- [[Seven AI]] — company implementing this pattern in sales automation
- [[Matthias Luebken]] — speaker who articulated the pattern
- [[Agent Sandboxing]] — security layer for CLI access
