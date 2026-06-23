---
title: "summary-skills-vs-other-features"
type: source
tags: [source, claude-code, skills, comparison, transcript]
sources: [raw/03-transcripts/Claude/Claude Code Skills/04 - How skills compare to other Claude Code features.md]
last_updated: 2026-06-23
---

## Core Summary

Claude Code offers multiple customization mechanisms, each solving different problems: CLAUDE.md (always-on project standards), skills (task-specific, on-demand expertise), sub-agents (isolated execution contexts), hooks (event-driven automation), and MCP servers (external tools). Skills enhance Claude's knowledge for the current task and activate based on request matching. CLAUDE.md loads into every conversation. Sub-agents run in separate contexts. Hooks fire on events. A typical setup combines all: CLAUDE.md for always-on standards, skills for task expertise, hooks for automated operations.

## Key Points

- **CLAUDE.md:** loads into every conversation; for project-wide standards, constraints, framework preferences, coding style.
- **Skills:** load on demand via description matching; for task-specific expertise, knowledge only relevant sometimes, detailed procedures.
- **Sub-agents:** run in isolated context; for delegated tasks, different tool access, context isolation.
- **Hooks:** fire on events (file save, tool calls); for automated linting, validation, side effects.
- **MCP servers:** provide external tools; for connecting to databases, APIs, productivity apps.
- Skills add knowledge to current conversation; sub-agents work independently and return results.
- Don't force everything into skills when another option fits better; combine them for comprehensive customization.

## Related

- [[ClaudeCodeSkills]] — the skills system
- [[CLAUDE-md]] — always-on instructions
- [[ClaudeCodeHooks]] — event-driven automation
- [[ModelContextProtocol]] — external tool integration
- [[ClaudeCode]] — the tool being customized
