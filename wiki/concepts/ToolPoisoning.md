---
title: "Tool Poisoning"
type: concept
tags: [security, mcp, owasp, prompt-injection, agent-attack]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses.md"]
last_updated: 2026-06-30
---

## Definition
Tool Poisoning is OWASP MCP #3, a security vulnerability where attackers embed hidden instructions inside MCP tool descriptions that are invisible in the UI but are executed by the model without question.

## Key Information
- Ranked #3 on the OWASP MCP Top 10
- Works because agents enumerate every tool and read every description on every connection to an MCP server
- Hidden instructions in tool descriptions are invisible to human users reviewing the UI but the model will follow them without skepticism
- More tools means more surface area for injection attacks
- A poisoned tool description in a neighboring MCP server can shadow your own tools if your documentation is incomplete or ambiguous
- Mitigation: write clear, complete, unambiguous documentation for every tool to crowd out the space a poisoned neighboring server would try to fill
- Part of the "security shadow" cast by the Discovery dimension of agent-human differences (from Tun Shwe's extension of Jeremiah Lowin's framework)

## Related
- [[summary-20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses]] — source
- [[OWASPMCPTop10]] — the full top 10 list
- [[ContextInjectionAndOversharing]] — OWASP MCP #10
- [[SecurityShadow]] — the broader framework
- [[PromptInjection]] — related attack vector
- [[ToolCuration]] — mitigation strategy (fewer tools = less surface area)
- [[MCP]] — the protocol
- [[OWASP]] — organization
