---
title: "Claude 3.5 Haiku"
type: entity
tags: [claude, model, haiku, lightweight, fast, cost-effective, trainium2]
sources: [raw/01-articles/claude/2024-12-03 - Claude 3.5 Haiku on AWS Trainium2 and model distillation in Amazon Bedrock.md, raw/01-articles/claude/2025-06-23 - Introducing Citations on the Anthropic API.md, raw/01-articles/claude/2025-05-07 - Introducing web search on the Anthropic API.md]
last_updated: 2026-06-28
---

# Claude 3.5 Haiku

Claude 3.5 Haiku is Anthropic's fastest and most cost-effective model, optimized for real-time inference and latency-sensitive applications. It is the latest generation of the Haiku family and supports advanced optimization for high-speed deployment.

## Key Characteristics

- **Position**: Fastest and most cost-effective model in the Claude 3.5 lineup
- **Use Cases**: Real-time inference, code completions, content moderation, chatbots, lightweight applications
- **Architecture**: Latest generation with optimizations for latency
- **Availability**: Accessible across [[Anthropic]] API, [[AmazonBedrock]], and Google Cloud Vertex AI
- **Capabilities**: [[WebSearch]] for real-time information access with citations

## Performance and Optimization

### Trainium2 Optimization

As of December 2024, Claude 3.5 Haiku supports latency-optimized inference on [[AWS]] Trainium2 chips:

- **Performance Gain**: Up to 60% faster inference speed
- **Deployment**: Available in US East (Ohio) Region via cross-region inference
- **Use Cases**: Ideal for real-time requirements like code completions, content moderation, and chatbots
- **Status**: Public preview (December 2024)

### Pricing

- **Standard Pricing** (all platforms): $0.80 per million input tokens, $4 per million output tokens
- **Trainium2-Optimized Pricing** (Amazon Bedrock): $1 per million input tokens, $5 per million output tokens
- Price reduction announced December 2024 to make the model more accessible

## Model Distillation Capability

Claude 3.5 Haiku serves as a foundation for model distillation in [[AmazonBedrock]], where knowledge from larger models can be transferred to optimize performance for specific tasks. The [[Claude3.5Sonnet]] acts as a "teacher" model in distillation scenarios.

## Related

- [[Claude3.5Sonnet]] — more capable sibling in the Claude 3.5 family
- [[Claude3Haiku]] — previous generation Haiku model
- [[Anthropic]] — creator of Claude 3.5 Haiku
- [[AmazonBedrock]] — AWS service offering Claude 3.5 Haiku with optimization and distillation
- [[AWS]] — infrastructure provider for Trainium2 optimization
- [[ModelDistillation]] — technique where Haiku serves as foundation
- [[FineTuning]] — alternative customization approach
- [[Citations]] — API feature for citations that Claude 3.5 Haiku supports
- [[WebSearch]] — web search capability available on this model
- [[summary-2024-12-03 - Claude 3.5 Haiku on AWS Trainium2 and model distillation in Amazon Bedrock]] — announcement article
- [[summary-2025-05-07 - Introducing web search on the Anthropic API]] — web search feature announcement
