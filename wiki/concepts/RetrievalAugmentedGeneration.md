---
title: "RetrievalAugmentedGeneration"
type: concept
tags: [rag, llm-technique, information-retrieval, inference-time, application-architecture]
sources: ["raw/01-articles/claude/2024-05-20 - Generate better prompts in the developer console.md", "raw/01-articles/claude/2025-06-23 - Introducing Citations on the Anthropic API.md"]
last_updated: 2026-06-28
---

## Definition

Retrieval Augmented Generation (RAG) is an application architecture pattern where an AI model generates responses enhanced by dynamically retrieving and incorporating relevant information from external sources at inference time. Unlike training-time augmentation, RAG allows applications to leverage current, domain-specific, or proprietary information without retraining the model.

## Key Information

- **Architecture pattern**: Combines a retriever (document/knowledge base search) with a generator (language model) in a single pipeline.
- **Timing**: Information retrieval happens at inference time, enabling real-time access to up-to-date or context-specific data.
- **Use cases**: Ideal for applications needing to ground responses in specific documents, knowledge bases, or enterprise data (e.g., customer history, legal documents, training datasets).
- **Development efficiency**: RAG applications can be built and brought to MVP quickly with effective prompt engineering, as demonstrated by [[ZoomInfo]]'s 80% reduction in prompt tuning time.
- **Quality vs. retraining**: Achieves high-quality outputs without the cost and complexity of fine-tuning or retraining models.

## Contrast with Citations

[[Citations]] and RAG are complementary approaches to grounding AI responses in external sources:

- **RAG**: System automatically retrieves relevant documents from a knowledge base/database at inference time based on the query. Good for open-ended search and exploration.
- **Citations**: User explicitly provides source documents; Claude grounds responses in those specific documents with precise citations. Better for verification and accountability when sources are known upfront.

Both approaches reduce hallucination and improve verifiability, but differ in how documents are selected.

## Related

- [[PromptEngineering]] — critical discipline for optimizing RAG system prompts
- [[Citations]] — alternative approach to grounding responses in external sources
- [[summary-2024-05-20 - Generate better prompts in the developer console]] — article featuring RAG case study
- [[ZoomInfo]] — company that successfully deployed RAG with Claude
- [[Anthropic]] — provider of Claude models used in RAG applications
