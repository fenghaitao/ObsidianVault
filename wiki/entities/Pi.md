---
title: "Pi"
type: entity
tags: [tool, ai-coding-assistant, agent-cli, harness, multi-model]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260604 - Claude Plans, Gemini Designs： The Workflow to Build BEAUTIFUL Frontends.md"
last_updated: 2026-06-21
---

## Definition

Pi is a coding-agent harness (CLI) that [[ColeMedin]] uses as a provider-flexible alternative to [[ClaudeCode]] / [[Codex]] — notably to run non-Anthropic models like Gemini 3.5 Flash (via **OpenRouter**). It recurs in Cole's "Claude Code, Codex, Pi, you name it" framing as a third major coding agent.

## Key Information

- **Provider flexibility**: configured with OpenRouter, Pi can drive many models (Gemini 3.5 Flash, Kimi K2.6, etc.) — making it the natural host for the non-Claude steps of a [[CrossProviderWorkflow]].
- **Skills-compatible**: skills are invoked the same way as in [[ClaudeCode]] (`/skill-name` + path arguments), and `/model` switches the active model — so Cole's skill-based workflows port to Pi with minimal change.
- **Role in the frontend workflow** (`summary-claude-plans-gemini-designs`): Pi runs the **UI design** step on Gemini 3.5 Flash while Claude Code runs the Opus/Sonnet steps; [[Antigravity]] is the alternative Gemini host.

## Related

- [[ClaudeCode]], [[Codex]] — the other major coding agents Pi sits alongside
- [[Antigravity]] — alternative host for Gemini-powered steps
- [[CrossProviderWorkflow]] — where Pi runs the non-Claude nodes
- [[ClaudeSkills]] — Pi invokes skills like Claude Code does
- [[ColeMedin]] — user
- [[summary-20260604 - Claude Plans, Gemini Designs： The Workflow to Build BEAUTIFUL Frontends]] — primary source
