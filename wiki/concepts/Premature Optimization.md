---
title: "Premature Optimization"
type: concept
tags: [concept, performance, engineering]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md"]
last_updated: 2026-09-22
---
## Definition
Premature optimization is optimizing before measurement shows it is needed — famously warned against by Donald Knuth.

## Key Information
- Knuth: don't do premature optimization; but he also pointed to optimizing the ~2–3% of code that matters — "exactly the number" Bjarne uses.
- Bjarne's method: build with high-level facilities, check if it's fast enough, time (don't guess), find where the time is spent, then optimize only that.
- In a paper with a Spanish fluid-dynamics collaborator, removing "clever" 1990s optimizations and reducing code to ~80% yielded a 20% improvement — proof the technique works.
- Clever manual optimizations age poorly: code "cleverly and correctly optimized in the 1990s" is often pessimized today as architectures and compilers improve.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[Donald Knuth]] — coined the warning
- [[Zero Overhead Abstraction]] — the alternative approach
- [[C++]] — the context of his advice
