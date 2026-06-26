---
title: "SyntheticContinuedPreTraining"
type: concept
tags: [fine-tuning, synthetic-data, training, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Synthetic Continued Pre-Training is a technique where a small domain-specific dataset is expanded into a large, diverse synthetic training dataset using an LLM, which is then used to fine-tune a model. This breaks the conventional ML paradigm that small datasets inevitably lead to overfitting.

## Key Information
- Originated from Stanford researchers who needed to teach models domain knowledge without breaking base capabilities
- The key insight: LLMs can generate training data that is good enough to train themselves on — a capability that only recently became viable
- Process: extract entities from small source data → generate large, diverse synthetic dataset → fine-tune model on synthetic data
- At ~100M to ~1B tokens of synthetic data, models can outperform GPT-4 on domain-specific tasks
- Direct fine-tuning on raw data (without synthetic expansion) causes the model to memorize exact sentences and fail on any slightly different questions
- Related techniques include: Active Reading (LLM decides what to generate), Self-Study (model quizzes itself), Rephrasing the Web (rephrasing entire pre-training data)
- SEAL (Self-Adapting Language Models) takes this further by having the model decide what data to generate to improve itself
- Andrej Karpathy demonstrated this approach by generating diverse training examples to teach a small LLM about himself

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[Datalogi]] — company specializing in this
- [[CatastrophicForgetting]] — the problem this technique helps avoid
- [[ParameterEfficientFineTuning]] — complementary approach
- [[AndrejKarpathy]] — demonstrated the technique
