---
title: "Amazon Bedrock"
type: entity
tags: [aws, amazon, cloud, foundation-model, managed-service, enterprise-ai]
sources: ["raw/01-articles/claude/2023-08-23 - Claude 2 on Amazon Bedrock.md", "raw/01-articles/claude/2023-09-28 - Claude on Amazon Bedrock now available to every AWS customer.md", "raw/01-articles/claude/2024-07-10 - Fine-tune Claude 3 Haiku in Amazon Bedrock.md", "raw/01-articles/claude/2024-10-08 - Introducing the Message Batches API.md", "raw/01-articles/claude/2025-06-23 - Introducing Citations on the Anthropic API.md", "raw/01-articles/claude/2025-08-14 - Prompt caching with Claude.md", "raw/01-articles/claude/2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md"]
last_updated: 2026-07-04
---

# Amazon Bedrock

Amazon Bedrock is a fully managed AWS service that makes leading foundation models accessible via an API, enabling businesses to build and scale generative AI applications without managing underlying infrastructure.

## Key Information

- Provider: Amazon Web Services (AWS)
- Type: Fully managed foundation model API service
- Launched: April 2023
- Purpose: Lower the barrier for enterprises to adopt and deploy large language models
- Initial models at launch: Claude 1.3, Claude Instant (among the first), plus other foundation models
- Claude 2 availability: Added August 2023
- General availability (GA) to every AWS customer: announced September 28, 2023, expanding from the April 2023 preview.

## Role in the Claude Ecosystem

[[Anthropic]] has been a key partner on Amazon Bedrock since its April 2023 launch. Claude models available on Bedrock:
1. Claude 1.3 (available at Bedrock launch, April 2023)
2. Claude Instant (available at Bedrock launch, April 2023)
3. [[Claude2]] (added August 2023)
4. [[Claude3Haiku]] (with [[FineTuning]] capability as of July 2024)
5. [[Claude3.5Haiku]] (with [[ModelDistillation]] capability and [[AWS]] Trainium2 optimization as of December 2024)

Claude models on Bedrock now support [[Citations]] (available June 30, 2025), enabling grounded responses with precise source citations.

[[PromptCaching]] is available in preview on Amazon Bedrock, enabling cost reductions up to 90% and latency reductions up to 85% for long-context applications.

[[Claude4Sonnet]] on Bedrock supports the **1M token [[ContextWindow]]** (public beta, August 2025), enabling processing of entire codebases and large-scale document synthesis in a single request.

## Enterprise Use Cases

Enterprise customers such as [[LexisNexis]], [[LonelyPlanet]], and [[RicohUSA]] adopted Claude 2 via Bedrock for:
- Legal document analysis (long context processing)
- Travel content generation
- Training data generation with compliance guarantees (HIPAA, SOC II)

At GA (September 2023), [[BridgewaterAssociates]] was highlighted building an Investment Analyst Assistant with Claude on Bedrock.

## Agents for Amazon Bedrock (2023)

Announced in preview alongside the September 2023 GA milestone, [[AgentsForAmazonBedrock]] lets Claude orchestrate API calls via AWS Lambda functions — breaking tasks into steps, holding clarifying conversations, and taking actions (e.g., updating orders in an e-commerce chat assistant), not just answering queries. Anthropic's team was instrumental in its development. Secure customization and fine-tuning of Claude on Bedrock were also announced as forthcoming at this time.

## Batch Inference (2024)

Customers using Claude on Amazon Bedrock can use [[MessageBatchesAPI|batch inference]] for asynchronous, non-time-sensitive processing, mirroring the discounted batch processing available on the direct Anthropic API (announced October 2024).

## Fine-Tuning Capability

As of July 2024, [[AmazonBedrock]] supports [[FineTuning]] of [[Claude3Haiku]]:
- Customers can train custom models with their own prompt-completion pairs
- Text-based fine-tuning with up to 32K token context length
- Available in US West (Oregon) AWS Region (preview July 2024, generally available November 2024)
- Vision capabilities planned for future

### Fine-Tuning Use Cases

- **SK Telecom**: Customer support automation (73% improvement in agent feedback)
- **Thomson Reuters**: Professional services AI (legal, tax, accounting, compliance expertise)
- **Comment Moderation**: 81.5% → 99.6% accuracy; 85% token reduction

## Model Distillation Capability

As of December 2024, [[AmazonBedrock]] supports [[ModelDistillation]] for [[Claude3Haiku]]:
- Automates knowledge transfer from [[Claude3.5Sonnet]] (teacher) to [[Claude3Haiku]] (student)
- Generates synthetic training data, handles training/evaluation, and manages deployment
- Enables frontier-level performance at lower cost for specific tasks
- Status: Preview (December 2024)

### Distillation Use Cases

- **Retrieval Augmented Generation (RAG)**: Execute RAG pipelines cost-effectively
- **Data Analysis**: Complex analysis at fraction of large model cost
- **High-volume Repetitive Tasks**: Specialized use cases at scale

## Trainium2 Optimization

As of December 2024, [[AmazonBedrock]] offers latency-optimized [[Claude3.5Haiku]] powered by [[AWS]] Trainium2 chips:
- **Performance**: Up to 60% faster inference speed
- **Deployment**: US East (Ohio) Region via cross-region inference
- **Pricing**: $1 per million input tokens, $5 per million output tokens
- **Use Cases**: Real-time inference, code completions, content moderation, chatbots
- **Status**: Public preview (December 2024)

## Related

- [[Anthropic]] — key model partner on Bedrock
- [[Claude2]] — Anthropic model available on Bedrock since August 2023
- [[Claude3Haiku]] — Claude model with fine-tuning support
- [[Claude3.5Haiku]] — latest Claude model with distillation and Trainium2 optimization
- [[Claude3.5Sonnet]] — teacher model for distillation capability
- [[FineTuning]] — model customization technique
- [[ModelDistillation]] — knowledge transfer technique available in Bedrock
- [[Citations]] — API feature for grounding responses in source documents, available on Bedrock
- [[LexisNexis]] — enterprise customer (legal AI)
- [[LonelyPlanet]] — enterprise customer (travel content)
- [[RicohUSA]] — enterprise customer (workplace solutions)
- [[SK Telecom]] — customer using fine-tuned Claude for support
- [[Thomson Reuters]] — customer planning to fine-tune Claude
- [[summary-2023-08-23 - Claude 2 on Amazon Bedrock]] — source article
- [[summary-2024-07-10 - Fine-tune Claude 3 Haiku in Amazon Bedrock]] — fine-tuning announcement
- [[summary-2024-12-03 - Claude 3.5 Haiku on AWS Trainium2 and model distillation in Amazon Bedrock]] — Trainium2 and distillation announcement
- [[PromptCaching]] — API feature available in preview on Bedrock
- [[Claude4Sonnet]] — Claude model with 1M context window available on Bedrock
- [[ContextWindow]] — 1M token window available for Claude Sonnet 4 on Bedrock
- [[summary-2025-08-14 - Prompt caching with Claude]] — prompt caching launch article noting Bedrock preview availability
- [[summary-2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context]] — 1M context window availability on Bedrock
- [[BridgewaterAssociates]] — enterprise customer (Investment Analyst Assistant)
- [[AgentsForAmazonBedrock]] — agent-orchestration feature announced alongside GA
- [[MessageBatchesAPI]] — batch inference available on Bedrock
- [[summary-2023-09-28 - Claude on Amazon Bedrock now available to every AWS customer]] — general-availability announcement
