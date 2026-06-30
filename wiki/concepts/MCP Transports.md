---
title: "MCP Transports"
type: concept
tags: [mcp, protocol, stdio, http, serverless, web, agent-integration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors.md"]
last_updated: 2026-06-30
---

## Definition
MCP Transports are the communication protocols used by MCP servers to communicate with AI agents. The two primary transport modes are STDIO (standard input/output, for local processes) and HTTP (for web-based services). Choosing the right transport has significant implications for deployment, user experience, and scalability.

## Key Information
- **STDIO ("studio")**: Server runs as a local process spawned by the client. Communication happens via standard input and output. The server stays alive throughout the session. Users must configure a JSON string with command-line inputs, creating a poor UX for non-technical users.
- **HTTP**: Server runs as a web service listening at an HTTP endpoint. Communication happens via HTTP POST requests. Works well with serverless setups (Vercel edge functions, Cloudflare Workers). User experience is as simple as pasting a URL into agent settings.
- **STDIO UX pain**: Wiring up a STDIO-based MCP app requires a JSON string with command-line inputs that most users don't want to configure.
- **HTTP UX simplicity**: Users go to agent settings, give the connector a name, paste a URL (e.g., `/mcp`), and the server is connected. Demonstrated with Claude's MCP connector UI.
- **HTTP security**: Security and privacy concerns exist for both layers but are beyond the scope of RL Nabors's talk.
- **Serverless compatibility**: HTTP transport works well with serverless platforms like Vercel and Cloudflare, giving edge functions a natural use case for hosting MCP tools.

## Related
- [[summary-20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors]] — source transcript
- [[MCP]] — the Model Context Protocol
- [[RL Nabors]] — speaker who explained the transport modes
- [[StatelessTransportProtocol]] — Google's proposal for a stateless MCP transport (June 2026)
- [[MCP Apps]] — MCP extension that works with HTTP transport
- [[Serverless]] — deployment model compatible with HTTP transport
