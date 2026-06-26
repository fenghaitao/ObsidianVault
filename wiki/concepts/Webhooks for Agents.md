---
title: "Webhooks for Agents"
type: concept
tags: [agents, api, integration, patterns, event-driven]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
Webhooks for agents is an event-driven integration pattern where the agent platform sends HTTP notifications to a registered endpoint when a task starts and when it completes, eliminating the need for polling.

## Key Information
- Manus sends two webhooks per task: one when processing starts, one when the task completes
- Typical Manus task takes 3-5 minutes; complex tasks take longer
- Webhook payload includes task ID, task URL, status, and conversation output
- Enables event-driven architectures where the client only acts when notified
- Much more sustainable and cheaper than polling at scale (hundreds of concurrent tasks)
- Requires a publicly accessible endpoint (e.g., deployed via Modal, Cloudflare Workers)
- Registered webhooks appear in the Manus connector settings under "integrations built with Manus API"
- After receiving a webhook, clients can fetch the full conversation history via the task details API

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAPI]] — API supporting webhooks
- [[Agent Polling Pattern]] — simpler alternative for prototyping
- [[Agent Task States]] — states reported via webhooks
- [[Modal]] — deployment platform used in demo
