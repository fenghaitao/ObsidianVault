---
title: "ClaudeCodeRoutines"
type: concept
tags: [claude-code, automation, scheduling, cron, autonomous]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/13 - Running an AI-native engineering org.md]
last_updated: 2026-06-23
---

## Definition

Claude Code Routines are scheduled, cron-triggered autonomous runs of Claude Code that execute tasks on a recurring basis without manual triggering. They replace manual daily rituals (e.g., checking customer feedback channels, running stand-up summaries) with automated agent workflows.

## Key Information

- **/schedule command:** Use `/schedule` in Claude Code to set up cron-triggered autonomous runs.
- **Replaces manual rituals:** Morning customer feedback summaries, stand-up reports, and other recurring tasks can be automated.
- **Self-iteration on a timer:** Claude can run the write-run-fix loop autonomously on a schedule.
- **Example:** Fiona Fung (Claude Code engineering lead) replaced her morning ritual of manually asking Claude to summarize customer feedback with a routine that runs automatically.
- **Related to Cowork scheduled tasks:** Claude Cowork offers similar scheduling for knowledge worker tasks (weekly metrics reviews, daily legal briefs).

## Related

- [[ClaudeCode]] — the tool where routines are implemented
- [[ClaudeCowork]] — scheduled tasks for knowledge workers
- [[summary-running-ai-native-engineering-org]] — source talk mentioning routines
