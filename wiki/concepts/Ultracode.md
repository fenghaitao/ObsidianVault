---
title: "Ultracode"
type: concept
tags: [claude-code, effort-setting, dynamic-workflows]
sources: ["raw/01-articles/claude/2026-05-28 - Introducing dynamic workflows in Claude Code.md"]
last_updated: 2026-07-07
---

## Definition

Ultracode is a [[ClaudeCode]]-specific effort setting that sets the effort level to `xhigh` while letting Claude decide automatically when to use [[DynamicWorkflows|dynamic workflows]] to handle a task.

## Key Information

- Accessible through the effort menu in Claude Code.
- Combines maximum effort (`xhigh`) with automatic workflow invocation — Claude determines whether the task benefits from parallel subagent orchestration without the user needing to request it explicitly.
- Recommended alongside **auto mode** for the best experience when using dynamic workflows.

## Related

- [[DynamicWorkflows]] — the orchestration feature ultracode enables automatically
- [[ClaudeCode]] — the tool providing the effort menu
- [[summary-2026-05-28 - Introducing dynamic workflows in Claude Code]] — source article
