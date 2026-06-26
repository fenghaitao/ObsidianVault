---
title: "ContextOwnership"
type: concept
tags: [agents, context, architecture, tools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
Context ownership refers to the question of who controls what goes into an agent's context window — the user or the harness. Mario Zechner's primary complaint about Claude Code was that the harness controls the context behind the user's back, inserting system reminders, modifying tools, and changing system prompts without the user's knowledge or consent.

## Key Information
- Mario Zechner: "The real problem is that my context wasn't my context. Claude Code is the thing that controls my context and behind my back Claude Code does things to the context."
- System prompt changes on every release, including tool definitions — tools get removed or modified without notice
- System reminders are inserted "in the most inopportune place in your context telling the model, 'Here's some information. It may or may not be relevant to what you're doing.'"
- This confused the model and broke Mario's workflows
- Contrasts with Pi's approach: minimal system prompt, user-controlled extensions, no hidden context manipulation
- Related to broader concerns about agent harness transparency and observability

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[ClaudeCode]] — the harness with context ownership problems
- [[Pi (coding agent)]] — built to give context ownership back to the user
- [[MarioZechner]] — originator of the critique
- [[AgentObservability]] — what Claude Code lacks
- [[Context Management]] — broader field
- [[AgentHarnessSeparation]] — related architectural concern
