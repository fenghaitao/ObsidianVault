---
title: "Edge Agents"
type: concept
tags: [agents, architecture, http, internet, deployment]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

Edge Agents are AI agents designed to be publicly routable, internet-connected server programs that speak HTTP. Jonas Templestein argues that the moment an agent exists, it should have a URL — otherwise developers end up retrofitting connector concepts to get external inputs (Slack messages, web form submissions) into the agent.

## Key Information

- **Core principle**: Agents should be first-class internet citizens — not locked inside a single process or laptop
- **HTTP as universal interface**: An agent speaking HTTP can receive webhooks, serve web forms, integrate with any internet service without custom connectors
- **Digital entity concept**: "An intelligent entity, like a digital one, that's not a robot in the future. It's just an internet-connected server program"
- **Slack webhook parity**: Getting a Slack message into an agent should be as simple as receiving a webhook — "that's kind of like the same thing as a Slack webhook"
- **URL identity**: The agent's URL serves as its identity and address on the internet
- **Security concern**: In the proof-of-concept, there is no authentication — agents are publicly accessible. Jonas acknowledges this is "not very safe" and needs to be solved
- **Public namespace idea**: A temporary public namespace cleared every hour could enable experimentation where "anybody anywhere on the internet can just curl a thing and then suddenly have like a flavor of agent"

## Related

- [[Agent Harness]] — the broader system
- [[Push Subscriptions]] — the mechanism for external services to reach agents
- [[Durable Streams]] — the event log underlying edge agents
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
- [[Events.iterateCom]] — the implementation
