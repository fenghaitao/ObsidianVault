---
title: "DocTags"
type: concept
tags: [document-processing, format, docling, intermediate-representation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - OpenRAG： An open-source stack for RAG — Phil Nash.md"]
last_updated: 2026-06-30
---

## Definition

DocTags is an XML-ish intermediate document representation format produced by Docling during document processing. It models the hierarchical structure of a document and can be converted to multiple output formats including Markdown, HTML, and JSON.

## Key Information

- Produced by Docling as an intermediate representation during document parsing
- Models document structure hierarchically
- XML-ish format
- Can be converted to Markdown, HTML, and JSON
- Docling's chunker uses the hierarchy in DocTags for intelligent, hierarchically-aware chunking

## Related

- [[Docling]] — produces DocTags
- [[summary-20260408 - OpenRAG： An open-source stack for RAG — Phil Nash]] — source
- [[OpenRAG]] — stack using Docling and DocTags
