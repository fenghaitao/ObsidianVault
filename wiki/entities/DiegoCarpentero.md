---
title: "DiegoCarpentero"
type: entity
tags: [person, ai-safety, researcher]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

Diego Carpentero is an AI safety researcher who presented on building low-cost, low-latency AI guardrails using fine-tuned ModernBERT encoder models.

## Key Information

- Presented "$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs" on aiDotEngineer
- Demonstrated a complete pipeline: dataset preparation (InjectGuard), tokenization, fine-tuning ModernBERT with a classification head, and inference at 35ms per classification
- Achieved ~85% accuracy on safety classification using ModernBERT-large fine-tuned on 75K labeled examples
- Advocated for encoder models as a practical, self-hostable, and privacy-preserving alternative to LLM-as-judge for safety checks
- Emphasized that AI safety is a common responsibility and that anyone can build a defensive layer with commodity hardware

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[ModernBERT]] — model used in the presentation
- [[Guardrails]] — core topic of the presentation
- [[EncoderModels]] — model class advocated for safety checks
