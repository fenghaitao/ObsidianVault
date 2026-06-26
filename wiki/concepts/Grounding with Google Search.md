---
title: "Grounding with Google Search"
type: concept
tags: [gemini, tool, search, grounding, google]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Grounding with Google Search is a Gemini tool that automatically incorporates Google Search results into the model's responses, providing citations and enabling the model to answer questions about events and information beyond its training data cutoff.

## Key Information
- Available as a toggleable tool in AI Studio and via Gemini APIs
- Automatically incorporates Google Search as a tool the model can call
- Provides inline citations with source URLs for factual claims
- Enables models to answer questions about events after their training data cutoff
- Demonstrated with video analysis: creating tables with fun facts about dinosaurs, citing search results
- Works with Gemini Live for real-time grounded conversations
- Can be combined with other tools like code execution and URL context

## Related
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[AI Studio]] — platform where it's available
- [[URL Context]] — complementary grounding feature
- [[KnowledgeCutoff]] — problem it solves
- [[Gemini 3.1 Flash Live]] — model supporting search grounding in real-time
