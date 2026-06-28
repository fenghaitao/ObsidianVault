---
title: "Token Optimization"
type: concept
tags: [claude, api, cost, efficiency, optimization, throughput]
sources: [raw/01-articles/claude/2025-03-13 - Token-saving updates on the Anthropic API.md]
last_updated: 2026-06-28
---

# Token Optimization

Token optimization refers to techniques and features that reduce token consumption in [[Anthropic]] API usage, lowering costs while maintaining or improving output quality. It encompasses multiple strategies for efficient API utilization.

## Definition

Token optimization is the practice of minimizing the number of tokens consumed in API requests and responses while maintaining or improving the quality of results. This reduces operational costs and increases throughput within rate limits.

## Key Token Optimization Strategies

### 1. Prompt Caching
[[PromptCaching]] stores frequently used context, reducing redundant token processing across multiple requests. Demonstrates up to 90% cost reduction for long-prompt scenarios.

### 2. Token-Efficient Tool Use
[[Claude3.7Sonnet]] supports token-efficient tool use, reducing output token consumption by up to 70% (average 14% reduction in early deployments). This is particularly effective for structured data extraction and API automation tasks.

### 3. Text Editor Tool
A specialized tool for document collaboration that allows [[Claude3.7Sonnet]] to make targeted edits to specific text portions instead of reproducing entire documents. Reduces both token consumption and latency while improving accuracy.

### 4. Cache-Aware Rate Limits
Prompt cache read tokens are excluded from Input Tokens Per Minute (ITPM) limits for [[Claude3.7Sonnet]], allowing higher throughput without proportional rate limit increases.

## Availability

As of March 2025, token optimization features are available on:
- [[Anthropic]] API
- Amazon Bedrock
- Google Cloud Vertex AI

## Business Impact

Token optimization enables:
- **Cost reduction**: Significant per-request savings through multiple complementary techniques
- **Throughput scaling**: Process more requests within existing rate limits
- **Quality improvement**: Specialized tools improve accuracy for specific tasks
- **Minimal code changes**: Features integrate with existing API patterns

## Real-World Impact

[[Cognition]] (maker of [[Devin]]) uses token optimization to:
- Provide more context about codebases with reduced costs
- Increase throughput within existing rate allocations
- Maintain or improve result quality

Early adopters have achieved 14% average output token reduction through token-efficient tool use alone.

## Related

- [[Claude3.7Sonnet]] — model with token optimization features
- [[PromptCaching]] — context reuse for cost savings
- [[ToolUse]] — tool use capability with token-efficient variants
- [[Anthropic]] — provider of token optimization features
- [[Cognition]] — enterprise customer leveraging token optimization
- [[summary-2025-03-13 - Token-saving updates on the Anthropic API]] — source article
