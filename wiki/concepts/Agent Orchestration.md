---
title: "Agent Orchestration"
type: concept
tags: [agents, orchestration, parallelism, architecture, openhands]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
Agent orchestration is the practice of coordinating multiple AI coding agents working in parallel on decomposed sub-tasks of a larger software engineering problem, with human review at intermediate steps. It represents the bleeding edge of AI-assisted development, enabling massive productivity lifts on repeatable, automatable tasks that are too large for a single agent.

## Key Information
- Agent orchestration is the fourth stage in the evolution of AI coding: context-unaware snippets → context-aware code generation → autonomous coding agents → parallel agent orchestration.
- Tasks suited for orchestration are repeatable and automatable: CVE remediation, code modernization, dependency updates, framework migrations, documentation automation.
- One client achieved a 30x improvement in CVE resolution time using orchestrated OpenHands agents.
- The goal is ~90% automation with human review at intermediate steps, not 100% hands-off operation.
- Most developers will use single local agents; only ~1% of early adopters are experimenting with orchestration.
- Key challenges: limited context windows, agent laziness, lack of domain knowledge, compounding errors, and difficulty conveying human intuition.
- Effective orchestration requires decomposing tasks into independently verifiable, parallelizable units with clear dependencies.
- Cloud-based sandboxes (Docker/Kubernetes) are essential for running agents securely and scalably in orchestration scenarios.
- The workflow: decompose task → dispatch parallel agents → review intermediate outputs → collate results → merge.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Task Decomposition]] — prerequisite for orchestration
- [[Parallel Agents]] — agents running concurrently
- [[Sub-agent Orchestration]] — related architecture pattern
- [[Context Sharing Between Agents]] — coordination mechanism
- [[Human-in-the-Loop Orchestration]] — review pattern
- [[Cloud-Based Agent Sandboxes]] — infrastructure for orchestration
- [[CVE Remediation at Scale]] — example use case
