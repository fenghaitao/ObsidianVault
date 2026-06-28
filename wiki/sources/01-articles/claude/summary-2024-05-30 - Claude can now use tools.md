---
title: "Claude can now use tools"
type: source
tags: [claude, tool-use, api, anthropic, general-availability]
sources: ["raw/01-articles/claude/2024-05-30 - Claude can now use tools.md"]
last_updated: 2026-06-28
---

# Claude can now use tools

**Core thesis**: Tool use — the ability for Claude to interact with external tools and APIs — became generally available across the entire Claude 3 model family in May 2024, available on the Anthropic Messages API, Amazon Bedrock, and Google Cloud's Vertex AI. This enables developers to build more dynamic and accurate applications by allowing Claude to select and execute appropriate tools within defined workflows.

## Summary

[[ToolUse|Tool use]] became generally available (GA) across all [[Claude3]] models on May 30, 2024, enabling Claude to interact with external tools and APIs to perform tasks, manipulate data, and deliver more accurate responses.

### Availability

Tool use is available on:
- [[Anthropic]] Messages API
- [[AmazonBedrock]] (AWS)
- Google Cloud's Vertex AI

### Developer Experience

Developers define a toolset for Claude and specify their request in natural language. Claude then:
- Selects the appropriate tool to fulfill the task
- Executes the corresponding action when appropriate
- Returns results for further reasoning

### Model Enhancements

[[Claude3Opus]], the flagship model, now includes `<thinking>` tags in its outputs to clarify its reasoning, simplifying debugging for developers.

**Limitation**: Claude 3 models do not support parallel tool calls.

## Enterprise Use Cases

### StudyFetch
[[StudyFetch]], an AI-native learning platform, uses Claude's tool use capabilities to power **Spark.E**, a personalized AI tutor.

**Integration**: Tools track student progress, navigate course materials and lectures, and create interactive user interfaces.

**Impact**: 42% increase in positive human feedback after implementation. Enabled live voice-enabled AI tutoring sessions and deployment in just days.

**Quote** (Ryan Trattner, CTO and Co-Founder): *"Claude with tool use is accurate and cost-effective, and now powers our live voice-enabled AI tutoring sessions. Within just a few days, we integrated tools into our platform. As a result, our AI tutor, Spark.E, acts agentively—displaying interactive UIs, tracking student progress in context, and navigating through lectures and materials. Since implementing Claude with tool use, we've observed a 42% increase in positive human feedback."*

### Intuned
[[Intuned]], a browser automation platform, uses Claude to power data extraction within its cloud platform.

**Focus**: AI-powered data extraction for more reliable browser automations.

**Impact**: Drastically improved developer experience in building and executing browser automations.

**Tool**: [[Claude3Haiku]] with tool use capabilities.

**Quote** (Faisal Ilaiwi, Co-Founder): *"Claude 3 Haiku with tool use has been a game changer for us. After accessing the model and running our benchmarks on it, we realized the quality, speed, and price combination is unmatched. Haiku is helping us scale our customers' data extraction tasks to a completely new level."*

### Hebbia
[[Hebbia]] builds AI knowledge worker software for financial and legal services firms, using [[Claude3Haiku]] to power multi-step customer workflows.

**Use cases**: Generating live suggestions, automating prompt writing, extracting key metadata from long documents.

**Impact**: Tool use feature unlocked capabilities and speed for generating reliable suggestions and prompts in real-time.

**Quote** (Divya Mehta, Product Manager): *"We leverage Claude 3 Haiku for generating live suggestions, automating prompt writing, and extracting key metadata from long documents. Claude 3 Haiku's tool use feature has unlocked capabilities and speed for our platform to generate reliable suggestions and prompts in real-time."*

## Developer Resources

Documentation and educational materials available:
- [[Anthropic]] tool use documentation
- Tool use tutorial on GitHub
- Anthropic Cookbooks on tool use (including calculator tool example)

## Related

- [[ToolUse]] — the core capability described in this article
- [[Claude3]] — the model family now with tool use support
- [[Claude3Opus]] — flagship model with thinking tags
- [[Claude3Haiku]] — efficient model highlighted for production use
- [[Anthropic]] — creator of Claude and tool use capability
- [[StudyFetch]] — AI tutoring platform using tool use
- [[Intuned]] — browser automation platform using tool use
- [[Hebbia]] — financial and legal AI platform using tool use
- [[AmazonBedrock]] — AWS service offering Claude with tool use
