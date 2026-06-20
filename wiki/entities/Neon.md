---
title: "Neon"
type: entity
tags: [tool, database, postgres, serverless, vector-database, pgvector]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260226 - This One Command Makes Coding Agents Find All Their Mistakes (Use it Now).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260423 - Parallel Claude Code + Git Worktrees： This Setup Will Change How You Ship.md"
last_updated: 2026-06-20
---

## Definition

Neon is a serverless Postgres platform with `pgvector` support, used by [[ColeMedin]] as a vector-database backend for RAG agents — an alternative to [[Supabase]] that's also Postgres-under-the-hood. Became Cole's stated go-to for Postgres in his late-2025 content ("quickly becoming my go-to for Postgres").

## Key Information

### What distinguishes it

- **Serverless Postgres** — autoscaling infrastructure that adjusts to load, vs. paying for a fixed instance size and managing scaling yourself.
- **Database branching** — create/test schema changes in isolated branches (dev/test/prod), like git branches for your database. Cole also uses this for **end-to-end test-data isolation** (`summary-self-healing-e2e-validation`): branch the DB, let the agent create throwaway test users/records during validation, then delete the branch to keep the main DB clean. In [[ParallelAgenticDevelopment]] he takes it further — **one Neon branch per git worktree** (copying tables + data from main) so parallel agents get database isolation, not just code isolation (`summary-parallel-claude-code-worktrees`).
- **`pgvector`** — same vector-search extension as [[Supabase]], so RAG implementations are interchangeable between them (just swap the Postgres connection).
- **MCP server** — Neon ships a [[ModelContextProtocol]] server; the agent can create tables, manage records, run migrations via natural language while coding.

### Relationship to Supabase

Both run Postgres with `pgvector`, so for RAG purposes they're largely interchangeable. Cole historically defaulted to [[Supabase]] (and Archon uses it), but uses Neon in several RAG demos. Differences are operational: Neon's serverless autoscaling and branching vs. Supabase's broader BaaS feature set (auth, storage, etc.).

### Context

- Powers Vercel, Replit, and Highkey (per Cole's sponsor segment).
- A Neon co-founder has contributed to Postgres for 20+ years.
- Appears as a sponsored mention in Cole's RAG videos, but he uses it for genuine production demos including the [[ContextualRetrieval]] pipeline.

## Related

- [[Supabase]] — the interchangeable Postgres/pgvector alternative
- [[RetrievalAugmentedGeneration]] — what Cole uses Neon for
- [[ContextualRetrieval]] — implemented on Neon in Cole's demo
- [[ModelContextProtocol]] — Neon ships an MCP server (database-management slot)
- [[ColeMedin]] — advocate
- [[summary-easiest-strategy-for-accurate-rag]], [[summary-every-rag-strategy-explained]] — sources
- [[summary-self-healing-e2e-validation]] — Neon branching for test-data isolation
- [[summary-parallel-claude-code-worktrees]] — Neon branch per worktree (parallel-dev DB isolation)
