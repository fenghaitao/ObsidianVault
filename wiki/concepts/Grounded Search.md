---
title: "Grounded Search"
type: concept
tags: [search, gemini, rag, citations, web]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Definition
Grounded Search is a Gemini API capability that performs web searches and returns answers with explicit source citations (URL, title, and snippets). It provides precise, sourced responses to queries, enabling deep research agents to gather information with verifiable provenance.

## Key Information
- **Gemini API feature**: Uses Google Search grounding to provide answers with sources
- **Output structure**: Returns answer text plus structured sources (URL, title, snippets)
- **Used in deep research**: The deep research tool in the Towards AI system wraps grounded search, saving results to a .memory folder
- **Prompt guidance**: The research prompt instructs the model to focus on official authoritative references and cite sources clearly
- **Source structuring**: Raw Gemini API sources are not in structured form, so the tool restructures them into a consistent format
- **Iterative gap-filling**: The agent uses grounded search results to identify knowledge gaps and runs additional targeted queries
- **Alternative to Perplexity**: The team previously used Perplexity but switched to Gemini with grounding for precise answers with sources

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[Gemini3]] — the model providing grounded search capability
- [[Deep Research Agent]] — system using grounded search as a core tool
- [[RAG]] — related retrieval technique
- [[GoogleDeepMind]] — developer of Gemini and grounded search
