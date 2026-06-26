---
title: "DoomLoop"
type: concept
tags: [agent-failure, coding-agent, context-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code.md"]
last_updated: 2026-06-25
---

## Definition
The doom loop is a failure mode in AI coding agents where the agent does not gather enough context at the start of a task, fails to figure out what it needs to do, and then retries the same incorrect approach repeatedly.

## Key Information
- Triggered by the naive fix for context exhaustion: prompting the agent to do fewer reads/context-gathering steps
- Without sufficient context, the agent cannot correctly diagnose the problem or plan the solution
- Results in wasted iterations as the agent loops on the same failed approach
- The proper solution is sub-agents, which allow thorough context gathering in a separate window without consuming the main agent's context

## Related
- [[summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code]] — source
- [[ContextExhaustion]] — the problem whose naive fix triggers doom loops
- [[SubAgents]] — the proper architectural solution
