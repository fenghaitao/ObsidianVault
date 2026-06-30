---
title: "Git Ledger"
type: concept
tags: [git, version-control, serialization, agents, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
The Git Ledger is a conceptual model of a Git repository as a serialized commit ledger — a single, ordered sequence of changes where every commit must be serialized. Under agentic development at scale, this resembles high-performance database problems where serialization and locking become critical bottlenecks.

## Key Information
- Proposed by [[HugoSantos]] as a way to understand Git repositories at agent scale
- Every change must go into a single ledger with guaranteed ordering
- Analogous to database serialization: you must lock the database to commit, and lock time matters
- With humans: lock time is large but change volume is low — manageable
- With agents: lock time must be short but change volume is massive — the "opportunity to merge" becomes the critical bottleneck
- The [[Pre-merge Queue]] reconciles parallel changes before they enter the ledger
- Serializability guarantees that all changes can be ordered correctly despite concurrent agent activity
- The rate of change increases dramatically as code generation accelerates, making serialization the bottleneck

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[Continuous Compute]] — paradigm that addresses the ledger bottleneck
- [[Pre-merge Queue]] — mechanism for serializing into the ledger
- [[Serializability]] — the guarantee required for the ledger
- [[Merge Queue]] — the traditional bottleneck the ledger model explains
- [[The Multiverse (agent development)]] — agents operating on multiple ledger candidates
