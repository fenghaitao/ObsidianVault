---
title: "Quora"
type: entity
tags: [company, qa-platform, ai-adopter, batch-processing]
sources: ["raw/01-articles/claude/2024-10-08 - Introducing the Message Batches API.md"]
last_updated: 2026-07-04
---

## Definition

Quora is a user-based question-and-answer platform. It is also the parent of [[Poe]], its multi-model AI chat product.

## Key Information

- Uses Anthropic's [[MessageBatchesAPI|Batches API]] for summarization and highlight extraction to build new end-user features.
- Andy Edmonds, Product Manager at Quora: batching provides cost savings while reducing the complexity of running large numbers of non-real-time queries, freeing engineers to work on "more interesting problems" instead of managing parallel live-query infrastructure.

## Related

- [[MessageBatchesAPI]] — the API Quora uses for summarization and highlight extraction
- [[Poe]] — Quora's AI chat product, also integrating Claude
- [[Anthropic]] — API provider
- [[summary-2024-10-08 - Introducing the Message Batches API]] — source article
