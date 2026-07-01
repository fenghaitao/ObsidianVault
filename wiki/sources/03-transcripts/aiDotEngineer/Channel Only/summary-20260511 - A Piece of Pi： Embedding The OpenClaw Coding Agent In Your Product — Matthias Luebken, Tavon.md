---
title: "summary-20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon"
type: source
tags: [source, transcript, coding-agents, openclaw, pi, agent-architecture, agent-embedding, product-integration, agent-extensions, multi-agent, session-reuse, sandboxing, cli-for-agents, agent-hooks]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon.md"]
last_updated: 2026-06-29
---

## Core Summary
Matthias Luebken from Seven AI presents a practical guide to embedding coding agents into products using Pi (the open-source agent framework) and OpenClaw. He walks through the progression from the core agent loop (LLM + tools in a loop) to the coding agent (adds shell/runtime) to the OpenClaw multi-channel architecture. The centerpiece is a real-world sales automation system that monitors email inboxes, routes requests to per-customer agents (each with agent.md and customer.md context files), reuses sessions for continuity, exposes backend systems via CLIs, and generates draft email responses — all built on Pi's extensibility. Key architectural patterns: make systems easy for agents (expose CLIs, not complex APIs), use sessions for context continuity, and leverage extension APIs for UI interaction beyond the terminal.

## Key Points

### From Agent Core to Coding Agent to OpenClaw
- **Agent Core**: An LLM agent that runs tools in a loop — goals → context → tool calls → results → loop. Pi's agent core is a TypeScript class with event system and tool injection hooks.
- **Coding Agent**: Same thing, but adds a runtime and shell (typically bash). The shell gives the agent access to system tools like FFmpeg, which it can discover and compose on its own.
- **OpenClaw**: Built on Pi's core packages — adds multi-channel routing, plugin support, sub-agent orchestration, gateway support, and provider orchestration on top of Pi's session, agent core, and coding agent components.

### Example: OpenClaw Discovering FFmpeg
- Peter Steinberger sent a voice message to OpenClaw, which didn't have a native voice message plugin
- OpenClaw autonomously created and used tools, eventually discovering FFmpeg on the local machine
- From the outside it looks like "learning," but internally it's just another tool call available through the shell — demonstrating the power of a coding agent's runtime access

### Cohere's Excel Skill Pattern
- Cohere bundles coding agent capabilities into domain-specific skills (e.g., Excel)
- The Excel skill doesn't talk to Excel directly — it uses small CLI tools (Pandas, OpenPyXL, LibreOffice) packaged into a skill
- This is a pattern for embedding coding agent capabilities into products: wrap CLI tools as skills

### Extension API: UI Interaction and Session Events
- Pi's extension API enables slash commands, session event hooks, and UI interaction (select dropdowns, context UI)
- Matthias demonstrated a CRM pipeline command that loads contacts and presents a UI selection — all within the terminal
- Same extension mechanism works for web UIs: Pi can build a web UI with the same selection patterns
- Currently the framework is catered to coding agent use cases, but the vision is broader application integration

### Architectural Pattern: Make It Easy for Coding Agents
- Design your systems so coding agents can easily work with them
- Agents are really good at using CLIs — expose system functionality as CLIs rather than complex APIs
- Cohere's Excel skill is the example: instead of building a complex Excel integration, they wrapped existing CLI tools

### Real-World System: Sales RFP Processing
- **Email monitoring**: Inbox is monitored for incoming requests for proposals (RFPs)
- **Gateway routing**: Email is routed to the appropriate agent based on customer context
- **Per-customer agents**: One agent per customer, each with:
  - **Agent MD**: General harness — how to use the system, how to react to inputs/outputs
  - **Customer MD**: Customer-specific context — quirks, access levels, discounts
- **Session reuse**: Each case gets a session that is created and reused for back-and-forth context continuity
- **CLI tools**: Backend systems (CRM, ERP) are exposed as CLIs that agents can call
- **Draft generation**: Output is a draft email that stays in the user's inbox — users stay in their email workflow
- **Sandboxing**: Data is secured in a sandbox; Nvidia's open shell approach (via NeMo Claw) is being explored for security

### Event Hooks for Enterprise Control
- `beforeToolCall` hook: Inject authorization checks, role-based access, enterprise features before a tool executes
- Event subscriptions: Subscribe to tool call results, stream events for monitoring
- These hooks make the agent controllable in enterprise contexts

### Key Takeaways
- Coding agents are and will be a core building block for software systems
- Pi is perfect for tinkering — it's minimal, open source, and you can rip things apart and put them together
- There are no established patterns yet — we're in the "fuck around and find out" phase
- Go tinker: open Pi and ask it to build what you want

## Related
- [[Matthias Luebken]] — speaker, co-founder of Seven AI
- [[Seven AI]] — company building agents for organizations
- [[Pi (coding agent)]] — the open-source agent framework
- [[OpenClaw]] — multi-channel coding agent built on Pi
- [[Coding Agents as Building Blocks]] — core thesis
- [[Make it Easy for Agents]] — architectural pattern
- [[Agent Session Reuse]] — pattern for context continuity
- [[AgentSpecific MD Files]] — agent.md and customer.md pattern
- [[MultiChannel Agent Routing]] — routing emails to per-customer agents
- [[AgentExtensibility]] — Pi's extension API
- [[AgentHooks]] — beforeToolCall and event hooks
- [[CLI for Agents]] — exposing systems via CLIs
- [[Agent Sandboxing]] — security via sandboxing
- [[Cohere]] — example of bundling coding agent as product skill
- [[LibreOffice]] — tool used by Cohere's Excel skill
- [[FFmpeg]] — tool discovered autonomously by OpenClaw
- [[Nvidia]] — NeMo Claw sandboxing
- [[Ken Thompson]] — Unix philosophy quoted: "Write programs that do one thing and do one thing well"
- [[MarioZechner]] — creator of Pi
- [[PeterSteinberger]] — creator of OpenClaw, voice message example
- [[LeadQualificationAgents]] — related CRM use case
- [[AgentInboxProcessing]] — related inbox monitoring pattern
- [[MultiAgentArchitecture]] — related multi-agent pattern
- [[aiDotEngineer]] — event host
