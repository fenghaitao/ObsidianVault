---
title: "summary-2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-05-27 - How CodeRabbit used Claude to build an agent orchestration system.md"]
last_updated: 2026-07-07
---

## Core Summary

CodeRabbit built an agent orchestration layer on Claude that inserts a structured planning phase between a coding request and a coding agent. The core insight is that planning quality determines output quality: vague prompts force coding agents to fill gaps with plausible but incorrect assumptions, and late validation in AI workflows is disproportionately expensive. The orchestration system coordinates multiple Claude model tiers (Opus for strategy, Sonnet for planning structure, Haiku for narrowly scoped operations) to produce a collaborative Product Requirements Document (PRD) that stakeholders review before any code is generated. CodeRabbit validated this approach through a custom evaluation harness using LLM judges to score plan quality dimensions and compare outcomes with and without the planning step.

## Key Points

- CodeRabbit's analysis of AI-generated pull requests found the most frequent failure mode was code that compiled and passed tests but didn't solve the intended problem — caused by developers omitting requirements they consider obvious and the agent filling gaps with guesses.
- The planning layer is explicitly positioned above Claude Code's Plan Mode: it is a higher-level orchestration that runs before Claude Code, making everything explicit and surfacing assumptions before implementation begins.
- The output is a collaborative PRD created with full context, validated by stakeholders, and used by Claude Code to generate a fine-grained implementation plan — serving as a shared artifact for alignment, onboarding, and later validation.
- CodeRabbit matches model tiers to task complexity: Opus for orchestration and strategic understanding, Sonnet for sequencing into structured steps, Haiku for context distillation and targeted tool use — guided by evaluation data rather than intuition.
- The team built a custom evaluation harness with LLM judges scoring plan quality dimensions, then measured downstream code quality, scope creep, and token consumption with and without the planning step to isolate planning's value.
- Finding the right level of plan abstraction required iteration: overly granular plans went stale as codebases shifted; overly high-level plans left room for agent assumption-filling.

## Related

- [[CodeRabbit]] — the company that built this system
- [[AgentOrchestration]] — the orchestration pattern
- [[ModelTiering]] — matching model tiers to task complexity
- [[ClaudeCode]] — the coding agent the planning layer sits above
- [[AgenticCoding]] — the broader paradigm this approach improves
