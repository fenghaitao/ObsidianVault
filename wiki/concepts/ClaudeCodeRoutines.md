---
title: "ClaudeCodeRoutines"
type: concept
tags: [claude-code, automation, scheduling, cron, autonomous]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/13 - Running an AI-native engineering org.md]
last_updated: 2026-07-04
---

## Definition

Claude Code Routines are scheduled, cron-triggered autonomous runs of Claude Code that execute tasks on a recurring basis without manual triggering. They replace manual daily rituals (e.g., checking customer feedback channels, running stand-up summaries) with automated agent workflows.

## Key Information

- **/schedule command:** Use `/schedule` in Claude Code to set up cron-triggered autonomous runs.
- **Replaces manual rituals:** Morning customer feedback summaries, stand-up reports, and other recurring tasks can be automated.
- **Self-iteration on a timer:** Claude can run the write-run-fix loop autonomously on a schedule.
- **Example:** Fiona Fung (Claude Code engineering lead) replaced her morning ritual of manually asking Claude to summarize customer feedback with a routine that runs automatically.
- **Related to Cowork scheduled tasks:** Claude Cowork offers similar scheduling for knowledge worker tasks (weekly metrics reviews, daily legal briefs).
- **Formal research-preview launch (April 14, 2026):** Routines shipped as a named Claude Code feature — configured once (prompt, repo, connectors) and then run on a schedule, from an API call, or in response to an event; runs on Claude Code's web infrastructure so nothing depends on a laptop being open.
- **Three trigger types:** (1) schedule — cadence like hourly/nightly/weekly (e.g. "Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR"); (2) API call — every routine gets its own endpoint and auth token, POST a message and get back a session URL; (3) GitHub repository events — a routine subscribes to PR events matching filters, opening one session per matching PR and continuing to feed follow-up updates (comments, CI failures) into that session.
- **`/schedule` supersession:** Tasks created via `/schedule` in the CLI are now surfaced as scheduled routines — confirms and formalizes the `/schedule` command described above.
- **Availability and limits:** Available to Claude Code users on Pro, Max, Team, and Enterprise plans with Claude Code on the web enabled (create at claude.ai/code or via `/schedule` in the CLI). Routines draw down subscription usage limits like interactive sessions, plus daily caps: Pro 5/day, Max 15/day, Team/Enterprise 25/day; extra routines available via extra usage.

## Related

- [[ClaudeCode]] — the tool where routines are implemented
- [[ClaudeCowork]] — scheduled tasks for knowledge workers
- [[summary-13 - Running an AI-native engineering org]] — source talk mentioning routines
- [[summary-18 - Scheduled Tasks in Cowork： Set it once, Claude handles the rest]] — analogous scheduled-task feature on Cowork
- [[summary-2026-04-14 - Introducing routines in Claude Code]] — source summary announcing routines research preview
- [[summary-2026-05-11 - Agent view in Claude Code]] — CLI feature surfacing routines' next-run time in a session list
- [[MCPConnector]] — connectors packaged into routines
