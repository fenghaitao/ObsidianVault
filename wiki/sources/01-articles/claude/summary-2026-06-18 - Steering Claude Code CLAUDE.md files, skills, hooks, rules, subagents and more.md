---
title: "summary-2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more.md"]
last_updated: 2026-07-07
---

## Core Summary

Claude Code offers seven methods for instructing Claude's behavior: CLAUDE.md files, rules, skills, subagents, hooks, output styles, and appending the system prompt. Each method differs in when instructions load into context, whether they persist through compaction, and how much authority they carry. The post provides a decision framework for determining where each instruction belongs, with practical tips for avoiding common anti-patterns like stuffing procedures into CLAUDE.md or using unscoped rules that waste tokens.

## Key Points

- CLAUDE.md files come in two types: always-loaded root files (re-read on compaction) and on-demand subdirectory files that load only when that subdirectory is accessed. Keep root CLAUDE.md under 200 lines and treat it as an index pointing to other context sources.
- Rules in `.claude/rules/` support path scoping via YAML frontmatter `paths:` fields, loading only when relevant files are touched. An unscoped rule is mechanically identical to CLAUDE.md content — always loaded, always costing tokens.
- Skills live in `.claude/skills/` and load only their name/description at session start; the full body loads on demand. They are best for procedural instructions like deploy workflows and release checklists.
- Subagents run in isolated context windows via the Agent tool; their body never enters the parent conversation. Use subagents for side tasks that would clutter the main conversation (deep search, log analysis) and skills when you want to see and steer each step.
- Hooks are deterministically triggered lifecycle event handlers with low context cost. Use hooks for anything that should happen deterministically (running linters, blocking dangerous commands) rather than as prompted instructions.
- Output styles in `.claude/output-styles/` inject into the system prompt, carrying the highest instruction-following weight. Custom styles replace the default coding instructions unless `keep-coding-instructions: true` is set.
- Appending the system prompt via the `append-system-prompt` flag is additive only — it does not modify Claude's default role, applies only to a single invocation, and has diminishing returns for adherence as more instructions are added.

## Related

- [[CLAUDE-md]] — the persistent project memory mechanism
- [[ClaudeCodeRules]] — path-scoped rule files in `.claude/rules/`
- [[ClaudeCodeSkills]] — on-demand procedural expertise
- [[ClaudeCodeSubagents]] — isolated context-window delegation
- [[ClaudeCodeHooks]] — deterministic lifecycle event handlers
- [[ClaudeCodeOutputStyles]] — system-prompt-injected behavior modifiers
- [[ClaudeCodeSystemPrompt]] — additive, invocation-scoped instruction flag
- [[ClaudeCode]] — the tool these seven methods steer
- [[ClaudeCodePlugins]] — bundling mechanism for skills, subagents, hooks, and output styles
