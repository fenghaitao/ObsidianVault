---
title: "MCP Security Cliff"
type: concept
tags: [security, mcp, production, deployment, stdio, http]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses.md"]
last_updated: 2026-06-30
---

## Definition
The MCP Security Cliff is the gap between local STDIO-based MCP deployment (a walled garden with no network exposure) and production Streamable HTTP deployment (requiring OAuth, token management, CORS, TLS, rate limiting, and more), where there is no gradual on-ramp — teams must implement all security concerns simultaneously.

## Key Information
- Coined by Tun Shwe (Lenses)
- **STDIO mode**: Local process, single user, no network exposure, no authentication needed. A walled garden that works beautifully for single-player developer productivity
- **Streamable HTTP transport**: Remote deployment, multiple clients connecting to the same server, horizontal scaling, centralized governance. This is where MCP becomes genuinely valuable to an organization
- **No gradual on-ramp**: Teams go from zero security surface to needing OAuth, token management, CORS configuration, TLS, rate limiting, and more all at once
- **Cannot stay local**: Stack lock testing showed STDIO transport fails with just 20 concurrent connections (20/22 requests failed), so scaling out requires crossing the chasm
- MCP becomes the single interface all clients use without worrying about API versions or scaling resources — but only if you cross the cliff
- "There's no halfway house because you can't do a little bit of production. You're either behind the wall or you're standing out in the open."

## Related
- [[summary-20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses]] — source
- [[TunShwe]] — coined the term
- [[StreamableHTTPTransport]] — the production transport that triggers the cliff
- [[MCP Transports]] — STDIO vs HTTP comparison
- [[MCPSecurityDesignPrinciples]] — design principles to apply before crossing the cliff
- [[MCP]] — the protocol
