---
title: "Supervised Fine-Tuning"
type: concept
tags: [training, fine-tuning, llm, ml-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - What Lies Beneath the API — Benjamin Cowen, Modal.md"]
last_updated: 2026-06-30
---

## Definition
Supervised Fine-Tuning (SFT) is a training technique where a pre-trained model is further trained on a curated dataset of input-output pairs to adapt its behavior to a specific domain or task. Modern open-source libraries have reduced SFT to approximately 300 lines of Python.

## Key Information
- Accessible implementation: achievable in ~300 lines of Python with modern open-source libraries
- Requires curated training data (input-output pairs) and mature eval systems before starting
- Provides algorithm-level control without the infrastructure burden of full training
- Garbage in, garbage out: data quality is the primary determinant of success
- Contrasted with the traditional image of training as requiring thousands of lines in a monorepo
- Example code available on Modal's examples repository

## Related
- [[summary-20260602 - What Lies Beneath the API — Benjamin Cowen, Modal]] — source
- [[Fine-tuning]] — parent category
- [[Model Customization]] — broader framework
- [[Domain-Specific Models]] — the output of SFT
- [[DataFlywheel]] — prerequisite data collection cycle
