---
title: "EditPrediction"
type: concept
tags: [code-editing, model-training, distillation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed.md"]
last_updated: 2026-06-30
---

## Definition

Edit prediction is the task of predicting the next code edit a developer will make, given context around the cursor including recent edits, type definitions, variable definitions, and diagnostics. It requires low latency (per-keystroke) and is ideal for small specialized models fine-tuned via distillation.

## Key Information

- Input: cursor region, recent edits, type/variable definitions, diagnostics, errors
- Must run on every keystroke — requires small specialized model, not general-purpose LLM
- Training via distillation: frontier model as teacher, specialized model as student
- Settled data technique: wait for user to finish editing, snapshot result, filter noise
- Evaluation metrics: delta char F (n-gram Levenshtein), reversal ratio, kept rate in production

## Related

- [[summary-20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed]] — source
- [[Zeta2]] — Zed's implementation
- [[Zed]] — code editor
- [[ModelDistillation]] — training technique
- [[SettledData]] — filtering technique
