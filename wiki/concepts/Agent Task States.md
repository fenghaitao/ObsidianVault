---
title: "Agent Task States"
type: concept
tags: [agents, api, lifecycle, state-machine]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-25
---

## Definition
Agent task states are the lifecycle stages an agent task progresses through: running (actively processing), pending (awaiting user input), completed (finished successfully), and error (failed). These states drive both polling and webhook-based integration patterns.

## Key Information
- Four states in the Manus API: running, pending, completed, error
- Running: agent is actively working on the task
- Pending: agent requires more input or clarification from the user before continuing
- Completed: agent has finished the task successfully; final output is available
- Error: rare failure state; ideally never encountered
- State transitions are communicated via both polling responses and webhook notifications
- The pending state is critical for multi-turn conversations — it signals that the agent is waiting for user response
- Clients should handle each state appropriately: poll/await for running, prompt user for pending, process output for completed, handle gracefully for error

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAPI]] — API implementing these states
- [[Agent Polling Pattern]] — pattern driven by state checking
- [[Webhooks for Agents]] — pattern driven by state transitions
- [[Multi-Turn Conversations]] — relies on pending state
