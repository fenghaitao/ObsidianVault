---
title: "MCP Enterprise Challenges"
type: concept
tags: [mcp, enterprise, observability, access-control, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gateways are All You Need — Karan Sampath, Anthropic.md"]
last_updated: 2026-06-26
---

## Definition
MCP Enterprise Challenges refers to the three core problems enterprises face when adopting the Model Context Protocol at scale: observability, access control, and security — described by Karan Sampath as a "three-headed hydra."

## Key Information
- **Observability**: Enterprises lack visibility into who is using MCP servers, which tools are being used, which parts of the protocol aren't working properly, and how to improve tool definitions. Currently "completely opaque."
- **Access control**: No standardized way to ensure correct users have access to correct servers. Tools cannot be scoped to specific groups (e.g., read-only dashboard viewing vs. dashboard modification). Not something the community has worked on enough.
- **Security**: Two dimensions — (1) verifying server safety (correct protocols, preventing data exfiltration, preventing harmful tool usage on internal and external infrastructure), and (2) securing access from potentially untrusted remote clients to private enterprise data
- **Registry gap**: While MCP registries are useful and growing rapidly, they lack authentication, access control, observability, and credential management — all critical for enterprise use
- **Current bottleneck**: Teams can develop MCPs but can't deploy them; security teams are overloaded; C-suites see agents as ineffective. This bottleneck fundamentally restricts the MCP protocol and hurts agent adoption
- **Solution**: An MCP Gateway that centralizes these cross-cutting concerns, establishing a root of trust and enabling decentralized MCP development

## Related
- [[MCP]] — underlying protocol
- [[MCPGateway]] — proposed solution
- [[RootOfTrust]] — architectural principle for solving these challenges
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — source
