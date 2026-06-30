---
title: "The Multiverse (agent development)"
type: concept
tags: [agents, git, concurrency, exploration, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
The Multiverse, in agentic software development, is a future state where AI agents work on multiple Git commit candidates simultaneously to address the same development plan. Instead of starting from the latest commit (the "tip of the ledger"), agents explore multiple starting points in parallel to find the optimal path to implementation.

## Key Information
- Proposed by [[HugoSantos]] as a likely future state beyond the current agent development paradigm
- Agents don't start from the latest commit — they work on multiple candidates simultaneously
- Purpose: explore multiple implementation paths for the same [[Intent and Plan]]
- Dramatically increases resource usage because of all the candidates explored simultaneously
- Requires the inner agent loop to be extremely fast to be feasible
- Depends on [[Stateful Development Environment]] to maintain context across candidates
- All candidates feed into the [[Pre-merge Queue]] for reconciliation
- Represents the logical extreme of agent parallelism in software development
- Timeline: weeks to months, not years

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[Continuous Compute]] — paradigm that enables the Multiverse
- [[Pre-merge Queue]] — where Multiverse candidates are reconciled
- [[Git Ledger]] — the serialized target candidates compete for
- [[Serializability]] — the guarantee needed across candidates
- [[Stateful Development Environment]] — prerequisite for Multiverse speed
- [[Intent and Plan]] — the goal agents pursue across multiple candidates
