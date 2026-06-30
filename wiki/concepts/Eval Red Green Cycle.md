---
title: "Eval Red Green Cycle"
type: concept
tags: [evals, agents, prompt-engineering, workflow, coding-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Fighting AI with AI — Lawrence Jones, Incident.md"]
last_updated: 2026-06-30
---

## Definition

The eval red-green cycle is an automated workflow where coding agents modify AI prompts through a structured pass/fail loop: create an eval case proving a failure (red), modify the prompt until the eval passes (green), verify no other evals regressed, and consolidate the prompt to prevent bloat. It treats evals as unit tests for prompts, with agents acting as the developer in a TDD-like loop.

## Key Information

- **Origin**: Developed at [[IncidentIo]] to allow coding agents (Claude Code, Codex) to reliably modify prompts without human intervention
- **Red phase**: The agent creates an eval case that reproduces the failure — proving the current prompt produces wrong output for a specific input
- **Green phase**: The agent modifies the prompt to make the new eval pass, often running multiple repeats to account for non-determinism
- **Regression check**: After the new eval passes, the agent runs the full eval suite to ensure no existing evals broke
- **Consolidation pass**: A final step where the agent attempts to simplify the prompt, since repeated modifications tend to produce bloated, hard-to-maintain prompts
- **Prerequisite**: Requires [[Agent-Ready Eval Tooling]] — a CLI or API that lets coding agents programmatically interact with eval suites
- **Relationship to TDD**: Mirrors the test-driven development cycle (red → green → refactor) applied to prompt engineering
- **Scalability**: This cycle works well when you know which prompt to change, but breaks down in multi-agent systems where the root cause is unclear — requiring complementary patterns like [[File System Downloads for Agent Debugging]]

## Related

- [[summary-20260517 - Fighting AI with AI — Lawrence Jones, Incident]] — primary source
- [[Agent-Ready Eval Tooling]] — prerequisite CLI infrastructure
- [[EvalEngineering]] — the practice of crafting evaluation prompts
- [[EvalFlywheel]] — broader continuous improvement loop
- [[Eval-Driven Development]] — TDD applied to AI evaluation
- [[Evaluator-Optimizer Pattern]] — related agent pattern
- [[PromptOptimization]] — prompt improvement methodology
- [[IncidentIo]] — company that developed this workflow
