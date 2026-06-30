---
title: "summary-20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed"
type: source
tags: [source, transcript, edit-prediction, model-training, distillation, zed]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed.md"]
last_updated: 2026-06-30
---

## Core Summary

Ben Kunkle from Zed presents the training pipeline for Zeta2, a small specialized edit prediction model. Using distillation from frontier models on opt-in production data, the pipeline includes static evaluations, repair steps, and settled data filtering via student model checkpoints to identify ideal training examples.

## Key Points

- Edit prediction: model predicts next edit given cursor region, recent edits, type definitions, diagnostics.
- Pipeline: opt-in production snapshots → teacher (frontier model) distillation → static eval heuristics → repair step → prompt formatting → train student model.
- Settled data technique: wait until user stops editing, snapshot the result, filter noisy examples using student checkpoint similarity (Levenshtein distance).
- The "interesting middle" — examples that are neither trivially predictable nor pure noise — are the ideal training data.
- 100K examples for peak training, 10-50K for experiments. All JSONL format with additive fields per stage.
- Production deployment: gradual traffic ramp (15% → 20% → live), tracking acceptance rate, latency, diagnostic error counts.
- Evaluations use delta char F (n-gram Levenshtein), reversal ratio, kept rate; validated against 3 teacher predictions since there's no single right answer.

## Related

- [[BenKunkle]] — speaker, edit predictions lead at Zed
- [[Zed]] — code editor company
- [[Zeta2]] — Zed's edit prediction model
- [[ModelDistillation]] — teacher-student training technique
- [[EditPrediction]] — concept of predicting next code edit
- [[SettledData]] — filtering technique for training data
- [[LevenshteinDistance]] — similarity metric used
