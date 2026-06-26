---
title: "URL Context"
type: concept
tags: [gemini, tool, retrieval, context, grounding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
URL Context is a Gemini feature that allows the model to incorporate content from specified URLs into its context window, described as "poor man's retrieval." It enables the model to ground outputs using publicly available web content with inline citations.

## Key Information
- Available as a toggleable tool in AI Studio
- Users provide a list of URLs, and the model incorporates their content into its context window
- Described by Paige Bailey as "poor man's retrieval" — simpler than setting up a vector database
- Provides inline citations to source URLs in model responses
- Demonstrated comparing and contrasting Genie 3 and Gemma 4 using blog posts published after training data cutoff
- Complements Vertex AI's custom document retrieval for internal documents
- "Get Code" provides Python/TypeScript/Java code to replicate URL context usage

## Related
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[AI Studio]] — platform where it's available
- [[Grounding with Google Search]] — complementary grounding feature
- [[Vertex AI]] — platform for internal document retrieval
- [[RAG]] — more sophisticated retrieval approach
