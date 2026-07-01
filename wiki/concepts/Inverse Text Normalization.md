---
title: "Inverse Text Normalization"
type: concept
tags: [speech-to-text, nlp, post-processing, voice-ai, contact-center]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Contact Center Voice AI： Low-Latency Intelligence Extraction from Messy Audio Streams — Dippu Singh.md"]
last_updated: 2026-06-30
---

## Definition

Inverse Text Normalization (ITN) is a speech-to-text post-processing technique that converts spoken word forms into their written numerical or canonical representations. For example, when a customer says "five thousand dollars," the STT engine outputs "$5,000" in numerical format rather than the textual "five thousand dollars."

## Key Information

- **Purpose**: Drastically improves the LLM's ability to extract entities (amounts, dates, account numbers) from transcripts
- **Examples**: Spoken "$5,000" → numerical "$5,000"; spoken dates → standardized date formats
- **Pipeline Position**: Occurs in the STT post-processing stage, after acoustic modeling and language logic, before the transcript reaches the generative AI core
- **Combined With**: Auto-punctuation, which adds sentence boundaries and punctuation marks to improve LLM comprehension
- **Impact**: Without ITN, numerical information in transcripts is harder for LLMs to parse and extract as structured entities, reducing downstream data quality
- **Relationship to Domain Dictionaries**: ITN works alongside domain-specific dictionaries (e.g., distinguishing "term life" from "term" in insurance) to improve overall STT accuracy

## Related

- [[summary-20260408 - Contact Center Voice AI： Low-Latency Intelligence Extraction from Messy Audio Streams — Dippu Singh]] — source
- [[Contact Center Voice AI]] — broader domain
- [[Dippu Singh]] — speaker who described the technique
