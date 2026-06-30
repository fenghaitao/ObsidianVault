---
title: "ConstrainedDecoding"
type: concept
tags: [safety, generation, llm, guardrails, output-control]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-26
---

## Definition

Constrained decoding is a safety implementation technique that restricts LLM output generation to a predefined set of valid tokens or patterns, preventing the model from producing harmful or unauthorized content. It is one of several defensive options for AI safety checks in production.

## Key Information

- Listed as one of the implementation options for AI safety alongside rule filtering, canary tokens, discriminators (encoder models), and LLM-as-judge
- Operates at the token-generation level rather than post-hoc checking
- Part of a defense-in-depth strategy where multiple safety checkpoints are placed throughout the LLM application pipeline
- The choice between constrained decoding and other approaches depends on latency tolerance and use case requirements

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[Guardrails]] — broader defensive framework
- [[DeterministicGuardrails]] — related defensive approach
- [[EncoderModels]] — alternative discriminator-based approach
