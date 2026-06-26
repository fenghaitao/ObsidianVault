---
title: "OpenHands"
type: entity
tags: [tool, ai-coding, agent-orchestration, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
OpenHands is an MIT-licensed autonomous coding agent and orchestration platform that enables developers to automate large-scale software engineering tasks using parallel agents, cloud-based sandboxes, and an SDK for building custom refactoring pipelines.

## Key Information
- MIT-licensed, community-driven coding agent
- Originally started as OpenDevin in early 2024, rebranded to OpenHands
- Provides both a local CLI (similar to Claude Code) and cloud-based agent sandboxes
- The OpenHands Agent SDK powers the Refactor SDK, which enables verifier-fixer pipelines for large-scale code modernization
- Supports running agents in Docker containers for security and scalability, with Kubernetes for massive parallel deployments
- Used by clients for CVE remediation (30x improvement), framework migrations (Redux to Zustand), Spark 2 to Spark 3 migrations, and automated error handling
- The Refactor SDK uses dependency graph-based batching, verifier-fixer pipelines, and batch graphs to orchestrate parallel refactoring
- App available at app.allhands.dev with $10 free LLM credits

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[RobertBrennan]] — co-founder and CEO
- [[OpenDevin]] — original name of OpenHands
- [[Agent Orchestration]] — core capability
- [[Verifier-Fixer Pipeline]] — key SDK pattern
- [[Dependency Graph Refactoring]] — batching strategy
- [[CVE Remediation at Scale]] — use case
