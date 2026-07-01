---
title: "VisualStudioCode"
type: entity
tags: [tool, editor, microsoft, ide, ai-coding, mcp, mcp-apps, mcp-host]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub.md"]
last_updated: 2026-06-30
---

## Definition

Visual Studio Code (VS Code) is a popular code editor developed by Microsoft. It serves as an MCP host, rendering MCP Apps in sandboxed iframes within its chat interface while using GitHub Copilot as its MCP client.

## Key Information

- **Developer**: Microsoft
- **MCP Host**: VS Code acts as the MCP host — it fetches HTML UI resources from MCP servers and renders them in sandboxed iframes within the chat. GitHub Copilot serves as the MCP client handling LLM communication and tool calling.
- **MCP App Rendering**: When an MCP server returns a tool result with a UI resource reference, VS Code (the host) fetches the HTML and renders it in a sandboxed iframe. The iframe isolates the app from VS Code settings, APIs, and external access.
- **MCP Server Discovery**: VS Code's extensions tab allows searching for MCP servers by typing `@MCP`. Microsoft recommends using the VS Code server list for security rather than downloading random servers from the internet.
- **Usage by Poolside**: Used as the interface for their Malibu Agent coding assistant demo
- **Features in Demo**: Live diff view showing streaming changes, file creation tracking, integrated terminal for testing
- **Significance**: Currently the dominant form factor for AI coding assistants, though Poolside expects form factors to evolve
- **Kilo Code integration**: Kilo Code provides VS Code integration with right-click "add to Kilocode" for selected code sections, at-mentioning for context, slash commands, and autocomplete for both code and prompting

## Related

- [[summary-20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub]] — source (MCP Apps hosting)
- [[MCP Apps]] — protocol for interactive UI rendered in VS Code
- [[MCP]] — underlying protocol
- [[GitHubCopilot]] — MCP client within VS Code
- [[Microsoft]] — developer
- [[Sandboxed Iframe]] — security mechanism for MCP App rendering
- [[Poolside]]
- [[MalibuAgent]]
- [[AICodingAgents]]
- [[KiloCode]] — provides VS Code integration
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source (Kilo Code VS Code integration)
