---
title: "Agent Sandbox"
type: concept
tags: [agents, infrastructure, execution, docker]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
An agent sandbox is an isolated Docker-based execution environment provided per agent chat session, enabling the agent to install arbitrary packages, run code, set up services, and build full applications without affecting other sessions.

## Key Information
- Every Manus chat ships with its own sandbox, providing a full Docker image
- Supports installing any pip package, Redis (via BMQ), and other services
- Enables webhook support (e.g., Stripe) because the sandbox is a full application, not just a front-end
- Allows running multiple Selenium instances in parallel for web scraping
- Supports structured outputs, Whisper transcription, and any language model provider
- Future plans include autoscaling and warm deployments
- Differentiates from platforms that only provide front-end capabilities
- The sandbox is what enables general AI agents to do things verticalized products cannot

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAI]] — platform providing sandboxes
- [[General AI Agent]] — philosophy enabled by sandboxes
- [[Computer Use]] — related sandboxed browser approach
- [[Browser Use]] — related browser automation approach
