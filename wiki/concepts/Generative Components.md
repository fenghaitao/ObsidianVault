---
title: "Generative Components"
type: concept
tags: [ui, agents, generative-ui, code-generation, mcp, sandbox]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman.md"]
last_updated: 2026-06-30
---

## Definition
Generative Components is the most advanced paradigm for AI-generated UI, where models generate HTML, CSS, and JavaScript on demand at runtime with no predefined components. The agent uses its code generation capabilities to create fully custom UI from scratch for each interaction.

## Key Information
- Models generate HTML/CSS/JS on demand at runtime — no predefined components, no translation layer
- The agent can call the same model (with reverse sampling) or another model to generate the UI code
- All UI is created by the agent — "there is no component, there is no translation"
- Represents the third era in Ruben Casas's three-era framework (static → declarative → generative)
- **Requires a distribution model** with boundaries, containment, and a sandbox
- MCP Apps provides the ideal distribution mechanism: authentication, tool calling, message passing, double iFrame sandbox
- **Trust problem**: if we don't trust third-party code, we shouldn't trust LLM-generated code presented directly to users
- **Ruben Casas's Postman experiment**: weather agent that goes to a weather API, creates a joke, generates HTML/CSS/JS all in one tool call — produces "random but very imaginative UI"
- Most personalized but also least predictable and most expensive (high token usage)
- Anthropic's Claude visualizer feature uses generative UI via MCP Apps under the hood

## Related
- [[summary-20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman]] — source transcript
- [[Ruben Casas]] — speaker who presented the concept and built the experiment
- [[GenerativeUI]] — broader concept this falls under
- [[Static UI Generation]] — first era in the framework
- [[Declarative UI]] — second era in the framework
- [[UI Generation Spectrum]] — overall framework
- [[MCP Apps]] — ideal distribution mechanism
- [[Double iFrame Sandbox]] — sandboxing mechanism required
- [[Anthropic]] — uses generative UI in Claude visualizer
- [[Postman]] — where the weather agent experiment was built
