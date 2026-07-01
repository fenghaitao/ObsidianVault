---
title: "Docling"
type: entity
tags: [tool, ibm, document-processing, open-source, pdf, rag]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - OpenRAG： An open-source stack for RAG — Phil Nash.md"]
last_updated: 2026-06-30
---

## Definition
Docling is an open-source document processing tool built by IBM Research Zurich that parses and processes PDFs, HTML, Word documents, slides, spreadsheets, audio, and video. It is the document ingestion component of the OpenRAG stack.

## Key Information
- Developed at IBM Research in Zurich
- Handles: PDFs, HTML, Markdown, Word documents, slides, spreadsheets, audio, video
- **Standard pipeline**: Small focused models for layout analysis, table extraction, image extraction and description; supports OCR backend for scanned documents
- **VLM pipeline**: Uses Granite Docling 258M vision language model for all-in-one extraction (newer, simpler)
- **ASR pipeline**: Automatic speech recognition for audio and video
- **Simple pipeline**: For straightforward text documents (Markdown, HTML, Word)
- Produces intermediate "DocTags" format (XML-ish) that models document structure
- DocTags can be converted to Markdown, HTML, JSON
- Includes a hierarchical chunker that uses document hierarchy for intelligent chunking
- Can run entirely offline in air-gap situations

## Related
- [[OpenRAG]] — uses Docling as ingestion component
- [[IBM]] — developed by IBM Research Zurich
- [[Granite]] — Granite Docling 258M vision model
- [[summary-20260408 - OpenRAG： An open-source stack for RAG — Phil Nash]] — source
- [[DocTags]] — intermediate representation format
- [[LangFlow]] — integrates Docling in visual flows
