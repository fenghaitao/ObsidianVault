---
title: "Multi-Turn Conversations"
type: concept
tags: [agents, context, conversation, integration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
Multi-turn conversations are sequential interactions with an AI agent where each message is pushed to the same task session, preserving context across turns rather than starting a new task each time.

## Key Information
- In the Manus API, multi-turn is achieved by keeping the task ID and pushing follow-up messages to the same session
- Requires tracking which thread/conversation maps to which task ID (e.g., via a KV store or database)
- When a new message arrives in an existing thread, the system pushes it to the existing task rather than creating a new one
- Enables complex workflows where the agent can ask clarifying questions and receive follow-up input
- The agent can be in a "pending" state when waiting for user input
- In Slack bots, thread timestamps (thread_ts) serve as the conversation identifier mapped to task IDs
- Essential for building conversational agent experiences in messaging platforms

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAPI]] — API supporting multi-turn
- [[Slack Bot Integration]] — application context
- [[Agent Task States]] — pending state for awaiting input
- [[Agent Memory]] — related concept for persistent preferences
