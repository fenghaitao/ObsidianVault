---
title: "Context Injection and Oversharing"
type: concept
tags: [security, mcp, owasp, context, prompt-injection, pii]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses.md"]
last_updated: 2026-06-30
---

## Definition
Context Injection and Oversharing is OWASP MCP #10, a security vulnerability where MCP servers return unfiltered data into the agent's context window, exposing PII, credentials, internal identifiers, and system details that can be exfiltrated via prompt injection.

## Key Information
- Ranked #10 on the OWASP MCP Top 10
- Turns the agent's context window into a liability: every piece of sensitive data in context is one prompt injection away from exfiltration
- An agent has to load all context before making a decision, making it vulnerable to poisoned hay in the haystack
- The agent simply won't notice if some of the context is poisoned — it's finding a needle in a haystack
- Mitigation: strip payloads to the minimum. If the agent doesn't need a piece of data for its immediate task, don't return it. Curate and aim to expose the smallest amount of information.
- Related to the "security shadow" cast by the Context dimension: agents have limited context (~200K tokens) with no intuition, so unfiltered data in that limited window is a critical vulnerability
- Also related to the Iteration dimension: agents retry with full conversation history including previously returned data, creating cumulative data leakage risk

## Related
- [[summary-20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses]] — source
- [[OWASPMCPTop10]] — the full top 10 list
- [[ToolPoisoning]] — OWASP MCP #3
- [[SecurityShadow]] — the broader framework
- [[PromptInjection]] — the exfiltration mechanism
- [[DataMaskingForAgents]] — mitigation: masking PII before agent exposure
- [[MCP]] — the protocol
- [[OWASP]] — organization
- [[Context Management]] — broader context discipline
