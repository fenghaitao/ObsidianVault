---
title: "PromptCaching"
type: concept
tags: [concept, llm, cost-optimization, anthropic, openai, caching]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide).md"
last_updated: 2026-06-20
---

## Definition

Prompt caching is an LLM provider feature that reduces the cost of repeated prompt prefixes. When the same tokens appear at the start of many requests, the provider caches them after the first request and charges a reduced rate for the cached portion on subsequent ones. [[ColeMedin]] highlights it as the technique that makes [[ContextualRetrieval]] economically viable at scale.

## Key Information

### Why it matters

Several patterns repeat a large block of context across many requests:
- **[[ContextualRetrieval]]** — each chunk's context-generation prompt includes the *entire document*. For a 100-chunk doc, that's the document sent 100 times.
- **Agentic loops** — the system prompt + tool definitions + conversation history repeat every turn.
- **Batch processing** — a shared instruction prefix across many items.

Without caching, you pay full price for the repeated prefix every time. With caching, the repeated part is much cheaper after the first request.

### Provider-specific behavior (per Cole)

| Provider | Cached-token discount | Activation |
|---|---|---|
| **[[OpenAI]]** | ~50% cheaper | Automatic, on by default |
| **[[Anthropic]]** | ~90% cheaper | Toggle in the API request |
| **Gemini** | ~90% cheaper | Toggle in the API request |

So you pay more for the *first* request (which populates the cache) and substantially less for every subsequent request that reuses the prefix.

### The cost model

```
Without caching:  N requests × full_prefix_cost
With caching:     1 × full_prefix_cost  +  (N-1) × discounted_prefix_cost
```

For contextual retrieval over a large corpus, this is the difference between "too expensive to bother" and "cheap enough to run on everything." Combined with using a small/cheap model for the context-generation step (GPT-4o-mini class), the per-document cost becomes negligible.

### Prefix-matching requirement

Caching keys on the *prefix* — the repeated content must be at the *start* of the prompt and byte-identical across requests. Put the stable, repeated content first (the document, the system prompt, the tool definitions) and the varying content (the specific chunk, the user's question) last. This ordering is what lets the provider recognize and reuse the cached prefix.

### Where it appears in this corpus

Cole's primary citation is in the [[ContextualRetrieval]] walkthrough (`summary-easiest-strategy-for-accurate-rag`) — the technique would be cost-prohibitive without prompt caching, and Cole explicitly walks through the economics. It's also implicitly relevant to any [[AgentHarness]] running many sessions with shared context.

## Related

- [[ContextualRetrieval]] — the technique prompt caching makes economical
- [[RetrievalAugmentedGeneration]] — broader context
- [[Anthropic]], [[OpenAI]] — providers with the feature
- [[ColeMedin]] — articulator in this corpus
- [[summary-easiest-strategy-for-accurate-rag]] — primary source
