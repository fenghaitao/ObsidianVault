---
title: "Fine-tune Claude 3 Haiku in Amazon Bedrock"
type: source
tags: [fine-tuning, AWS, Bedrock, Haiku, customization]
sources: [raw/01-articles/claude/2024-07-10 - Fine-tune Claude 3 Haiku in Amazon Bedrock.md]
last_updated: 2026-06-28
---

# Fine-tune Claude 3 Haiku in Amazon Bedrock

**Summary**: Anthropic announced that Claude 3 Haiku can be fine-tuned within Amazon Bedrock, allowing customers to customize the model with their own training data. The capability is available in preview (as of July 2024) and became generally available by November 1, 2024.

## Key Points

- **What**: Fine-tuning enables creating a customized version of Claude 3 Haiku by training it on high-quality prompt-completion pairs specific to a business use case.

- **How**: Customers prepare training data, use the fine-tuning API (available in Amazon Bedrock console or API), test and refine the custom model, and deploy when ready.

- **Benefits**:
  - Specialized business knowledge integration
  - Improved accuracy and consistency for domain-specific tasks
  - Faster inference (reduced tokens per query)

## Notable Use Cases

**Comment Moderation**: Fine-tuned Haiku improved classification accuracy from 81.5% to 99.6% while reducing tokens per query by 85%.

**SK Telecom**: Trained a custom Claude model for customer support workflows. Results: 73% increase in positive feedback for agent responses and 37% improvement in key performance indicators for telecommunications tasks. The fine-tuned model generates topics, action items, and summaries from customer call logs.

**Thomson Reuters**: Plans to fine-tune Claude 3 Haiku to enhance Claude-powered solutions for legal, tax, accounting, compliance, government, and media professionals. Focus: industry-specific expertise and faster, more relevant results.

## Technical Details

- **Context Length**: Supports up to 32K tokens at launch
- **Data Format**: Text-based fine-tuning
- **Vision**: Planned for future
- **Availability**: US West (Oregon) AWS Region at launch

## Related

[[Claude3Haiku]] — [[AmazonBedrock]] — [[FineTuning]] — [[SKTelecom]] — [[ThomsonReuters]]
