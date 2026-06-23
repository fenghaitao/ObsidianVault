---
title: "Choosing Between Skills, Sub-agents, Hooks, and CLAUDE.md"
type: synthesis
tags: [claude-code, extension-mechanisms, skills, subagents, hooks, claude-md, decision-guide]
sources: []
last_updated: 2026-06-23
---

## Question

How should you choose between Skills, Sub-agents, Hooks, and CLAUDE.md for extending Claude Code?

## Answer

Claude Code offers four primary extension mechanisms, each with distinct trade-offs around **when they load**, **how deterministic they are**, and **whether they isolate context**. Picking the right mechanism — or combining several — is the difference between a slow, context-bloated agent and a fast, reliable one.

### The Four Mechanisms

| Mechanism | Load Timing | Determinism | Context Isolation | Best For |
|---|---|---|---|---|
| **[[CLAUDE-md]]** | Always (every conversation) | Soft (prompt-based) | No | Project-wide rules, conventions, persistent context |
| **[[ClaudeCodeSkills]]** | On demand (description matches) | Soft (prompt-based) | No (loads into main context) | Task-specific knowledge that should apply automatically when relevant |
| **[[ClaudeCodeSubagents]]** | On demand (delegation) | Soft (prompt-based) | Yes (separate context window) | Research and review tasks where intermediate work is noise |
| **[[ClaudeCodeHooks]]** | On lifecycle events | Hard (always executes) | N/A (shell commands) | Mandatory automation and safety enforcement |

### Decision Framework

**Start with the determinism question:** *"Does this need to happen every time without fail?"*

- **Yes → Use Hooks.** Hooks are deterministic lifecycle handlers (`PostToolUse`, `PreToolUse`, `Stop`, etc.) that always execute. Use for auto-formatting after edits, blocking writes to production config, or preventing commits to protected branches. The rule of thumb: *if something needs to happen every time without fail, use a hook, not a prompt.*
- **No → Continue to context question.**

**Next: the context question:** *"Does the intermediate work matter, or only the final answer?"*

- **Only the answer matters → Use Sub-agents.** Sub-agents run in isolated context windows; all intermediate file reads, edits, and tool calls are discarded after they return a summary. Use for research tasks, code review with fresh eyes, or tasks needing different system prompts.
- **The intermediate work matters → Continue to scope question.**

**Next: the scope question:** *"Should this apply to every conversation, or only when relevant?"*

- **Every conversation → Use CLAUDE.md.** CLAUDE.md is persistent project memory loaded into every conversation. Use for project conventions, architecture overviews, and rules that always apply.
- **Only when relevant → Use Skills.** Skills load on demand via description matching, keeping only a name and description in context until activated. Use for code review standards, commit message formats, brand guidelines, or any repeated explanation.

### Combining Mechanisms

The mechanisms compose well:

- **CLAUDE.md + Skills:** CLAUDE.md sets always-on conventions; skills handle task-specific workflows that activate when triggered.
- **Sub-agents + Skills:** Custom sub-agents can explicitly list skills in their `agent.md` (built-in agents like explore/plan cannot access skills at all). Use this to give a specialized agent a curated set of always-relevant skills.
- **Hooks + Skills:** Hooks enforce non-negotiable rules (e.g., format-on-edit); skills carry the team's preferred patterns. Together they create a "guardrails + guidance" pattern.

### Anti-patterns

- **Don't use sub-agents for sequential pipelines:** Information is lost between steps because intermediate work is discarded.
- **Don't use sub-agents as "experts":** Claude already has the knowledge; the overhead of context-switching isn't justified.
- **Don't use CLAUDE.md as a dumping ground:** Everything in CLAUDE.md is loaded every conversation, consuming context. Move task-specific content to skills.
- **Don't use prompts when you need hooks:** If safety or formatting matters, hooks are the only mechanism that guarantees execution.
- **Don't use hooks for content judgement:** Hooks run shell commands; they can't reason about whether something is correct. Reserve them for deterministic checks.

### Priority Hierarchy for Skills

When skills exist at multiple levels, the priority order is: **enterprise > personal > project > plugins.** Use descriptive names to avoid conflicts. Enterprise admins can deploy skills via managed settings that override all others with the same name.

## Related

- [[CLAUDE-md]] — persistent project memory
- [[ClaudeCodeSkills]] — on-demand task-specific instructions
- [[ClaudeCodeSubagents]] — isolated context delegation
- [[ClaudeCodeHooks]] — deterministic lifecycle automation
- [[ClaudeCode]] — the tool these mechanisms extend
- [[ContextWindow]] — the constraint these mechanisms help manage
- [[summary-04 - How skills compare to other Claude Code features]] — source comparison