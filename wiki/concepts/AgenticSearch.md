---
title: "AgenticSearch"
type: concept
tags: [concept, rag, retrieval, ai-coding, terminal, ripgrep]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260219 - Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260521 - Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases).md"
last_updated: 2026-06-20
---

## Definition

Agentic search is retrieval in which an agent uses **tools to navigate and search data directly** — terminal commands (`ripgrep`, `glob`, `grep`, `sed`, `cat`), file-system navigation, and its own context window — instead of embedding chunks into a vector database. [[ColeMedin]] stresses it is **still [[RetrievalAugmentedGeneration|RAG]]** (it pulls external info into the LLM's context) — just *without* semantic/vector search. It's what the best coding agents shifted to as a replacement for traditional RAG over codebases.

## Key Information

### Why it beats traditional RAG for code

Code is **structured data**, which makes vector search unnecessary:

- **Exact identifiers + perfect spelling** → keyword/regex search works; no need to match synonyms or concepts.
- **File-structure organization** → file-navigation tools let the agent hone in on the right folder/file.
- **Terminal-native** → agents live in the shell and can use powerful built-in tools (ripgrep, glob).
- **No index to maintain** → a codebase index is another pipeline, and code changes too often to keep an index in sync (unlike slow-changing document knowledge bases). Not needing one is "a beautiful thing."

Cole also argues a directed tool search (e.g. ripgrep) is often *more focused* than pulling fuzzy vector chunks, which can confuse the LLM more than help.

### Variants in the wild

- **[[ClaudeCode]]**: started with a local vector DB, moved to agentic search (per maintainer **Boris Cherny**); now wraps `grep`/`sed`/`cat` behind a search tool.
- **Cline**: co-creator **Nick** no longer recommends RAG for autonomous coding agents ("mind virus").
- **Aider**: uses **tree-sitter** to inject a high-level repo map (files, core classes/functions) into the system prompt — an index *without* a vector DB.

### The limit: cost at scale

Agentic search is slow and expensive over *large unstructured* knowledge bases — running many grep/cat calls and reading whole documents. For those, traditional RAG (small targeted chunks) is roughly **~100× cheaper**. So agentic search wins for structured code; semantic RAG wins for large seas of unstructured text.

For very large *codebases* specifically (~6-digit LOC+), even grep gets slow and token-inefficient — so Cole complements agentic search with **LSP (Language Server Protocol) exposed via an MCP server** for symbol-level navigation (go-to-definition, find-references). Not a replacement — a directed complement. See [[LargeCodebaseStrategies]].

### The bridge

Give an agent **both** modes and let it choose *what* and *how* to search per query (regex/agentic for exact matches; semantic/vector when concepts must match). Still RAG — just smarter retrieval. See [[RetrievalAugmentedGeneration]].

## Related

- [[RetrievalAugmentedGeneration]] — the umbrella; agentic search is a non-vector form of it
- [[ClaudeCode]] — moved from vector RAG to agentic search
- [[ColeMedin]] — articulator
- [[Archon]] — its RAG-for-coding purpose is what agentic search displaces
- [[summary-is-rag-dead-for-coding]] — primary source
- [[cole-medin-rag-playbook]] — the broader RAG playbook