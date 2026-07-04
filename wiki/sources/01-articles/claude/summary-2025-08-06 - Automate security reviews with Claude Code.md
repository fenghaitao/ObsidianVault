---
title: "summary-2025-08-06 - Automate security reviews with Claude Code"
type: source
tags: [source, original-material, security, claude-code, github-actions]
sources: ["raw/01-articles/claude/2025-08-06 - Automate security reviews with Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic introduced automated security reviews in [[ClaudeCode]]: a new `/security-review` terminal command for ad-hoc vulnerability analysis before committing code, and a GitHub Actions integration that automatically reviews every new pull request. Both features are built on a specialized security-focused prompt covering common vulnerability classes (SQL injection, XSS, auth flaws, insecure data handling, dependency vulnerabilities) and can also have Claude implement fixes. Anthropic reports using these features internally — including to secure Claude Code itself — catching a DNS-rebinding remote code execution vulnerability and an SSRF vulnerability in a credential-management proxy before either reached production.

## Key Points

- **`/security-review` command**: run ad-hoc from the terminal before committing; searches the codebase for vulnerabilities and explains issues found; Claude can also implement fixes.
- Checks for: SQL injection, cross-site scripting (XSS), authentication/authorization flaws, insecure data handling, dependency vulnerabilities.
- **GitHub Actions integration**: triggers automatically on new pull requests, reviews code changes, applies customizable rules to filter false positives/known issues, and posts inline PR comments with concerns and fix recommendations.
- Both features available now for all Claude Code users; documented at `anthropics/claude-code-security-review` on [[GitHub]].
- **Internal dogfooding at Anthropic**: since deploying the GitHub Action, it has caught vulnerabilities in Anthropic's own code before merge, including:
  - A remote code execution vulnerability exploitable via DNS rebinding, found in a new internal tool's local HTTP server.
  - An SSRF vulnerability in a proxy system built for secure management of internal credentials.

## Related

- [[ClaudeCode]] — the tool these features extend
- [[AutomatedSecurityReview]] — the concept this article introduces
- [[VulnerabilityDetection]] — the vulnerability classes these features target
- [[GitHub]] — hosts the documentation and the GitHub Action integration
