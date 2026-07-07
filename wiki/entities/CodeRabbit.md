---
title: "CodeRabbit"
type: entity
tags: [company, code-review, developer-tool, claude-api, agent-orchestration]
sources: ["raw/01-articles/claude/2026-04-29 - Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp.md", "raw/01-articles/claude/2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system.md"]
last_updated: 2026-07-07
---

## Definition

CodeRabbit is an AI-powered code review platform that also builds agent orchestration systems on [[Claude]]. It bundles Anthropic's [[ClaudeCodeSkills|claude-api]] skill (April 2026) and has developed a planning-first agent orchestration layer that inserts structured planning between a coding request and a coding agent.

## Key Information

### Claude API Skill Integration

- One of four external developer tools (alongside [[JetBrains]], [[ResolveAI|Resolve AI]], and [[Warp]]) that bundle the open-source `claude-api` skill from `anthropics/skills`.
- The skill was first introduced inside [[ClaudeCode]] in March 2026 before being bundled by partner tools.

### Agent Orchestration System

CodeRabbit built an [[AgentOrchestration|agent orchestration]] layer on Claude that sits between a coding request and a coding agent. The system was driven by an observation from CodeRabbit's VP of AI, David Loker: the most frequent failure mode in AI-generated pull requests was code that compiled and passed tests but didn't solve the intended problem. The root cause was developers omitting requirements they considered obvious, and coding agents filling the gaps with plausible guesses.

The orchestration system:
- Runs a structured planning phase before any code is generated
- Coordinates multiple [[Claude]] model tiers using [[ModelTiering]]: Opus for strategic understanding, Sonnet for planning structure, Haiku for context distillation and targeted tool use
- Produces a collaborative Product Requirements Document (PRD) that stakeholders review before implementation
- Positions itself above [[ClaudeCode]]'s Plan Mode as a higher-level orchestration that makes all assumptions explicit
- Uses a custom evaluation harness with LLM judges to score plan quality and compare outcomes with and without the planning step

The PRD becomes a shared artifact capturing what was decided and why — helping teams avoid rework, validate that output matched intent, and onboard new engineers.

## Related

- [[summary-2026-04-29 - Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp]] — source summary
- [[summary-2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system]] — source summary
- [[AgentOrchestration]] — the orchestration pattern CodeRabbit implements
- [[ModelTiering]] — the model-to-task matching practice used in the system
- [[ClaudeCodeSkills]] — the Skills mechanism the claude-api skill is an instance of
- [[ClaudeCode]] — where the claude-api skill originated, and the coding agent the planning layer sits above
- [[AgenticCoding]] — the broader paradigm this approach improves
