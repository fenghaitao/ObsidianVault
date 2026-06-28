---
title: "Token-saving updates on the Anthropic API"
type: source
tags: [anthropic, api, optimization, token-efficiency, cost-reduction, prompt-caching, tool-use]
sources: [raw/01-articles/claude/2025-03-13 - Token-saving updates on the Anthropic API.md]
last_updated: 2026-06-28
---

# Summary: Token-saving updates on the Anthropic API

This article announces three major token optimization features for [[Claude3.7Sonnet]] on the [[Anthropic]] API, enabling developers to reduce costs and increase throughput within existing rate limits.

## Key Updates

### 1. Cache-Aware Rate Limits for Prompt Caching

[[PromptCaching]] read tokens no longer count against Input Tokens Per Minute (ITPM) limits for [[Claude3.7Sonnet]]. This enables:
- Higher throughput within existing ITPM rate limits
- More efficient scaling for context-heavy applications
- Optimal rate limit utilization

**Impact**: Up to 90% cost savings for long prompts by reducing redundant token transmission.

**Simplified Prompt Caching**: Developers no longer manually track cached segments. [[Claude3.7Sonnet]] automatically identifies and uses the longest previously cached prefix, reducing developer workload and freeing up more tokens.

### 2. Token-Efficient Tool Use

[[Claude3.7Sonnet]] now supports token-efficient tool invocations available via beta header `token-efficient-tools-2025-02-19`.

**Impact**: Reduces output token consumption by up to 70% (average 14% reduction in early deployments).

**Use Cases**: Particularly effective for:
- Structured data extraction from unstructured text
- API automation and integration tasks
- Multi-step workflows with tool interactions

**Availability**: Beta feature on [[Anthropic]] API, Amazon Bedrock, and Google Cloud Vertex AI.

### 3. Text Editor Tool

A new specialized `text_editor` tool enables targeted edits to specific text portions within documents, source code, or research reports.

**Benefits**:
- Reduces token consumption compared to full document regeneration
- Reduces latency
- Improves accuracy for document collaboration scenarios

**Availability**: [[Anthropic]] API, Amazon Bedrock, and Google Cloud Vertex AI.

## Enterprise Adoption

[[Cognition]] (maker of [[Devin]], the AI software engineer) is an early adopter:
- Uses [[PromptCaching]] to provide more context about codebases
- Achieves higher quality results with reduced costs and latency
- Uses cache-aware ITPM limits to optimize throughput within existing rate allocations

**Scott Wu, CEO of Cognition**: "Prompt caching allows us to provide more context about the codebase to get higher quality results while reducing cost and latency. With cache-aware ITPM limits, we are further optimizing our prompt caching usage to increase our throughput and get more out of our existing rate limits."

## Implementation

All features integrate with existing API patterns and require minimal code changes:
- Prompt caching uses standard cache breakpoint syntax
- Token-efficient tool use requires single beta header addition
- Text editor tool provided like any standard tool definition

## Strategic Impact

These updates demonstrate [[Anthropic]]'s focus on:
- **Developer efficiency**: Minimal code changes required for significant cost savings
- **Throughput optimization**: Process more requests within existing rate limits
- **Practical cost reduction**: Multi-faceted approach (caching + tool optimization + rate limit changes)
- **Enterprise adoption**: Enabling power users like [[Cognition]] to scale effectively

## Related

- [[Claude3.7Sonnet]] — model with token optimization features
- [[PromptCaching]] — cost-reduction feature through context reuse
- [[TokenOptimization]] — broader concept of reducing token consumption
- [[ToolUse]] — tool use capability with token-efficient variants
- [[Anthropic]] — API provider
- [[Cognition]] — enterprise customer adopting these features
- [[Devin]] — AI software engineer using these optimizations
- [[AnthropicConsole]] — developer interface for working with these features
