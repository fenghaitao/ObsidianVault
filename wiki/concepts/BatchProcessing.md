---
title: "BatchProcessing"
type: concept
tags: [api, cost-reduction, throughput, async, anthropic]
sources: ["raw/01-articles/claude/2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md"]
last_updated: 2026-06-28
---

## Definition

Batch processing is an [[Anthropic]] API capability that allows developers to submit large volumes of requests for asynchronous processing, offering significant cost savings compared to real-time API calls.

## Key Information

- Provides an additional **50% cost reduction** on top of standard API pricing.
- Particularly valuable for large-scale, non-time-sensitive workloads.
- Can be combined with the 1M token [[ContextWindow]] on [[Claude4Sonnet]] for maximum cost efficiency on large-context jobs.
- Use cases: bulk document processing, offline analysis pipelines, dataset generation.

## Related

- [[Claude4Sonnet]] — model that supports batch processing with 1M context
- [[ContextWindow]] — 1M context window is compatible with batch processing
- [[PromptCaching]] — complementary cost-reduction technique for repeated context
- [[TokenOptimization]] — broader concept of reducing token consumption and cost
- [[Anthropic]] — API provider
- [[summary-2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context]] — source article mentioning batch processing
