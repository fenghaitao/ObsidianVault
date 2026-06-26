---
title: "Modal"
type: entity
tags: [platform, serverless, deployment, python]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
Modal is a Python serverless platform used for deploying webhook endpoints and Slack bot servers, providing public URLs for receiving agent task notifications.

## Key Information
- Provides $5 free credit for new accounts
- Used to deploy FastAPI endpoints for receiving Manus webhooks
- Supports simple KV store (Modal Dict) for persisting state across requests
- Used in the Manus API workshop to host both webhook receivers and Slack bot servers
- Enables quick prototyping of agent integrations without managing infrastructure

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAPI]] — API integrated via Modal
- [[Slack]] — Slack bot deployed on Modal
- [[Webhooks for Agents]] — pattern implemented with Modal
