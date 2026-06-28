---
title: "WebSearch"
type: concept
tags: [web-search, real-time, citations, api]
sources: [raw/01-articles/claude/2025-05-07 - Introducing web search on the Anthropic API.md]
last_updated: 2026-06-28
---

# WebSearch

Real-time internet search capability integrated into Claude models, enabling access to current information with cited sources.

## Overview

WebSearch is a [[ToolUse|tool]] that allows Claude to search the web and retrieve current information when handling requests. This capability is available through the [[MessagesAPI]] for Claude 3.7 Sonnet, Claude 3.5 Sonnet, and Claude 3.5 Haiku models.

## Key Features

- **Real-time Information Access**: Claude can retrieve current web content without developers needing to manage their own search infrastructure
- **Automatic Reasoning**: Claude uses its reasoning capabilities to determine when web search would improve answer accuracy
- **Agentic Search**: Claude can conduct multiple progressive searches, refining queries based on earlier results for comprehensive research
- **Citations**: Every response includes citations to source materials, enabling users to verify information directly
- **Developer Control**: The `max_uses` parameter allows developers to control how many searches Claude can perform

## How It Works

When Claude receives a request that would benefit from up-to-date information or specialized knowledge:

1. Claude determines whether web search would help improve accuracy
2. If beneficial, Claude generates a targeted search query
3. Retrieves relevant results from the web
4. Analyzes the results for key information
5. Provides a comprehensive answer with citations back to source material

Behind the scenes, Claude may refine queries to deliver more accurate responses.

## Use Cases

WebSearch enables Claude to power various applications requiring real-time data:
- Current events and news analysis
- Technical research and documentation lookup
- Market research and competitive intelligence
- Financial and economic data analysis
- Troubleshooting with latest error documentation

## Integration Points

### Claude Code
[[WebSearch]] is available in [[ClaudeCode]], adding the latest information from the web to development workflows. This is particularly valuable for:
- Accessing current API documentation
- Reading technical articles on evolving frameworks
- Troubleshooting obscure errors with latest solutions
- Implementing features requiring version-specific API references

### Admin Controls
Organizations can maintain additional control through admin settings on the Anthropic API console to manage web search usage and policies.

## Pricing

WebSearch is available on the Anthropic API at $10 per 1,000 searches plus standard token costs.

## Web Fetch Extension

As of September 2025, a web fetch tool has been added alongside web search, allowing Claude to fetch and analyze content from any specific webpage URL that developers specify.

## Related

- [[summary-2025-05-07 - Introducing web search on the Anthropic API]] — Source announcement
- [[MessagesAPI]] — The API where web search is available
- [[Citations]] — Source attribution mechanism for web search results
- [[ToolUse]] — Broader capability of which web search is a part
- [[ClaudeCode]] — Development tool with integrated web search support
- [[Claude3.7Sonnet]] — Model supporting web search
- [[Claude3.5Sonnet]] — Model supporting web search
- [[Claude3.5Haiku]] — Model supporting web search
- [[AIAgent]] — Agentic patterns leveraging web search for research
