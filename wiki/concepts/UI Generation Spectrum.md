---
title: "UI Generation Spectrum"
type: concept
tags: [ui, agents, generative-ui, mcp, framework]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman.md"]
last_updated: 2026-06-30
---

## Definition
The UI Generation Spectrum is a three-era framework presented by Ruben Casas for understanding how AI agents generate user interfaces, ranging from static (agent as orchestrator passing props to predefined components) through declarative (agent generates JSON descriptors mapped to a design system) to generative (models write UI code on demand at runtime).

## Key Information

### Era 1: Static UI Generation
- Agent as orchestrator: makes tool calls, passes props/data to predefined static components
- Most common approach today
- Examples: AGUI Protocol, Goose Auto Visualizer
- Similar to traditional server-client rendering from the past 20 years

### Era 2: Declarative UI Generation
- Agent generates a descriptor (JSON, YAML, Python) mapped to a design system's predefined components
- More dynamic and personalized than static, but still constrained to existing components
- "Perfect balance" of flexibility and consistency today
- Examples: JSON Render (Vercel), Netflix server-driven UI
- Precedents: Netflix has been doing personalized server-driven UI for years

### Era 3: Generative Components
- Models generate HTML/CSS/JS on demand at runtime with no predefined components
- Most personalized, least predictable, most expensive
- Requires sandboxing, containment, and a distribution model
- MCP Apps is the ideal distribution mechanism
- Example: Ruben Casas's weather agent experiment at Postman

### The Inflection Point
- GPT 5.2 and Opus 4.5 (late 2025) made models extremely good at high-fidelity UI generation
- Models now write better front-end code than humans
- This capability enables the generative components paradigm

## Related
- [[summary-20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman]] — source transcript
- [[Ruben Casas]] — speaker who presented the framework
- [[Static UI Generation]] — first era
- [[Declarative UI]] — second era
- [[Generative Components]] — third era
- [[GenerativeUI]] — broader concept
- [[MCP Apps]] — distribution mechanism for generative UI
- [[GPT 5.2]] — inflection point model
- [[Opus 4.5]] — inflection point model
