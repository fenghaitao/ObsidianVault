---
title: "NeuralFileSystem"
type: concept
tags: [weights, knowledge, llm, memory, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Neural File System is a concept coined by Jack Morris describing the idea of storing knowledge directly in model weights rather than in external retrieval systems. It contrasts with Andrej Karpathy's characterization of embeddings as "the file system of LLMs" — Morris argues weights, not embeddings, are the file system of the future.

## Key Information
- Contrasts with Karpathy's "embeddings are the file system of LLMs" from his OS-for-LLMs diagram
- Morris argues embeddings are "the file system of today" but not the future
- The core idea: train all relevant data into model weights so the model knows it natively without needing retrieval
- Enables zero-prompt inference — the model implicitly knows which document is being asked about
- Trade-off: expensive at training time but cheap at inference time (opposite of deep research / agentic RAG)
- Requires synthetic data generation and parameter-efficient methods to be practical
- Part of a broader vision where each user/company has their own fine-tuned model with domain-specific knowledge baked in

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[JackMorris]] — coined the term
- [[AndrejKarpathy]] — coined the contrasting "embeddings as file system" concept
- [[ParameterEfficientFineTuning]] — enabling technique
- [[SyntheticContinuedPreTraining]] — enabling technique
