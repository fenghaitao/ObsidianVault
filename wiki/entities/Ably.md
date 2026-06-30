---
title: "Ably"
type: entity
tags: [company, real-time, messaging, pubsub, streaming, ai-transport, durable-sessions]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably.md"]
last_updated: 2026-06-30
---

## Definition

Ably is a real-time messaging platform that provides SDKs and APIs for live and interactive experiences, including AI experiences. The platform operates at scale — handling traffic for over 2 billion devices, 30+ billion monthly connections, and 2+ trillion API operations per month. Ably's core abstraction is channels (pub/sub), which serve as the foundation for building durable session layers in AI applications.

## Key Information

- **Core abstraction**: Channels — a pub/sub primitive where publishers and subscribers communicate through a shared, decoupled resource
- **Channel properties**: Independently addressable (any client/agent connects via channel name), persistent (messages outlive individual connections), fully resumable (automatic reconnect with event delivery from where left off)
- **Scale**: 2+ billion devices, 30+ billion monthly connections, 2+ trillion monthly API operations
- **AI Transport**: A drop-in SDK that builds durable session patterns on Ably channels — materializes text chunks into complete responses, provides automatic resumability, handles multiplexing for concurrent activity, supports multi-client bidirectional control
- **Additional AI tools**: Push notifications for async agent completion, APIs for shared/subscribable data objects for real-time collaboration between agents and users
- **Industry research**: Spoke with 40+ companies across 10 industries building AI agents, co-pilots, and assistants

## Related

- [[Mike Christensen]] — Staff Engineer and speaker
- [[Durable Sessions]] — the pattern built on Ably channels
- [[PubSub]] — the underlying messaging paradigm
- [[Live Control]] — capability enabled by the platform
- [[Server-Sent Events]] — the default protocol Ably's approach replaces
- [[summary-20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably]] — source
