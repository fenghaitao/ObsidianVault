---
title: "summary-2026-05-28 - Introducing dynamic workflows in Claude Code"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-05-28 - Introducing dynamic workflows in Claude Code.md"]
last_updated: 2026-07-07
---

## Core Summary

Dynamic workflows in Claude Code enable Claude to tackle large-scale engineering tasks end-to-end by dynamically writing orchestration scripts that fan out work across tens to hundreds of parallel subagents, with independent verification and adversarial checking before results reach the user. Work that would normally be planned in quarters now finishes in days, handling codebase-wide bug hunts, large migrations touching thousands of files, and critical work requiring double-checking. Available across CLI, Desktop, VS Code extension, and the Claude API on major cloud platforms for Pro, Max, Team, and Enterprise plans.

## Key Points

- Dynamic workflows let Claude plan, break tasks into subtasks, fan work across parallel subagents, verify results, and iterate until answers converge — producing results a single pass cannot.
- The Bun rewrite from Zig to Rust (~750,000 lines, 99.8% test pass rate, 11 days) is a flagship example: parallel subagents wrote every `.rs` file with two reviewers each, and a fix loop drove the build and test suite clean.
- Two invocation modes: ask Claude to create a workflow directly, or enable `ultracode` (effort level xhigh) which lets Claude decide automatically when to use workflows.
- Progress is saved as the run goes, so interrupted jobs resume where they left off without restarting.
- Dynamic workflows consume substantially more tokens than typical Claude Code sessions; organization admins can disable them through managed settings.
- Use cases include codebase-wide bug hunts, security audits, large migrations/modernization efforts, profiler-guided optimization, and adversarial verification of critical work.

## Related

- [[DynamicWorkflows]] — the concept page
- [[ClaudeCode]] — the tool dynamic workflows extend
- [[ClaudeCodeSubagents]] — subagent architecture underlying workflow parallelism
- [[Ultracode]] — effort setting that enables automatic workflow invocation
- [[Bun]] — flagship example: Zig-to-Rust rewrite using dynamic workflows
- [[JarredSumner]] — Bun creator who used dynamic workflows for the port
