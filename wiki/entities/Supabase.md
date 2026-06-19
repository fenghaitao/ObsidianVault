---
title: "Supabase"
type: entity
tags: [tool, database, vector-database, postgres, rag]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

Supabase is an open-source Firebase alternative — managed Postgres with auth, storage, and (most relevant here) `pgvector`-based vector search built in. [[ColeMedin]] uses it as the default vector database backing [[Archon]]'s [[RetrievalAugmentedGeneration]] knowledge base.

> **Note on transcripts**: YouTube auto-captions consistently render "Supabase" as "Superbase". The actual product name is **Supabase**.

## Key Information

### Role in the playlist

- **Archon's RAG backend.** Archon ingests the [[PydanticAI]] documentation (and, in v7+, [[LangGraph]] documentation) into a Supabase Postgres table with `pgvector`. The Coder agent queries it during generation to ground code in current docs.
- **Default but swappable.** Archon's roadmap includes integrations with other vector DBs (Pinecone, Weaviate, Qdrant, Chroma) — Supabase is the default because it's free, self-hostable, and feels familiar to Postgres users.

### Why Cole picks it as the default

- Self-hostable (no required cloud account, fits the open-source ethos).
- Postgres familiarity — existing relational tools and SQL workflows still apply.
- Free tier sufficient for personal RAG use cases.
- `pgvector` integrates vector search naturally with relational data, simpler than running a dedicated vector DB.

### Other vector DBs Cole mentions in passing

| DB | Trade-off Cole cites |
|---|---|
| **Qdrant** | Faster than Supabase; self-hostable |
| **Pinecone** | Serverless, very fast, but not open source |
| **Weaviate** | Mentioned as a popular alternative |
| **Chroma** | Mentioned as another open-source option |

These are all on Archon's "future integrations" list but not yet implemented as of the playlist's recording.

## Related

- [[Archon]] — primary user of Supabase in this playlist
- [[ColeMedin]] — advocate for the choice
- [[RetrievalAugmentedGeneration]] — what Supabase backs in this stack
- [[PydanticAI]] — framework whose docs are stored in Supabase for RAG
