---
title: "Cross-Content Modeling"
type: concept
tags: [embeddings, representation-learning, spotify, personalization, multimodal]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify.md"]
last_updated: 2026-06-30
---

## Definition

Cross-content modeling is the practice of embedding different content types (users, tracks, podcast episodes, audiobooks) into a shared embedding space, enabling the model to learn relationships across modalities and place users in context with the content they consume.

## Key Information

- **Shared Embedding Space**: Users, tracks (music), and episodes (podcasts) are all embedded as points in the same high-dimensional space, typically on a hypersphere
- **Visualization**: On a hypersphere, a user's embedding sits near the content they listen to — e.g., a machine learning engineer's embedding clusters near tech podcasts and ML-related content
- **Neighborhood Exploration**: The shared space allows exploring what content is "close" to a user, what is not, and how users relate to each other through content proximity
- **Enables**: Recommendations that cross content type boundaries (e.g., recommending a podcast to a music listener based on shared semantic space)
- **Transformer-Based**: Spotify's newer models use transformers to learn these cross-content embeddings, moving beyond earlier autoencoder approaches
- **Contextual**: The embedding of a user changes based on their interaction history, placing them in different regions of the space at different times

## Related

- [[summary-20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify]] — source
- [[Spotify]] — company
- [[User Embeddings]] — the user-side vectors in the shared space
- [[Semantic IDs]] — how content vectors are tokenized for LLMs
- [[Soft Tokenization]] — how user vectors are projected into LLM space
- [[Generative Recommender Systems]] — the paradigm enabled by cross-content understanding
