---
title: "ClaudeCodeRules"
type: concept
tags: [claude-code, rules, configuration, context]
sources: ["raw/01-articles/claude/2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more.md"]
last_updated: 2026-07-07
---

## Definition

Claude Code rules are markdown files in `.claude/rules/` that give Claude specific constraints or conventions. They support path scoping via YAML frontmatter, loading only when relevant files in the codebase are touched, which avoids wasting context tokens on instructions irrelevant to the current task.

## Key Information

- **Unscoped rules** behave like [[CLAUDE-md|CLAUDE.md]] content: always loaded at session start and re-injected on compaction. This wastes tokens when the instruction is irrelevant to the current task.
- **Path-scoped rules** use a `paths:` field in YAML frontmatter to control when they load. Example: a rule scoped to `src/api/**` stays out of context during a docs-only session and only loads when Claude reads files within `src/api/`.
- **Frontmatter example**:
  ```yaml
  ---
  paths:
    - "src/api/**"
    - "**/*.handler.ts"
  ---
  All API handlers must validate input with Zod before processing.
  ```
- **When to use**: file-specific constraints (e.g., "migrations are append-only") fit best as path-scoped rules. Use a path-scoped rule over a nested CLAUDE.md file when the instruction concerns a cross-cutting concern or file that appears in multiple but not all corners of the codebase.
- **Rule of thumb**: if a rule only applies to a specific directory, scope it with `paths:` to keep it out of context during unrelated work. An unscoped rule is mechanically identical to putting the content in CLAUDE.md.

## Related

- [[summary-2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more]] — source summary
- [[CLAUDE-md]] — the always-loaded counterpart to path-scoped rules
- [[ClaudeCode]] — the tool rules extend
- [[ClaudeCodeSkills]] — on-demand procedural alternative
- [[ClaudeCodeHooks]] — deterministic enforcement alternative for must-not-happen constraints
- [[analysis-claude-code-extension-mechanisms]] — decision guide for choosing among extension mechanisms
