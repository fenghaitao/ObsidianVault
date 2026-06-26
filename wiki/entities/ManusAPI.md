---
title: "Manus API"
type: entity
tags: [api, agents, tool]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
The Manus API is a programmatic interface for the Manus AI agent platform, providing the same capabilities as the web app — including sandboxed code execution, file uploads, connectors, and browser operation — with identical billing.

## Key Information
- Billing is identical to web app usage: same cost per query as a Manus chat
- Supports OpenAI responses SDK compatibility
- Two agent profiles: Manus 1.5 (complex tasks) and Manus 1.5 Light (simpler, faster queries)
- Features unlimited context management with smart KV caching for fast responses
- Three API pillars: task creation/management, file uploads, and webhooks
- File uploads auto-deleted after 48 hours; supports PDFs, images, JSON, and multimodal content
- Supports URL attachments for transcripts, PDFs, and other publicly accessible files
- Supports base64-encoded image attachments for visual tasks
- Connector UIDs enable pre-configured integrations (Gmail, Notion) out of the box
- Webhooks notify on task start and completion for event-driven architectures
- Documentation at open.manus.ai
- Base URL: api.manus.ai/v1

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAI]] — parent company
- [[Agent Task States]] — lifecycle states
- [[Agent Polling Pattern]] — basic integration pattern
- [[Webhooks for Agents]] — scalable integration pattern
- [[File Upload for Agents]] — context provision method
