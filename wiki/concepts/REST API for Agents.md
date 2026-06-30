---
title: "REST API for Agents"
type: concept
tags: [api, agents, integration, n8n, webhook]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md"]
last_updated: 2026-06-29
---

## Definition
REST API for agents is the practice of exposing agent workflows as RESTful API endpoints, enabling other systems and workflows to invoke agent capabilities programmatically. In n8n, this is achieved via webhook triggers with RESTful path naming, turning agent workflows into callable services.

## Key Information

- **Implementation**: Use a webhook trigger node with a RESTful path (e.g., `/user` for POST to create a user). The webhook receives HTTP requests and passes data into the workflow
- **Use Case**: Liam McGarrigle built n8n's entire coupon generation system as a REST API in n8n in ~6 hours, abstracting all coupon systems (merch, enterprise, giveaway, cloud) behind a single entry point
- **Benefits**: Centralizes audit logs, credential management, and business logic. Other team members can integrate via standard REST API docs without knowing the internal workflow
- **Human-in-the-Loop**: REST API workflows can still include human review nodes — the workflow suspends until approval, and the API caller waits
- **Integration**: REST APIs built in n8n can be consumed by other n8n workflows or external tools, enabling composable agent architectures
- **Documentation**: n8n can generate Swagger-style API docs for webhook-triggered workflows

## Related

- [[n8n]] — platform for building REST APIs from workflows
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — source
- [[Webhooks for Agents]] — webhook pattern for agent integration
- [[Agent as a Service]] — exposing agents as callable services
- [[WorkflowPattern]] — underlying workflow architecture
