---
title: "OWASP"
type: entity
tags: [organization, security, standards, mcp, web-security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses.md"]
last_updated: 2026-06-30
---

## Definition
OWASP (Open Web Application Security Project) is a nonprofit foundation that works to improve software security. It publishes the OWASP MCP Top 10, a list of the most critical security risks for MCP (Model Context Protocol) servers and agentic AI systems.

## Key Information
- Published the OWASP MCP Top 10 security vulnerability list for MCP servers
- #3 on the list: Tool Poisoning — embedding malicious instructions in tool descriptions that are invisible in the UI but executed by models
- #10 on the list: Context Injection and Oversharing — unfiltered data dumping PII, credentials, and system details into the agent context window, where they are one prompt injection away from exfiltration
- The MCP Top 10 was recommended by Tun Shwe (Lenses) as essential reading for anyone building MCP servers

## Related
- [[summary-20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses]] — source
- [[OWASPMCPTop10]] — the MCP-specific top 10 list
- [[ToolPoisoning]] — OWASP MCP #3
- [[ContextInjectionAndOversharing]] — OWASP MCP #10
- [[MCP]] — the protocol the Top 10 covers
