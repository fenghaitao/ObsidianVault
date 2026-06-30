---
title: "Loop Command"
type: concept
tags: [claude-code, cli, automation, cron, loop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
The Loop Command is a built-in Claude Code feature that sets up cron-based repeating agent tasks. It uses a cron creator tool to schedule tasks that run at specified intervals, enabling continuous agent loops without external scripting.

## Key Information
- Built into Claude Code as `loop` command
- Uses a cron creator tool (five-star cron syntax) to schedule recurring tasks
- Example: `loop every minute build the next ticket from doc tickets`
- The agent executes the task, finishes, checks the cron schedule, and runs again at the next interval
- Sessions last about 3 days before needing to be refreshed
- Can be used for continuous ticket implementation, periodic checks (e.g., "every 1 hour check Linear for new bug reports"), or any recurring agent task
- Simpler than external while-loop scripting but keeps context across iterations (trade-off: context rot vs convenience)
- Chris Parsons demonstrated it live, running through 6+ tickets while he continued his talk

## Related
- [[ClaudeCode]] — the tool it's part of
- [[Cron Creator]] — the underlying scheduling mechanism
- [[Ralph Loop]] — the pattern it implements
- [[ChrisParsons]] — demonstrated in his workshop
- [[Context Rot]] — trade-off of persistent context
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
