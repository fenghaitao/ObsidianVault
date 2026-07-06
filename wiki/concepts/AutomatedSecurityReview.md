---
title: "AutomatedSecurityReview"
type: concept
tags: [security, claude-code, automation, github-actions, devsecops]
sources: ["raw/01-articles/claude/2025-08-06 - Automate security reviews with Claude Code.md"]
last_updated: 2026-07-04
---

## Definition

Automated security review is a feature pattern that automates detection (and optionally remediation) of security vulnerabilities in code, integrated directly into a developer's terminal workflow and CI/CD pipeline via [[ClaudeCode]].

## Key Information

- **Terminal workflow**: the `/security-review` command runs ad-hoc, pre-commit vulnerability analysis in [[ClaudeCode]], using a specialized security-focused prompt. Claude can also implement fixes for issues it finds, keeping review in the "inner development loop" where issues are cheapest to fix.
- **CI/CD workflow**: a GitHub Action automatically analyzes every new pull request, applies customizable rules to filter false positives and known issues, and posts inline PR comments with concerns and fix recommendations — creating a consistent security baseline across a team.
- Both are available to all Claude Code users (as of August 2025); documented at `anthropics/claude-code-security-review` on [[GitHub]].
- **Anthropic's own dogfooding**: the GitHub Action caught a DNS-rebinding remote code execution vulnerability in a local HTTP server, and an SSRF vulnerability in an internal credential-management proxy — both fixed before merging to production.
- See [[VulnerabilityDetection]] for the specific vulnerability classes these features target.
- Positioned by Anthropic as a concrete instance of the "find bugs before you ship them" recommendation in its broader [[AIAcceleratedOffense]] security-program guidance, motivated by [[ProjectGlasswing]]'s finding that AI is collapsing the time needed to turn known vulnerabilities into exploits.

## Related

- [[ClaudeSecurity]] — sibling standalone product (public beta, April 2026): repo-level scheduled scanning via claude.ai/security, distinct from this terminal/CI feature
- [[ClaudeCode]] — the tool hosting both the `/security-review` command and the GitHub Action
- [[VulnerabilityDetection]] — the vulnerability classes detected
- [[CodeSecurity]] — the broader security-in-development-workflows concept this feature belongs to
- [[GitHub]] — hosts the GitHub Action integration and documentation
- [[summary-2025-08-06 - Automate security reviews with Claude Code]] — source announcement
- [[CodeReview]] — the deeper, more expensive multi-agent PR review feature that complements this one
- [[AIAcceleratedOffense]] — broader org-wide security-program playbook this feature is one instance of
