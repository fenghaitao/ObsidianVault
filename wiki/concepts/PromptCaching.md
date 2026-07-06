---
title: "Prompt Caching"
type: concept
tags: [claude, api, optimization, caching, cost-reduction, latency]
sources: [raw/01-articles/claude/2025-08-14 - Prompt caching with Claude.md, raw/01-articles/claude/2025-03-13 - Token-saving updates on the Anthropic API.md, raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md, "raw/01-articles/claude/2026-04-30 - Lessons from building Claude Code Prompt caching is everything.md"]
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

## Engineering Lessons from Claude Code (April 2026)

Thariq Shihipar (Claude Code team) shared unintuitive lessons from optimizing prompt caching at production scale in [[ClaudeCode]]'s harness, treated as foundational enough that Anthropic alerts on cache hit rate and declares SEVs when it drops too low:

- **Static-first, dynamic-last ordering**: caching works by exact prefix matching up to each `cache_control` breakpoint, so requests should put static content first and dynamic content last to maximize shared-prefix hits across sessions. Named causes of accidental breaks: an in-depth timestamp embedded in the static system prompt, non-deterministic tool-definition ordering, and mid-conversation tool-parameter changes.
- **Prefer messages over prompt edits for stale info**: rather than editing the system prompt when data goes stale (which forces a cache miss), pass updated information via a `<system-reminder>` tag in the next user message or tool result, preserving the cache.
- **Caches are model-specific**: switching models mid-conversation (e.g., Opus → Haiku for an easy follow-up question) can be *more* expensive than staying on the original model, since the cache must be rebuilt from scratch for the new model. Claude Code's recommended pattern is a subagent "hand-off": the current model prepares a summary message for the next model, as used by Claude Code's Haiku-based Explore agents.
- **Never change the tool set mid-conversation** — called out as one of the most common ways to break caching, since tool definitions are part of the cached prefix. This is why Plan Mode is implemented by keeping *all* tools present at all times and adding `EnterPlanMode`/`ExitPlanMode` as callable tools (with a system message explaining Plan Mode's rules), rather than swapping in a read-only tool subset. A side benefit: because `EnterPlanMode` is itself a tool, the model can autonomously enter plan mode on a hard problem without any cache break.
- **`defer_loading` over tool removal**: for large MCP tool sets, Claude Code sends lightweight stubs (tool name only, `defer_loading: true`) discoverable via the tool search tool, loading full schemas only once a tool is selected — keeping the cached prefix stable since the same stubs appear in the same order every request.
- **Cache-safe forking for compaction**: naive compaction (a separate API call with its own summarization system prompt and no tools) diverges from the cached prefix at the first token, making the *entire* conversation being compacted uncached — worst exactly when conversations are longest. The fix: run the compaction call with the exact same system prompt, context, and tools as the parent conversation, prepending the parent's messages and appending only the compaction prompt as a new final user message, so the cached prefix is reused and a "compaction buffer" of context-window headroom is reserved for the compact message and summary output. These patterns are now built directly into the Claude API's native [[ContextWindow|compaction]] feature.

See [[summary-2026-04-30 - Lessons from building Claude Code Prompt caching is everything]].

## Cache Breakpoints for Computer-Use / Screenshot Agents (May 2026)

For [[ComputerUse|computer-use]] agents, the API's 4 total cache breakpoints are best allocated as 1 on the stable prefix (system prompt, tool definitions — already hit once and never invalidates, so more than one breakpoint there is wasted) and the remaining 3 spread across recent conversation history, where invalidation risk is highest and savings compound over long sessions. Spreading breakpoints across recent positions gives graceful degradation: if the newest breakpoint is invalidated (e.g. by an image prune or compaction), an earlier breakpoint can still hit, so the request pays 10% of full input cost instead of 100%. This pairs with a batched screenshot-pruning rolling buffer (see [[ContextWindow]]) to keep the cached prefix byte-stable across several turns at a time. See [[summary-2026-05-13 - Best practices for computer and browser use with Claude]].

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
- [[summary-2026-04-02 - Harnessing Claude’s intelligence]] — restates cache-breakpoint mechanism and pricing in a harness-design context
- [[summary-2026-04-30 - Lessons from building Claude Code Prompt caching is everything]] — Claude Code engineering lessons: static/dynamic ordering, system-reminder tags, model-switch cost, Plan Mode design, defer_loading, cache-safe compaction forking
- [[ClaudeCode]] — product whose harness these caching engineering lessons were drawn from
- [[summary-2026-05-13 - Best practices for computer and browser use with Claude]] — cache breakpoint allocation strategy for screenshot-heavy computer-use agents
- [[ComputerUse]] — capability whose screenshot volume motivates this caching strategy
