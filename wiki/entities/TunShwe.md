---
title: "Tun Shwe"
type: entity
tags: [person, ai-engineer, mcp, security, lenses]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses.md"]
last_updated: 2026-06-30
---

## Definition
Tun Shwe is the Head of AI at Lenses, an AI engineer focused on production MCP security and agentic AI design.

## Key Information
- Leads AI at Lenses, a data operating fabric for agentic AI
- Presented "Your Insecure MCP Server Won't Survive Production" at aiDotEngineer
- Extended Jeremiah Lowin's three-dimension framework (discovery, iteration, context) with a security shadow for each dimension
- Articulated the "MCP Security Cliff": the gap between local STDIO deployment and production HTTP deployment where all security concerns (OAuth, CORS, TLS, rate limiting) arrive simultaneously
- Proposed five principles for secure MCP design that protect against the OWASP MCP Top 10 before writing any OAuth code: shrink attack surface, constrain inputs at schema level, treat documentation as defensive layer, return only what the agent needs, minimize blast radius
- Core thesis: good MCP design and good MCP security are the same discipline

## Related
- [[summary-20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses]] — source
- [[Lenses]] — company where he leads AI
- [[JeremyFronae]] — co-presenter
- [[JeremiahLowin]] — whose framework he extended
- [[MCPSecurityDesignPrinciples]] — five principles he articulated
- [[MCPSecurityCliff]] — concept he named
- [[SecurityShadow]] — concept he introduced
- [[ToolPoisoning]] — OWASP MCP #3, discussed in his talk
- [[ContextInjectionAndOversharing]] — OWASP MCP #10, discussed in his talk
