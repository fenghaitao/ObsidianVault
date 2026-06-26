---
title: "Verifier-Fixer Pipeline"
type: concept
tags: [agents, refactoring, pipeline, verification, openhands]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
The verifier-fixer pipeline is a two-step agent orchestration pattern where a verifier identifies problems in a code batch and a fixer spins up an agent to address those problems, producing a pull request ready for human approval. It is the core mechanism of the OpenHands Refactor SDK.

## Key Information
- Verifier: identifies what's wrong in a code batch. Can be programmatic (runs a lint command, unit tests) or LLM-based (analyzes code against a set of rules).
- Fixer: addresses the issues found by the verifier. Can be programmatic (runs a batch command), single-shot LLM, or a full OpenHands agent with access to tools.
- The most powerful fixer uses the OpenHands Agent SDK to spin up an agent with terminal, file editor, and other tools.
- Each fixer produces a tidy pull request with a summary of code smells identified, changes made, and notes for future work.
- Batches are processed in dependency order: leaf nodes first, then batches whose dependencies are already completed.
- The pipeline repeats until the entire batch graph turns green (all batches verified clean).
- Human review happens at the PR level: each fixer's output is reviewed and merged before unblocking dependent batches.
- The batching strategy and narrow instructions ensure PRs are tightly focused, typically modifying only a couple hundred lines.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Dependency Graph Refactoring]] — batching strategy
- [[Batch Graph]] — visualization of pipeline progress
- [[Agent Orchestration]] — broader practice
- [[OpenHands]] — platform implementing this pipeline
- [[Calvin]] — engineer who demonstrated the pipeline
