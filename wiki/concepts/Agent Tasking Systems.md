---
title: "Agent Tasking Systems"
type: concept
tags: [AI, agent, task-management, workflow, OpenClaw]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md"]
last_updated: 2026-07-11
---

## Definition

Agent tasking systems are the methods by which AI agents track, manage, and execute tasks — both tasks assigned to them by humans and tasks they assign back to humans. In OpenClaw, this includes agent-maintained to-do files and integration with project management tools like Linear.

## Key Information

- **Agent-to-agent tasking:** Each agent maintains a to-do file with checked-off items. "It's very loose."
- **Agent-to-human tasking:** Agents assign tasks back to humans via project management tools. Claire Vo has her agents create Linear tickets for her: "I need to fax the doctor's office" or "I need to walk and do a return."
- This creates a bidirectional workflow: Claire tasks agents, agents task Claire
- "I am just a hand for the AI at this point. I'm just a vessel of Polly."
- **Task management hygiene:** After long conversations, check in: "Make sure to write all this to your memory in case it gets compacted" or "Make sure our to-do list is updated with the latest."
- The heartbeat mechanism (scheduled cron jobs) is the execution engine for the tasking system

## Why It Matters

- Completes the loop: agents don't just do work, they also manage work
- "Let your agent project manage your tasks as well" — inverts the typical human-agent relationship
- Using a real project management tool (Linear) rather than chat-based reminders makes tasks harder to forget

## Related

- [[OpenClaw]] — the platform
- [[Agent Heartbeat]] — the execution engine
- [[Linear]] — the tasking substrate used by Claire Vo
- [[Employee Mental Model for AI Agents]] — the philosophy
- [[summary-18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo]] — source summary
