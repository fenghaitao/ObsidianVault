---
title: "Cognition"
type: entity
tags: [company, devin, ai-software-engineer, coding-agent]
sources: [raw/03-transcripts/Claude/The Problem Solvers/06 - The Problem Solvers： Scott Wu at Cognition.md, raw/01-articles/claude/2025-03-13 - Token-saving updates on the Anthropic API.md]
last_updated: 2026-06-28
---

## Definition

Cognition is the company behind Devin, the first AI software engineer. Founded by Scott Wu (former world champion competitive programmer), Cognition builds tools that help institutions — banks, health insurers, governments, private equity firms — build software 10x faster. The company maintains a collaborative co-opetition relationship with [[Anthropic]].

## Devin: AI Software Engineer

Devin is Cognition's flagship product, an AI software engineer capable of:
- Writing, reviewing, and deploying code
- Building software end-to-end with minimal human intervention
- Collaborating with engineering teams on complex projects

## Token Optimization with Claude 3.7 Sonnet

As of March 2025, Cognition leverages [[Claude3.7Sonnet]]'s [[TokenOptimization]] features:

- **[[PromptCaching]]**: Provides extensive codebase context while reducing costs and latency
- **Cache-Aware ITPM Limits**: Optimizes prompt caching usage to increase throughput within existing rate limits
- **Token-Efficient Tool Use**: Improves token efficiency for code analysis and generation tasks

According to Scott Wu, CEO of Cognition: "Prompt caching allows us to provide more context about the codebase to get higher quality results while reducing cost and latency. With cache-aware ITPM limits, we are further optimizing our prompt caching usage to increase our throughput and get more out of our existing rate limits."

## Related

- [[summary-06 - The Problem Solvers： Scott Wu at Cognition]] — source talk
- [[Claude3.7Sonnet]] — model powering Devin with token optimization
- [[PromptCaching]] — cost-reduction feature used by Cognition
- [[TokenOptimization]] — efficiency improvements leveraged by Cognition
- [[ClaudeCode]] — Anthropic's coding agent (overlapping product)
- [[Anthropic]] — model provider and partner
- [[summary-2025-03-13 - Token-saving updates on the Anthropic API]] — announcement of token optimization features
