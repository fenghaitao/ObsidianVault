---
title: "summary-is-rag-dead-for-coding"
type: source
tags: [source, original-material, rag, agentic-search, ai-coding]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260219 - Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead).md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] resolves the "RAG is dead" narrative with one key distinction: what's dying is **traditional RAG** (semantic/embedding/vector-DB chunk search) **for code specifically** — because code is highly *structured* — while [[RetrievalAugmentedGeneration|RAG]] in the broad sense (pulling any external info into context) is alive and well. The best coding agents have shifted to **[[AgenticSearch]]** (grep/glob/file-navigation in the terminal), which is *still RAG, just without a vector database*. For the majority of agentic use cases — unstructured knowledge bases — traditional semantic RAG remains essential.

## Key Points

- **Definitional fix**: "RAG is dead" really means *traditional/semantic RAG* (chunk → embed → vector DB → nearest-neighbor) is dead. But RAG = retrieval-augmented generation = grabbing *any* external info into the context window, so agentic terminal search is also RAG — a different kind.
- **It depends on your data's structure**:
  - **Structured (code)** → traditional RAG is dead. Code is perfectly spelled with exact identifiers/syntax (keyword/regex search works), organized by file structure (file-navigation tools), and lives in the terminal (ripgrep, glob). No need for embeddings/synonyms.
  - **Unstructured (Drive/SharePoint/SQL seas of text)** → traditional RAG is very much alive. You need the embedding model to find **synonyms and conceptually-similar** text buried across thousands/millions of docs. Cole's example: searching "Star Wars spaceships" won't keyword-match X-wing / TIE fighter / Millennium Falcon — only semantic similarity catches them.
- **Why coding agents dropped codebase indexing**: an index is *another pipeline to maintain*, and keeping a code index in sync is hard because **code changes far more often** than typical knowledge-base documents.
- **Industry evidence**:
  - **Boris Cherny** (Claude Code maintainer): early Claude Code used a local vector DB, but they found **agentic search generally works better** and moved away. (Claude Code now has a search tool that hides underlying `grep`/`sed`/`cat` calls.)
  - **Nick** (a Cline co-creator): article "*Why I no longer recommend RAG for autonomous coding agents*" — calls the RAG-for-everything narrative a "**mind virus**," a distraction for both the team and the agent.
  - **Aider**: uses **tree-sitter** to build a high-level repo map (files, core classes/functions) injected into the system prompt — an *index without a vector DB*.
- **Cost angle**: for *large* unstructured knowledge bases, traditional RAG is roughly **~100× cheaper** at scale — small targeted chunks vs. an agent reading whole documents via many grep/cat calls (which is slow/expensive). So chunking is a feature, not just overhead. (For small knowledge bases, maintaining a pipeline can be hard to justify.)
- **The bridge (where Cole is exploring)**: give the agent **both** retrieval modes and let it decide not just *what* to search but *how* — regex/agentic search for exact matches, semantic/vector search when concepts must be matched. Still RAG, just smarter retrieval; increasingly viable as LLMs and harnesses improve. Pair with accuracy strategies like **hierarchical RAG** so a few chunks suffice.
- **Bottom line**: "Is RAG dead? For coding, yes. For literally everything else, definitely not." (Customer support, compliance/legal, internal knowledge bases all still need semantic RAG.) This nuance is also why Cole is shifting [[Archon]]'s direction away from RAG-for-coding.

## Related

- [[RetrievalAugmentedGeneration]] — the pattern whose "death" is clarified
- [[AgenticSearch]] — what coding agents use instead (still RAG, no vector DB)
- [[ClaudeCode]] — moved from vector RAG to agentic search (Boris Cherny)
- [[Archon]] — vision shift away from RAG-for-coding
- [[cole-medin-rag-playbook]] — the consolidated RAG playbook this refines
