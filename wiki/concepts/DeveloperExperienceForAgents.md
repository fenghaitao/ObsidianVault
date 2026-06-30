---
title: "Developer Experience for Agents"
type: concept
tags: [dx, agents, api-design, documentation, code-mode, self-documenting-tools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
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
- **Philipp Schmid's framing**: Agents don't see the code, don't have years of context from working on the API. They only see function schemas and docstrings. Tools must be self-documenting with semantic interfaces designed for agent consumption — don't assume long-term developer expertise. A `delete_item` endpoint that's self-explanatory to its creator is opaque to an agent without proper docstrings and error documentation

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker who framed agent-ready API design
- [[CodeMode]] — paradigm driving the need for agent-oriented DX
- [[AgentHarness]] — infrastructure where agents consume APIs
- [[CapabilityBasedSecurity]] — security model for agent API access
- [[SunilPai]] — speaker who presented the concept
- [[AgentReadyCodebases]] — related concept about making codebases consumable by agents
- [[Errors as Prompts]] — related concept: error messages as agent guidance
