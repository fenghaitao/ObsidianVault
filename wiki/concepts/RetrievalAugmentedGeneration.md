---
title: "RetrievalAugmentedGeneration"
type: concept
tags: [concept, rag, retrieval, vector-search, llm]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260219 - Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260326 - Everything You Thought About Building AI Agents is Wrong.md"
last_updated: 2026-06-20
---

## Definition

Retrieval-Augmented Generation (RAG) is a pattern where an LLM's response is grounded by retrieved external documents, rather than relying purely on the model's training data. The standard pipeline: ingest documents → split into chunks → embed each chunk into a vector → store in a vector database → at query time, embed the user's question, fetch the nearest-neighbor chunks, and prepend them to the LLM prompt.

## Key Information

### "Is RAG dead?" — the structured-vs-unstructured distinction

Per `summary-is-rag-dead-for-coding`, the "RAG is dead" narrative conflates two things. What's dying is **traditional RAG** (chunk → embed → vector DB → semantic nearest-neighbor), and only **for code** — because code is *structured* (exact identifiers, perfect spelling, file-structure organization, terminal tools). There, agents use **[[AgenticSearch]]** (ripgrep/glob/file navigation) instead — which is *still RAG* (it pulls external info into context), just without a vector DB.

But for **unstructured** data (Drive/SharePoint/SQL seas of text), traditional semantic RAG is essential: only embeddings catch **synonyms and conceptually-similar** passages (Cole's example: "Star Wars spaceships" won't keyword-match X-wing / TIE fighter / Millennium Falcon). 

| Axis | Structured (code) | Unstructured (docs) |
|---|---|---|
| Retrieval | [[AgenticSearch]] (grep/glob) | Traditional semantic RAG |
| Why | exact match, file structure, changes often (index hard to sync) | need synonym/concept matching across millions of docs |
| Cost at scale | slow/expensive over big corpora | ~100× cheaper (small targeted chunks) |

Industry evidence: **Boris Cherny** (Claude Code) — early Claude Code used a local vector DB, moved to agentic search; **Nick** (Cline co-creator) — RAG-for-coding is a "mind virus"; **Aider** — tree-sitter repo map in the system prompt (an index without a vector DB). **The bridge**: give the agent both modes and let it decide *what* and *how* to search per query. Bottom line: "for coding, RAG is dead; for everything else, definitely not."

### The broader arc: small-corpus file search vs large-corpus RAG → agentic RAG

Per `summary-sdk-vs-framework-agents`, the same nuance generalizes beyond coding:
- **2024** — RAG (semantic search) in nearly every agent.
- **2025** — file search rose; a **LlamaIndex** study showed **file search outperforms RAG for *small* corpuses**, and coding agents dropped vector DBs for grep (now built into the SDKs).
- **But large knowledge bases** (thousands of docs) — semantic search is still **more accurate and far cheaper** than reading/searching everything.
- **2026 middle ground — agentic RAG**: give the agent *both* semantic and grep/keyword search and let it choose per query; **Graph RAG** for massive or multi-codebase projects. RAG remains necessary for most *non-coding* agents and enterprise coding — even SDK agents add semantic search back via [[ClaudeSkills|skills]]/MCP.

### Standard pipeline

```
Documents → Chunker → Embedder → Vector DB
                                    ↑
User query → Embedder → Vector DB ──┘
              → top-K chunks → prepended to LLM prompt → answer
```

### RAG in Archon (specific use)

[[Archon]] uses RAG to keep its [[PydanticAI]] (and, in v7+, [[LangGraph]]) code generation grounded in current framework docs:

