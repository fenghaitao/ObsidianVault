---
title: "SettledData"
type: concept
tags: [ai, data-filtering, model-training, training-data, zed, edit-prediction]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed.md"]
last_updated: 2026-06-30
---

## Definition
Settled data is a technique for filtering training examples in edit prediction models. Instead of relying entirely on teacher model predictions, the approach waits until the user stops editing a region (10-second pause heuristic), snapshots the final state, and uses it to identify high-quality training examples by comparing multiple student model predictions against the settled state using Levenshtein distance.

## Key Information
- **Core Idea**: The user eventually writes the answer. By waiting for the edit region to settle, the editor can capture what the user actually wanted.
- **Settling Heuristic**: The user stops editing the region for 10 seconds — a rough but effective signal. Does not yet use git commits.
- **Noise Problem**: The settled state can be noisy — users change their minds, agents rewrite code, and the final state may be completely different from when the prediction was made.
- **Filtering with Frontier Models (Expensive)**: Generating 10 frontier model predictions per example and comparing with Levenshtein distance — 1M requests for 100K examples, prohibitively expensive.
- **Filtering with Student Model (Efficient)**: Once the student model approaches teacher quality, generate ~50 student predictions at near-zero cost. Compare each to the settled state using Levenshtein distance.
- **Three Quality Bands**:
  - **Too close**: Trivially predictable (e.g., "function add A plus" → "B"). Not useful for training.
  - **Too far**: Likely noise — the settled state is unrelated to the original prediction context. Filtered out.
  - **Ideal middle**: Close but not exact — often contains new functions past the training data cutoff that the student has never seen. These are the best training examples.
- **Training Target**: Train on what was closest to the settled state, not the actual settled state (still noisy).

## Related
- [[summary-20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed]] — source
- [[EditPrediction]] — the task using this technique
- [[TeacherStudentDistillation]] — the broader training pipeline
- [[LevenshteinDistance]] — similarity metric used for comparison
- [[BenKunkle]] — developed the technique
- [[Zed]] — company using this approach
