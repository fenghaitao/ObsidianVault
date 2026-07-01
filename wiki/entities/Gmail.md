---
title: "Gmail"
type: entity
category: service
tags: [service, email, google, integration, agent-tool]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md"]
last_updated: 2026-06-29
---

## Definition
Gmail is Google's email service, used as an integration target for AI agents. In n8n workshops, Gmail nodes (send message, get messages, reply, archive) are converted into tools that AI agents can call, with human-in-the-loop review intercepting destructive actions before execution.

## Key Information

- **Agent Integration**: n8n provides Gmail nodes that can be converted into AI agent tools
- **Available Actions**: Send email, get many messages, reply to message, archive email
- **Human-in-the-Loop**: Destructive actions (send, reply) are routed through human review nodes to prevent accidental sends
- **Fine-Grained Permissions**: Only explicitly configured fields (to, subject, message) are exposed to the AI agent
- **Authentication**: One-click OAuth setup with Google account
- **Field Descriptions**: Can add descriptions to individual fields (e.g., thread ID vs message ID) to guide the AI
- **Tool Prompting**: Node names and descriptions serve as tool names and descriptions passed to the LLM

## Related

- [[n8n]] — platform providing Gmail integration
- [[Google Calendar]] — companion service for calendar management agents
- [[Google]] — parent company
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — workshop source
- [[HumanInTheLoopWorkflows]] — pattern for intercepting email sends
- [[FineGrained Tool Permissions]] — field-level access control
