---
title: "summary-20260408 - OpenRAG： An open-source stack for RAG — Phil Nash"
type: source
tags: [source, transcript, rag, open-source, ibm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - OpenRAG： An open-source stack for RAG — Phil Nash.md"]
last_updated: 2026-06-30
---

## Core Summary

Phil Nash from IBM presents OpenRAG, an open-source RAG stack combining Docling (document processing), OpenSearch (hybrid vector+keyword search with JVector), and LangFlow (visual orchestration). RAG isn't dead — it's hard and complex. OpenRAG provides an opinionated but extensible baseline with agentic retrieval.

## Key Points

- "RAG is dead" claims ignore that most businesses have more than a million tokens of data and can't afford per-query million-token costs.
- OpenRAG stack: Docling (document parsing with layout analysis, table extraction, OCR, VLM pipeline) → OpenSearch (JVector KNN plugin for disk-based indexing, hybrid search) → LangFlow (drag-and-drop agentic retrieval).
- Docling handles PDFs, HTML, Word, slides, audio/video via multiple pipelines including Granite Docling 258M VLM.
- Agentic retrieval: agent decides what searches to perform with tools, rather than naive top-K chunk retrieval.
- Fully offline-capable: all components run locally, no external services needed.
- JVector enables live indexing and disk-based KNN — entire index doesn't need to fit in memory.

## Related

- [[Phil Nash]] — speaker, IBM developer relations
- [[IBM]] — company
- [[OpenRAG]] — open-source RAG stack
- [[Docling]] — document processing
- [[OpenSearch]] — search engine
- [[LangFlow]] — visual orchestration
- [[JVector]] — vector index
- [[Agentic Retrieval]] — search paradigm
