---
title: "ACDC Framework"
type: concept
tags: [framework, agentic-development, code-quality, sonar, software-lifecycle]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
The ACDC (Agent-Centric Development Cycle) framework is Sonar's three-stage approach to embedding code quality throughout the AI-assisted development lifecycle: Guide (prevent quality issues at the source), Verify (catch issues before commit), and Solve (remediate issues that slip through). It operates across inner and outer loops to ensure LLM-generated code meets enterprise quality standards.

## Key Information

### Guide Phase
- **Sonar Sweep** (private beta): Treats training data quality — if problematic data is used to train models, models produce problematic code. Fix data at the source.
- **Sonar Context Augmentation**: Pushes the entire codebase context into the LLM so generated code aligns with existing architecture and standards.

### Verify Phase
- **SonarQube Agentic Analysis** (open beta): Runtime code analysis before commit — 1-5 seconds vs. 1-5 minutes for CI
- Integrated via MCP — agent can request analysis, receive results, and fix issues before code is committed
- Second line of defense: PR analysis runs after commit

### Solve Phase
- **SonarQube Remediation Agent** (open beta): Fixes issues that slipped through the verify stage
- Creates one PR per issue with fix, re-runs analysis and compilation, and discards any fix that creates regressions
- Can bulk-fix tech debt from the SonarQube dashboard — select issues and assign to agent
- Developers review, approve, and merge

### Architecture
- Inner loop: immediate feedback during coding (agentic analysis)
- Outer loop: PR-level quality gates and automated remediation
- Three phases work together to prevent, catch, and fix quality issues throughout the development cycle

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Sonar]] — creator of the framework
- [[SonarQube]] — platform implementing Verify and Solve phases
- [[Enterprise Quality Code]] — quality standard the framework enforces
- [[Sonar Leaderboard]] — evaluation context
- [[LLM Code Quality Evaluation]] — evaluation methodology
- [[AgenticEngineering]] — broader paradigm shift
- [[Mixed Quality Training Data]] — problem addressed in Guide phase
