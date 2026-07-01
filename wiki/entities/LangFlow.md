---
title: "LangFlow"
type: entity
tags: [tool, visual-editor, orchestration, agents, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - OpenRAG： An open-source stack for RAG — Phil Nash.md"]
last_updated: 2026-06-30
---

## Definition
LangFlow is a drag-and-drop visual editor for AI flows. In the OpenRAG stack, it serves as the orchestration layer, integrating Docling and OpenSearch for ingestion and powering agentic retrieval on the generation side.

## Key Information
- Drag-and-drop visual editor for AI workflows
- Integrates Docling, OpenSearch, embedding models, and data enrichment into the ingestion pipeline
- Powers agentic retrieval on the generation side with tool-calling agents
- Supports multiple model providers: OpenAI, Anthropic, Ollama, What's Next AI
- Allows deep customization via "Edit in LangFlow" — users can unlock flows and add components (guardrails, parsers, custom tools)
- Supports MCP servers as tools within flows
- Components available include: guardrails, calculators, URL ingestors, prompt templates, chat input/output

## Related
- [[OpenRAG]] — uses LangFlow as the orchestration layer
- [[summary-20260408 - OpenRAG： An open-source stack for RAG — Phil Nash]] — source
- [[Docling]] — integrated document processor
- [[OpenSearch]] — integrated search engine
- [[Agentic Retrieval]] — paradigm powered by LangFlow
- [[Guardrails]] — component available in LangFlow
- [[MCP]] — protocol supported as tools
