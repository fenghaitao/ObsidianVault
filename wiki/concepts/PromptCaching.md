---
title: "Prompt Caching"
type: concept
tags: [claude, api, optimization, caching, cost-reduction, latency]
sources: [raw/01-articles/claude/2025-08-14 - Prompt caching with Claude.md, raw/01-articles/claude/2025-03-13 - Token-saving updates on the Anthropic API.md, raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md]
last_updated: 2026-06-28
---

# Prompt Caching

Prompt caching is an [[Anthropic]] API feature that allows developers to store and reuse frequently accessed context between API calls. This reduces both costs and latency for applications that process large documents, system instructions, or examples repeatedly.

## Definition

Prompt caching enables applications to cache portions of prompts (context, instructions, documents) across multiple API calls, eliminating the need to retransmit identical information with each request.

## Key Benefits

- **Cost reduction**: Up to 90% cost savings for long prompts by avoiding redundant token processing
- **Latency reduction**: Up to 85% latency reduction by eliminating re-reading of cached content
- **Efficiency**: Allows applications to maintain extensive context without performance penalties

## How It Works

Developers set cache breakpoints in their prompts. [[Claude3.7Sonnet]] automatically reads from the longest previously cached prefix, eliminating manual tracking of cached segments. The system identifies and uses the most relevant cached content automatically.

## Cache Durations

Developers can choose between two time-to-live (TTL) options:

- **Standard 5-minute TTL** — Default cache duration, most cost-effective for typical applications
- **Extended 1-hour TTL (beta)** — New option available as of May 2025, 12x improvement over standard, enables up to 90% cost reduction and 85% latency reduction for long-running agent workflows

The extended 1-hour option incurs additional costs but is particularly valuable for agents that maintain context over extended periods.

## Cache-Aware Rate Limits

As of March 2025, prompt cache read tokens no longer count against the Input Tokens Per Minute (ITPM) limit for [[Claude3.7Sonnet]] on the [[Anthropic]] API. This allows:
- Increased throughput within existing ITPM rate limits
- More efficient scaling for context-heavy applications
- Optimal usage of rate limit allocations

The Output Tokens Per Minute (OTPM) rate limit remains standard.

## Use Cases

Prompt caching is particularly powerful for:
- Large document processing and analysis
- System instruction reuse across multiple requests
- Few-shot learning and example-based prompting
- Long-running knowledge base applications
- Batch processing with consistent context
- **Long-context cost mitigation**: When using [[Claude4Sonnet]]'s 1M token [[ContextWindow]] (where tiered pricing applies over 200K tokens), prompt caching can offset cost increases on repeated large-context requests

## Availability

- [[Anthropic]] API: Generally available; initial public beta launched with [[Claude3.5Sonnet]], [[Claude3Opus]], and [[Claude3Haiku]]
- [[AmazonBedrock]]: Available in preview
- [[VertexAI]] (Google Cloud): Available in preview
- Cache-aware ITPM limits available for [[Claude3.7Sonnet]] only

## Pricing

- **Cache write**: 25% more than the base input token price for the given model
- **Cache read**: 10% of the base input token price (90% discount vs. base input tokens)

## Real-World Examples

[[Cognition]] (maker of [[Devin]]) leverages prompt caching to provide more context about codebases and achieve higher quality results while reducing cost and latency. With cache-aware ITPM limits, Cognition further optimizes throughput within existing rate limits.

[[Notion]] integrates prompt caching into [[Notion]]'s Claude-powered Notion AI features, enabling faster and cheaper AI responses while maintaining quality. Simon Last (Co-founder, Notion) noted the feature makes Notion AI "faster and cheaper, all while maintaining state-of-the-art quality."

## Related

- [[Claude3.7Sonnet]] — model with native prompt caching support
- [[Claude4Opus]] — supports extended 1-hour TTL caching
- [[Claude4Sonnet]] — supports extended 1-hour TTL caching
- [[Anthropic]] — API provider
- [[TokenOptimization]] — broader concept of reducing token consumption
- [[ToolUse]] — related capability for efficient API interactions
- [[CodeExecutionTool]] — works with extended caching for long-running analysis
- [[Cognition]] — enterprise customer using prompt caching
- [[summary-2025-03-13 - Token-saving updates on the Anthropic API]] — source article on standard 5-minute TTL
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — announcement of extended 1-hour TTL
- [[ContextWindow]] — 1M context window pairs with prompt caching to reduce large-context costs
- [[BatchProcessing]] — complementary API cost-reduction technique
- [[summary-2025-08-14 - Prompt caching with Claude]] — original launch announcement, pricing details, and Notion use case
- [[summary-2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context]] — mentions prompt caching as a cost mitigation for 1M context requests
