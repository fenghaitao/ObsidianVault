---
title: "summary-2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md"]
last_updated: 2026-06-28
---

## Core Summary

Claude Sonnet 4 expands its context window to 1 million tokens — a 5x increase over its prior limit — enabling processing of entire codebases (75,000+ lines), large document sets, and complex multi-step agentic workflows in a single request. The capability launched in public beta on the Anthropic API, Amazon Bedrock, and Google Cloud Vertex AI. Pricing scales for prompts over 200K tokens; combining with prompt caching or batch processing yields additional cost savings.

## Key Points

- **1M token context window** is now available for [[Claude4Sonnet]] (5x previous limit).
- Available in public beta on the [[Anthropic]] API (Tier 4 and custom rate limits), [[AmazonBedrock]], and [[VertexAI]] (added Aug 26, 2025).
- **Tiered pricing**: additional per-token cost applies to prompts over 200K tokens.
- **Batch processing** integration available for an extra 50% cost reduction.
- **Prompt caching** integration available to reduce both latency and cost at scale.
- **Use cases enabled**:
  - Large-scale code analysis (entire codebases, cross-file dependency understanding)
  - Document synthesis (legal contracts, research papers, technical specs across hundreds of documents)
  - Context-aware agents (hundreds of tool calls without losing coherence, full API docs + interaction history in context)
- **Customer spotlight — [[BoltNew]]**: CEO Eric Simons notes Sonnet 4 remains their primary model for code generation; the 1M window allows developers to work on significantly larger projects.
- **Customer spotlight — [[iGentAI]]**: CEO Sean Ward describes Maestro, iGent AI's software engineering agent, as unlocking "true production-scale engineering" with multi-day sessions on real-world codebases.

## Related

- [[Claude4Sonnet]] — model receiving the 1M context window expansion
- [[ContextWindow]] — core concept explained in this article
- [[PromptCaching]] — complementary cost-reduction technique
- [[BatchProcessing]] — additional 50% cost savings when combined with long context
- [[AmazonBedrock]] — cloud platform where 1M context is available
- [[VertexAI]] — cloud platform where 1M context is available
- [[Anthropic]] — publisher of the article
- [[BoltNew]] — customer spotlight: code generation platform
- [[iGentAI]] — customer spotlight: agentic software engineering
- [[AIAgent]] — primary beneficiary of extended context window
