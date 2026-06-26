---
title: "ContextExhaustion"
type: concept
tags: [agent-architecture, context-management, coding-agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code.md"]
last_updated: 2026-06-25
---

## Definition
Context exhaustion is a failure mode in AI coding agents where the context window fills up with tool calls and results (e.g., grep and file reads) before the agent reaches the editing phase, forcing it to stop prematurely or produce incomplete output.

## Key Information
- Caused by agents gathering context through many tool calls (grepping, reading files) that consume the context window
- Naive fix: prompt the agent to do fewer reads — but this leads to the "doom loop" failure mode where insufficient context causes repeated failed attempts
- Solution: sub-agents that isolate subtask context in separate windows and return only relevant results to the main agent
- The Finder sub-agent in Amp Code is specifically designed to solve this by using a small, fast model with an optimized tool set for codebase search

## Related
- [[summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code]] — source
- [[SubAgents]] — architectural solution
- [[DoomLoop]] — related failure mode from insufficient context
