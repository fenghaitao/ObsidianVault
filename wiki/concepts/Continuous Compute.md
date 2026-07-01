---
title: "Continuous Compute"
type: concept
tags: [infrastructure, CI-CD, agents, paradigm-shift, stateful-compute]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
Continuous Compute is the proposed successor to traditional CI/CD for agentic software development. It replaces batch-oriented PR-based pipelines with a stateful, high-speed inner loop where code generation, internal validation (build/test), and external validation (by specialized review agents) happen continuously. CI principles (validation, invariants, governance) shift into the agent harness rather than remaining as separate phases.

## Key Information
- Proposed by [[HugoSantos]] and [[MadisonFaulkner]] as the paradigm that will eclipse CI/CD
- Addresses the fundamental mismatch: CI/CD was designed for human-scale (1-2 PRs/week) but agents produce thousands of concurrent changes
- Core components:
  - **Ingress shaping and rate limiting** for agent intake
  - **Caching as the orchestration layer** via hardware-software co-design
  - **Agentic identity** for software, enabling retries at scale
  - **Stateful environments** with memory and warm caches for speed
- No PRs: work starts with intent and plan, flows through a continuous agent harness loop
- Validation is continuous: every iteration includes build, test, and external agent review
- Changes flow through a pre-merge queue for serialization into the Git ledger
- Humans approve intent and results, not individual code diffs
- CI does not go away — its principles (compiling from well-known source, no regressions, allowed changes) are enforced continuously within the harness

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[PreMerge Queue]] — serialization mechanism for Continuous Compute
- [[AgentHarness]] — the loop that executes Continuous Compute
- [[Stateful Development Environment]] — prerequisite for Continuous Compute speed
- [[Internal Validation]] — validation within the Continuous Compute loop
- [[External Validation]] — agent review within the Continuous Compute loop
- [[Git Ledger]] — the serialized commit target
- [[Merge Queue]] — the bottleneck Continuous Compute addresses
- [[HugoSantos]] — proposer of the paradigm
- [[Namespace]] — company building Continuous Compute infrastructure
