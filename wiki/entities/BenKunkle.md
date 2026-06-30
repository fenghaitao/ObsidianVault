---
title: "BenKunkle"
type: entity
tags: [person, engineer, zed, edit-prediction, model-training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed.md"]
last_updated: 2026-06-30
---

## Definition
Ben Kunkle is the edit predictions lead at Zed, where he oversees the training and deployment of edit prediction models including Zeta2 — a small, specialized model that predicts the next code edit on every keystroke.

## Key Information
- Edit predictions lead at [[Zed]]
- Presented at [[aiDotEngineer]] on how Zeta2 was trained
- Leads the pipeline for distilling edit prediction models from frontier model teachers
- Developed the settled data technique for filtering training examples using student model sampling
- Built a JSONL-based training pipeline with repair steps, offline evaluations, and production experimentation

## Related
- [[Zed]] — company
- [[summary-20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed]] — source talk
- [[EditPrediction]] — core product area
- [[TeacherStudentDistillation]] — training methodology
- [[SettledData]] — data filtering technique
- [[ModelRepairStep]] — pipeline stage
- [[aiDotEngineer]] — conference where he presented
