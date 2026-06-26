---
title: "Validation"
type: concept
tags: [validation, testing, quality, developer-experience, ai-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One.md"]
last_updated: 2026-06-25
---

## Definition
Validation, in the context of AI coding agents, refers to objective, deterministic checks (such as tests, linters, and type checkers) that produce clear, actionable error messages, enabling agents to iteratively correct their output.

## Key Information
- One of the most important investments for increasing AI coding agent capability
- Must be deterministic and objective — agents need unambiguous pass/fail signals
- Error messages must be clear and actionable; agents cannot interpret "500 internal error" with no context
- Agents will run validation in loops: write code → run tests → fix errors → run tests → repeat; fast feedback (30 seconds) is critical
- Untestable codebases lead agents to produce meaningless validation (e.g., tests that always pass without meaningful checks)
- Validation tools must run at development time, not just in CI, to support fast agent iteration loops
- The same qualities that make validation useful for agents (clarity, speed, determinism) also make it useful for human developers
- Can be agent-generated (agents writing their own tests) or pre-existing (existing test suites, linters, type systems)

## Related
- [[summary-20251223 - Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One]] — source transcript
- [[AICodingAgents]] — primary consumer of validation feedback
- [[CodebaseTestability]] — prerequisite for effective validation
- [[DevelopmentEnvironmentStandardization]] — related tooling concern
- [[NoRegretsInvestments]] — validation improvement as a no-regrets investment
