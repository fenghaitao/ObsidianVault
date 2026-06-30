---
title: "Temporal"
type: entity
tags: [company, open-source, distributed-systems, workflow, durability, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md"]
last_updated: 2026-06-26
---

## Definition
Temporal is an open-source distributed systems backing service that provides durability for long-running workflows and agents. It allows developers to program only the "happy path" business logic while the platform handles retries, state management, crash recovery, and scaling. Temporal was forked from Uber's Cadence project and has been around for 5-6 years.

## Key Information
- **Open source**: Vast majority MIT licensed, some Apache 2.0 in the Java SDK
- **Age**: Around 5-6 years old, well predates the GenAI boom
- **Origin**: Forked from Uber's Cadence project
- **Business model**: Temporal Cloud (SaaS) available in 15+ AWS regions and multiple Google Cloud regions, with multi-region namespaces
- **SDK support**: Formally supports 7 programming languages (Python, TypeScript, Java, Go, etc.); Apple released a Swift SDK
- **Production usage**: Every Snapchat goes through Temporal, every Airbnb booking, Pizza Hut/Taco Bell orders, OpenAI Codex, OpenAI image gen, Lovable
- **Two foundational abstractions**:
  - **Activities**: Chunks of work (external API calls, heavy computation) wrapped with decorators for retries and state recording
  - **Workflows**: Orchestrations that compose activities into business logic with built-in durability
- **Event sourcing**: Records every activity call and return as events; replays event history to recover from crashes without re-executing completed work
- **Dynamic activities**: Can call activities by name at runtime without static registration, enabling generic agentic loops
- **Worker architecture**: Workers are multi-threaded processes that pull work from event queues; typically run several hundred threads per worker
- **Latency**: Activity calls add tens of milliseconds of overhead to communicate with the Temporal server
- **Streaming**: Not natively supported yet but is a top priority; customers have built streaming on top of Temporal
- **Large payload storage**: Another top priority — pass data by reference instead of by value for LLM payloads
- **Self-hosting**: Supports relational databases and Cassandra as backing stores
- **Conference**: Replay conference held annually, typically at Moscone in San Francisco

## Related
- [[CorneliaDavis]] — Developer Advocate
- [[Johan]] — Head of AI Engineering
- [[Cadence]] — predecessor project from Uber
- [[OpenAIAgentsSDK]] — integration partner
- [[Codex]] — runs on Temporal
- [[OpenAI]] — Codex and image gen run on Temporal
- [[summary-20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer]] — source (Uber spinout)
- [[Uber]] — origin company
- [[Chronosphere]] — another Uber spinout
- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source (mentioned as comparable workflow solution)
- [[Effect]] — has comparable workflow/clustering capabilities
