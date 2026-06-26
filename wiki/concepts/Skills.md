---
title: "Skills"
type: concept
tags: [coding-agents, prompt-engineering, system-prompt, extensibility]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md"]
last_updated: 2026-06-25
---

## Definition
Skills are an extendable system prompt mechanism in Claude Code that allows loading specialized instructions on demand. They function as optional context modules — the agent has a list of available skills with one-line descriptions and can invoke them when needed, loading additional context without permanently cluttering the main context window.

## Key Information
- Think of skills as extendable system prompts loaded on demand
- Designed to avoid cluttering the main context while providing deep specialized knowledge when needed
- Examples: docs updates (writing style and product knowledge), editing Microsoft Office files, design style guides, deep research
- Jared Zoneraich built his entire slide deck using skills: a slide-dev skill, a deep research skill, and a design skill
- Skills are not automatically invoked — users often need to manually call them
- The model should theoretically pick up skills automatically based on one-line descriptions, but this doesn't always work well yet
- Represents a new "first class paradigm" in agent design, similar to todo lists
- May require more post-training to get models to reliably invoke skills when appropriate
- Zoneraich built a deep research skill by feeding Claude Code an article on how deep research works and asking it to rebuild as a skill
- Brendan O'Leary describes skills as reusable playbooks for agents — on-demand workflows for repetitive tasks (motion graphics, daily/weekly/monthly changelog compilation). Skills are part of a three-bucket agent configuration system alongside modes (role-based behavior) and agents.md (always-on project rules).

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[ClaudeCode]] — the agent that implements skills
- [[Context Management]] — the problem skills help solve
- [[TodoListPattern]] — another prompt-based paradigm in Claude Code
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source (skills as reusable playbooks)
- [[AgentModes]] — complementary mode-based configuration
- [[AgentsDotMd]] — complementary always-on configuration
