---
title: "Figma"
type: entity
tags: [tool, design, multimodal, requirements, mcp, mcp-apps]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub.md"]
last_updated: 2026-06-30
---

## Definition
Figma is a collaborative design tool used to create visual UI designs. In agentic workflows, Figma designs can serve as multimodal requirements that AI agents read and compare against actual implementations. Figma is also using MCP Apps to generate design components on the fly within chat interfaces.

## Key Information
- Used in Baz's spec reviewer as a source of visual requirements alongside ticket descriptions.
- The spec reviewer reads Figma designs multimodally (as images) to understand intended visual layouts.
- Enables AI agents to perform visual verification by comparing Figma designs against screenshots of actual implementations.
- Combined with ticket text requirements to give agents a complete picture of what was asked of developers.
- **MCP Server**: Figma provides an MCP server that agents can connect to. In the XAA demo, Figma's MCP server was automatically connected via Okta SSO without a consent screen
- **Sensitive Data**: Figma contains sensitive design data that IT teams may not want arbitrary AI agents to access
- **MCP Apps adoption**: Using MCP Apps to generate design components that render directly in chat, keeping the design workflow within the conversational interface

## Related
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]] — source
- [[summary-20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub]] — source (MCP Apps adoption)
- [[Baz]] — company using Figma in spec reviewer
- [[Playwright]] — used to capture screenshots for comparison
- [[CrossAppAccess]] — XAA enables automatic Figma MCP connections
- [[MCP]] — Figma as MCP server
- [[MCP Apps]] — protocol for generating design components in chat
