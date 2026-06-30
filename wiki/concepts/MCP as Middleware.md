---
title: "MCP as Middleware"
type: concept
tags: [mcp, framework, integration, web-development, nextjs]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
MCP as Middleware is the vision that MCP will become a native flag in web frameworks rather than a separate concern. When building an API service, MCP support will be enabled with a simple configuration flag (`MCP=true`), making every API endpoint automatically available as an MCP tool.

## Key Information
- Matt Carey's prediction: by end of year, MCP will be natively integrated into every TypeScript full-stack framework
- The MCP SDK is getting super lightweight — will literally just express the protocol itself
- It will be "silly for them not to have it" — frameworks will have native MCP integration
- Enables expressing thousands of APIs from one Next.js app with `MCP=true`
- Combined with programmatic tool calling on the client side, this makes large API surfaces accessible without context explosion
- The last blocker: fixing the SDK so it can fit in every bundle
- Represents MCP maturing from a separate protocol concern to an infrastructure primitive

## Related
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source
- [[MCP]] — the protocol
- [[NextJS]] — framework where MCP will be natively integrated
- [[CodeMode]] — complementary pattern for wide API surfaces
- [[ProgrammaticToolCalling]] — client-side pattern that pairs with MCP middleware
- [[MattCarey]] — presenter of this vision
