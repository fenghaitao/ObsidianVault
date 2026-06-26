---
title: "Wolfer"
type: entity
tags: [tool, personal-agent, agent-framework, codex, experimental]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md"]
last_updated: 2026-06-26
---

## Definition
Wolfer is Kitze's personal agent framework — a tiny abstraction on top of Codex designed for multi-agent orchestration with predictable UI, nested topic context injection, and agent management. It is a personal experiment, not intended for mass release.

## Key Information
- Built on Codex only (Kitze avoids Claude Code: "I might get arrested")
- Not extensible, doesn't support multiple providers, not modular
- "Made by an ADHD squirrel brain that will forget about it by the end of the month"
- No OpenAI funding, no lobster logo

### Key Features
- **Nested topics**: hierarchical topic tree (work → projects → Benji → Benji customer support). When chatting in a child topic, the first prompt injects descriptions of all parent topics — no memory retrieval needed
- **Predictable UI**: built for multi-agent orchestration with multiple topics and conversations
- **Tool call visibility**: can see, collapse, uncollapse tool calls with loading spinners; stop button without slash commands
- **Predictable cron jobs**: cron messages read from entire conversation and are labeled as cron
- **Agent management UI**: right-side panel shows agent name, model, capabilities — can toggle capabilities on/off
- **Knowledge base & mentions**: write markdown documents, mention them in conversations; combine multiple @-mentions (knowledge base, password, skill) to give exact context
- **Workspaces**: switch between different contexts

### Limitations
- Forced to use the app's UI chat (no Telegram, iMessage, WhatsApp support)
- Opposite of OpenClaw/Hermes extensibility — not built with plugins in mind
- No memory system — relies on nested context injection instead
- Not modular

## Related
- [[Kitze]] — creator
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — source
- [[Codex]] — underlying agent
- [[Benji]] — Kitze's life OS app
- [[OpenClaw]] — alternative agent framework (opposite design philosophy)
- [[Hermes]] — alternative agent framework
- [[Nested Context]] — key design concept
- [[Agent Specialization]] — multi-agent design pattern
- [[Personal Agent]] — the vision Wolfer serves
