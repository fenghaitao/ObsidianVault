---
title: "Merge Queue"
type: concept
tags: [CI-CD, git, merge, serialization, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
The Merge Queue is the serialization bottleneck in traditional CI/CD where concurrent PRs must be ordered and committed to the repository one at a time. Under agentic development at scale, this becomes the critical limiting factor — analogous to a database serialization problem — and must evolve into a [[PreMerge Queue]] to handle the volume.

## Key Information
- Described by [[HugoSantos]] as analogous to high-performance database serialization
- Every change must go into a single ledger, requiring locking to commit
- With human developers: lock time is large (minutes to hours) but change volume is low — manageable
- With agents: lock time must be short (seconds) but change volume is massive — the merge queue breaks
- The "opportunity to merge" — time from work completion to commit — becomes the critical bottleneck
- In traditional CI/CD, merge queues already cause friction: another colleague's code gets in first, forcing rebase
- At agent scale, thousands of short-lived branches make merge queues impossible without architectural change
- The solution is the [[PreMerge Queue]]: reconciles parallel changes before entering the merge queue
- Merge queue problems are what motivate the entire [[Continuous Compute]] paradigm

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[PreMerge Queue]] — the evolution of the merge queue for agent scale
- [[Git Ledger]] — the conceptual model explaining the merge queue bottleneck
- [[Serializability]] — the guarantee the merge queue must provide
- [[Continuous Compute]] — paradigm that replaces the traditional merge queue
- [[MergeabilityScoring]] — related concept for evaluating merge readiness
