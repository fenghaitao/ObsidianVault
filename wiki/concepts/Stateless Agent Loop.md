---
title: "Stateless Agent Loop"
type: concept
tags: [agents, cloud, architecture, state, scalability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
Stateless Agent Loop is a cloud-native agent architecture where agent state can be toggled on or off, enabling horizontal scaling. It contrasts with the local-first approach of running sandboxes for every agent, which becomes unsustainable when there are hundreds of agents per person.

## Key Information
- Current approach: sandboxes for every agent running code locally — fine for millions of agents, but not for 100 agents per person
- As agent adoption scales, a cloud-native approach becomes necessary
- State must be something you can turn on or off — enabling stateless horizontal scaling
- Related to the Stateless Transport Protocol for MCP, which enables MCP servers to be treated like stateless REST servers
- Part of Matt Carey's prediction that more MCP clients will be built and deployed to the cloud
- Enables the "100 agents per person" future where each person has many specialized agents running concurrently

## Related
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source
- [[AgenticLoop]] — the core execution pattern
- [[StatelessTransportProtocol]] — related MCP transport proposal from Google
- [[MCP]] — protocol
- [[CloudBased Agent Sandboxes]] — deployment pattern
