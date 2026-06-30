---
title: "summary-20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman"
type: source
tags: [source, transcript, ai, generative-ui, mcp, mcp-apps, ui, agents, declarative-ui, human-agent-collaboration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman.md"]
last_updated: 2026-06-30
---

## Core Summary
Ruben Casas (staff engineer at Postman) presents a framework for understanding the evolution of AI-generated UI, arguing we are moving through three paradigms: static UI (agent as orchestrator passing props to predefined components), declarative UI (agent generates descriptors like JSON mapped to a design system), and generative components (models write HTML/CSS/JS on demand at runtime). He argues MCP Apps is the ideal distribution mechanism for generative UI because of its built-in sandboxing (double iFrame), authentication, and message passing. The ultimate future is not just generative UI but collaborative human-agent experiences where shared artifacts like Excalidraw canvases become the new interface — moving beyond components entirely toward true collaboration.

## Key Points

### Three Eras of AI-Generated UI
- **Static UI (Today's Default)**: Agent as orchestrator makes tool calls, passes props/data to predefined static components. AGUI protocol and Goose Auto Visualizer exemplify this. Similar to traditional server-client rendering where the agent generates the data but components are pre-built by developers.
- **Declarative UI (Current Sweet Spot)**: Agent generates a descriptor (JSON, YAML, Python) mapped to a design system's predefined components. More personalized and dynamic than static, but still constrained to existing components. Netflix's server-driven UI is a precedent. JSON Render by Vercel is a leading tool. This is the "perfect balance" of flexibility and consistency today.
- **Generative Components (Next Frontier)**: Models generate HTML/CSS/JS on demand at runtime with no predefined components. Requires sandboxing, containment, and a distribution model. The most personalized but also the least predictable and most expensive.

### The Inflection Point
- GPT 5.2 and Opus 4.5 (late 2025) marked an inflection point — models became extremely good at high-fidelity UI generation, writing better front-end code than humans
- Casas demonstrated this when a model spontaneously added a search box with blur animation and accessibility to his blog rewrite
- In 3 years, we went from "a few lines of code is great" to "models write better front-end code than me"

### MCP Apps as the Distribution Model
- Generative UI needs a distribution model with boundaries, containment, and sandboxing
- MCP Apps provides: authentication, tool calling, message passing between UI and agent, double iFrame sandbox by default
- Anthropic's visualizer feature uses MCP Apps for first-party UI delivery — strategically significant because they could have built their own rendering mechanism
- If Anthropic uses MCP Apps for first-party UI, others should consider it too

### Beyond Components: Human-Agent Collaboration
- The Excalidraw MCP App creates a shared canvas where humans and agents collaborate — not just output/visualization but a bidirectional workspace
- Users can click around, modify UI traditionally while the agent also contributes
- This collaborative experience represents the future beyond static, declarative, or even generative components

### The "New Computer" Metaphor
- Andrej Karpathy: interacting with this new computer is like talking to the terminal — the GUI hasn't been invented yet
- We are like the early TV era when shows were "radio with cameras" — we cannot yet imagine what this new medium will enable
- The question is not just "where does the UI run" (third-party in super app vs. chat everywhere) but "what is the model generating"

### Open Questions
- Is chat the final interface? Is MCP Apps the final form? Neither is settled.
- The "Jarvis moment" of floating UI windows that appear and disappear hasn't arrived
- Consumers will decide which paradigm wins
- We are still in the radio era of this new technology

## Related
- [[Ruben Casas]] — speaker, staff engineer at Postman
- [[Postman]] — company, generative UI experiment
- [[MCP Apps]] — ideal distribution mechanism for generative UI
- [[MCP]] — underlying protocol
- [[GenerativeUI]] — the fully model-generated end of the spectrum
- [[Declarative UI]] — middle ground approach
- [[Static UI Generation]] — current default paradigm
- [[Generative Components]] — runtime model-generated UI code
- [[UI Generation Spectrum]] — static → declarative → generative
- [[AGUI Protocol]] — SDK for mapping tool calls to React components
- [[Goose Auto Visualizer]] — Goose feature for auto-visualizing data
- [[Goose]] — MCP client with visualizer feature
- [[JSON Render]] — Vercel tool for declarative UI via JSON/YAML
- [[Vercel]] — creator of JSON Render
- [[Excalidraw MCP App]] — shared canvas for human-agent collaboration
- [[Excalidraw]] — drawing tool underlying the MCP app
- [[Anthropic]] — uses MCP Apps for first-party visualizer feature
- [[GPT 5.2]] — inflection point model for UI generation
- [[Opus 4.5]] — inflection point model for UI generation
- [[AndrejKarpathy]] — "new computer" metaphor
- [[Agent-Human Collaboration]] — the future beyond components
- [[Double iFrame Sandbox]] — MCP Apps sandboxing mechanism
- [[Agent as Orchestrator]] — static UI paradigm
- [[Netflix]] — precedent for server-driven personalized UI
- [[Sandboxed Code Execution]] — containment requirement for generative UI
- [[Agents on Canvas]] — shared artifact collaboration pattern
- [[Chat as Lowest Common Denominator]] — critique of chat-only interfaces
- [[End of Apps]] — related vision of UI evolution
