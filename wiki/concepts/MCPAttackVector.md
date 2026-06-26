---
title: "MCPAttackVector"
type: concept
tags: [security, mcp, attack, llm, tool-calling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

The MCP (Model Context Protocol) attack vector exploits the asymmetry between what the user sees when approving a tool call (a simplified function name and one-liner description) and what the LLM actually reads (the full tool description, which can contain hidden instructions for data exfiltration).

## Key Information

- When using MCP, users approve external function calls based on a simplified summary (function name + short description)
- The LLM reads the full tool description which can contain hidden instructions — e.g., exfiltrating private keys and MCP credentials as hidden side-note parameters
- After user approval, the exfiltration occurs invisibly; the operation shows normal behavior and the user only sees the function result
- Reference publications document additional exploits including exfiltration of WhatsApp chat histories via MCP
- This is an example of the "iceberg effect": what the human reviewer sees is not what they are actually approving

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[MCP]] — the protocol being exploited
- [[Guardrails]] — defensive mechanism
- [[AgenticAttackVector]] — related attack class
