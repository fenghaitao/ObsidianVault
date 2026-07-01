---
title: "Sandboxed Iframe"
type: concept
tags: [security, mcp, mcp-apps, iframe, sandbox, isolation, ui]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub.md"]
last_updated: 2026-06-30
---

## Definition
The sandboxed iframe is the security mechanism used by MCP Apps hosts (like VS Code) to render interactive HTML UI from MCP servers. The iframe isolates the app from the host's settings, APIs, and any external access, preventing malicious or buggy apps from affecting the development environment.

## Key Information
- **Purpose**: Isolates MCP App UI from the host application (VS Code), preventing the app from accessing VS Code settings, internal APIs, or making unauthorized external connections
- **Analogy**: Liam Hampton compares it to putting a hamster in a cage — "if you don't let it loose in a room, it's just going to chew things up." The iframe keeps the app contained and safe.
- **Architecture**: The host (VS Code) fetches HTML from the UI resource reference returned by the MCP server and renders it inside the iframe. The app communicates back to the host via standardized MCP message passing (notifications, tool calls, prompts).
- **Bidirectional communication**: While the iframe sandboxes the app, it still allows controlled communication back to the host via MCP message passing, and the app can call back to its MCP server for fresh data
- **Host vs Client**: The host (VS Code) handles rendering and sandboxing; the client (GitHub Copilot) handles LLM communication and tool calling. This separation means the iframe isolation is the host's responsibility
- **Use case**: Enables rich interactive UIs (charts, diagrams, forms, checkout flows) to render safely within chat interfaces without compromising the development environment

## Related
- [[summary-20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub]] — source
- [[MCP Apps]] — protocol using sandboxed iframes
- [[MCP]] — underlying protocol
- [[VisualStudioCode]] — host that implements sandboxed iframe rendering
- [[MCP Apps Message Passing]] — communication mechanism within the sandbox
- [[Agent Sandbox]] — broader concept of agent isolation
- [[Liam Hampton]] — introduced the hamster-in-a-cage analogy
