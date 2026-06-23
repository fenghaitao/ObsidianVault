---
title: "summary-build-proactive-agent-workflow"
type: source
tags: [source, claude-code, routines, automation, transcript]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/19 - Build a proactive agent workflow with Claude Code.md]
last_updated: 2026-06-23
---

## Core Summary

Maya from Anthropic's applied AI team presents Claude Code Routines, a feature that turns Claude Code from a tool (waits for you to press enter) into a teammate (notices when something breaks and acts). Routines handle hosting, session state, and connectors on managed infrastructure. Triggers can be time-based (cron) or event-based (GitHub webhooks, custom API endpoints). Sessions are interactive and steerable from web, CLI, or desktop. Internal use case: automating documentation creation -- weekly review of code changes against docs repo, creating PRs automatically.

## Key Points

- **Three challenges with proactive agents:** where to run (hosting, persistence, auth), when to trigger (cron, webhooks, endpoints), and human-in-the-loop control (watch, steer, resume).
- **Routines solve all three:** managed infrastructure (no laptop dependency), customizable triggers (schedule or event-based), interactive sessions (open from web/CLI/desktop).
- **Internal use case:** Sarah, Anthropic's docs engineer, uses routines to review weekly code changes against docs and auto-create PRs. Weekly PRs up 200% since start of year.
- **Three decisions when creating a routine:** trigger (schedule vs. event), context (repos, connectors like Google Drive and Slack), steerability (agent-on-agent review, human monitoring).
- **Agent-on-agent review:** one routine creates docs PRs; another routine triggers on PR creation to leave review comments before a human sees it.
- **Trigger types:** cron schedule, GitHub events (PR merged, issue labeled), custom webhook/API with event payload as context.

## Related

- [[ClaudeCodeRoutines]] — the routines concept
- [[ClaudeCode]] — the tool routines extend
- [[summary-running-ai-native-engineering-org]] — related engineering practices
