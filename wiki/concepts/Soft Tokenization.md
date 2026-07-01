---
title: "Soft Tokenization"
type: concept
tags: [personalization, llm, embeddings, spotify, recommender-systems]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify.md"]
last_updated: 2026-06-30
---

## Definition

Soft tokenization is a technique for personalizing LLM-based recommender systems by projecting user embedding vectors into the token space of the LLM. The projected vector becomes a "soft token" that represents the user contextually within the model, enabling personalized generation without needing to train the LLM on every individual user's data.

## Key Information

- **Motivation**: LLMs are trained on limited data and cannot be trained on every user (Spotify has 750M+ users). Collaborative filtering alone provides generalization, but personalization requires user-specific context.
- **How It Works**: A user embedding vector (from the user modeling pipeline) is projected via a learned transformation into the same dimensional space as the LLM's token embeddings. This projected vector is inserted into the prompt as a soft token.
- **Contextual**: The soft token is context-dependent — it changes based on which user is being served, enabling per-user personalization
- **Role in Pipeline**: The final piece of the puzzle — after user modeling (user embeddings) and catalog understanding (semantic IDs), soft tokenization combines both into a single steerable personalized generative recommender
- **Production Status**: Already productionized for podcast episode recommendations on Spotify as of May 2026
- **Advantage**: Gives the LLM "context on you" — whoever the recommendation is being generated for — without retraining the base model per user

## Related

- [[summary-20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify]] — source
- [[Spotify]] — company
- [[User Embeddings]] — the vectors being projected
- [[Semantic IDs]] — complementary content-side tokenization
- [[Generative Recommender Systems]] — the paradigm enabled by soft tokenization
- [[CrossContent Modeling]] — the shared embedding space that feeds into soft tokenization
