---
title: "Claude 3.5 Haiku on AWS Trainium2 and model distillation in Amazon Bedrock"
type: source
tags: [bedrock, trainium2, distillation, haiku, aws, pricing]
sources: [raw/01-articles/claude/2024-12-03 - Claude 3.5 Haiku on AWS Trainium2 and model distillation in Amazon Bedrock.md]
last_updated: 2026-06-28
---

# Claude 3.5 Haiku on AWS Trainium2 and Model Distillation in Amazon Bedrock

This article announces two major enhancements to Claude models on AWS: latency-optimized inference for Claude 3.5 Haiku on Trainium2, and model distillation capability in Amazon Bedrock.

## Trainium2 Optimization

[[Anthropic]] and [[AWS]] are collaborating to optimize Claude models for AWS Trainium2, the next-generation AI chip. As part of Project Rainier—an EC2 UltraCluster containing hundreds of thousands of Trainium2 chips—Anthropic is building infrastructure for next-generation model training.

### Claude 3.5 Haiku on Trainium2

- **Availability**: Public preview in US East (Ohio) Region via cross-region inference
- **Performance**: Up to 60% faster inference speed compared to baseline
- **Pricing**: $1 per million input tokens and $5 per million output tokens (Trainium2-optimized version)
- **Use Cases**: Code completions, real-time content moderation, chatbots
- **Status**: Latency-optimized inference now available

## Model Distillation in Amazon Bedrock

[[Amazon Bedrock]] now supports model distillation, enabling smaller, faster, more cost-effective models to achieve frontier-level performance through knowledge transfer from larger models.

### How Distillation Works

Distillation transfers knowledge from a "teacher" model ([[Claude3.5Sonnet]]) to a "student" model ([[Claude3Haiku]]), allowing the smaller model to achieve similar accuracy on specific tasks.

### Automation Over Manual Fine-tuning

Unlike traditional [[FineTuning]], which requires manual training data curation and parameter adjustment, Amazon Bedrock Model Distillation automates:
1. **Synthetic Training Data Generation**: Automatically creates high-quality training data from Claude 3.5 Sonnet
2. **Model Training & Evaluation**: Trains and tests Claude 3 Haiku
3. **Model Hosting**: Manages inference deployment

The system applies different data synthesis methods including prompt similarity-based generation and response synthesis.

### Benefits

- **Cost Efficiency**: Run sophisticated tasks like [[RetrievalAugmentedGeneration]] (RAG) and data analysis at lower cost
- **Performance Parity**: Achieve Claude 3.5 Sonnet-level accuracy for specific tasks
- **Speed**: Maintains fast inference of Claude 3 Haiku
- **Availability**: Preview available in Amazon Bedrock

## Pricing Changes

New pricing for [[Claude3.5Haiku]] across all platforms:
- **Input**: $0.80 per million tokens (down from baseline)
- **Output**: $4 per million tokens (down from baseline)
- Applies to [[Anthropic]] API, [[AmazonBedrock]], and Google Cloud Vertex AI

## Project Rainier

Anthropic and AWS are building an EC2 UltraCluster of Trn2 UltraServers containing hundreds of thousands of Trainium2 chips, delivering more than 5x the computing power used to train current generation leading AI models.

## Related

- [[Claude3.5Haiku]] — optimized for Trainium2 with latency optimization
- [[Claude3.5Sonnet]] — teacher model for distillation
- [[Claude3Haiku]] — student model for distillation capability
- [[AWS]] — infrastructure partner
- [[AmazonBedrock]] — service offering both features
- [[ModelDistillation]] — knowledge transfer technique
- [[FineTuning]] — traditional alternative to distillation
- [[RetrievalAugmentedGeneration]] — use case for distilled models
