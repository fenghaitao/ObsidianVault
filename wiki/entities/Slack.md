---
title: "Slack"
type: entity
tags: [platform, messaging, integration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski.md"]
last_updated: 2026-06-29
---

## Definition
Slack is a messaging platform used as an integration target for AI agent bots, demonstrated with the Manus API to build a multi-turn conversational agent accessible directly in Slack channels. Viktor takes this further by using Slack as its sole interface — the AI employee lives entirely in Slack without any web app.

## Key Information
- Manus ships a Slack app integration out of the box
- Slack bot integration requires a bot token and signing secret
- Slack has a 3-second response timeout requirement; servers should be kept warm
- Slack Block Kit enables rich UI elements (buttons, emoji, formatted text) in bot responses
- File uploads in Slack require careful thread management to ensure files appear in the correct thread
- Slack sends webhook events with user IDs, channel IDs, and thread timestamps that bots must parse
- The Slack Events API uses a challenge-response verification for endpoint registration
- Multi-turn conversations require tracking thread-to-task mappings (e.g., via KV store)
- OpenClaw has a Slack plugin maintained by a contributor from Slack — "there's cool people at Slack"
- Slack's use of Axios as a dependency (without pinning versions) caused a supply chain vulnerability that affected OpenClaw even though OpenClaw doesn't directly use Axios
- **n8n Integration**: Slack can serve as the chat interface for human-in-the-loop review in n8n workflows. The chat trigger can be replaced with Slack triggers, and human review messages route through Slack with approve/deny buttons. A loading indicator can be added via a Slack node with a GIF
- **Viktor Integration**: Viktor is an AI employee that lives entirely in Slack with no web app. Uses Slack's multiple interaction modes (DMs, channels, threads, emoji reactions, message edits) as its entire input surface. Chosen over web apps for two reasons: (1) interacting in Slack feels like interacting with a human employee, (2) Slack's async nature makes long-running agent tasks (10+ minutes) feel fast compared to human response times. Slack's multi-modal interaction surface (DMs, threads, edits, reactions) creates challenges for linear context management that Viktor had to solve

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source (OpenClaw integration, supply chain)
- [[summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]] — source (critiqued as not designed for agentic development)
- [[ManusAPI]] — API integrated with Slack
- [[Slack Bot Integration]] — concept for building Slack-based agents
- [[Modal]] — deployment platform used in demo
- [[OpenClaw]] — project with Slack integration
- [[SupplyChainAttack]] — Axios vulnerability that propagated through Slack
- [[ACE]] — GitHub Next prototype that aims to replace Slack for software development collaboration
- [[n8n]] — platform integrating Slack for human-in-the-loop review
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — source
- [[Viktor]] — AI employee that lives entirely in Slack as its primary interface
- [[summary-20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski]] — source (Slack as sole agent interface)
- [[Slack-based Agent Interface]] — the interface paradigm Viktor pioneered
