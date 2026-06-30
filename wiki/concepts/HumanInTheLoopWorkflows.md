---
title: "Human-in-the-Loop Workflows"
type: concept
tags: [agents, workflow, human-review, orchestration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md"]
last_updated: 2026-06-29
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
- **n8n Human Review Node**: A visual node placed on a tool's output branch that intercepts tool calls before execution. The workflow cannot proceed past this node without human approval. Works with chat platforms (native n8n chat, Slack). Supports custom approve/deny buttons, custom messages showing tool parameters, and deny-by-response (typing anything denies). The agent is unaware of the review step — it calls the tool and n8n intercepts transparently
- **n8n Response Mode**: Chat trigger must be set to "using respond nodes" (not streaming) for human review to work. A "Send Message" chat node must be added after the agent to return responses
- **n8n Wait Time Limits**: Human review nodes can have a timeout (e.g., 10 minutes) after which the action is automatically denied, preventing indefinite workflow suspension
- **Multiple Tools Under One Review**: Multiple tool branches can share a single human review node, intercepting all of them without configuration changes

## Related

- [[WorkflowDevKit]]
- [[DurableAgents]]
- [[WorkflowPattern]]
- [[StepCaching]]
- [[Human-in-the-Loop Orchestration]] — broader orchestration-level pattern
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Paperclip]] — implements reviewer/approver human-in-the-loop gates for agent tasks
- [[AgentReviewerApprover]] — Paperclip's QA review and manager approval workflow pattern
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source (agent-human collaboration framework with trust and control dimensions)
- [[Agent-Human Collaboration]] — broader framework with trust and control dimensions
- [[Decision Log]] — non-blocking alternative: agents make decisions and log them for later human review instead of blocking
- [[Elicitation]] — asking the human at decision points, with non-blocking variant
- [[n8n]] — platform with visual human review nodes
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — source
- [[Visual Automation]] — visual workflow building with human review
- [[DeterministicGuardrails]] — human review as a hard block, not LLM-decided
