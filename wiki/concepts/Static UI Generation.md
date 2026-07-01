---
title: "Static UI Generation"
type: concept
tags: [ui, agents, mcp, static-ui, components]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman.md"]
last_updated: 2026-06-30
---

## Definition
Static UI Generation is the current default paradigm for AI-generated UI, where the agent acts as an orchestrator making tool calls that pass props and data to predefined static components created by developers. The agent generates the data, but the UI components are pre-built.

## Key Information
- The agent is just an orchestrator: makes a tool call via MCP Apps or direct agent tool call
- Parameters and data are passed to predefined static components created by developers
- Similar to traditional server-client rendering — the server sends data, the client renders it with pre-built components
- Very similar to what UI development has been doing for the past 20 years
- **AGUI Protocol**: SDK where client tools map to React components; tool calls pass props mapped to static components
- **Goose Auto Visualizer**: accepts any data, matches and organizes it, passes to predefined visualization components
- Most common way of generating UI today
- Contrasts with declarative UI (agent generates JSON descriptors) and generative components (agent writes UI code at runtime)
- Represented by Ruben Casas as the first era in the three-era framework of AI-generated UI

## Related
- [[summary-20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman]] — source transcript
- [[Ruben Casas]] — speaker who presented the framework
- [[AGUI Protocol]] — SDK exemplifying static UI
- [[Goose Auto Visualizer]] — Goose feature exemplifying static UI
- [[Declarative UI]] — next era in the framework
- [[Generative Components]] — third era in the framework
- [[UI Generation Spectrum]] — overall framework
- [[Agent as Orchestrator]] — the agent's role in this paradigm
- [[Predefined UI]] — related concept in MCP Apps context
