---
title: "Memory and Dreaming for Self-Learning Agents (San Francisco)"
type: source
tags: [memory, dreaming, managed-agents, multi-agent, self-learning]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/18 - Memory and dreaming for self-learning agents.md]
last_updated: 2026-06-23
---

## Core Summary

Mahesh from Anthropic's platform team presents memory and dreaming as the next primitive for self-learning agents, covering similar ground to the London version with additional detail on multi-agent memory architecture and enterprise controls. Memory is modeled as a file system that Claude manages using bash and grep. Dreaming is launched in research preview as an out-of-band batch process that analyzes cross-session transcripts to find patterns, deduplicate, verify, and enrich memory stores. The SRE agent demo shows read-only org-wide memory (runbooks, SLOs) alongside read-write working memory, with dreaming identifying patterns like a recurring 60-second CPU spike triggering retry logic.

## Key Points

- **Memory evolution:** CLAUDE.md (constrained, user+agent notes) → Memory tool in SDKs (well-specified tool call) → File-system-based memory (Claude manages with bash/grep, minimal constraints).
- **Opus 4.7 state-of-the-art at file-system memory:** Better at discerning what to remember, how to structure memory, and organizing it within a file system.
- **Permission scopes:** Read-only for org-wide knowledge (runbooks, SLOs), read-write for per-agent working memory. Mix and match per session.
- **Optimistic concurrency:** Content hash prevents agents from clobbering each other's writes in multi-agent systems.
- **Enterprise controls:** Version history with full audit trail, attribution metadata (which agent, which session, when), standalone API for external management (PII scanning, cleanup, cloning).
- **Dreaming launched in research preview:** Out-of-band batch process, separate from task completion objectives. Harvey saw 6x completion rate increase on legal benchmark.
- **Dreaming as compute scaling:** Similar to test-time compute — spending more tokens upfront to curate high-quality memory pays dividends for all downstream agents.
- **Dreaming as search index:** Creates and maintains a high-quality index that all agents benefit from, amortizing the upfront cost.

## Related

- [[summary-18 - Memory and dreaming for self-learning agents]] — London version of the same talk
- [[ClaudeManagedAgents]] — the platform for memory and dreaming
- [[AgenticMemory]] — the concept of persistent agent learning
- [[ClaudeFable5]] — Opus 4.7 enabling file-system memory
