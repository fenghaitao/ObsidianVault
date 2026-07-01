---
title: "Decision Capture Loop"
type: concept
tags: [agent-harness, enforcement, feedback-loop, git-hooks, ci, linting]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence.md"]
last_updated: 2026-06-30
---

## Definition

The Decision Capture Loop is a reinforcement loop that enforces architectural and process rules on AI agents through automated checks (git hooks, skills, CI, linters) that provide immediate feedback at commit time, linking violations back to the governing documents (ADRs, PRDs, design systems) that explain why the rule exists.

## Key Information

- The loop: git hooks → skills → CI → linters → other checks
- The agent's goal is to deliver a pull request. To do that, they must use git, so git hooks run predefined tasks. The same tasks execute on CI — if agents skip hooks, they get caught on CI.
- Includes: linting, formatting, type checking, code duplication, architecture checks, document linting — everything automatable
- Code reviews are no longer about style, tabs, and spaces. These are rules, enforced and automated. There is no space for discussion about them anymore — reviews focus on high-level concepts instead.
- Core principle: "What you cannot find, you cannot enforce."
- The agent workflow: try to commit → get rejected → get linked back to the governing document → read it → fix it → iterate
- The loop is generic, but the focus changes per context via skills: ADR skill (look up ADRs and affected code), PRD skill, UI loop (skip certain checks, iterate quickly in browser), test skill (run focused suite based on code coverage and file changes), goal execution skill (keep decisions for later review)
- All skills provide focus within the same loop structure
- Context compacts are an accepted cost: sessions with 20-50 compacts are fine because the important things survive and the agent always looks them up again
- The goal: multi-hour sessions with a clear goal where agents operate autonomously with defined rules

## Related

- [[summary-20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence]] — source
- [[AgentHarness]] — broader concept of agent harness engineering
- [[Architecture Decision Record (ADR)]] — a document type enforced by the loop
- [[PRD (Product Requirements Document)]] — a document type enforced by the loop
- [[BehaviorDriven Development (BDD)]] — a practice validated by the loop
- [[Design System]] — rules enforced by the loop
- [[Architecture Enforcement]] — the module import linting aspect of the loop
- [[Enforce Dont Instruct]] — related principle
- [[Compacting]] — context compacts are an accepted cost of the loop
- [[AgentSpecific MD Files]] — skills that focus the loop
