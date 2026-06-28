---
title: "Claude 3 Opus"
type: entity
tags: [claude, model, anthropic, llm, flagship, thinking, tool-use]
sources: [raw/01-articles/claude/2024-05-30 - Claude can now use tools.md]
last_updated: 2026-06-28
---

# Claude 3 Opus

[[Claude3Opus]] is [[Anthropic]]'s flagship model in the [[Claude3]] family, designed for the most complex, reasoning-intensive tasks. It offers the strongest reasoning and analytical capabilities across the Claude model lineup.

## Key Characteristics

- **Position**: Flagship, most capable model in Claude 3 family
- **Strength**: Advanced reasoning, complex analysis, sophisticated task handling
- **Distinguishing feature**: Includes `<thinking>` tags in outputs to show reasoning process
- **Use cases**: Complex reasoning, strategic analysis, sophisticated data interpretation
- **Tool use**: Full support for [[ToolUse|tool use]] capability (as of May 2024)

## Capabilities

- **Advanced reasoning**: Superior logical reasoning and planning
- **Code generation**: Complex software development tasks
- **Document analysis**: In-depth analysis of long, complex documents
- **Tool use**: Can select and execute external tools and APIs
- **Thinking transparency**: `<thinking>` tags clarify Claude's reasoning to developers
- **Vision**: Image understanding and analysis
- **Multilingual**: Support for multiple languages

## Development Experience

The inclusion of `<thinking>` tags in Opus outputs simplifies the debugging process for developers by making Claude's internal reasoning transparent and verifiable.

## Availability

Accessible through:
- [[Anthropic]] Messages API
- [[AmazonBedrock]] (AWS)
- Google Cloud's Vertex AI
- Claude web platform

## Related

- [[Claude3]] — the parent model family
- [[Claude3Haiku]] — efficient variant for cost-sensitive workloads
- [[Claude3.5Sonnet]] — balanced model between Opus and Haiku
- [[Anthropic]] — creator of Claude 3 Opus
- [[ToolUse]] — core capability of Claude 3 Opus
- [[AdaptiveThinking]] — related concept for Claude's thinking capabilities
- [[summary-2024-05-30 - Claude can now use tools]] — Feature announcement including Opus enhancements
