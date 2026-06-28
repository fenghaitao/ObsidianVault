---
title: "Introducing web search on the Anthropic API"
type: source
tags: [web-search, api, real-time-information, citations, agents]
sources: [raw/01-articles/claude/2025-05-07 - Introducing web search on the Anthropic API.md]
last_updated: 2026-06-28
---

# Introducing web search on the Anthropic API

Claude can now search the web through the API, giving developers access to real-time information with citations for building up-to-date AI applications.

## Overview

Anthropic has launched [[WebSearch]] on the Anthropic API, enabling [[Claude]] models to access current information from across the web when making requests through the [[MessagesAPI]]. This capability allows developers to build Claude-powered applications and agents that deliver up-to-date insights without managing their own web search infrastructure.

## How It Works

When Claude receives a request that would benefit from up-to-date information or specialized knowledge, it uses its reasoning capabilities to determine whether the [[WebSearch]] tool would help. If searching would be beneficial, Claude:

1. Generates a targeted search query
2. Retrieves relevant results
3. Analyzes key information
4. Provides a comprehensive answer with [[Citations]]

Claude can operate agentically and conduct multiple progressive searches, using earlier results to inform subsequent queries for light research. Developers control this behavior by adjusting the `max_uses` parameter, and Claude may refine queries behind the scenes for greater accuracy.

## Features

- **Real-time Information**: Access to current web content without managing search infrastructure
- **Citations**: Every response includes citations to source materials, enabling verification and accountability
- **Agentic Search**: Multi-step, progressive searches that refine queries based on earlier results
- **Reasoning Integration**: Claude determines when web search would improve accuracy

## Use Cases

Web search enables Claude to power various use cases requiring real-time data and specialized knowledge:
- Current events and news analysis
- Technical research and documentation lookup
- Market research and competitive intelligence
- Financial and economic data analysis

## Admin Controls

Organizations can maintain additional control through admin settings on the Anthropic API console.

## Integration with Claude Code

[[WebSearch]] is available in [[ClaudeCode]], adding the latest information from the web to development workflows. This is particularly valuable for:
- Accessing current API documentation
- Reading technical articles and library information
- Troubleshooting obscure errors
- Implementing features requiring version-specific API references

## Update (September 10, 2025)

A web fetch tool has been added, allowing Claude to fetch and analyze content from any webpage URL that developers specify.

## Pricing

Web search is available on the Anthropic API for [[Claude3.7Sonnet]], [[Claude3.5Sonnet]], and [[Claude3.5Haiku]] at $10 per 1,000 searches plus standard token costs.

## Customer Testimonials

**Quora/Poe**: Spencer Chan, Head of Poe Product, noted that Anthropic's web search tool is cost-effective and delivers search results with impressive speed, benefiting Poe users who need real-time information while using Claude models.

**Adaptive**: Dennis Xu, Co-founder of Adaptive (an AI tool for creating end-to-end apps), stated that the web search tool delivers consistently thorough results that outperformed other tools tested, and praised Claude's ability to function as a research agent.

## Related

- [[WebSearch]] — The core capability enabling real-time internet search
- [[MessagesAPI]] — The API endpoint where web search is available
- [[ClaudeCode]] — Development tool with integrated web search support
- [[Citations]] — Source attribution mechanism for web search results
- [[AIAgent]] — Agentic patterns that leverage web search for research
- [[ToolUse]] — Broader tool-use capability of which web search is a part
- [[Claude3.7Sonnet]] — Model supporting web search
- [[Claude3.5Sonnet]] — Model supporting web search
- [[Claude3.5Haiku]] — Model supporting web search
- [[Quora]] — Customer using web search on Poe platform
- [[Adaptive]] — Customer using web search in end-to-end app creation
