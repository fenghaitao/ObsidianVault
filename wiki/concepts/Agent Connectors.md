---
title: "Agent Connectors"
type: concept
tags: [agents, integration, platform]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
Agent connectors are pre-configured integrations between an AI agent platform and external services (Gmail, Notion, etc.) that work out of the box by referencing a connector UID in API calls, without requiring the developer to set up authentication or API logic.

## Key Information
- Manus provides connectors for Gmail, Notion, and other platforms
- Connectors are configured once in the Manus web app settings
- Each connector has a UID that can be copied and included in API task payloads
- When a connector UID is provided, the agent automatically has access to that integration
- Demonstrated with Notion: agent read company policies, analyzed receipts, and updated expense tracking pages
- Enables internal deep research agents that reference company knowledge bases
- Reduces integration complexity — developers don't need to manage OAuth, API keys, or webhook setup per integration

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAI]] — platform providing connectors
- [[ManusAPI]] — API using connector UIDs
- [[Notion]] — example connector platform
- [[General AI Agent]] — philosophy supported by connectors
