---
title: "summary-20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses"
type: source
tags: [source, transcript, mcp, security, owasp]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses.md"]
last_updated: 2026-06-30
---

## Core Summary

Tun Shwe and Jeremy from Lenses present five security principles for MCP server design. Good MCP design and good MCP security are the same discipline. Each design dimension (discovery, iteration, context) casts a security shadow: tool poisoning via descriptions, data leakage via retries, and context injection via oversharing.

## Key Points

- Five principles: (1) Shrink attack surface — consolidate fine-grained operations into coarse outcome-oriented tools. (2) Constrain inputs at schema level — use enums, reject free-form nested payloads. (3) Documentation as defense — clear descriptions crowd out poisoned neighboring servers. (4) Return only what the agent needs — strip PII, credentials, internal details. (5) Minimize blast radius — scope permissions at tool/resource level, use read-only annotations.
- Three design dimensions with security shadows: discovery (tool poisoning via descriptions), iteration (data leakage via retries), context (context injection/oversharing, OWASP MCP #10).
- OWASP MCP Top 10: tool poisoning (#3), context injection (#10), command injection via unconstrained strings.
- Lenses: data operating fabric providing trusted real-time context to agentic AI. Open-source MCP server applying production security learnings.

## Related

- [[TunShwe]] — speaker, Lenses
- [[Lenses]] — company, data operating fabric
- [[MCPSecurity]] — MCP server security
- [[OWASPMCP]] — OWASP MCP Top 10
- [[ToolPoisoning]] — attack vector
- [[ContextInjection]] — OWASP MCP #10
