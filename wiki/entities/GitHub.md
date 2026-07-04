---
title: "GitHub"
type: entity
tags: [company, version-control, devops, ci-cd, claude-code]
sources: ["raw/01-articles/claude/2025-08-06 - Automate security reviews with Claude Code.md", "raw/01-articles/claude/2025-10-01 - How enterprises are driving AI transformation with Claude.md"]
last_updated: 2026-07-04
---

## Definition

GitHub is a version control and collaboration platform for software development, widely used for hosting repositories, managing pull requests, and running CI/CD pipelines via GitHub Actions.

## Key Information

- [[ClaudeCode]] integrates with GitHub via a GitHub Action that automatically reviews pull requests for security vulnerabilities — see [[AutomatedSecurityReview]].
- Anthropic hosts the security review GitHub Action and `/security-review` command documentation at `anthropics/claude-code-security-review` on GitHub.
- More broadly, GitHub Actions integration lets Claude Code automate PR comments, test generation, and code review as part of a team's existing CI/CD pipeline.
- [[Netflix]] is cited (alongside GitHub itself) as an example of developers tackling complex, codebase-spanning tasks with Claude Sonnet 4.5.

## Related

- [[ClaudeCode]] — integrates with GitHub via Actions for automated PR review
- [[AutomatedSecurityReview]] — the security-review feature delivered via GitHub Actions
- [[GitHubIntegration]] — the broader native GitHub sync feature for Claude Enterprise
- [[Claude4.5Sonnet]] — model cited for helping GitHub developers with codebase-spanning tasks
- [[Netflix]] — cited alongside GitHub for the same capability
- [[summary-2025-08-06 - Automate security reviews with Claude Code]] — source article on the security review GitHub Action
- [[summary-2025-10-01 - How enterprises are driving AI transformation with Claude]] — source noting GitHub developers' use of Claude Sonnet 4.5
