---
title: "MergeabilityScoring"
type: concept
tags: [evaluation, code-quality, benchmark, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR.md"]
last_updated: 2026-06-25
---

## Definition
Mergeability Scoring is a holistic evaluation approach for AI-generated code that goes beyond unit test pass/fail to consider whether the code is maintainable, matches quality standards, and would be accepted by human reviewers in a real codebase.

## Key Information
- Contrasted with "algorithmic costless scoring at the margin" used by benchmarks like SWE-bench
- SWE-bench scores do not account for whether code is "spelunkable" by other people in the future or matches quality considerations not captured by unit tests
- AI may be performant according to SWE-bench-like scoring but not according to mergeability scoring
- This gap is one hypothesis for why benchmark results don't translate to real-world productivity gains
- Represents the difference between "does it pass tests" and "would a team actually merge this"

## Related
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — source
- [[SWE-bench]] — benchmark with unit-test-based scoring
- [[AIReliability]] — related concept: mergeability requires higher reliability
- [[CodeSlop]] — code that might pass tests but fails mergeability criteria
