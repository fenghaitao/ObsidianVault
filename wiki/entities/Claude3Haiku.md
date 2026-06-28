---
title: "Claude 3 Haiku"
type: entity
tags: [claude, model, haiku, lightweight, fast, cost-effective]
sources: [raw/01-articles/claude/2024-07-10 - Fine-tune Claude 3 Haiku in Amazon Bedrock.md, raw/01-articles/claude/2024-05-30 - Claude can now use tools.md]
last_updated: 2026-06-28
---

# Claude 3 Haiku

Claude 3 Haiku is Anthropic's fastest and most cost-effective model in the Claude 3 family, designed for lightweight tasks and real-time applications. It supports fine-tuning to customize behavior for specialized business use cases.

## Key Characteristics

- **Position**: Fastest and most cost-effective model in Claude 3 lineup
- **Use Cases**: Real-time tasks, lightweight applications, cost-sensitive workloads
- **Tool use**: Supports [[ToolUse|tool use]] for agentic task automation (GA May 2024)
- **Fine-tuning**: Supports fine-tuning in [[AmazonBedrock]] with custom training data
- **Context Length**: Up to 32K tokens for fine-tuned versions
- **Data Formats**: Text-based fine-tuning (vision capabilities planned)

## Fine-tuning Capability

As of July 2024, Claude 3 Haiku can be fine-tuned in [[AmazonBedrock]] to improve performance for domain-specific tasks:

- **Training Method**: Prepare high-quality prompt-completion pairs
- **Benefits**: Improved accuracy, consistency, reduced inference tokens
- **Use Case Example**: Comment moderation (81.5% → 99.6% accuracy, 85% token reduction)
- **Availability**: US West (Oregon) AWS Region (preview July 2024, generally available November 2024)

## Enterprise Adoption

- [[SKTelecom]]: Fine-tuned for customer support workflows (73% increase in positive feedback)
- [[ThomsonReuters]]: Plans to fine-tune for legal, tax, accounting, and compliance expertise

## Related

- [[Claude3]] — parent model family
- [[Claude3.5Haiku]] — next generation of the Haiku family
- [[Anthropic]] — creator of Claude 3 Haiku
- [[ToolUse]] — agentic capability supported by Claude 3 Haiku
- [[AmazonBedrock]] — AWS service offering Claude 3 Haiku with fine-tuning and distillation
- [[FineTuning]] — model customization capability
- [[ModelDistillation]] — knowledge transfer technique using Claude 3 Haiku as student model
- [[Intuned]] — browser automation platform using Claude 3 Haiku with tool use
- [[Hebbia]] — financial/legal services platform using Claude 3 Haiku with tool use
- [[SKTelecom]] — fine-tuning adoption case study
- [[ThomsonReuters]] — fine-tuning adoption case study
- [[summary-2024-05-30 - Claude can now use tools]] — Tool use GA announcement featuring Haiku
- [[summary-2024-07-10 - Fine-tune Claude 3 Haiku in Amazon Bedrock]] — Fine-tuning announcement
