---
title: "Fine-Tuning"
type: concept
tags: [machine-learning, model-customization, training, optimization]
sources: [raw/01-articles/claude/2024-07-10 - Fine-tune Claude 3 Haiku in Amazon Bedrock.md]
last_updated: 2026-06-28
---

# Fine-Tuning

Fine-tuning is a machine learning technique that customizes a pre-trained foundation model by training it on domain-specific data. This allows organizations to adapt a model to excel at specialized tasks without retraining from scratch.

## Core Concept

Fine-tuning takes an existing, pre-trained model (such as [[Claude3Haiku]]) and trains it further on a curated dataset of examples specific to a particular task or domain. This approach combines the general knowledge of the foundation model with specialized expertise from the custom training data.

## Process

1. **Prepare Training Data**: Gather high-quality prompt-completion pairs representing ideal outputs for the target task
2. **Train**: Use fine-tuning API or service to train the model on the custom data
3. **Test & Iterate**: Evaluate the fine-tuned model and refine until performance meets goals
4. **Deploy**: Release the customized model for production use

## Benefits

- **Improved Accuracy**: Models achieve higher accuracy on domain-specific tasks
- **Consistency**: Ensures consistent behavior aligned with organizational standards
- **Token Efficiency**: Reduces tokens per query by encoding domain knowledge
- **Cost Reduction**: Smaller fine-tuned models can replace larger base models for specific tasks
- **Knowledge Integration**: Encodes specialized business knowledge directly into the model

## Empirical Results

Fine-tuning [[Claude3Haiku]] has demonstrated significant improvements:
- **Comment Moderation**: 81.5% → 99.6% accuracy; 85% token reduction
- **SK Telecom Support**: 73% increase in positive agent feedback; 37% KPI improvement
- **Thomson Reuters Professional Services**: Expected measurable improvements in accuracy and speed

## Deployment Platforms

- [[AmazonBedrock]]: Supports fine-tuning of [[Claude3Haiku]] and other Claude models
- Other cloud providers: Fine-tuning increasingly available across major ML platforms

## Related

- [[Claude3Haiku]] — model with fine-tuning capability
- [[Claude3.5Haiku]] — next-generation Haiku model
- [[AmazonBedrock]] — service offering fine-tuning
- [[ModelDistillation]] — alternative approach to model customization
- [[SKTelecom]] — customer using fine-tuned Claude
- [[ThomsonReuters]] — customer planning to use fine-tuning
- [[summary-2024-07-10 - Fine-tune Claude 3 Haiku in Amazon Bedrock]] — fine-tuning announcement
