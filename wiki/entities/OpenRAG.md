---
title: "OpenRAG"
type: entity
tags: [project, ibm, rag, open-source, agentic-retrieval]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - OpenRAG： An open-source stack for RAG — Phil Nash.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM.md"]
last_updated: 2026-06-30
---

## Definition
OpenRAG is an open-source RAG (Retrieval-Augmented Generation) stack developed at IBM that combines Docling for document processing, OpenSearch for search and indexing, and LangFlow for visual orchestration and agents. It provides an opinionated but extensible baseline for building RAG systems with agentic retrieval.

## Key Information
- **Version**: 0.4.0 (as of April 2026)
- **Components**: Docling (document processing), OpenSearch (search/indexing), LangFlow (visual orchestration/agents)
- **Frontend**: Next.js application; **Backend**: Python
- **Retrieval approach**: Agentic — an agent decides what searches to perform rather than single-shot embedding-to-search
- **Search**: Hybrid vector + keyword search via OpenSearch with JVector KNN plugin for disk-based live indexing
- **Embeddings**: Supports OpenAI, What's Next AI, Ollama; can run entirely offline in air-gap situations
- **Cloud connectors**: Sync documents from Google Drive, SharePoint, OneDrive (requires Google OAuth)
- **Customizability**: Edit agent flows directly in LangFlow; add guardrails, tools, and custom components
- **API**: Exposes API keys for programmatic access; also provides an MCP server for agent-to-agent communication
- **Enterprise focus**: Deploys in private, data-sensitive environments with a strong security harness

## Related
- [[summary-20260408 - OpenRAG： An open-source stack for RAG — Phil Nash]] — source
- [[summary-20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM]] — source (enterprise security harness)
- [[IBM]] — develops the project
- [[Phil Nash]] — presenter
- [[Docling]] — document processing component
- [[OpenSearch]] — search and indexing component
- [[LangFlow]] — visual orchestration component
- [[JVector]] — vector index plugin
- [[Granite]] — IBM models used in the stack
- [[Ollama]] — local model hosting
- [[Agentic Retrieval]] — search paradigm
- [[Hybrid Search]] — search approach
- [[OpenRAG]] (concept) — the conceptual framework
