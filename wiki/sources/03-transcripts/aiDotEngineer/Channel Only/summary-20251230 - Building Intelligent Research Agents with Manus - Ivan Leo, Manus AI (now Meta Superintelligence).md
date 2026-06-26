---
title: "Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)"
type: source-summary
source: raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md
author: aiDotEngineer
date: 2025-12-30
---

## Core Thesis

Ivan Leo from Manus AI demonstrates the newly launched Manus API and argues that building a general AI agent first — rather than verticalized products — enables far more capabilities. By meeting users where they are (web, Slack, API, iOS, mail, Microsoft 365, browser), Manus provides a customizable platform for building complex agentic applications without managing infrastructure, sandboxes, or reliability.

## Key Points

- **Manus 1.5**: Re-architected models with increased quality, speed, and user satisfaction, scaling to millions of daily conversations.
- **General AI Agent Philosophy**: Manus is designed as a general agent usable across many interfaces — web app, Slack, API, iOS, mail, Microsoft 365, and browser operator — rather than a verticalized product.
- **API Fundamentals**: The Manus API mirrors the web app experience: same billing, same capabilities. Tasks have four states (running, pending, completed, error). The API supports file uploads (auto-deleted after 48 hours), URL attachments, base64-encoded images, and connector UIDs.
- **Webhooks Pattern**: For scalable agent applications, webhooks replace polling. Manus sends notifications when tasks start and complete, enabling event-driven architectures.
- **Slack Bot Integration**: A live-coded demo builds a Slack bot using Modal for deployment, with multi-turn conversation support via a simple KV store mapping thread IDs to task IDs.
- **Browser Operator**: A new feature that opens tabs on the user's local computer, enabling authenticated platform interactions (LinkedIn, Instagram) that sandbox browsers cannot access.
- **Connectors**: Pre-configured integrations (Gmail, Notion) work out of the box via connector UIDs, demonstrated with a Notion-based expense claims workflow.
- **Web Development Platform**: Manus ships with a full Docker sandbox, enabling complex apps with Redis, Stripe webhooks, Chroma embeddings, and any pip-installable package.
- **Demos shown**: French learning app with structured corrections, conference event scraper with Chroma embeddings and calendar integration, Rick and Morty character visualization dashboard, Warren Buffett investor letter analysis, automated bug investigation from screenshots, and receipt-to-Notion expense processing.

## Entities

- [[IvanLeo]] — Speaker from Manus AI, presented the API workshop
- [[ManusAI]] — Company building a general AI agent platform (now Meta Superintelligence)
- [[ManusAPI]] — Programmatic API for Manus agent tasks
- [[Slack]] — Messaging platform used for bot integration demo
- [[Modal]] — Python serverless platform for deploying webhook endpoints
- [[Chroma]] — Vector database used for embedding-based recommendations
- [[Notion]] — Knowledge management platform with Manus connector
- [[ElevenLabs]] — Text-to-speech provider used in language learning app
- [[Stripe]] — Payment platform with Manus webhook integration
- [[Microsoft365]] — Office suite with new Manus integration
- [[BrowserOperator]] — Manus feature for controlling user's local browser

## Concepts

- [[General AI Agent]] — An AI agent designed for diverse tasks across many interfaces
- [[Agent Polling Pattern]] — Repeatedly checking task status until completion
- [[Webhooks for Agents]] — Push-based notification for agent task lifecycle events
- [[Multi-Turn Conversations]] — Maintaining context across sequential agent interactions
- [[File Upload for Agents]] — Providing files as context for agent tasks
- [[Agent Sandbox]] — Isolated Docker-based execution environment for agent code
- [[Agent Connectors]] — Pre-configured integrations that work out of the box
- [[Slack Bot Integration]] — Building Slack bots backed by AI agent APIs
- [[Remote Browser Operator]] — Agent controlling a user's local browser
- [[Agent Memory]] — Persistent user preferences across agent conversations
- [[Structured Outputs]] — Language model outputs in structured data formats
- [[Agent Task States]] — Lifecycle states of an agent task

## Related

- [[ManusAI]] — company behind the platform
- [[IvanLeo]] — presenter
- [[General AI Agent]] — core philosophy
- [[Agent Sandbox]] — key infrastructure
