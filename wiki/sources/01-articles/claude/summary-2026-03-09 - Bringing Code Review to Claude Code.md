---
title: "summary-2026-03-09 - Bringing Code Review to Claude Code"
type: source
tags: [source, claude-code, code-review, multi-agent]
sources: ["raw/01-articles/claude/2026-03-09 - Bringing Code Review to Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic launched **Code Review** in Claude Code (research preview, Team/Enterprise): a multi-agent system dispatched on every PR that finds bugs in parallel, verifies them to filter false positives, ranks by severity, and posts a high-signal overview comment plus inline bug comments — a deeper, more expensive alternative to the existing (still-available, open-source) Claude Code GitHub Action.

## Key Points

- Motivated by code review becoming a bottleneck as AI-assisted code output grows (Anthropic engineers' output per person up 200% in a year); reviewers increasingly skim rather than deeply read PRs.
- **Internal results at Anthropic**: substantive review comments rose from 16% to 54% of PRs after adopting Code Review; large PRs (1,000+ lines) get findings 84% of the time (averaging 7.5 issues), small PRs (<50 lines) 31% of the time (averaging 0.5 issues); under 1% of findings are marked incorrect by engineers. Does not auto-approve PRs — that stays a human call.
- **Scaling behavior**: reviews scale with PR size/complexity — larger or more complex changes get more agents and a deeper read; trivial changes get a lightweight pass. Average review takes ~20 minutes.
- **Concrete catches**: a one-line production-service change that looked routine was flagged as critical (would have broken authentication) and fixed before merge; on a TrueNAS ZFS encryption refactor (open-source, early access), Code Review surfaced a pre-existing type-mismatch bug in adjacent code that was silently wiping the encryption key cache on every sync.
- **Cost**: billed on token usage, averaging $15-25 per review depending on PR size/complexity; admins have spend/usage controls.
- Available now as a research preview in beta for Team and Enterprise plans.

## Related

- [[ClaudeCode]] — the product Code Review extends
- [[AutomatedSecurityReview]] — the earlier, lighter-weight security-focused review mechanism (the `/security-review` command and GitHub Action) this complements
- [[MultiAgentSystem]] — the multi-agent architecture underlying Code Review's parallel bug-finding
