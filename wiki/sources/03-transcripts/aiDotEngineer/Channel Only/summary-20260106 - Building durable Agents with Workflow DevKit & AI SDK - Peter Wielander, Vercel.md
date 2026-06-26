---
title: "Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel"
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel.md"
date: 2026-01-06
author: "Peter Wielander"
organization: "Vercel"
type: transcript
---

# Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel

## Core Thesis

The Workflow DevKit enables building durable, production-ready AI agents by adding a workflow orchestration layer that provides durability, resumability, observability, and human-in-the-loop capabilities with minimal code changes -- just extracting agent logic into a separate function and adding directives like `use workflow` and `use step`.

## Key Takeaways

1. **Workflow pattern for agents**: The workflow pattern separates agent code into deterministic orchestration and isolated steps, enabling retries, caching, and state persistence without custom queue/database wiring.
2. **Minimal refactoring**: Adding workflow support requires only: (a) extracting agent logic into a separate function, (b) adding `use workflow` directive, (c) marking tool calls with `use step`, and (d) calling the workflow via `start()`.
3. **Durable Agent class**: Vercel provides a `DurableAgent` class that wraps the AI SDK's `Agent` with `use step` markers on LLM calls under the hood.
4. **Built-in observability**: The `workflow web` CLI provides a local UI for inspecting runs, steps, inputs/outputs, and events -- same UI works for production deployments.
5. **Resumable streams**: Streams are decoupled from the API handler; clients can reconnect to a workflow stream at any point using the workflow ID, enabling durable sessions.
6. **Sleep and long-running agents**: Workflows can `sleep` for arbitrary durations (days, weeks) without consuming resources, then resume from the exact point where they paused -- enabling cron-like agent patterns.
7. **Human-in-the-loop via webhooks**: `createWebhook()` suspends the workflow until an external HTTP call arrives, with optional body schema validation -- making approval flows trivial.
8. **Step isolation in production**: Each step runs in its own serverless instance; only the orchestration layer is invoked briefly between steps, enabling infinite horizontal scaling.
9. **Versioning and upgrades**: Workflows are bound to deployments; new deploys are isolated from running workflows. An upgrade mechanism checks step signature compatibility for in-place migration.
10. **Platform-agnostic**: The TypeScript framework runs on any cloud; adapters connect to any storage/queue backend (Postgres, Redis, etc.), with first-party Vercel deployment as one option.

## Entities

- [[PeterWielander]] — Speaker from Vercel, presented the Workflow DevKit
- [[Vercel]] — Company behind the Workflow DevKit, AI SDK, and Next.js
- [[WorkflowDevKit]] — Open-source TypeScript library for building durable, observable workflows
- [[AISDK]] — Vercel's AI SDK providing `streamText`, `Agent`, and `useChat` for building AI applications
- [[NextJS]] — React framework used as the deployment target for the demo coding agent
- [[VercelSandbox]] — Vercel's sandbox service providing isolated VMs for running agent-generated code

## Concepts

- [[WorkflowPattern]] — Orchestration pattern separating code into deterministic orchestration and isolated, retryable steps
- [[DurableAgents]] — AI agents built on workflow infrastructure for durability, resumability, and production reliability
- [[ResumableStreams]] — Streams decoupled from API handlers that can be reconnected at any point using a workflow ID
- [[HumanInTheLoopWorkflows]] — Workflow suspension pattern using webhooks to pause execution until human approval
- [[DeterministicWorkflows]] — Workflow orchestration compiled into side-effect-free bundles for deterministic replay
- [[StepCaching]] — Automatic caching of step inputs/outputs enabling retry without re-execution and state rehydration
- [[AgentObservability]] — Built-in inspection of agent runs, steps, inputs, outputs, and events via a web UI

## Related

- [[WorkflowDevKit]]
- [[Vercel]]
- [[AISDK]]
- [[DurableAgents]]
- [[WorkflowPattern]]
