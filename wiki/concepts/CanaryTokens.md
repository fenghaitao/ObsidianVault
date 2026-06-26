---
title: "CanaryTokens"
type: concept
tags: [security, defensive, detection, honeypot]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

Canary tokens are decoy data elements placed within systems to detect unauthorized access or data exfiltration. In the context of AI safety, they serve as one implementation option for defensive layers alongside rule filtering, discriminators, constrained decoding, and LLM-as-judge.

## Key Information

- Mentioned as one of several implementation options for AI safety checks in production LLM-based applications
- Part of a defense-in-depth strategy alongside encoder-based discriminators (like fine-tuned ModernBERT), rule filtering, constrained decoding, and LLM-as-judge
- Traditional security concept adapted for the AI safety domain

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[Guardrails]] — broader defensive framework
- [[DeterministicGuardrails]] — related defensive approach
- [[ConstrainedDecoding]] — alternative implementation option
