---
title: "Semantic IDs"
type: concept
tags: [tokenization, recommender-systems, llm, spotify, content-representation, catalog]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify.md"]
last_updated: 2026-06-30
---

## Definition

Semantic IDs are hierarchical token representations of content items (tracks, episodes, artists) created by compressing high-dimensional content embedding vectors into a small number of discrete tokens (typically 4-6). They enable LLMs to auto-regressively generate recommendations — predicting the next song or episode — the same way LLMs predict the next word in text.

## Key Information

- **Origin**: Concept introduced in a Google paper a few years ago in the context of YouTube recommendations
- **How It Works**: A content vector (e.g., 1000-dimensional track embedding) is tokenized into 4-6 semantic tokens that form a hierarchical structure
- **Hierarchical Nature**: The first tokens capture broad categories (e.g., shared tokens for pop artists like Ariana Grande and Bruno Mars), while later tokens represent increasingly niche attributes
- **Purpose**: Allows LLMs to "speak" in content tokens — the LLM is post-trained (continually trained) on Spotify catalog data using semantic IDs, teaching it to auto-regressively generate the next content item
- **Integration with LLMs**: Semantic IDs replace text tokens in the training data; the model learns to predict the next semantic ID token (next song/episode) given user context and listening history
- **Domain Adaptation**: This is how Spotify teaches open-weight LLMs (Llama, Qwen, etc.) about its catalog — fine-tuning with semantic ID data embeds Spotify-specific knowledge into the model
- **Trade-off**: Catastrophic forgetting is a concern when fine-tuning LLMs with semantic ID data

## Related

- [[summary-20260519 - Personalization in the Era of LLMs - Shivam Verma, Spotify]] — source
- [[Spotify]] — company using semantic IDs
- [[User Embeddings]] — complementary user-side representation
- [[Soft Tokenization]] — technique for user-side tokenization
- [[Catalog Understanding]] — broader concept of teaching LLMs about content
- [[Generative Recommender Systems]] — the paradigm enabled by semantic IDs
- [[Tokenization]] — general concept of converting data to tokens
