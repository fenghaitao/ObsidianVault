---
title: "Claude 3.7 Sonnet"
type: entity
tags: [claude, model, anthropic, llm, foundation-model, sonnet, latest]
sources: [raw/01-articles/claude/2025-03-06 - Get to production faster with the upgraded Anthropic Console.md, raw/01-articles/claude/2025-03-13 - Token-saving updates on the Anthropic API.md, "raw/01-articles/claude/2025-04-02 - Claude on Google Cloud’s Vertex AI FedRAMP High and IL2 Authorized.md", raw/01-articles/claude/2025-05-07 - Introducing web search on the Anthropic API.md, raw/01-articles/claude/2025-03-20 - Claude can now search the web.md]
last_updated: 2026-07-04
---

# Claude 3.7 Sonnet

Claude 3.7 Sonnet is [[Anthropic]]'s latest and most intelligent Claude model, featuring advanced reasoning capabilities including [[ExtendedThinking]], significant token optimization features, and government/defense compliance authorizations.

## Definition

Claude 3.7 Sonnet is [[Anthropic]]'s high-capability general-purpose model, introducing advances in reasoning, cost efficiency, and compliance. It represents the cutting-edge of the Claude Sonnet family.

## Key Information

- **Creator**: [[Anthropic]]
- **Status**: Latest and most intelligent Claude model to date
- **Classification**: High-capability general-purpose frontier model
- **Key Capabilities**: Extended thinking, token optimization, vision, multilingual support, complex reasoning
- **Availability**: [[Anthropic]] API, Amazon Bedrock, Google Cloud Vertex AI (including government authorized environments)

## Core Capabilities

Claude 3.7 Sonnet supports:
- **Extended Thinking**: Visible step-by-step reasoning with controllable token budgets
- **Complex Reasoning**: Advanced analysis and problem-solving
- **Vision**: Image understanding and analysis
- **Multilingual Support**: Processing across multiple languages
- **Agentic Behavior**: Tool use and multi-step workflows
- **Web Search**: Real-time internet search with citations for up-to-date information access. This model powered the initial consumer launch of [[WebSearch]] in Claude.ai (March 20, 2025, feature preview for US paid users) ahead of the May 2025 Anthropic API web search tool.

## Token Optimization Features

Claude 3.7 Sonnet introduces significant cost-reduction innovations (as of March 2025):

- **[[PromptCaching]]**: Stores and reuses frequently accessed context, reducing costs by up to 90% for long prompts
- **Cache-Aware Rate Limits**: Prompt cache read tokens no longer count against Input Tokens Per Minute (ITPM) limits, increasing throughput within existing rate allocations
- **Token-Efficient [[ToolUse]]**: Reduces output token consumption by up to 70% (average 14% in early deployments) for tool interactions
- **Text Editor Tool**: Specialized tool for document collaboration with targeted edits, reducing token consumption and latency

## Government and Defense Deployment

Claude 3.7 Sonnet is authorized for government and defense workloads:
- **FedRAMP High Authorization**: For federal civilian agencies handling sensitive unclassified data
- **DoD IL2 Compliance**: For defense contractors with non-controlled unclassified information
- **Deployment**: Available through [[GoogleCloud]] Vertex AI with managed serverless infrastructure
- **Use Cases**: Healthcare, law enforcement, finance, emergency services, digital transformation

## Relationship to Earlier Models

Claude 3.7 Sonnet succeeds [[Claude3.5Sonnet]] with enhanced capabilities across reasoning (extended thinking), cost efficiency (token optimization), and compliance (government authorizations).

## Related

- [[Anthropic]] — creator of Claude 3.7 Sonnet
- [[Claude3.5Sonnet]] — previous generation Sonnet model
- [[Claude3]] — third-generation Claude model family
- [[ExtendedThinking]] — reasoning feature of this model
- [[PromptCaching]] — cost-reduction feature
- [[TokenOptimization]] — token efficiency improvements
- [[ToolUse]] — tool use capability with token-efficient variants
- [[WebSearch]] — web search capability available on this model
- [[AnthropicConsole]] — development platform supporting extended thinking optimization
- [[GoogleCloud]] — cloud provider offering Claude 3.7 Sonnet
- [[VertexAI]] — Vertex AI platform hosting this model
- [[FedRAMP]] — federal compliance standard
- [[DoD-IL2]] — defense compliance standard
- [[PromptEngineering]] — discipline enhanced by this model's capabilities
- [[AdaptiveThinking]] — complementary thinking capability
- [[Cognition]] — enterprise customer leveraging this model
- [[summary-2025-03-06 - Get to production faster with the upgraded Anthropic Console]] — extended thinking announcement
- [[summary-2025-03-13 - Token-saving updates on the Anthropic API]] — token optimization announcement
- [[summary-2025-04-02 - Claude on Google Cloud’s Vertex AI FedRAMP High and IL2 Authorized]] — government compliance announcement
- [[summary-2025-05-07 - Introducing web search on the Anthropic API]] — web search feature announcement
- [[summary-2025-03-20 - Claude can now search the web]] — initial consumer web search launch in Claude.ai
