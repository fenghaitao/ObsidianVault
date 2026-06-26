---
title: "MCP Applications"
type: concept
tags: [mcp, protocol, ui, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md"]
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

## Related
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source
- [[MCP]] — the underlying protocol
- [[DavidSoriaParra]] — presenter who demonstrated MCP applications
- [[Anthropic]] — company developing the feature
