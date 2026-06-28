---
title: "summary-2025-08-14 - Prompt caching with Claude.md"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2025-08-14 - Prompt caching with Claude.md"]
last_updated: 2026-06-28
---

# Summary: Prompt Caching with Claude

Original article: [Prompt caching with Claude](https://claude.com/blog/prompt-caching) — Anthropic, published 2025-08-14 (last modified 2026-06-21).

## Core Summary

Claude's prompt caching feature lets developers cache frequently used context between API calls, reducing costs by up to 90% and latency by up to 85% for long prompts. The feature launched in public beta for Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku on the Anthropic API, and is also available in preview on Amazon Bedrock and Google Cloud's Vertex AI.

## Key Points

- **What it does**: Caches frequently used prompt context (knowledge bases, system instructions, example outputs, conversation turns) across multiple API calls so developers do not need to retransmit the same tokens on each request.
- **Cost model**: Writing to the cache costs 25% more than the base input token price; reading cached content costs only 10% of the base input token price — a significant discount that makes long-context applications economically viable.
- **Headline gains**: Up to 90% cost reduction and up to 85% latency reduction for long prompts.
- **Initial model availability (public beta)**: Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku.
- **Platform availability**: Generally available on the Anthropic API; in preview on Amazon Bedrock and Google Cloud's Vertex AI.
- **Use cases highlighted**: Full knowledge-base inclusion, 100-shot example prompts, multi-turn conversation context.
- **Early customer — Notion**: Notion is adding prompt caching to Claude-powered features in Notion AI, optimizing internal operations and improving response speed for end users. Quote from Simon Last (Co-founder, Notion): "We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality."

## Related

- [[PromptCaching]] — concept page for this feature
- [[Anthropic]] — API provider that released the feature
- [[AmazonBedrock]] — cloud platform with prompt caching in preview
- [[VertexAI]] — Google Cloud platform with prompt caching in preview
- [[Notion]] — early adopter integrating prompt caching into Notion AI
- [[Claude3.5Sonnet]] — one of the initial models supporting prompt caching
- [[Claude3Opus]] — one of the initial models supporting prompt caching
- [[Claude3Haiku]] — one of the initial models supporting prompt caching
- [[TokenOptimization]] — broader cost-efficiency concept
