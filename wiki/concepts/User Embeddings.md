---
title: "User Embeddings"
type: concept
tags: [personalization, recommender-systems, spotify, representation-learning, embeddings]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify.md"]
last_updated: 2026-06-30
---

## Definition

User embeddings are vector representations that compress a user's entire interaction history (across sessions and years) into a dense numerical vector. At Spotify, the User Representations team builds these embeddings daily for 1B+ users, and they serve as the foundational input for all downstream recommendation models.

## Key Information

- **Purpose**: Represent a user's taste and preferences holistically, capturing patterns across all content types (music, podcasts, audiobooks)
- **Architecture**: Historically built using autoencoder models that compress user features into a small vector and then reconstruct features from it — the compression-decompression process forces the model to learn meaningful representations
- **Scale at Spotify**: Embeddings generated daily for 1B+ users (including non-MAUs); massive and expensive pipeline
- **Evolution**: Moving from generalized autoencoder-based representations to sequential transformer-based models that treat user interaction history as part of the prompt (context engineering on the modeling side)
- **Foundation Role**: User embeddings become the input to all downstream models — ranking, search, recommendations across all product surfaces
- **Cross-Content Modeling**: Newer models embed users, tracks, and episodes in the same space, enabling cross-content relationships to be visualized on a hypersphere
- **Soft Tokenization**: User embeddings can be projected into an LLM's token space as a "soft token," enabling personalized generation without training the LLM on every individual user

## Related

- [[summary-20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify]] — source
- [[Spotify]] — company
- [[Shivam Verma]] — Tech Lead of User Representations team
- [[Semantic IDs]] — complementary concept for content representation
- [[Soft Tokenization]] — technique for injecting user embeddings into LLMs
- [[CrossContent Modeling]] — embedding users and content in shared space
- [[Generative Recommender Systems]] — downstream application
- [[Autoencoders]] — related architecture used historically
- [[Foundation Models]] — broader model class
