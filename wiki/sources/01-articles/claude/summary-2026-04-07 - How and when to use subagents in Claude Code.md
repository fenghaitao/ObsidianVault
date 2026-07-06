---
title: "summary-2026-04-07 - How and when to use subagents in Claude Code"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-07 - How and when to use subagents in Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

This Anthropic blog post is a practical guide to Claude Code subagents: isolated Claude instances, each with its own context window, that take a task, do the work, and return only the result to the main conversation (the "browser tabs of a Claude Code session" analogy). It lays out five concrete signals for when delegation pays off — heavy research, independent parallel sub-tasks, unbiased/fresh review, pre-commit second opinions, and staged multi-phase pipelines — plus a quantified rule of thumb (10+ files to explore, or 3+ independent work items). It then walks through an escalating ladder of invocation methods: ad hoc conversational prompting, custom subagent definitions (`.claude/agents/`), CLAUDE.md policies dictating when subagents must be used, skills for reusable multi-subagent workflows, and hooks for fully automated orchestration. It closes with a caution that subagents carry real overhead and aren't worth it for small or tightly sequential tasks.

## Key Points

- **Definition and mechanics**: a subagent is an isolated Claude instance with its own context window; it reads files, explores code, or makes changes independently, then returns only the relevant result. Each starts fresh, unburdened by conversation history or invoked skills. Multiple subagents can run in parallel, each with different permissions (e.g., read-only research vs. full-editing implementation subagent).
- **Five signals for delegation**: (1) research requiring reading dozens of files — a subagent returns a synthesized summary instead of dumping raw content into the conversation; (2) independent, non-dependent sub-tasks (e.g., fixing the same pattern across several files) — parallel subagents finish faster; (3) unbiased/fresh review — a subagent has no inherited assumptions or blind spots from the main conversation (contrasted with `/clear`, which resets context too but destroys conversation history entirely, whereas a subagent preserves the main thread); (4) a second opinion before finalizing changes — an independent subagent checks for overfitting to tests or missed edge cases; (5) sequential multi-stage pipelines (design → implement → test) — each stage gets focused attention via clear handoffs, using output files (e.g., `docs/api-spec.md`) as the handoff mechanism between stages.
- **Quantified threshold**: exploring 10+ files, or 3+ independent pieces of work, is called out as a strong signal to direct Claude toward subagents.
- **Invocation ladder**: conversational natural-language requests (works across terminal, VS Code, JetBrains, web, desktop) → custom subagents (created via the `/agents` command or hand-written as markdown files with YAML frontmatter — name, description, tools, model — stored in `.claude/agents/` for project-level/team-shared or `~/.claude/agents/` for user-level/cross-project) → CLAUDE.md policies that mandate subagent use for specific triggers (e.g., always use a read-only subagent for code review) → skills for repeatable multi-step workflows that themselves launch parallel subagents (example: a `/deep-review` skill running three parallel subagent reviews — security, performance, style) → hooks for fully automated, event-triggered orchestration (example given: a Stop hook blocking completion until tests pass, though this example runs tests directly rather than via a subagent).
- **Background execution**: Ctrl+B sends a running subagent to the background so the main conversation can continue; results surface automatically on completion; `/tasks` lists anything running in the background.
- **Description field is the routing key**: for custom subagents, the `description` field is what Claude uses to decide when to delegate — specific trigger conditions ("reviews code for security issues before commits") route better than vague capability claims ("security expert").
- **Overhead caveat**: subagents spin up their own context, consume tokens, and add a layer of indirection; they're worth the cost only when context isolation, parallelism, or a fresh perspective actually helps. For small or tightly sequential tasks, the main conversation is simpler.
- **Anomaly**: the scraped page ends with unrelated newsletter-signup boilerplate ("Get the developer newsletter... Delivered monthly to your inbox") — standard page-widget footer text, not a prompt-injection attempt, but noted here since it's a non-substantive scrape artifact left in the raw file.

## Related

- [[ClaudeCodeSubagents]] — the concept page this article most directly expands
- [[MultiAgentSystem]] — orchestrator-subagent pattern; this article's sequential-pipeline guidance is in tension with existing anti-pattern guidance there
- [[CLAUDE-md]] — CLAUDE.md as the policy layer for mandatory subagent triggers
- [[ClaudeCodeSkills]] — skills as reusable multi-subagent workflow definitions
- [[ClaudeCodeHooks]] — hooks as the most automated layer of subagent orchestration
- [[ClaudeCode]] — the tool subagents extend
