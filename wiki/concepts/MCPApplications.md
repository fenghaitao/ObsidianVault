---
title: "MCP Applications"
type: concept
tags: [mcp, protocol, ui, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-26
---

## Definition
MCP Applications are a feature of the Model Context Protocol that allows an MCP server to ship its own user interface, rendered by the client without plugins, SDKs, or client-side code generation. The server defines the UI and the client renders it, enabling the same application to work across different MCP clients like ChatGPT, VS Code Cursor, and Claude.

## Key Information
- An agent ships its own interface over an MCP server — not through a plugin, not through an SDK, not rendered on the fly by the model on the client side, and not hardcoded into the product
- The same MCP server can be placed into cloud, ChatGPT, VS Code Cursor, and it will just work
- Requires semantics on both sides (client and server) to understand how to render the UI
- An MCP server can ship both an application (for human interaction) and tools (for model interaction) — a unique capability not yet widely explored
- Demonstrated as an experimental feature in the MCP protocol
- Primarily supported by web-based interfaces; CLI clients have difficulty rendering HTML
- Under the hood, Anthropic's graph rendering product feature is an MCP application
- Part of the "rich semantics" that MCP offers over alternatives like CLI-based connectivity
- Standardized as MCP Apps, the first official MCP extension, co-developed with Anthropic and OpenAI
- Evolved from MCPUI, originally released by Ido Salomon in May 2025
- Supports three UI generation approaches: predefined UI (company-built black box), declarative UI (structured JSON, host renders components), and generative UI (model-generated)
- Adopted by Claude, ChatGPT, VS Code, Cursor, Copilot, GitHub, Postman, Goose, LibreChat, Spy, and others
- Write once, run everywhere: the same MCP App works across all supporting hosts
- Standardizes bidirectional message passing: UI interactions send messages (notification, tool call, or prompt) back to the host
- Upcoming features: reusable views, agent-to-UI interaction
- Working on interoperability with A2UI (Google) and WebMCP

## Related
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source
- [[MCP]] — the underlying protocol
- [[DavidSoriaParra]] — presenter who demonstrated MCP applications
- [[Anthropic]] — company developing the feature
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — source (MCP Apps standardization)
- [[MCP Apps]] — the standardized MCP extension
- [[MCPUI]] — predecessor project
- [[IdoSalomon]] — creator of MCPUI, co-creator of MCP Apps
- [[Liad Yosef]] — co-creator of MCP Apps
- [[OpenAI]] — co-developer of the spec
- [[MCP Apps Message Passing]] — standardized message passing mechanism
- [[MCP Apps UI Spectrum]] — notification, tool call, prompt message types
- [[Predefined UI]] — black-box company-built UI approach
- [[Declarative UI]] — structured JSON UI approach
- [[GenerativeUI]] — model-generated UI approach
- [[Reusable Views]] — upcoming performance feature
- [[Agent-to-UI Interaction]] — upcoming model-driven UI interaction feature
- [[A2UI]] — Google's generative UI protocol, interoperability target
- [[WebMCP]] — related protocol, interoperability target
