---
title: "summary-2026-03-13 - 1M context is now generally available for Opus 4.6 and Sonnet 4.6"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-03-13 - 1M context is now generally available for Opus 4.6 and Sonnet 4.6.md"]
last_updated: 2026-07-04
---

## Core Summary

The 1M-token context window for [[Claude4.6Opus|Claude Opus 4.6]] and [[Claude4.6Sonnet|Claude Sonnet 4.6]] reaches general availability on the Claude Platform, with standard per-token pricing ($5/$25 per million tokens for Opus 4.6, $3/$15 for Sonnet 4.6) applied across the full window — no long-context premium multiplier. [[ClaudeCode]] sessions for Max, Team, and Enterprise users on Opus 4.6 now default to the full 1M window automatically, previously an extra-usage feature, reducing compactions and preserving more conversation history. Opus 4.6 scores 78.3% on MRCR v2, the highest among frontier models at that context length, meaning the extra capacity translates into usable recall rather than just raw token capacity. Media limits also expand to 600 images or PDF pages. 1M context is available natively on the Claude Platform and through [[AmazonBedrock|Amazon Bedrock]], Google Cloud's [[VertexAI|Vertex AI]], and Microsoft Foundry.

## Key Points

- Standard pricing now applies across the entire 1M-token window for both Opus 4.6 and Sonnet 4.6 — a 900K-token request costs the same per-token rate as a 9K-token one.
- Opus 4.6: $5/$25 per million tokens (input/output); Sonnet 4.6: $3/$15 per million tokens.
- Claude Code for Max, Team, and Enterprise users on Opus 4.6 now defaults to 1M context automatically (previously required extra usage), yielding fewer compactions and more intact conversation history.
- Opus 4.6 scores 78.3% on MRCR v2 (multi-round co-reference resolution), the highest among frontier models at 1M-token length.
- Enables loading entire codebases, thousands of pages of contracts, or the full trace of a long-running agent directly, without lossy summarization or manual context-clearing.
- Media limits expand to 600 images or PDF pages.
- Available today natively on the Claude Platform, and through Amazon Bedrock, Google Cloud's Vertex AI, and Microsoft Foundry.

## Related

- [[Claude4.6Opus]] — model reaching 1M context GA; scores 78.3% on MRCR v2
- [[Claude4.6Sonnet]] — sibling model reaching 1M context GA
- [[ClaudeCode]] — now defaults to 1M context for Max/Team/Enterprise Opus 4.6 users
- [[ContextWindow]] — the underlying capability reaching general availability here
- [[AmazonBedrock]] — cloud platform offering 1M context
- [[VertexAI]] — cloud platform offering 1M context
- [[ClaudeMax]] — plan tier receiving automatic 1M context
- [[ClaudeTeamPlan]] — plan tier receiving automatic 1M context
- [[ClaudeEnterprise]] — plan tier receiving automatic 1M context
- [[Anthropic]] — publisher of this announcement
