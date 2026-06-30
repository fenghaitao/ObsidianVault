---
title: "Catalog Understanding"
type: concept
tags: [recommender-systems, llm, content-representation, spotify, domain-adaptation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify.md"]
last_updated: 2026-06-30
---

## Definition

Catalog understanding is the process of teaching LLMs about a platform's content catalog — songs, artists, podcasts, episodes — so the model can reason about and recommend items. At Spotify, this is achieved by tokenizing content vectors into semantic IDs and fine-tuning open-weight LLMs on catalog data.

## Key Information

- **Two Knowledge Sources**: Platform knowledge (Spotify's content vectors — what Spotify knows about each item) combined with world knowledge (from open-weight LLMs like Llama and Qwen)
- **Semantic IDs as Bridge**: Content embedding vectors are compressed into 4-6 hierarchical semantic tokens, making them digestible by LLMs trained on text tokens
- **Training Process**: LLMs are post-trained (continually trained) on Spotify catalog data using semantic ID tokens, teaching the model to auto-regressively generate the next content item
- **Domain Adaptation**: This fine-tuning embeds Spotify-specific knowledge into the LLM, creating a model that understands both the world and Spotify's catalog
- **Benefits**: Steerability (natural language control), better recommendations (world knowledge + platform knowledge), and explainability (LLMs can explain why they recommended something)
- **Challenges**: Catastrophic forgetting — the model may lose some general capabilities when fine-tuned on domain-specific data
- **Production**: Combined with user embeddings and soft tokenization to form the full generative recommender pipeline

## Related

- [[summary-20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify]] — source
- [[Spotify]] — company
- [[Semantic IDs]] — the tokenization technique used
- [[User Embeddings]] — complementary user-side understanding
- [[Soft Tokenization]] — personalization layer on top
- [[Generative Recommender Systems]] — the full system
- [[Fine-tuning]] — the training approach
- [[Foundation Models]] — the base models being adapted
