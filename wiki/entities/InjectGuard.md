---
title: "InjectGuard"
type: entity
tags: [dataset, safety, prompt-injection, classification]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

InjectGuard is a dataset of 75,000 labeled prompt safety examples drawn from 20 open sources, used for fine-tuning encoder models to classify prompts as safe or unsafe.

## Key Information

- Contains 75,000 labeled examples from 20 open sources
- Each example includes the prompt text, a label (safe/unsafe), and the source
- Used via HuggingFace Datasets library with train/test split
- Serves as training data for building low-cost AI guardrails with ModernBERT
- Achieved ~85% accuracy when used to fine-tune ModernBERT-large

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[ModernBERT]] — model fine-tuned on this dataset
- [[Guardrails]] — application domain
- [[PromptInjection]] — attack type the dataset helps detect
