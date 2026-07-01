---
title: "Slack Bot Integration"
type: concept
tags: [agents, slack, integration, bots]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md"]
last_updated: 2026-06-29
---

## Definition
Slack bot integration is a pattern for building AI agent-powered bots in Slack, where Slack webhook events trigger agent tasks and agent responses are formatted and posted back to the appropriate Slack thread.

## Key Information
- Slack requires a 3-second response to webhook events, necessitating warm servers or async processing
- Bot setup requires: Slack bot token, signing secret, and event subscription verification via challenge-response
- Slack sends webhook events containing user ID, channel ID, thread timestamp, and message text
- User IDs in message text need to be parsed out for clean display
- Slack Block Kit enables rich UI (buttons, emoji, formatted text, "View on Web" links) in bot responses
- Multi-turn conversations require mapping Slack thread_ts to agent task IDs in a persistent store
- File uploads in Slack need both channel and thread parameters to appear in the correct thread
- Agent markdown output must be transformed to Slack-compatible markdown format
- The pattern: receive Slack event → parse message → check if thread exists → create or push to task → return acknowledgment → process webhook → format and post response

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[Slack]] — messaging platform
- [[ManusAPI]] — agent API integrated
- [[MultiTurn Conversations]] — conversation pattern used
- [[Webhooks for Agents]] — notification mechanism
- [[Modal]] — deployment platform used in demo
