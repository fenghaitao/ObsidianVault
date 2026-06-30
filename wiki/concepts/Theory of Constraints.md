---
title: "Theory of Constraints"
type: concept
tags: [management, methodology, optimization, bottleneck, systems-thinking]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
The Theory of Constraints, from Eliyahu Goldratt's "The Goal" (1984), states that in any system there is always exactly one bottleneck (constraint). Optimizing anything other than that bottleneck is pointless and often counterproductive. Once the bottleneck is fixed, a new bottleneck emerges elsewhere, and the process repeats.

## Key Information
- From Eliyahu Goldratt's book "The Goal" (1984)
- Core principle: every system has exactly one bottleneck at any given time
- Fix the bottleneck first, then find where it moves, then fix the new bottleneck
- Chris Parsons applies this to AI adoption: some teams using AI go slower because they're not working on the constraint
- Example: if your release process ships once a month and AI produces 200 PRs instead of 20, the release process breaks — the constraint is the release process, not coding speed
- Example: if microservice dependencies are the bottleneck, fix the release coordination before optimizing coding
- Parsons recommends reading The Goal for understanding how to optimize AI-driven development
- Implication for Ralph loops: don't parallelize until the sequential bottleneck is addressed; the bottleneck is usually human review speed, not agent throughput

## Related
- [[EliyahuGoldratt]] — author
- [[ChrisParsons]] — applies to AI adoption
- [[Ralph Loop]] — workflow pattern informed by this theory
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
