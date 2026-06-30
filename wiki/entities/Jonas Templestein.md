---
title: "Jonas Templestein"
type: entity
category: person
tags: [person, speaker, event-sourcing, stream-processors, agent-harness, iterate]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

Jonas Templestein is a software engineer at Iterate who advocates for building AI agent harnesses using pure event sourcing and stream processors. He presented a workshop at aiDotEngineer demonstrating events.iterate.com and the stream processor pattern for agent construction.

## Key Information

- **Affiliation**: Works at [[Iterate]], which he describes as a "hacker hobby club" rather than a commercial enterprise
- **Core philosophy**: Everything in an agent system should be an event in an append-only log — makes agents trivially debuggable and extensible
- **Key contribution**: events.iterate.com, a lightweight streaming event service for building event-sourced agents
- **Architectural positions**:
  - Against before hooks (pre-append filters) — prefers eventual consistency with timeouts
  - For distributed, polyglot agent extensions running on different machines
  - Agents should be publicly routable, internet-connected HTTP-speaking programs
  - Stream processors should be composable — "I made this extension. You made that extension. And you can combine them"
- **Workshop style**: Described as "improvised hackathon" — only decided to do the workshop the previous Monday, pushed SDK literally 1 minute before starting
- **Self-assessment**: Unsure whether the event-sourced agent approach is "dumb or cool" — seeking community feedback

## Related

- [[Iterate]] — company
- [[Misha]] — co-worker and co-presenter
- [[events.iterate.com]] — the streaming event service
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
- [[Event Sourcing]] — foundational architecture
- [[Stream Processor]] — core programming model
- [[Agent Harness]] — the system being built
- [[aiDotEngineer]] — conference
