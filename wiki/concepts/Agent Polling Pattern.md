---
title: "Agent Polling Pattern"
type: concept
tags: [agents, api, integration, patterns]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
The agent polling pattern is a basic integration approach where a client repeatedly checks the status of an agent task at fixed intervals until it reaches a terminal state (completed or error).

## Key Information
- Simplest way to get started with the Manus API for prototyping
- Client polls the task endpoint every ~20 seconds to check status
- Four possible states: running, pending, completed, error
- Pending state means the agent requires more input from the user (clarification, follow-up)
- Not viable at scale — keeping many workers polling wastes resources
- Webhooks are the recommended alternative for production applications
- Useful during initial development and testing before implementing webhook-based architectures

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAPI]] — API using this pattern
- [[Webhooks for Agents]] — scalable alternative
- [[Agent Task States]] — states being polled