- Documentation is crawled and chunked.
- Chunks are embedded and stored in [[Supabase]] with `pgvector`.
- The Coder agent, when generating code for a user request, retrieves the most relevant doc chunks and uses them to ground the generated code (avoids hallucinating API surfaces that don't exist).

This is the difference Cole highlights between [[Windsurf]]'s `@PydanticAI` doc retrieval (basic RAG with general-purpose embeddings) and Archon's curated RAG (deeper chunking, framework-specific configuration).

### The 11-strategies survey (Cole's Nov 2025 deep dive)

In `summary-every-rag-strategy-explained`, [[ColeMedin]] surveys 11 distinct RAG strategies. Production systems typically combine 3-5. His starter combo: **Reranking + Agentic RAG + Context-Aware Chunking** (specifically hybrid chunking via the **Docling** library).

| # | Strategy | Essence | Cost |
|---|---|---|---|
| 1 | **Reranking** | Pull big candidate set, rerank with cross-encoder, return top few | Slight latency + small model |
| 2 | **Agentic RAG** | Agent picks search method (semantic, full-doc fetch, etc.) per query | More LLM calls; less predictable |
| 3 | **Knowledge Graph RAG** | Entities/relationships in graph DB alongside vectors | Slow + expensive ingest |
| 4 | **[[ContextualRetrieval]]** | Per-chunk LLM context prepended at ingest | Per-chunk LLM (mitigated by [[PromptCaching]]) |
| 5 | **Query Expansion** | LLM rewrites query before search | One extra LLM per query |
| 6 | **Multi-Query RAG** | LLM generates N variants, parallel search | N retrievals + LLM call |
| 7 | **Context-Aware Chunking** | Split at natural boundaries (embedding-found) | Higher ingest complexity |
| 8 | **Late Chunking** | Embed whole doc first, chunk the embeddings | Most complex |
| 9 | **Hierarchical RAG** | Parent-child chunk metadata; search small, return big | Variant of agentic RAG |
| 10 | **Self-Reflective RAG** | LLM grades retrieved chunks, retries if low | Extra LLM per search |
| 11 | **Fine-Tuned Embeddings** | Train domain-specific embedding model | 5-10% accuracy gain; training data + infra |

Key libraries Cole names:
- **Docling** — hybrid chunking (Cole's go-to chunker).
- **Graphiti** — knowledge graph library Cole uses.

### Advanced techniques on Archon's roadmap (v12)

Cole calls out these as planned improvements:

| Technique | Purpose |
|---|---|
| **Hybrid search** | Combine vector similarity with keyword (BM25) search for better recall on rare terms |
| **Reranking** | Take top-K from initial retrieval, then re-rank with a stronger model |
| **Query decomposition** | Split a complex query into sub-queries, retrieve for each, merge |
| **Hierarchical chunking** | Multi-level chunks (sentence + paragraph + section) for context-appropriate retrieval |

### [[ContextualRetrieval]] — Anthropic's accuracy enhancement

The most impactful single addition to a basic RAG pipeline. Each chunk is augmented at ingest time with 1-2 sentences of LLM-generated context positioning it within its source document. Anthropic's data: contextual embedding alone reduces retrieval failure ~35%; combined with hybrid search and reranking, drops failure rate from ~10% to under 3%.

Cost mitigated via [[PromptCaching]] (the document repeats across every chunk's prompt — providers cache it, ~50-90% cheaper depending on provider) and small models (GPT-4o-mini class is sufficient for the context-generation step).

Cole has implementations in two places:
- [[N8N]] workflow demonstrating the pattern visually.
- [[Crawl4AIRAG]] — his open-source MCP server's `generate_contextual_embeddings` Python function.

See the [[ContextualRetrieval]] page for the full pattern, prompt template, and evaluation data.

### Cole's broader stance: RAG as data-engineering problem

A recurring theme across Cole's content (echoed in the Vectorize sponsor segment in video 1): the hard part of RAG isn't the LLM call — it's the **pipeline**. Getting documents from where they live (Drive, GitHub, Notion, etc.) into a usable vector store with proper chunking and metadata is where most projects fail or burn time.

### Vector DB choices Cole references

- **[[Supabase]]** — Archon's default. Postgres-friendly, free, self-hostable. Uses `pgvector`.
- **[[Neon]]** — serverless Postgres alternative; same `pgvector` extension. Sponsored mention but Cole has used it for production demos.
- **Qdrant** — faster than Supabase, also self-hostable.
- **Pinecone** — serverless, very fast, not open source.
- **Weaviate**, **Chroma** — also mentioned as popular options.

## Knowledge Conflicts

> **RAG vs. agent-side reading.** The Karpathy-style LLM-Wiki philosophy underpinning this knowledge base is *opposed* to vanilla RAG (it favors "compile knowledge once into structured wiki pages"). Cole's use of RAG inside Archon, however, is for ephemeral framework-doc grounding during code generation — a different use case. The two views are compatible: use RAG for ephemeral retrieval over high-volume reference material; use compiled wiki pages for distilled, reusable knowledge.

## Related

- [[Archon]] — uses RAG over PydanticAI docs
- [[AgenticSearch]] — the non-vector RAG coding agents use instead (for structured code)
- [[Crawl4AIRAG]] — Cole's open-source RAG MCP server with [[ContextualRetrieval]] built in
- [[ContextualRetrieval]] — Anthropic's accuracy enhancement; biggest single win
- [[Supabase]] — Archon's vector DB backend
- [[Neon]] — alternative serverless Postgres backend
- [[PydanticAI]] — the framework whose docs are RAG-indexed
- [[N8N]] — visual surface where Cole prototypes RAG pipelines
- [[ColeMedin]] — frequent advocate of robust RAG pipelines
- [[ToolUse]] — agents can also expose RAG as a tool rather than building it into the prompt
- [[summary-20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)]] — the contextual-retrieval walkthrough
- [[summary-20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)]] — RAG as part of the AI-coding MCP triad
- [[summary-20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff)]] — the 11-strategies survey
- [[cole-medin-rag-playbook]] — synthesis: Cole's consolidated RAG playbook (strategies, tooling, cost controls)
- [[summary-20260219 - Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)]] — the "RAG is dead?" structured-vs-unstructured resolution
- [[summary-20260326 - Everything You Thought About Building AI Agents is Wrong]] — small-corpus file search vs large-corpus RAG; agentic RAG
