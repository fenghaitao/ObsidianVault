---
title: "Zeta2"
type: entity
tags: [model, edit-prediction, zed, code-editor]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed.md"]
last_updated: 2026-06-30
---

## Definition

Zeta2 (Zed 2) is Zed's small specialized edit prediction model, trained via distillation from frontier models on opt-in production data. It predicts the next code edit based on cursor context, recent edits, type definitions, and diagnostics.

## Key Information

- Small specialized model fine-tuned for edit prediction only
- Trained via teacher-student distillation from frontier models on 100K production examples
- Runs on every keystroke, requiring very low latency
- Pipeline: distillation → static eval heuristics → repair → settled data filtering
- Deployed with gradual traffic ramp (15% → live) with acceptance rate and latency dashboards

## Related

- [[summary-20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed]] — source
- [[Zed]] — code editor
- [[BenKunkle]] — edit predictions lead
- [[ModelDistillation]] — training technique
- [[EditPrediction]] — concept
