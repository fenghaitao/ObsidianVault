---
title: "summary-2024-10-08 - Introducing the Message Batches API"
type: source
tags: [source, original-material, batch-processing, api, cost-optimization]
sources: ["raw/01-articles/claude/2024-10-08 - Introducing the Message Batches API.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic introduced the [[MessageBatchesAPI]], letting developers submit up to 10,000 queries per batch for asynchronous processing at 50% lower cost than standard API calls, with each batch completing in under 24 hours (often faster). Launched in public beta on the Anthropic API with support for Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku; batch inference was also available for Bedrock customers, with Vertex AI support announced as coming soon (and confirmed in preview by a December 17, 2024 update). [[Quora]] is cited as an early adopter, using the Batches API for summarization and highlight extraction.

## Key Points

- Up to **10,000 queries per batch**, processed in under 24 hours, at a **50% discount** on both input and output tokens versus standard API calls.
- Public beta on the Anthropic API at launch, supporting Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku.
- Available via [[AmazonBedrock|Bedrock batch inference]] for AWS customers; [[VertexAI|Google Cloud Vertex AI]] batch predictions support announced as "coming soon," later confirmed in preview (December 17, 2024 update).
- Eliminates the need to manage complex queuing systems or worry about rate limits for non-time-sensitive workloads.
- Makes large-scale data processing (e.g., analyzing entire corporate document repositories with millions of files) more economically viable.
- **[[Quora]]** case study: uses the Batches API for summarization and highlight extraction to power end-user features, per Andy Edmonds (Product Manager at Quora) — cost savings and reduced complexity versus running many parallel live queries.

## Related

- [[MessageBatchesAPI]] — the API this article introduces
- [[Quora]] — featured early-adopter case study
- [[BatchProcessing]] — the broader cost-optimization pattern this API implements
