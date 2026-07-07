---
title: "Bun"
type: entity
tags: [company, javascript-runtime, open-source, automation, claude-code]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/04 - Live coding session with Boris Cherny and Jarred Sumner.md, "raw/01-articles/claude/2026-05-28 - Introducing dynamic workflows in Claude Code.md", "raw/01-articles/claude/2026-06-02 - A harness for every task dynamic workflows in Claude Code.md"]
last_updated: 2026-07-07
---

## Definition

Bun is a fast JavaScript runtime and toolkit created by [[JarredSumner|Jarred Sumner]]. The Bun project uses an advanced Claude Code automation pipeline (Robo Bun) that automatically reproduces every GitHub issue, writes tests, submits PRs, and engages in autonomous code review with other bots. Robo Bun is now a bigger contributor to Bun than its creator.

## Key Information

- **Robo Bun:** Automated Claude Code bot that reproduces issues, writes tests, and submits PRs before any human looks at them.
- **Adversarial code review:** Engages in back-and-forth with Code Rabbit (stylistic) and Claude Code Review (deep bug detection).
- **Compound engineering:** Every repeated mistake documented in CLAUDE.md for future runs.
- **Model threshold:** Opus 4.7 is the first model where this pipeline is efficient enough for day-to-day use.
- **Zig-to-Rust rewrite (May 2026):** Jarred Sumner used [[DynamicWorkflows]] to port Bun from Zig to Rust — approximately 750,000 lines of Rust with 99.8% of the existing test suite passing, completed in eleven days from first commit to merge. One workflow mapped the right Rust lifetime for every struct field in the Zig codebase. The next wrote every `.rs` file as a behavior-identical port of its `.zig` counterpart, with hundreds of agents working in parallel and two reviewers on each file. A fix loop then drove the build and test suite until both ran clean. After the port landed, an overnight workflow addressed unnecessary data copies and opened a PR for each for final review. While not yet in production, all of this was handled by dynamic workflows.

## Related

- [[summary-04 - Live coding session with Boris Cherny and Jarred Sumner]] — source talk
- [[ClaudeCode]] — the tool powering Robo Bun and dynamic workflows
- [[ClaudeFable5]] — Opus 4.7 enabling autonomy
- [[CLAUDE-md]] — compound engineering documentation
- [[JarredSumner]] — Bun creator
- [[DynamicWorkflows]] — the orchestration feature used for the Zig-to-Rust rewrite
- [[summary-2026-05-28 - Introducing dynamic workflows in Claude Code]] — dynamic workflows announcement featuring the Bun rewrite
- [[summary-2026-06-02 - A harness for every task dynamic workflows in Claude Code]] — follow-up article citing the Bun rewrite as a workflow pattern example
