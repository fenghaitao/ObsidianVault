---
title: "Pre-merge Queue"
type: concept
tags: [CI-CD, agents, merge, serialization, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
A Pre-merge Queue is a queue of agent-completed changes that have passed all validation but have not yet been merged into the main repository. It reconciles parallel agent changes to guarantee serializability before committing to the Git ledger, and is the point where humans approve intent and results rather than individual code diffs.

## Key Information
- Proposed by [[HugoSantos]] as a critical architectural component of [[Continuous Compute]]
- Sits between the agent harness loop and the [[Git Ledger]]
- Purpose: reconcile parallel agent changes operating on the same parts of the codebase
- Guarantees serializability despite massive concurrent agent activity
- Changes may be semantically grouped across multiple agents before human review
- Human approval happens at this stage: reviewing intent and results (feature videos, security reports) rather than code
- Analogous to high-performance database serialization problems
- The "opportunity to merge" — the time from work completion to commit — must be minimized
- Distinct from traditional merge queues, which handle far lower volumes

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[Continuous Compute]] — paradigm this queue enables
- [[Git Ledger]] — the target for serialized commits
- [[Serializability]] — the guarantee the pre-merge queue provides
- [[Merge Queue]] — the traditional, lower-volume predecessor
- [[MergeabilityScoring]] — related concept for evaluating merge readiness
- [[The Multiverse (agent development)]] — agents working on multiple candidates that feed into the pre-merge queue
