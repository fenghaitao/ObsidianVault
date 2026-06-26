---
title: "Product-Driven Benchmarks"
type: concept
tags: [evaluation, benchmarks, product-development, ai-engineering, retrieval]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - How Codeium Breaks Through the Ceiling for Retrieval： Kevin Hou.md"]
last_updated: 2026-06-26
---

## Definition
Product-driven benchmarks (also called product-led eval) are evaluation datasets and metrics constructed from real user behavior and production data, rather than academic or synthetic benchmarks, to measure AI system quality against actual end-user experience. Codeium builds these by extracting commit messages from real pull requests and mapping them to the files modified in those commits.

## Key Information
- **Construction Method**: Parse PRs into commits, extract commit messages (English descriptions of changes), and match them to the list of modified files — creating a mapping from natural language queries to sets of relevant code files
- **Purpose**: Get as close as possible to the end-user distribution; measures what retrieval tweaks actually mean for the product experience
- **Contrast with Academic Benchmarks**: Standard benchmarks like MTEB focus on single-document relevance and don't capture the multi-document, real-world retrieval patterns of a code generation product
- **Scale**: Enables running eval at production scale, not just on curated academic datasets
- **Iteration Loop**: Product-driven data → eval system → model/infrastructure improvements → ship to users → measure production signals (thumbs up/down, acceptance rates) → refine eval datasets
- **Codeium's Finding**: Publicly available embedding models showed reduced performance on their product-driven benchmarks, unable to reason over the specific relationship between English commit messages and code files
- **Principle**: Start with the end problem (what users are asking for), build datasets and eval systems locally to iterate on metrics that matter

## Related
- [[summary-20240731 - How Codeium Breaks Through the Ceiling for Retrieval： Kevin Hou]] — source
- [[Recall@50]] — the specific metric used in product-driven eval
- [[BenchmarkSaturation]] — why new benchmarks are needed
- [[OfflineEvals]] — category of evaluation
- [[OnlineEvals]] — production-side evaluation companion
- [[EvalEngineering]] — broader discipline
