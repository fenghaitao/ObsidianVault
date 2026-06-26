---
title: "Agent Harness Separation"
type: concept
tags: [architecture, agents, mcp, enterprise, data-layer]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gateways are All You Need — Karan Sampath, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - The New Application Layer - Malte Ubl, CTO Vercel.md"]
last_updated: 2026-06-26
---

## Definition
Agent Harness Separation is the architectural principle of decoupling the agent runtime (the "harness") from where enterprise data lives and how MCP servers are structured, so that agents are not tightly coupled to data structure or MCP implementation details.

## Key Information
- Long-term vision for agent tech deployments as presented by Karan Sampath (Anthropic)
- Agents (the "orange box") should not be opinionated about data structure, and data/MCP layers should not be opinionated about which agents connect to them
- The MCP Gateway is the invariant layer that enables this separation — regardless of which agents an enterprise uses (in-house, external, Claude managed agents, custom SDK agents), the gateway remains
- Enables enterprises to quickly decide which agents to keep in-house vs. external without restructuring their MCP infrastructure
- Allows enterprises to invest strongly in opinionated MCP gateway primitives without worrying about agent design decisions
- Example: Claude managed agents (released recently) can connect to the same gateway as internally-built agents using the Claude Agent SDK
- Provides flexibility to meet wide-ranging agent needs of the future without lock-in
- **Malte Ubl's perspective**: Almost all currently popular agent harnesses have "fundamentally the wrong architecture" because they combine where the harness runs with where the generated code runs. Anthropic's new agent product (as of April 2026) separates these, which Malte praised as the correct approach. This separation is key to addressing the security nightmare that agent-based software faces.

## Related
- [[MCPGateway]] — the invariant layer enabling this separation
- [[MCP]] — underlying protocol
- [[DecentralizedMCPDevelopment]] — organizational pattern
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — source
- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — source (Malte's endorsement)
- [[Malte Ubl]] — endorsed the principle
- [[Anthropic]] — implemented in new agent product
- [[Sandboxing]] — related security concern
