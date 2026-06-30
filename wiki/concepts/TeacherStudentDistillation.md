---
title: "TeacherStudentDistillation"
type: concept
tags: [ai, model-training, distillation, frontier-models, fine-tuning, zed]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed.md"]
last_updated: 2026-06-30
---

## Definition
Teacher-student distillation is a model training approach where a large, powerful frontier model (the teacher) generates predictions that serve as training targets for a smaller, specialized model (the student). The student model learns to approximate the teacher's behavior on a specific task, enabling fast, focused inference suitable for latency-sensitive applications like edit prediction.

## Key Information
- **Teacher**: A frontier model (large, general-purpose) that generates predictions given the same input the student will receive
- **Student**: A small, specialized model (like Zeta2) trained to mimic the teacher's output
- **Noise Problem**: Frontier models are inconsistent — 100K requests yield 100,001 answers — requiring careful prompt engineering, repair steps, and filtering
- **Pipeline Structure**: All JSONL-based — each stage adds or moves fields in giant JSON objects, making the process fluid and dynamic
- **Caching**: Everything up to the teacher prediction stage is cached and reusable across experiments. Only prompt formatting is experiment-specific.
- **Scale**: Peak training uses 100K examples; smaller experiments use 10-50K
- **Prompt Formatting**: Experiment-specific stage that controls what data is included (diagnostics, edit history depth, etc.)
- **Student as Teacher (Settled Data)**: Once the student model approaches teacher quality, it can generate multiple predictions at near-zero cost for filtering training examples, replacing expensive frontier model calls

## Related
- [[summary-20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed]] — source
- [[EditPrediction]] — the task being distilled
- [[ModelDistillation]] — broader distillation concept
- [[ModelRepairStep]] — pipeline stage for fixing bad teacher predictions
- [[SettledData]] — data filtering technique using student model
- [[Zed]] — company using this approach
- [[BenKunkle]] — presenter
