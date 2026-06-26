---
title: "AutomatedValidation"
type: concept
tags: [concept, validation, testing, linters, ci-cd, coding-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Making Codebases Agent Ready – Eno Reyes, Factory AI.md"]
last_updated: 2026-06-25
---

## Definition
Automated validation encompasses the set of programmatic checks and verifications in a codebase that confirm code correctness, quality, and adherence to standards without human intervention.

## Key Information
- The eight pillars referenced by Eno Reyes: linters, tests (unit/integration/E2E), documentation, API specs, code formatting, CI/CD pipelines, code review automation, and agent-specific guidance (AGENTS.md)
- Key properties of good validation: objective truth, quick to validate, scalable (parallelizable), low noise, continuous signals (not just binary)
- Most organizations lack rigorous validation because humans compensate with manual testing and intuition
- Flaky builds and low test coverage (50-60%) are common but break agent capabilities
- "A slop test is better than no test" — having any validation creates a foundation for iterative improvement
- Validation criteria should be opinionated enough that agents consistently produce senior-engineer-quality code
- Tests should be designed to fail when AI-generated slop is introduced and pass when high-quality AI code is introduced
- The frontier of validation is expanding with tools like BrowserBase for visual/front-end testing

## Related
- [[summary-20251222 - Making Codebases Agent Ready – Eno Reyes, Factory AI]] — source transcript
- [[AgentReadyCodebases]] — the goal state
- [[SpecificationDrivenDevelopment]] — the paradigm enabled by validation
- [[VerificationAsymmetry]] — why validation is powerful
- [[DevXFeedbackLoop]] — the cycle validation enables
- [[BrowserBase]] — tool expanding validation frontier
