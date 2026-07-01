---
title: "summary-20260408 - Contact Center Voice AI： Low-Latency Intelligence Extraction from Messy Audio Streams — Dippu Singh"
type: source
tags: [source, transcript, voice-ai, contact-center, stt]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Contact Center Voice AI： Low-Latency Intelligence Extraction from Messy Audio Streams — Dippu Singh.md"]
last_updated: 2026-06-30
---

## Core Summary

Dippu Singh from Fujitsu presents a four-stage low-latency pipeline for contact center voice AI: voice capture with channel separation → speech-to-text (90%+ accuracy) → generative AI core for summarization → CRM data sync. The goal: reduce after-call work (ACW) from 6.3 minutes to near-zero by mechanizing summarization and data extraction.

## Key Points

- Contact center operators spend nearly 1:1 time on calls vs administrative after-call work (ACW).
- Four-stage pipeline: voice capture (noise filtering, channel mapping, PII masking) → STT (acoustic modeling, domain dictionaries, inverse text normalization) → GenAI core (intent recognition, summarization) → CRM sync.
- Channel separation is critical: agent on left, customer on right; mixing causes LLM confusion.
- PII masking at buffer level prevents sensitive data from entering LLM memory.
- STT must exceed 90% accuracy; domain-specific dictionaries handle terminology (e.g., "term life" vs "term").
- ROI: reduced ACW time, improved data quality, shift from handling calls to analyzing voice of customer.

## Related

- [[Dippu Singh]] — speaker, Fujitsu North America
- [[Fujitsu]] — company
- [[Voice AI]] — contact center voice AI
- [[ContactCenterAI]] — AI for customer service
- [[SpeechToText]] — STT component
- [[PII Masking]] — privacy technique
