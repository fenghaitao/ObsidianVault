---
title: "1M context is now generally available for Opus 4.6 and Sonnet 4.6"
type: article
source: https://claude.com/blog/1m-context-ga
description: "Standard pricing now applies across the full 1M window for both models, with no long-context premium. Media limits expand to 600 images or PDF pages."
author: "Anthropic"
published: 2026-03-13
last_modified: 2026-06-21
---

# 1M context is now generally available for Opus 4.6 and Sonnet 4.6

Standard pricing now applies across the full 1M window for both models, with no long-context premium. Media limits expand to 600 images or PDF pages.


Standard pricing now applies across the full 1M window for both models, with no long-context premium. Media limits expand to 600 images or PDF pages.


Claude Opus 4.6 and Sonnet 4.6 now include the full 1M context window at standard pricing on the Claude Platform. Standard pricing applies across the full window — $5/$25 per million tokens for Opus 4.6 and $3/$15 for Sonnet 4.6. There's no multiplier: a 900K-token request is billed at the same per-token rate as a 9K one.

**What's new with general availability:**

**1M context is now included in Claude Code for Max, Team, and Enterprise users with Opus 4.6.** Opus 4.6 sessions can use the full 1M context window automatically, meaning fewer compactions and more of the conversation kept intact. 1M context previously required extra usage.

A million tokens of context only matters if the model can recall the right details and reason across them. Opus 4.6 scores 78.3% on MRCR v2, the highest among frontier models at that context length.

That means you can load an entire codebase, thousands of pages of contracts, or the full trace of a long-running agent — tool calls, observations, intermediate reasoning — and use it directly. The engineering work, lossy summarization, and context clearing that long-context work previously required are no longer needed. The full conversation stays intact.

1M context is available today on the Claude Platform natively and through Amazon Bedrock, Google Cloud’s Vertex AI, and Microsoft Foundry. Claude Code Max, Team, and Enterprise users on Opus 4.6 will default to 1M context automatically.

See our [documentation](https://platform.claude.com/docs/en/build-with-claude/context-windows) and [pricing](https://platform.claude.com/docs/en/about-claude/pricing) for details.


Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.
