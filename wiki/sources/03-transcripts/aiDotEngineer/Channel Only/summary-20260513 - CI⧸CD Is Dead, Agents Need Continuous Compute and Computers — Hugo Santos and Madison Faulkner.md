---
title: "CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner"
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"
date: 2026-05-13
author: "Hugo Santos, Madison Faulkner"
organization: "Namespace, NEA"
type: transcript
---

# CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner

## Core Thesis

Traditional CI/CD is fundamentally broken for agentic software development at scale. Agents produce thousands of PRs across many short-lived branches, causing merge conflicts and overwhelming human reviewers. The future is **Continuous Compute** — a stateful, high-speed inner loop where code generation, internal validation (build/test), and external validation (by specialized review agents) happen continuously without human PRs. Changes flow through a pre-merge queue for serialization before human approval of intent and results (not code diffs). CI principles (validation, invariants, governance) shift into the agent harness rather than being separate phases.

## Key Takeaways

1. **CI/CD was designed for human scale**: 1-2 PRs per week, human reviewers, delayed feedback loops. The human developer was the "agent" in the loop, with stop conditions and multiple review cycles.
2. **Agent scale breaks CI/CD**: Thousands of short-lived branches, cache thrashing, and merge conflicts make traditional PR-based workflows impossible. GitHub activity shows unprecedented spikes in commits and code volume.
3. **The new architecture has no PRs**: Work starts with intent and plan (codified in Linear tickets, Slack, specs). An agent harness checks out a well-known commit, builds, tests, and iterates continuously.
4. **Internal validation moves into the loop**: Build and test are no longer separate CI phases — they run on every iteration within the agent harness.
5. **External validation by specialized agents**: Security-focused LLMs, API conformance LLMs, and other review agents replace human code reviewers, providing feedback within the loop.
6. **Statefulness is critical**: Agents need memory, warm caches, and incremental workflows. Starting from scratch on every iteration delays the entire loop.
7. **Pre-merge queue for serializability**: Parallel agent changes are reconciled in a pre-merge queue before entering the Git ledger, guaranteeing serializability despite massive concurrency.
8. **Human role shifts to intent approval**: Humans approve intent and results at the pre-merge queue, looking at feature videos or security reports, not individual code diffs. Changes may be semantically grouped across multiple agents.
9. **The Multiverse**: Agents may work on multiple commit candidates simultaneously to address the same plan, massively increasing resource usage but enabling faster convergence.
10. **CI principles don't disappear — they shift**: Validation invariants (compiling from well-known source, no regressions, allowed changes) are enforced continuously within the harness, not as separate phases.
11. **Hardware-software co-design is the orchestration layer**: Caching becomes the orchestration layer, with ingress shaping, rate limiting, and agentic identity as key infrastructure components.
12. **Mitchell Hashimoto's vision for GitHub**: Shut down Copilot and evolve GitHub to serve AI and agentic users first, with inference at scale and friendly code storage solutions.

## Entities

- [[HugoSantos]] — CEO of Namespace, former microservices lead at Google
- [[MadisonFaulkner]] — Partner at NEA, former Meta AI researcher
- [[Namespace]] — company building high-performance compute infrastructure to eclipse CI/CD
- [[NEA]] — venture capital firm investing in technology
- [[Fall]] — company working with Namespace on next-gen development workflows
- [[Zed]] — company working with Namespace on next-gen development workflows
- [[Ramp]] — company working with Namespace on next-gen development workflows
- [[MitchellHashimoto]] — founder of HashiCorp, referenced for his vision on fixing GitHub
- [[Google]] — where Hugo Santos led microservices
- [[Meta]] — where Madison Faulkner was an AI researcher
- [[GitHub]] — central platform in the CI/CD discussion
- [[HashiCorp]] — founded by Mitchell Hashimoto

## Concepts

- [[Continuous Compute]] — proposed replacement for CI/CD: stateful, high-speed agent development loops
- [[Pre-merge Queue]] — queue of agent-completed changes awaiting serialization and human approval
- [[Internal Validation]] — build and test that runs on every iteration within the agent harness
- [[External Validation]] — specialized review agents evaluating changes within the development loop
- [[Intent and Plan]] — codified goals (specs, tickets) replacing PRs as the unit of work
- [[Git Ledger]] — conceptual model of Git repository as serialized commit ledger requiring serializability
- [[Stateful Development Environment]] — agents need memory, warm caches, and incremental state for speed
- [[Serializability]] — ensuring parallel agent changes merge correctly into the Git ledger
- [[Microservices with Agents]] — evolution from monolithic agents to specialized agent microservices
- [[Agentic Identity for Software]] — identity management for agents in the software development lifecycle
- [[Hardware-Software Co-design for Caching]] — caching as the orchestration layer for accelerated CI/CD
- [[The Multiverse (agent development)]] — agents working on multiple commit candidates simultaneously
- [[Merge Queue]] — the serialization bottleneck where parallel agent changes must be ordered

## Related

- [[AgentHarness]] — the loop that manages agent development (Claude Code, Cursor, Factory, Amp)
- [[AgentIdentity]] — identity for agents, extended here to software development
- [[Plan and Review Shift]] — the shift from code review to plan/review
- [[SpecificationDrivenDevelopment]] — related to intent and plan as work unit
- [[MergeabilityScoring]] — related to pre-merge queue reconciliation
- [[Verification in Agentic Loops]] — related to internal validation as continuous process
- [[Reviewer Agents]] — related to external validation by specialized agents
- [[AgentMemory]] — related to statefulness in development environments
- [[AgenticEngineering]] — the broader paradigm this talk addresses
