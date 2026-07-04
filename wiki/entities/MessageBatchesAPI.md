---
title: "Message Batches API"
type: entity
tags: [anthropic, api, batch-processing, cost-optimization]
sources: ["raw/01-articles/claude/2024-10-08 - Introducing the Message Batches API.md"]
last_updated: 2026-07-04
---

## Definition

The Message Batches API is an Anthropic API endpoint that processes large volumes of queries asynchronously, letting developers submit up to 10,000 queries per batch at a 50% discount versus standard real-time API calls.

## Key Information

- **Capacity**: up to 10,000 queries per batch.
- **Turnaround**: each batch processed in under 24 hours, often much faster.
- **Pricing**: 50% discount on both input and output tokens compared to standard API calls.
- **Launch**: public beta on the Anthropic API (October 8, 2024), supporting Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku.
- **Platform availability**: [[AmazonBedrock|Bedrock batch inference]] available for AWS customers at launch; [[VertexAI|Google Cloud Vertex AI]] batch predictions announced as coming soon, later confirmed in preview (per a December 17, 2024 update to the announcement).
- Removes the need to manage queuing systems or rate limits for non-time-sensitive workloads; makes large-scale processing (e.g., analyzing millions of documents) more economically viable.
- **Adopter**: [[Quora]] uses it for summarization and highlight extraction to power end-user features.

## Related

- [[Anthropic]] — API provider
- [[BatchProcessing]] — the general cost-optimization pattern this API implements
- [[TokenOptimization]] — broader cost-reduction strategy category
- [[AmazonBedrock]] — platform offering equivalent batch inference
- [[VertexAI]] — platform with batch predictions in preview
- [[Quora]] — early adopter case study
- [[MessagesAPI]] — the core synchronous API this batches endpoint complements
- [[summary-2024-10-08 - Introducing the Message Batches API]] — source announcement
