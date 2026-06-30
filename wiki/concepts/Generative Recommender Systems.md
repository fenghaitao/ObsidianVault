---
title: "Generative Recommender Systems"
type: concept
tags: [recommender-systems, llm, personalization, spotify, generative-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify.md"]
last_updated: 2026-06-30
---

## Definition

Generative recommender systems are a paradigm shift from traditional multi-stage recommendation pipelines (candidate generation + ranking) to a unified model with an LLM backbone that auto-regressively generates the next recommended item — treating recommendations as a sequence generation problem similar to text generation.

## Key Information

- **Traditional Recs (Trad Recs)**: Multi-stage pipeline: massive catalog → candidate generation (millions → hundreds) → ranking (hundreds → final list). Each product surface (home, search, playlists, podcasts, ads) typically has its own team and model.
- **Generative Approach**: Single unified model with an LLM backbone that supports multiple product surfaces. The model auto-regressively generates the next item (song, episode) token by token, analogous to next-word prediction.
- **Three Components**:
  1. **User Context**: User embeddings representing interaction history, plus request context (query, product surface)
  2. **Content Tokens**: Items represented as semantic IDs (hierarchical tokens) that the LLM can process
  3. **Personalization**: User vectors projected into LLM token space as soft tokens
- **Steerability**: Users can influence recommendations via natural language (e.g., "play more Justin Bieber"), with edits feeding back into the model
- **Explainability**: LLMs provide natural language explanations for recommendations "for free"
- **Trade-offs**: Catastrophic forgetting when fine-tuning; limited training data means not every user is directly trained on (mitigated by collaborative filtering + soft tokenization)
- **Production at Spotify**: Already live for podcast episode recommendations; expanding to other surfaces

## Related

- [[summary-20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify]] — source
- [[Spotify]] — company pioneering this approach
- [[User Embeddings]] — user context component
- [[Semantic IDs]] — content tokenization component
- [[Soft Tokenization]] — personalization component
- [[Cross-Content Modeling]] — shared embedding space
- [[Taste Profile]] — user-facing steerability feature
- [[AI DJ]] — generative recs product
- [[Prompted Playlist]] — generative recs product
- [[Foundation Models]] — broader model class
