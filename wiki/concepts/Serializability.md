---
title: "Serializability"
type: concept
tags: [distributed-systems, git, agents, concurrency, merge]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
Serializability, in the context of agentic software development, is the guarantee that parallel agent-generated changes can be ordered and merged into the Git ledger without conflicts, despite massive concurrency. It is the property that the [[Pre-merge Queue]] must provide to enable [[Continuous Compute]] at scale.

## Key Information
- Adapted from database theory by [[HugoSantos]] to describe the merge problem at agent scale
- Traditional CI/CD: few concurrent changes, serialization is manageable
- Agent scale: thousands of parallel changes on the same codebase — serialization becomes the bottleneck
- The "opportunity to merge" (time from completion to commit) is critical
- With humans: long lock time, low volume → manageable
- With agents: short lock time required, massive volume → fundamental architecture challenge
- The [[Pre-merge Queue]] is the mechanism that reconciles parallel changes for serializability
- Without serializability guarantees, parallel agent changes produce unmergeable code

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[Git Ledger]] — the serialized target requiring serializability
- [[Pre-merge Queue]] — the mechanism providing serializability
- [[Continuous Compute]] — paradigm requiring serializability at scale
- [[Merge Queue]] — traditional merge mechanism that breaks at agent scale
- [[MergeabilityScoring]] — related concept for evaluating serializability
- [[The Multiverse (agent development)]] — scenario requiring serializability across candidates
