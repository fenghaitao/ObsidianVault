---
title: "JarredSumner"
type: entity
tags: [person, developer, open-source, javascript]
sources: ["raw/01-articles/claude/2026-05-28 - Introducing dynamic workflows in Claude Code.md"]
last_updated: 2026-07-07
---

## Definition

Jarred Sumner is the creator of [[Bun]], a fast JavaScript runtime and toolkit. He used [[ClaudeCode]] dynamic workflows to port Bun from Zig to Rust — approximately 750,000 lines of Rust, 99.8% of the existing test suite passing, completed in eleven days from first commit to merge.

## Key Information

- Creator of [[Bun]], an open-source JavaScript runtime focused on speed and developer experience.
- Applied [[DynamicWorkflows]] to orchestrate the Zig-to-Rust port: one workflow mapped Rust lifetimes for every struct field, the next wrote every `.rs` file as a behavior-identical port of its `.zig` counterpart using hundreds of parallel agents with two reviewers per file, and a fix loop drove the build and test suite until both ran clean.
- After the port landed, an overnight workflow addressed unnecessary data copies and opened a PR for each fix for final review.
- Previously presented at Code w/ Claude San Francisco 2026, where he discussed Robo Bun — an automated Claude Code pipeline that reproduces GitHub issues, writes tests, submits PRs, and engages in autonomous code review.

## Related

- [[Bun]] — the JavaScript runtime he created
- [[ClaudeCode]] — the tool powering both Robo Bun and the Zig-to-Rust port
- [[DynamicWorkflows]] — the Claude Code feature used for the Bun rewrite
- [[summary-2026-05-28 - Introducing dynamic workflows in Claude Code]] — source article
