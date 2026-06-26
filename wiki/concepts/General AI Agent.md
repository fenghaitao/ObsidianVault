---
title: "General AI Agent"
type: concept
tags: [agents, architecture, design-philosophy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
A general AI agent is an agent designed to handle a wide variety of tasks across multiple interfaces, rather than being specialized for a single vertical. The philosophy holds that building a general agent first enables far more capabilities than building verticalized products.

## Key Information
- Manus AI's core design philosophy: "build a general AI agent that you want to use in a variety of different ways"
- Meets users where they are: web app, Slack, API, iOS, mail, Microsoft 365, browser operator
- General agents with sandboxed execution environments can do things verticalized products cannot (e.g., install Redis, set up Stripe webhooks, run Selenium instances)
- Ivan Leo argues: "If you build a general AI agent instead of verticalized products, you can do so much more"
- The approach abstracts away infrastructure, sandboxes, and reliability concerns from the developer
- Contrasts with platforms that only provide a front-end without full application capabilities

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAI]] — company implementing this philosophy
- [[Agent Sandbox]] — enabling infrastructure
- [[Agent Connectors]] — integration mechanism
- [[Autonomous Coding Agents]] — related agent paradigm
