---
title: "Batch Graph"
type: concept
tags: [refactoring, visualization, graph-theory, agents, openhands]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
A batch graph is a simplified dependency graph where nodes represent batches of files (rather than individual files) and edges represent inherited dependencies between those batches. It provides a high-level visualization of refactoring progress in the OpenHands Refactor SDK.

## Key Information
- Constructed from a file-level dependency graph by grouping files into batches and inheriting dependencies.
- Much simpler than the raw file dependency graph — the entire structure fits on a single screen.
- Color-coded status indicators: green for completed/verified batches, red for batches with verification failures.
- Enables identifying batches with no dependencies (leaf nodes) that can be processed first.
- Code complexity measures per batch help humans identify which batches need more careful review.
- The goal of the verifier-fixer pipeline is to turn every node in the batch graph green.
- When a batch is blocked (its dependencies aren't all green), the human can continue verifying other unblocked batches.
- Serves as a human-AI collaboration tool: humans can add notes, move files between batches, or adjust the strategy based on what the graph reveals.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Dependency Graph Refactoring]] — underlying strategy
- [[Verifier-Fixer Pipeline]] — pipeline using the batch graph
- [[OpenHands]] — platform implementing this visualization
- [[Calvin]] — engineer who demonstrated the batch graph
