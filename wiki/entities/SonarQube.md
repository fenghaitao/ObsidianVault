---
title: "SonarQube"
type: entity
tags: [product, static-analysis, code-quality, security, sonar, devtools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
SonarQube is Sonar's flagship static code analysis platform for continuous code quality and security inspection. It has been extended with AI-specific capabilities including agentic analysis (pre-commit checks in 1-5 seconds), remediation agents (automated PR-based fixes), and an evaluation framework for assessing LLM-generated code quality.

## Key Information
- Enterprise-grade static analysis platform used for code quality and security
- SonarQube Agentic Analysis (open beta): runtime code analysis before commit, integrated via MCP — takes 1-5 seconds vs. 1-5 minutes for traditional CI
- Agent receives analysis results and can fix issues before code is committed
- SonarQube Remediation Agent (open beta): creates one PR per issue, runs analysis and compilation, discards regressions
- Can bulk-fix tech debt from the SonarQube dashboard — select issues and assign to agent
- Dashboard provides visibility into tech debt and quality metrics
- PR analysis runs after commit as a second line of defense
- Part of the ACDC framework's Verify and Solve phases

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Sonar]] — parent company
- [[ACDC Framework]] — product strategy framework
- [[Sonar Leaderboard]] — related evaluation initiative
- [[Enterprise Quality Code]] — quality standard enforced
- [[Cyclomatic Complexity]] — metric measured
- [[Cognitive Complexity]] — Sonar proprietary metric
