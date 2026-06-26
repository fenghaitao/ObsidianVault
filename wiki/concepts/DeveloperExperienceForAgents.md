---
title: "Developer Experience for Agents"
type: concept
tags: [dx, agents, api-design, documentation, code-mode]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md"]
last_updated: 2026-06-26
---

## Definition
Developer Experience for Agents is the practice of designing APIs, documentation, and error handling for consumption by AI agents (LLMs generating code) rather than exclusively for human developers. As agents become the primary consumers of APIs, the design of these interfaces must account for how agents discover, understand, and use them.

## Key Information
- Presented by Sunil Pai: "Your next billion users are these little robots that are generating code for you"
- Your customers are still humans, but the things interacting with your systems are agents
- Agents "don't hang out in the pub, they hang out in registries" — they discover APIs through code and documentation
- Agents "dream in types and syntax errors"
- Key design principles:
  - **Documentation as markdown**: agents consume docs programmatically
  - **Errors that guide agents**: error messages should tell the agent what to do next
  - **Discoverability via search**: agents need to find the right API endpoints
  - **Typed APIs**: agents benefit from type checking and syntax validation
- Several companies are already doing this well
- Part of the broader shift toward treating agents as first-class consumers of software interfaces
- Connects to capability-based security: agents should only have access to explicitly granted capabilities

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[CodeMode]] — paradigm driving the need for agent-oriented DX
- [[AgentHarness]] — infrastructure where agents consume APIs
- [[CapabilityBasedSecurity]] — security model for agent API access
- [[SunilPai]] — speaker who presented the concept
- [[AgentReadyCodebases]] — related concept about making codebases consumable by agents
