---
title: "summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands"
type: source
tags: [source, transcript, aiDotEngineer, agent-orchestration, refactoring, openhands, parallel-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Core Summary
Robert Brennan, co-founder and CEO of OpenHands, presents how parallel agent orchestration can automate large-scale refactors such as CVE remediation, code modernization, and framework migrations. He traces the evolution from context-unaware code snippets through autonomous coding agents to the current bleeding edge of agent orchestration, where multiple agents work in parallel on decomposed tasks. While most developers will use single agents locally, early adopters are using orchestrated parallel agents to achieve 30x productivity lifts on specific repeatable tasks, with key challenges being task decomposition, context sharing between agents, and maintaining human-in-the-loop review at intermediate steps.

## Key Points
- Agent orchestration enables automating tasks too large for a single agent by decomposing them into parallel, independently verifiable sub-tasks.
- One client achieved a 30x improvement in CVE resolution time by using OpenHands to scan repos and open PRs for each vulnerability.
- Effective task decomposition mirrors how you would break down work for an engineering team: separable tasks, clear dependencies, easy verification.
- The OpenHands Refactor SDK uses a verifier-fixer pipeline: the verifier identifies code smells, the fixer spins up an agent to address them and opens a PR.
- Dependency graph-based batching groups semantically related files and orders work from leaf nodes upward, ensuring dependencies are resolved first.
- Scaffolding patterns allow old and new systems to coexist during migration, enabling incremental validation as each component is migrated.
- Context sharing strategies range from manual human intervention to agent-to-agent messaging, with human review recommended to prevent agents from learning unimportant things.
- Cloud-based agent sandboxes (Docker containers) provide security and scalability, allowing hundreds or thousands of agents to run concurrently.
- The goal is ~90% automation with human review at intermediate steps, not 100% hands-off operation.

## Related
- [[RobertBrennan]] — Speaker, co-founder and CEO of OpenHands
- [[OpenHands]] — MIT-licensed coding agent and orchestration platform
- [[Agent Orchestration]] — Coordinating multiple agents for large-scale tasks
- [[Task Decomposition]] — Breaking large problems into agent-solvable sub-tasks
- [[Context Sharing Between Agents]] — Strategies for sharing learned information
- [[Dependency Graph Refactoring]] — Using dependency graphs to batch and order refactoring
- [[Verifier-Fixer Pipeline]] — Two-step pipeline for identifying and fixing code issues
- [[Scaffolding Pattern]] — Temporary code enabling old and new systems to coexist
- [[Batch Graph]] — Graph where nodes are file batches and edges are dependencies
- [[CVE Remediation at Scale]] — Parallel agents scanning and fixing vulnerabilities
- [[Cloud-Based Agent Sandboxes]] — Containerized cloud environments for agent execution
- [[Human-in-the-Loop Orchestration]] — Human review at intermediate orchestration steps
- [[Parallel Agents]] — Running multiple agents concurrently
- [[Sub-agent Orchestration]] — Pattern for agent architecture
- [[Context Management]] — Techniques for managing agent context
