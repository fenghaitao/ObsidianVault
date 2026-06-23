---
title: "summary-designing-effective-subagents"
type: source
tags: [source, claude-code, subagents, design, transcript]
sources: [raw/03-transcripts/Claude/Claude Code subagents/02 - Designing effective subagents.md]
last_updated: 2026-06-23
---

## Core Summary

Effective sub-agent design revolves around four principles: (1) define a structured output format to create natural stopping points and prevent over-researching, (2) report obstacles encountered (workarounds, environment quirks, special flags) so the main thread doesn't rediscover them, (3) write specific descriptions that guide both when the main agent launches the sub-agent and what input prompt it writes, and (4) limit tool access to only what the sub-agent actually needs (read-only for research, bash for diff, edit/write only for code-changing agents).

## Key Points

- **Output format:** the most important improvement. Without it, sub-agents struggle to decide when enough research is done and run much longer. Define a clear structure.
- **Obstacle reporting:** explicitly ask for workarounds, setup issues, environment quirks, commands needing special flags, dependency problems. Otherwise the main thread rediscovers them.
- **Description as guidance:** the main agent uses the description to decide when to launch the sub-agent AND to write the input prompt. Add instructions like "you must tell the agent precisely which files to review" or "return sources that can be cited."
- **Tool access:** read-only (glob, grep, read) for research agents; add bash for reviewers needing `git diff`; only give edit/write to agents that should change code.
- **Name and description** are included in the main agent's system prompt, controlling automatic delegation.

## Related

- [[summary-what-are-subagents]] — what sub-agents are
- [[summary-using-subagents-effectively]] — when to use sub-agents
- [[summary-creating-a-subagent]] — creation tutorial
- [[ClaudeCode]] — the tool sub-agents extend
