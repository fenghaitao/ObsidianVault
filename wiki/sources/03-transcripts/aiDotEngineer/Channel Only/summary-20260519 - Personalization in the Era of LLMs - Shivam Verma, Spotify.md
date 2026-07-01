---
title: "summary-20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify"
type: source
tags: [source, transcript, spotify, personalization, llm, recommender-systems, user-modeling, semantic-ids]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify.md"]
last_updated: 2026-06-30
---

## Core Summary

Shivam Verma, Tech Lead of the User Representations team in Spotify's AI Foundation org, presents Spotify's approach to personalization in the era of LLMs. Spotify is moving from traditional multi-stage recommender systems (candidate generation + ranking) toward a single unified generative model with an LLM backbone. The talk covers three pillars: foundational user modeling (building user embeddings from interaction history), catalog understanding (teaching LLMs about content via semantic IDs), and steerable personalization (combining both with soft tokenization to create a personalized generative recommender system).

## Key Points

- **From Traditional to Generative Recs**: Spotify is shifting from siloed per-product models toward a single unified LLM-based recommender that users can steer via natural language.
- **User Modeling**: The User Representations team builds user embeddings — vectors compressing a user's entire interaction history across sessions — updated daily for 750M+ users. These embeddings serve as the foundation for all downstream recommendation models.
- **Cross-Content Modeling**: Newer models embed users, tracks, and podcast episodes in the same embedding space, enabling visualization of how users relate to different content types on a hypersphere.
- **Catalog Understanding via Semantic IDs**: Content vectors (tracks, episodes) are tokenized into 4-6 hierarchical semantic tokens, allowing LLMs to auto-regressively generate the next item (song or episode) — similar to how LLMs predict the next word.
- **Soft Tokenization for Personalization**: User embeddings are projected into the LLM's token space as a "soft token" that represents the user contextually, enabling personalized generation without training on every user.
- **Taste Profile**: A newly launched feature that exposes what Spotify knows about a user and lets them edit it via natural language, with edits feeding back into the generative model to improve recommendations.
- **AI DJ and Prompted Playlist**: Products that allow users to steer recommendations through conversation or natural language prompts (now also supporting podcast episode playlists).
- **Spotify Scale**: 750M+ MAUs, 100M+ tracks, 400K+ audiobooks, millions of podcasts, operating in 184 markets.

## Related

- [[Spotify]] — company
- [[Shivam Verma]] — speaker
- [[User Embeddings]] — concept
- [[Semantic IDs]] — concept
- [[Soft Tokenization]] — concept
- [[CrossContent Modeling]] — concept
- [[Generative Recommender Systems]] — concept
- [[Taste Profile]] — Spotify feature
- [[AI DJ]] — Spotify product
- [[Prompted Playlist]] — Spotify feature
- [[Discover Weekly]] — Spotify product
- [[Catalog Understanding]] — concept
- [[Autoencoders]] — related technique
- [[Foundation Models]] — broader model class
