---
title: "Clean Code Bases"
type: concept
tags: [code-quality, ai, productivity, software-engineering, entropy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
Clean code bases are codebases with good test coverage, type coverage, documentation, and modularity. Research from a Stanford University study of 120,000 developers shows that clean code bases amplify AI productivity gains, while unchecked AI in a codebase amplifies entropy and reduces code quality.

## Key Information
- Stanford University study of 120,000 developers found that AI productivity depends on codebase quality
- Clean code bases amplify AI gains and AI productivity
- Unchecked AI in a codebase amplifies entropy (disorder, technical debt)
- Case study: a company used AI unchecked — PR count increased but code quality decreased, more time spent on rework and refactoring, net productivity gain only ~1%
- Key practices for clean code bases: good test coverage, type coverage, documentation, modularity
- Marlene Mhangami advocates standardizing clean code practices across teams and the industry
- Prerequisite for effective TDD with AI: the codebase must be testable and well-structured
- Related to the agent entropy problem: AI agents create more entropy in messy codebases

## Related
- [[summary-20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft]] — source
- [[AgentEntropy]] — what unchecked AI creates
- [[CodebaseTestability]] — prerequisite for testing
- [[AgentLegibleCodebase]] — designing codebases agents can work with
- [[TDD with AI]] — methodology enabled by clean code
- [[Marlene Mhangami]] — speaker advocating clean code standards
- [[AIAddictionTrap]] — related risk of over-relying on AI
- [[CodeSlop]] — what AI produces in messy codebases
