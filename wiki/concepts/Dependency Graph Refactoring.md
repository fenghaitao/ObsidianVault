---
title: "Dependency Graph Refactoring"
type: concept
tags: [refactoring, agents, graph-theory, batching, openhands]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
Dependency graph refactoring is a strategy for large-scale code modernization that uses a file dependency graph to batch related files and order work from leaf nodes upward, ensuring that dependencies are resolved before dependent code is modified.

## Key Information
- Each node in the dependency graph represents a file; edges represent imports/dependencies between files.
- Files are batched into PR-sized chunks that an agent can handle and a human can understand.
- Batching strategies include graph-theoretic algorithms (strong guarantees about edge structure) and directory-based grouping (semantically related files in the same batch).
- A batch graph is then constructed where nodes are batches and edges are inherited dependencies.
- Work proceeds from leaf nodes (no dependencies) upward to the entry point of the application.
- This approach ensures that when an agent works on a batch, all its dependencies have already been resolved.
- Code complexity measures per batch help humans identify which batches need more careful review.
- Used in the OpenHands Refactor SDK for eliminating code smells, adding type annotations, and improving test coverage.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Batch Graph]] — visualization of batched dependencies
- [[VerifierFixer Pipeline]] — pipeline using dependency graph ordering
- [[Task Decomposition]] — related decomposition strategy
- [[Agent Orchestration]] — broader practice
- [[OpenHands]] — platform implementing this strategy
