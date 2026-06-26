---
title: "Human-in-the-Loop Workflows"
type: concept
tags: [agents, workflow, human-review, orchestration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

# Human-in-the-Loop Workflows

## Definition

Human-in-the-loop workflows are a pattern where a workflow suspends execution at a specific point and waits for an external human action (typically via an HTTP request to a webhook URL) before resuming. This enables approval flows, manual interventions, and interactive decision points within otherwise autonomous agent pipelines.

## Key Information

- **Implementation in Workflow DevKit**:
  - `createWebhook()` generates a unique URL and suspends the workflow until an HTTP call arrives at that URL
  - The webhook can optionally validate the request body against a Zod schema before resuming
  - `respondWith()` allows the workflow to send a response back to the webhook caller
  - The webhook URL is deployment-specific (local host in development, production URL when deployed)
- **Observability**: The webhook suspension appears as a step in the workflow UI, showing that the workflow is paused waiting for human input
- **Use Cases**:
  - Approval gates before executing sensitive operations
  - Manual review of agent-generated content before publishing
  - Interactive debugging where a human can inspect state and decide next steps
- **Comparison to sleep**: Like `sleep`, `createWebhook` completely suspends the workflow (no resources consumed) until the external trigger arrives

## Related

- [[WorkflowDevKit]]
- [[DurableAgents]]
- [[WorkflowPattern]]
- [[StepCaching]]
- [[Human-in-the-Loop Orchestration]] — broader orchestration-level pattern
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
