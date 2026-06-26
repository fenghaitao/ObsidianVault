---
title: "Skills Over MCP"
type: concept
tags: [mcp, skills, protocol, extensibility]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md"]
last_updated: 2026-06-26
---

## Definition
Skills Over MCP is an upcoming MCP protocol extension that allows MCP server authors to ship domain knowledge (skills) directly with their servers, enabling continuous updates to agent instructions without relying on plugin registries or external mechanisms.

## Key Information
- Addresses the problem: large MCP servers with many tools need to ship domain knowledge about how to use those tools
- Allows server authors to continuously ship updated skills without relying on plugin mechanisms, registries, or other external infrastructure
- David Soria Parra: "it's very obvious that if you have a large MCP server with tons and tons of tools, you just want to ship the main knowledge with it and say, 'Oh, this is how you're supposed to use this'"
- Part of MCP's extension mechanism — some clients will support it, others won't (similar to how MCP applications only work with web-based interfaces)
- Can already be partially implemented today by giving the model a "load skills" tool, but the official semantics are being defined
- Announced as coming soon in the MCP roadmap

## Related
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source
- [[MCP]] — protocol
- [[Skills]] — the concept being shipped over MCP
- [[MCPApplications]] — another MCP extension
- [[DavidSoriaParra]] — presenter
