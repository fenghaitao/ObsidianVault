---
title: "Workflow DevKit"
type: entity
category: tool
---

# Workflow DevKit

## Definition

The Workflow Development Kit (Workflow DevKit) is an open-source TypeScript library by Vercel for building durable, observable, and production-ready workflows and AI agents. It provides an orchestration layer that separates code into deterministic workflow functions and isolated, retryable steps.

## Key Information

- **Creator**: Vercel
- **Type**: Open-source TypeScript library
- **Key Features**:
  - **Durable execution**: Steps run in isolated serverless instances with automatic input/output caching
  - **Resumability**: Workflows can pause (via `sleep`) and resume from any point, even after days or weeks
  - **Human-in-the-loop**: `createWebhook()` suspends workflows until external HTTP calls arrive
  - **Built-in observability**: `workflow web` CLI provides a UI for inspecting runs, steps, inputs, outputs, and events
  - **Streaming**: Decoupled streams that clients can reconnect to at any point using workflow IDs
  - **Versioning**: Workflows bound to deployments; supports in-place migration with step signature compatibility checks
  - **Platform-agnostic**: Runs on any cloud via adapters connecting to any storage/queue backend (Postgres, Redis, etc.)
- **Key Directives**:
  - `use workflow` — Marks a function as a workflow orchestration layer (compiled into a side-effect-free bundle)
  - `use step` — Marks a function as an isolated, retryable step
  - `start()` — Initiates a new workflow run
  - `sleep()` — Suspends the workflow for a specified duration
  - `createWebhook()` — Suspends the workflow until an external HTTP call
- **Companion Libraries**: `@workflow/next` for Next.js integration, `@workflow/react` for React, `DurableAgent` class for AI SDK integration
- **Status**: In beta as of January 2026; over 1 million workflows run per day internally at Vercel

## Related

- [[Vercel]]
- [[AISDK]]
- [[NextJS]]
- [[WorkflowPattern]]
- [[DurableAgents]]
- [[ResumableStreams]]
- [[HumanInTheLoopWorkflows]]
- [[DeterministicWorkflows]]
- [[StepCaching]]
- [[AgentObservability]]
