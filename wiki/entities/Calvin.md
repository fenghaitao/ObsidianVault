---
title: "Calvin"
type: entity
tags: [person, openhands, engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
Calvin is an engineer at OpenHands who demonstrated the Refactor SDK by eliminating code smells from the OpenHands codebase using dependency graph-based batching and a verifier-fixer pipeline.

## Key Information
- Engineer at OpenHands
- Demonstrated the OpenHands Refactor SDK live, showing how to eliminate code smells from a ~380-file, ~60,000-line codebase
- Used dependency graph visualization to batch files, then applied verifier-fixer pipeline: verifier identifies code smells, fixer spins up agents to address them and opens PRs
- Processed batches in dependency order, starting from leaf nodes with no dependencies
- Each fixer produces a tidy pull request ready for human approval

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[OpenHands]] — company
- [[VerifierFixer Pipeline]] — demonstrated pattern
- [[Dependency Graph Refactoring]] — batching strategy used
- [[Batch Graph]] — visualization tool used
