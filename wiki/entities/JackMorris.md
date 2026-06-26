---
title: "JackMorris"
type: entity
tags: [person, ai, researcher, fine-tuning, weights]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Jack Morris is an AI researcher and PhD candidate who researches knowledge injection into language models via weight updates. He argues that training information into model weights is superior to context stuffing and RAG for long-term knowledge retention. He has since started a company focused on building models that can be taught new knowledge.

## Key Information
- Conducted research on embedding inversion, demonstrating that 90% of text can be recovered from vector database embeddings, eliminating security benefits of vector databases
- Developed contextual embedding models that dynamically adjust embeddings based on surrounding documents, improving retrieval on niche/long-tail data
- Argues that models have fixed capacity (~3.6 bits per parameter) and waste it on irrelevant facts like obscure geographic trivia
- Advocates for synthetic data generation as the key enabler for weight-based knowledge injection
- Started a company in San Francisco focused on building teachable models
- Presented at the AI Engineer Summit (aiDotEngineer) on November 22, 2025

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[EmbeddingInversion]] — his PhD research
- [[ContextualEmbeddings]] — his research on adaptive embeddings
- [[SyntheticContinuedPreTraining]] — key technique he advocates
- [[ParameterEfficientFineTuning]] — approach he explores
- [[NeuralFileSystem]] — concept he coined
