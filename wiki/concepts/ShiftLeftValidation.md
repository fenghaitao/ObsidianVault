---
title: "ShiftLeftValidation"
type: concept
tags: [validation, platform-engineering, agents, ci-cd, local-first]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza.md"]
last_updated: 2026-06-30
---

## Definition
Shift-left validation is the practice of moving validation and failure detection as early as possible in the development workflow — ideally on the local machine — rather than deferring checks to CI/CD pipelines or remote environments. For AI agents, this means failing fast within the agent's iteration loop instead of pushing to version control and waiting minutes for a pipeline failure.

## Key Information
- Juan Herreros Elorza identifies shift-left as critical for AI agent productivity: "If something is going to fail, it should fail as soon as possible"
- AI agents work in iterative loops on the local machine — pushing to version control only to fail minutes later in CI breaks the agent's flow and wastes time
- Key practices: validate configuration, schemas, and dependencies locally; run tests and linting before pushing; use API-based validation that returns immediate feedback
- Contrast with traditional pipeline-based validation where developers push code and discover failures asynchronously — tolerable for humans, disruptive for agents
- Enables the agent's natural loop: try → get immediate feedback → adjust → retry until success
- Part of the broader "local-first" principle for agent-ready platforms

## Related
- [[summary-20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza]] — source transcript
- [[AgentReadyPlatform]] — the goal state
- [[APIFirstDesign]] — enables local validation via APIs
- [[PlatformEngineering]] — parent discipline
- [[AgentsAsPlatformUsers]] — the paradigm driving shift-left
- [[AgenticLoop]] — the iteration pattern shift-left supports
