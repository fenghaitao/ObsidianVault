---
title: "Live Coding Session with Boris Cherny and Jarred Sumner"
type: source
tags: [claude-code, automation, code-review, bun, robo-bun, CI]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/04 - Live coding session with Boris Cherny and Jarred Sumner.md]
last_updated: 2026-06-23
---

## Core Summary

Boris Cherny (Head of Claude Code) and Jarred Sumner (Creator of Bun) demonstrate an advanced Claude Code automation pipeline for the Bun open-source project. Robo Bun, an automated Claude Code bot, automatically reproduces every GitHub issue, writes tests, submits PRs, and engages in back-and-forth with code review bots (Code Rabbit and Claude Code Review). The session showcases how model capabilities (Opus 4.7) have reached a threshold where fully automated issue-to-PR pipelines are viable, with Jarred noting Robo Bun is now a bigger contributor to Bun than he is. Key themes include compound engineering (documenting every repeated fix in CLAUDE.md), adversarial code review, and the shifting bottleneck from code generation to verification and trust.

## Key Points

- **Robo Bun pipeline:** Every GitHub issue triggers an automated Claude Code bot that reproduces the issue, writes tests, and submits a PR — all before any human looks at it.
- **Hard requirements:** PRs must include tests that fail on the previous version and pass on the fix branch before submission.
- **Adversarial code review:** Robo Bun engages in back-and-forth with Code Rabbit (stylistic review) and Claude Code Review (deep bug detection via control flow tracing). Code Rabbit and Robo Bun exchange 30+ comments autonomously.
- **Compound engineering:** Every time a repeated mistake or pattern is observed, document it in CLAUDE.md so future runs get it right the first time. This includes build commands, test conventions, error message ordering, and folder layouts.
- **Model threshold:** Opus 4.7 is the first model where this level of autonomous pipeline is efficient enough for day-to-day use. Previously required excessive scaffolding.
- **Hill climbing with metrics:** Give Claude a target metric, a way to verify results, and let it iterate in auto mode. Claude ran benchmarks to make Bun's image processing faster than Sharp.
- **Bottleneck shift:** Code generation is no longer the bottleneck; verification and trust are. The challenge is communicating sufficient proof that changes are correct.
- **No-flicker mode:** Rewritten CLI renderer with virtualized scrolling for constant memory/CPU usage, enabling smooth long-running agent sessions.
- **Auto mode:** Essential for letting Claude run for hours without getting stuck on permission requests.

## Related

- [[ClaudeCode]] — the tool powering Robo Bun
- [[ClaudeFable5]] — Opus 4.7 enabling this level of autonomy
- [[CLAUDE-md]] — compound engineering documentation pattern
- [[Bun]] — the JavaScript runtime using this pipeline
