---
title: "Agent as Orchestrator"
type: concept
tags: [agents, ui, static-ui, orchestration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman.md"]
last_updated: 2026-06-30
---

## Definition
Agent as Orchestrator describes the role of AI agents in the static UI generation paradigm: the agent makes tool calls and passes props/data to predefined static components, but does not generate the UI itself. The agent orchestrates the data flow while developers build the components.

## Key Information
- The agent's role in static UI generation: orchestrator, not creator
- Agent makes tool calls via MCP Apps or direct agent tool call
- Parameters and data are passed to predefined static components built by developers
- The client renders the components — the agent never touches UI code
- Similar to a server sending data to a client where the client renders the UI
- Very similar to how UI has worked for the past 20 years
- Contrasts with declarative UI (agent generates JSON descriptors) and generative components (agent writes UI code)
- Ruben Casas argues this is the most common paradigm today but insufficient for the future

## Related
- [[summary-20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman]] — source transcript
- [[Ruben Casas]] — speaker
- [[Static UI Generation]] — the paradigm it describes
- [[Declarative UI]] — next level of agent involvement
- [[Generative Components]] — full agent UI generation
- [[UI Generation Spectrum]] — overall framework
- [[AGUI Protocol]] — SDK exemplifying this role
- [[Goose Auto Visualizer]] — feature exemplifying this role
