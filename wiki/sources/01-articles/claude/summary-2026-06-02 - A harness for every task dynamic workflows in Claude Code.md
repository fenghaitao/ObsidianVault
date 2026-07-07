---
title: "summary-2026-06-02 - A harness for every task dynamic workflows in Claude Code"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-06-02 - A harness for every task dynamic workflows in Claude Code.md"]
last_updated: 2026-07-07
---

## Core Summary

Claude Code now supports **dynamic workflows** — the ability to write and orchestrate its own multi-agent harness on the fly, custom-built for the task at hand. Powered by Claude Opus 4.8, dynamic workflows execute JavaScript files with special functions for spawning and coordinating subagents, letting Claude choose models, isolation levels, and coordination patterns per task. The article catalogs common workflow patterns (classifier routing, fan-out/synthesis, adversarial verification, tournaments, parallel competition, agentic loops, quarantine, model selection) and concrete use cases (debugging, research, triage, code migration, CLAUDE.md mining, evals), while cautioning that workflows use significantly more tokens and are best suited for complex, high-value tasks.

## Key Points

- Dynamic workflows combat single-context-window failure modes (context rot, self-preferential bias, lack of parallelization) by orchestrating separate Claude subagents with their own context windows and focused, isolated goals.
- Workflows are triggered by asking Claude to make one or using the trigger word "ultracode" — Claude then writes a JavaScript harness with special functions for spawning/coordinating subagents.
- Common workflow patterns include: classifier routing, fan-out with synthesis, adversarial verification, tournament selection, parallel competition, agentic loops (unknown work amounts), quarantine (security), and model-selection classifiers.
- Concrete use cases span debugging (independent hypotheses), research (fan-out web searches with verification), triage (classify, dedupe, act), code migration (e.g., Bun's Zig-to-Rust rewrite), CLAUDE.md rule mining, evals, and design exploration.
- Workflows can be saved to `~/.claude/workflows`, distributed via skills, paired with `/loop` for recurrence, and given explicit token budgets. Resuming a session after interruption picks up where the workflow left off.
- Written by Thariq Shihipar and Sid Bidasaria, members of technical staff on the Claude Code team at Anthropic.

## Related

- [[ClaudeCode]] — the tool where dynamic workflows run
- [[DynamicWorkflows]] — the concept this article introduces
- [[ClaudeCodeSubagents]] — subagent mechanism workflows orchestrate
- [[AgentWorkflowPatterns]] — the earlier static workflow patterns this extends
- [[MultiAgentSystem]] — the broader multi-agent architecture
- [[AgenticLoop]] — the loop pattern workflows can implement
- [[ThariqShihipar]] — co-author, Claude Code team member
