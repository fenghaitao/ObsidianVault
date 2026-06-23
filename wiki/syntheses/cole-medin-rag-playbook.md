---
title: "cole-medin-rag-playbook"
type: synthesis
tags: [synthesis, analysis, rag, retrieval, playbook]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff).md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-20
---

# Cole Medin's Complete RAG Playbook

A consolidated view of everything [[ColeMedin]] teaches about [[RetrievalAugmentedGeneration]] across the corpus — the strategies, the tooling, the cost controls, and his actual recommendations.

## The one-line thesis

**Don't build "basic RAG."** Vanilla chunk-and-embed fails ~10% of the time ([[Anthropic]]'s data). Stack 3-5 strategies and you drop failure to under 3%. The hard part isn't the LLM call — it's the *pipeline* (getting documents in, chunked well, with metadata).

## Cole's recommended starter combo

From [[summary-20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff)]], if you do nothing else, combine these three:

1. **[[Reranking]]** — "the first strategy I use for almost every RAG implementation." Retrieve many candidates, a cross-encoder returns the best few. Avoids overwhelming the LLM ([[ContextRot]]).
2. **Agentic RAG** — let the agent choose how to search (semantic vs. full-doc fetch) per query.
3. **Context-aware chunking** — split at natural boundaries. Cole's library: **Docling** (hybrid chunking).

## The full strategy menu (11 strategies)

Production systems combine 3-5. The complete survey lives in [[RetrievalAugmentedGeneration]]; the highlights:

| Strategy | When to reach for it |
|---|---|
| [[Reranking]] | Almost always — cheap accuracy win |
| Agentic RAG | When you have clear instructions for *how* to search differently |
| Knowledge Graph RAG | Highly interconnected data; entity-relationship queries (lib: Graphiti) |
| [[ContextualRetrieval]] | The single biggest accuracy win (-35% failures alone) |
| [[HybridSearch]] | Rare terms, proper nouns, exact-match needs |
| Query Expansion / Multi-Query | Improve recall by rewriting/multiplying the query |
| Context-Aware / Late / Hierarchical chunking | Better data-prep; preserve document structure |
| Self-Reflective RAG | Self-correcting search loop (grade, retry) |
| Fine-Tuned Embeddings | Domain-specific gains (5-10%); needs training data |

## The crown jewel: Contextual Retrieval

[[ContextualRetrieval]] (from [[Anthropic]]) is the strategy Cole spends the most time on. Prepend each chunk with 1-2 LLM-generated sentences positioning it within its source document. A bare chunk ("Progress is 72% complete") becomes useful once it's prefixed with what it's about. Result: ~35% fewer retrieval failures from this technique alone.

The cost concern (running an LLM call per chunk, each containing the whole document) is solved by [[PromptCaching]] — ~50% cheaper on [[OpenAI]], ~90% on [[Anthropic]]/Gemini — plus using a cheap model (GPT-4o-mini class) for the context-generation step.

## The tooling stack

| Layer | Cole's choice | Notes |
|---|---|---|
| Vector DB | [[Supabase]] or [[Neon]] (`pgvector`) | Interchangeable; both Postgres. Neon adds serverless autoscaling + branching. |
| Chunker | Docling (hybrid chunking) | His current favorite |
| Knowledge graph | Graphiti | For graph RAG |
| Reusable RAG server | [[Crawl4AIRAG]] | Cole's open-source MCP — crawls docs, contextual-retrieval baked in |
| Prototyping surface | [[N8N]] | Visualize the pipeline before porting to Python |
| Embedding model | OpenAI `text-embedding-3-small` | Default in his demos |

## How RAG fits into AI coding

In [[summary-20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)]], RAG is one of Cole's three must-have MCP server categories: **documentation RAG** ([[Crawl4AIRAG]] or Context7) lets the AI IDE query framework docs while coding, so it stops hallucinating APIs. Paired with Brave (web search) — query private docs first, fall back to web for examples.

[[Archon]] uses RAG internally over the [[PydanticAI]] docs to ground its code generation, and Cole plans to move it onto [[Crawl4AIRAG]].

## The big caveat: RAG vs. the Wiki pattern

There's a genuine tension in this knowledge base. The [[KarpathyLLMWiki]] pattern (which *this vault* implements) is explicitly *anti*-RAG — compile knowledge into persistent wiki pages rather than retrieve chunks at query time. Karpathy: "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files."

Reconciliation (per [[RetrievalAugmentedGeneration]]'s Knowledge-Conflicts section): the two are compatible at different layers — **RAG for ephemeral retrieval over high-volume reference material; the Wiki pattern for distilled, reusable, compounding knowledge.** Cole uses both: RAG inside Archon for doc-grounding, the Wiki pattern for his [[SecondBrain]].

## Related

- [[RetrievalAugmentedGeneration]] — the full strategy survey
- [[ContextualRetrieval]] — the crown-jewel strategy
- [[Reranking]], [[HybridSearch]] — top stacking strategies
- [[PromptCaching]] — makes contextual retrieval economical
- [[Crawl4AIRAG]] — Cole's open-source RAG MCP
- [[Neon]], [[Supabase]] — vector DB options
- [[KarpathyLLMWiki]] — the anti-RAG counterpoint this vault uses
- [[ColeMedin]] — the playbook's author
