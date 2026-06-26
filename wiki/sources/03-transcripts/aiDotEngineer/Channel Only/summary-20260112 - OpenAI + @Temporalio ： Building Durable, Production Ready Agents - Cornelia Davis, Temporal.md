---
title: "OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal"
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"
date: 2026-01-12
author: "Cornelia Davis"
organization: "Temporal"
type: transcript
---

# OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal

## Core Thesis

Temporal, an open-source distributed systems backing service, brings durability to AI agents built with the OpenAI Agents SDK by wrapping agent logic in Temporal workflows and tool calls in Temporal activities. This gives developers retries, state persistence, crash recovery, and horizontal scaling without writing infrastructure code — they program only the "happy path."

## Key Takeaways

1. **Agent definition**: An agent is distinguished from a GenAI application when the LLM has agency — the LLM decides the flow of the application, not the developer.
2. **OpenAI Agents SDK**: Launched ~May 2025, available in Python and TypeScript. Provides agents with tools, handoffs, guardrails, and tracing. Every `runner.run()` call corresponds to an independent agentic loop.
3. **Temporal as a backing service**: Like Redis or Kafka, Temporal is a backing service that delivers distributed systems durability. Developers program business logic (the "happy path") and Temporal handles retries, state management, and crash recovery.
4. **Two foundational abstractions**: **Activities** are chunks of work (external calls, heavy computation) wrapped with decorators for retries and state recording. **Workflows** orchestrate activities into business logic. When combined, they deliver the full durability magic.
5. **Event sourcing as a service**: Temporal records every activity call and return as events. If a process crashes, it replays the event history and picks up where it left off — no tokens re-burned, no work re-done.
6. **Dynamic activities**: Temporal allows calling activities by name at runtime without static registration, enabling generic agentic loops that can use any set of tools without code changes.
7. **OpenAI-Temporal integration**: OpenAI made the `Runner` class abstract in the Agents SDK so Temporal could provide a durable implementation. The integration provides `activity_as_tool()` to generate JSON tool descriptions from activity functions, and a plugin configures LLM retry policies.
8. **Durable agentic loop demo**: Cornelia showed an agent with three tools (get weather alerts, get IP address, get location from IP). When she killed the worker process mid-execution and restarted it, the agent resumed from where it left off via event sourcing — no tokens re-burned.
9. **Micro-agents**: Small, single-purpose agents analogous to microservices. Two orchestration modes in the Agents SDK: "just code" (sequential/parallel/loop orchestration) and "handoffs" (context switching within a single agentic loop).
10. **Human-in-the-loop**: Temporal makes human-in-the-loop trivial — the workflow simply waits, releases memory after a few seconds, and reconstitutes state when the human responds, even after days or weeks.
11. **Production usage**: Every Snapchat goes through Temporal, every Airbnb booking, Pizza Hut/Taco Bell orders, OpenAI Codex, OpenAI image gen, and Lovable all run on Temporal.

## Entities

- [[CorneliaDavis]] — Developer Advocate at Temporal, former Pivotal/Cloud Foundry engineer, author of a microservices book
- [[Temporal]] — Open-source distributed systems backing service providing durability for long-running workflows and agents
- [[OpenAIAgentsSDK]] — OpenAI's agent framework (Python/TypeScript) with tools, handoffs, guardrails, and tracing
- [[Cadence]] — Uber's workflow orchestration project that Temporal was forked from
- [[CloudFoundry]] — Early container technology incubated at VMware, predating Docker and Kubernetes
- [[Johan]] — Head of AI Engineering at Temporal

## Concepts

- [[AgenticLoop]] — The loop pattern where an LLM decides the flow, calling tools and routing results back until completion
- [[TemporalWorkflows]] — Business logic orchestrations in Temporal that compose activities with built-in durability
- [[TemporalActivities]] — Chunks of work in Temporal wrapped with decorators for retries, state recording, and durability
- [[DynamicActivity]] — Temporal feature allowing activities to be called by name at runtime without static registration
- [[DurableAgenticLoop]] — The combination of agentic loops with Temporal's durability for crash recovery and scaling
- [[MicroAgents]] — Small, single-purpose agents that do one thing well, analogous to microservices
- [[AgentHandoffs]] — OpenAI Agents SDK feature where one agent transfers control to another within the same agentic loop
- [[EventSourcing]] — Temporal's underlying mechanism: recording state changes as events to enable replay and crash recovery
- [[HappyPathProgramming]] — Temporal's philosophy: developers write only the success path, and the platform handles failures

## Related

- [[Temporal]]
- [[OpenAI]]
- [[OpenAIAgentsSDK]]
- [[DurableAgents]]
- [[AgenticLoop]]
- [[WorkflowPattern]]
