---
title: "CodeReview"
type: concept
tags: [claude-code, code-review, multi-agent, quality]
sources: ["raw/01-articles/claude/2026-03-09 - Bringing Code Review to Claude Code.md", "raw/01-articles/claude/2026-06-03 - Running an AI-native engineering org.md"]
last_updated: 2026-07-07
---

## Definition

Code Review is a Claude Code feature (research preview, Team/Enterprise) that dispatches a team of agents on every pull request to find bugs in parallel, verify them to filter false positives, rank by severity, and post a single high-signal overview comment plus inline bug comments — a deeper, more expensive alternative to the lighter-weight [[AutomatedSecurityReview|Claude Code GitHub Action]].

## Key Information

- **Motivation**: as AI-assisted code output grows (Anthropic engineers' output up 200% year-over-year), human review has become a bottleneck, with reviewers increasingly skimming rather than deeply reading PRs.
- **Mechanism**: a multi-agent system (see [[MultiAgentSystem]]) scales review depth with PR size/complexity — larger or more complex changes get more agents and a deeper read, trivial ones get a lightweight pass. Average review time ~20 minutes. Does not auto-approve PRs — that remains a human decision.
- **Internal results at Anthropic**: substantive review comments rose from 16% to 54% of PRs; large PRs (1,000+ lines) get findings 84% of the time (avg. 7.5 issues), small PRs (<50 lines) 31% of the time (avg. 0.5 issues); under 1% of findings are marked incorrect by engineers.
- **Concrete catches**: flagged a one-line production-service change as critical when it would have broken authentication — fixed before merge; on an open-source TrueNAS ZFS encryption refactor, surfaced a pre-existing type-mismatch bug in adjacent (untouched-by-the-PR) code silently wiping the encryption key cache on every sync.
- **Cost**: billed on token usage, averaging $15-25 per review depending on PR size/complexity; admins have spend/usage controls.
- Available now as a research preview in beta for Team and Enterprise plans.

### Usage on the Claude Code Team

The [[ClaudeCode]] engineering team at [[Anthropic]] uses Code Review heavily as part of their [[AINativeEngineeringOrg|AI-native engineering org]] transformation. Claude handles style, linting, PR feedback requests, catching bugs before full commits, and adding tests. Human review is reserved for where it still matters: legal review, security-sensitive code and trust boundaries, and product sense/taste from PMs and designers. The right balance of trust vs. verify keeps changing as models improve. See [[summary-2026-06-03 - Running an AI-native engineering org]].

## Related

- [[ClaudeCode]] — the product Code Review extends
- [[AutomatedSecurityReview]] — the earlier, lighter-weight security-focused review this complements (not replaces)
- [[MultiAgentSystem]] — the underlying multi-agent architecture
- [[summary-2026-03-09 - Bringing Code Review to Claude Code]] — source article
- [[summary-2026-06-03 - Running an AI-native engineering org]] — blog article describing team usage patterns
- [[AINativeEngineeringOrg]] — organizational context for automated review adoption
- [[FionaFung]] — engineering leader describing the human-in-the-loop boundaries
