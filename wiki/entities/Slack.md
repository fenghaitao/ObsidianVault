---
title: "Slack"
type: entity
tags: [platform, messaging, integration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
Slack is a messaging platform used as an integration target for AI agent bots, demonstrated with the Manus API to build a multi-turn conversational agent accessible directly in Slack channels.

## Key Information
- Manus ships a Slack app integration out of the box
- Slack bot integration requires a bot token and signing secret
- Slack has a 3-second response timeout requirement; servers should be kept warm
- Slack Block Kit enables rich UI elements (buttons, emoji, formatted text) in bot responses
- File uploads in Slack require careful thread management to ensure files appear in the correct thread
- Slack sends webhook events with user IDs, channel IDs, and thread timestamps that bots must parse
- The Slack Events API uses a challenge-response verification for endpoint registration
- Multi-turn conversations require tracking thread-to-task mappings (e.g., via KV store)

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAPI]] — API integrated with Slack
- [[Slack Bot Integration]] — concept for building Slack-based agents
- [[Modal]] — deployment platform used in demo
