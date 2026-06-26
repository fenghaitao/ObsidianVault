---
title: "Claude 3.5 Sonnet"
type: entity
category: model
tags: [anthropic, claude, frontier-model, llm, vision, coding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240805 - What's new from Anthropic and what's next： Alex Albert.md"]
last_updated: 2026-06-26
---

## Definition
Claude 3.5 Sonnet is Anthropic's first model in the Claude 3.5 family, positioned as the middle-tier model yet outperforming the previous flagship Claude 3 Opus. It combines speed, intelligence, vision capabilities, and low cost, making it one of the best models in the world at its time of release.

## Key Information
- **Family position**: First model in Claude 3.5 family; only the middle-tier model
- **Relative performance**: Outperforms Claude 3 Opus (Anthropic's previous best) across benchmarks
- **Benchmarks**: Top of its class on MMLU, HumanEval, GPQA, and tool use
- **Coding**: 64% on Anthropic's internal pull request evaluations (vs. 38% for Claude 3 Opus). Better at debugging, doesn't get stuck in loops, iteratively writes and tests solutions
- **Context**: 200k context window with near-perfect recall over the entire context
- **RAG**: Particularly strong in retrieval-augmented generation use cases
- **Vision**: State-of-the-art vision abilities with considerable improvement over 3 Opus. Excels at table transcriptions, OCR, and screenshot-to-code
- **Pricing**: 5x cheaper than Claude 3 Opus — $3 per million input tokens, $15 per million output tokens
- **Availability**: Anthropic API, AWS Bedrock, Vertex AI
- **Key capability**: Consistent structured JSON output when combined with Tool Use API

## Related
- [[Anthropic]] — creator
- [[Alex Albert]] — presented this model
- [[AmazonBedrock]] — platform availability
- [[Vertex AI]] — platform availability
- [[ToolCalling]] — Tool Use API enabling structured outputs
- [[Structured Outputs]] — JSON output capability
- [[Artifacts]] — product feature combining 3.5 Sonnet's coding, reasoning, and vision
- [[summary-20240805 - What's new from Anthropic and what's next： Alex Albert]] — source
