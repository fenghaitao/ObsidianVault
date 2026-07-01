---
title: "MCP Security Design Principles"
type: concept
tags: [security, mcp, design, owasp, agent-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses.md"]
last_updated: 2026-06-30
---

## Definition
The MCP Security Design Principles are five rules for secure agentic design articulated by Tun Shwe (Lenses), based on the thesis that good MCP design and good MCP security are the same discipline. They provide protection against the OWASP MCP Top 10 before writing any OAuth code.

## Key Information
The five principles, articulated by Tun Shwe:

1. **Shrink the attack surface by design**: Think in terms of outcomes, not operations. Consolidate fine-grained API calls into coarse-grained outcome-oriented tools. One permission check, one audit log entry, one authorization point per outcome. "Fewer doors with fewer locks to manage."

2. **Constrain inputs at the schema level**: Use enums and flat dictionaries (avoid nested free-form payloads). Use typing libraries like Pydantic. Free-form string arguments passed downstream to shells, query engines, or APIs are the root cause of command injection flaws. Constrained inputs are easier to validate and harder to exploit.

3. **Treat documentation as a defensive layer**: Tool descriptions are a security surface. Write clear, complete, unambiguous instructions for every tool. Incomplete descriptions leave room for attacker-controlled tool descriptions in neighboring MCP servers to shadow yours (Tool Poisoning, OWASP MCP #3).

4. **Return only what the agent needs**: Strip payloads to the minimum. PII, internal identifiers, credentials, and system details in the context window are one prompt injection away from exfiltration (Context Injection and Oversharing, OWASP MCP #10). If the agent doesn't need it for its immediate task, don't return it.

5. **Minimize the blast radius**: Scope permissions at the tool and resource level, not the session level. Use MCP read-only annotations for non-destructive tools. Consider turning read-only tools into MCP resources. Every tool removed is an attack vector eliminated. You're building an interface, not a tool.

## Related
- [[summary-20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses]] — source
- [[TunShwe]] — author of the principles
- [[ToolPoisoning]] — OWASP MCP #3, addressed by principle 3
- [[ContextInjectionAndOversharing]] — OWASP MCP #10, addressed by principle 4
- [[OWASPMCPTop10]] — the vulnerabilities these principles protect against
- [[MCPSecurityCliff]] — what comes after the design phase
- [[MCPRBAC]] — principle 5 extended to production
- [[OutcomesOverOperations]] — Jeremiah Lowin's related concept (principle 1)
- [[MCP]] — the protocol
