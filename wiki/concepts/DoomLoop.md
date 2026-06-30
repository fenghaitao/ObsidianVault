---
title: "DoomLoop"
type: concept
tags: [agent-failure, coding-agent, context-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked.md"]
last_updated: 2026-06-30
---

## Definition
The doom loop is a failure mode in AI coding agents where the agent does not gather enough context at the start of a task, fails to figure out what it needs to do, and then retries the same incorrect approach repeatedly. It is closely related to "babysitting" agents: the engineer must manually intervene to correct the agent, pointing it to the right files and patterns.

## Key Information
- Triggered by the naive fix for context exhaustion: prompting the agent to do fewer reads/context-gathering steps
- Without sufficient context, the agent cannot correctly diagnose the problem or plan the solution
- Results in wasted iterations as the agent loops on the same failed approach
- The proper solution is sub-agents (thorough context gathering in separate windows) or a context engine (pre-computed, exhaustive context)
- Related to babysitting: the engineer reads the agent's output and says "No, let me correct you, it's actually over here" — then points to the right file, manually feeding context
- Without a context engine, this cycle repeats every time the terminal window closes; the context is lost and must be rebuilt

## Related
- [[summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code]] — source
- [[summary-20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked]] — source
- [[ContextExhaustion]] — the problem whose naive fix triggers doom loops
- [[SubAgents]] — the proper architectural solution
- [[ContextEngine]] — alternative solution via pre-computed exhaustive context
- [[Satisfaction of Search]] — related failure mode where agents stop looking too early
