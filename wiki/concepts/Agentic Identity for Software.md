---
title: "Agentic Identity for Software"
type: concept
tags: [agents, identity, security, CI-CD, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
Agentic Identity for Software is the concept of providing identity and authentication for AI agents operating within the software development lifecycle, enabling controlled access, audit trails, and retry management at agent scale.

## Key Information
- Part of the [[Continuous Compute]] infrastructure stack described by [[HugoSantos]]
- Positioned after caching in the Continuous Compute pipeline architecture
- Enables retries at scale: agents need identity to manage retry logic and rate limiting
- Related to ingress shaping and rate limiting for agent intake
- Extends the [[AgentIdentity]] concept specifically to the software development domain
- Critical for governance in agent-native workflows: knowing which agent made which change
- Part of the shift where CI governance moves into the agent harness

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[Continuous Compute]] — paradigm requiring agentic identity
- [[AgentIdentity]] — broader concept of agent identity
- [[DelegatedAgentIdentity]] — related concept of identity delegation
- [[HardwareSoftware CoDesign for Caching]] — infrastructure stack containing agentic identity
