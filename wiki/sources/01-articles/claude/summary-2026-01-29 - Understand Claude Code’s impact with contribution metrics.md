---
title: "summary-2026-01-29 - Understand Claude Code's impact with contribution metrics"
type: source
tags: [source, claude-code, metrics, github]
sources: ["raw/01-articles/claude/2026-01-29 - Understand Claude Code’s impact with contribution metrics.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic introduced **contribution metrics** in Claude Code (public beta): a GitHub-integrated dashboard tracking PRs merged and lines of code committed with vs. without Claude Code assistance, plus per-user adoption data — requiring no external tools or data pipelines beyond installing the Claude GitHub App.

## Key Points

- Internal Anthropic results cited as motivation: a 67% increase in PRs merged per engineer per day since Claude Code adoption increased, with 70-90% of code across teams now written with Claude Code assistance.
- Contribution data is calculated conservatively by matching Claude Code session activity against GitHub commits/PRs; only high-confidence Claude-assisted code counts as "assisted."
- Designed to complement (not replace) existing engineering KPIs like DORA metrics and sprint velocity.
- Available now in beta for Claude Team and Enterprise customers; enabled via the Claude GitHub App plus a toggle in Admin settings > Claude Code > GitHub Analytics.

## Related

- [[ClaudeCode]] — the tool contribution metrics measure the impact of
- [[GitHub]] — the platform contribution metrics integrate with
