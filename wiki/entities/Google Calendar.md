---
title: "Google Calendar"
type: entity
category: service
tags: [service, calendar, google, integration, agent-tool]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md"]
last_updated: 2026-06-29
---

## Definition
Google Calendar is Google's calendar service, used as an integration target for AI agents. In n8n workshops, Google Calendar nodes (create event, get events) are converted into tools that AI agents can call, with human-in-the-loop review intercepting event creation before execution.

## Key Information

- **Agent Integration**: n8n provides Google Calendar nodes that can be converted into AI agent tools
- **Available Actions**: Create event, get events
- **Human-in-the-Loop**: Event creation is routed through human review nodes to prevent accidental calendar entries
- **API Naming Quirk**: The "summary" field in Google Calendar API is actually the event title — confusing for both humans and AI. Field descriptions should clarify this, and the auto-generated key can be renamed from "summary" to "title"
- **Date Formatting**: n8n uses Luxon date library for formatting event dates into human-readable format (e.g., `{{ $json.date.toDateTime().format('DDDD TT') }}`)
- **Authentication**: One-click OAuth setup with Google account (separate from Gmail credential)
- **Testing**: Dummy events can be created and reviewed before approval, enabling safe testing

## Related

- [[n8n]] — platform providing Google Calendar integration
- [[Gmail]] — companion service for email management agents
- [[Google]] — parent company
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — workshop source
- [[HumanInTheLoopWorkflows]] — pattern for intercepting calendar event creation
- [[FineGrained Tool Permissions]] — field-level access control
