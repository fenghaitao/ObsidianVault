---
title: "MCP Apps"
type: entity
tags: [tool, mcp, protocol, ui, agents, standard]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors.md"]
last_updated: 2026-06-30
---

## Definition
MCP Apps is the first official extension to the Model Context Protocol, standardized in partnership with Anthropic and OpenAI. It enables MCP servers to ship interactive, branded UI chunks to chat hosts, with standardized bidirectional message passing between the UI and the host. It evolved from the earlier MCPUI project.

## Key Information
- First official MCP extension, co-developed with Anthropic and OpenAI
- Evolved from MCPUI, originally released by Ido Salomon in May 2025
- Enables servers to return UI as resources instead of text from tool calls
- Standardizes message passing: every UI interaction sends a message (notification, tool call, or prompt) back to the host
- Host renders UI in a sandboxed iframe for security
- Adopted by Claude, ChatGPT, VS Code, Cursor, Copilot, GitHub, Postman, Goose, LibreChat, Spy, and others
- ChatGPT recommends MCP Apps as the way to build ChatGPT apps
- Agnostic to UI generation method: supports predefined UI, declarative UI, and generative UI
- Write once, run everywhere: the same MCP App works across all supporting hosts
- Official repo and SDK: XApps
- Tri-weekly public work group meetings to push the standard forward
- Upcoming features: reusable views, agent-to-UI interaction (model clicking buttons/filling forms)
- Working on interoperability with A2UI (Google) and WebMCP
- **Practical implementation** (from RL Nabors): MCP Apps are single HTML files — everything must be embedded as base64. External resources (fonts, CDN assets) require CSP configuration. No localStorage, no network access (must call server via call server tool). Links require host permission (`appref current open link`). Set `visibility: app` on tools meant only for app interaction to prevent models from calling them directly. Design systems are valuable since fonts/CSS can be shared from the same server with CORS configured.
- **Real-world example**: RL Nabors built a comic reader MCP App for her web comics site, rendered inside Claude, with navigation, commentary, comments, and a text mode toggle showing the transcript. Built with V single file components sharing the site's design system.

## Related
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — source transcript
- [[summary-20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors]] — source (practical implementation)
- [[IdoSalomon]] — co-creator
- [[Liad Yosef]] — co-creator
- [[RL Nabors]] — built a comic reader MCP App as a practical demo
- [[MCPUI]] — predecessor project
- [[MCP]] — the underlying protocol
- [[MCPApplications]] — concept page
- [[Anthropic]] — co-developer of the spec
- [[OpenAI]] — co-developer of the spec
- [[XApps]] — official SDK and repo
- [[MCP Apps Message Passing]] — message passing concept
- [[MCP Apps UI Spectrum]] — notification/tool call/prompt spectrum
- [[WebMCP]] — interoperability target
- [[A2UI]] — interoperability target (Google)
- [[Chat as Lowest Common Denominator]] — UX problem MCP Apps addresses
- [[Browser as Infinite Canvas]] — vision MCP Apps supports
