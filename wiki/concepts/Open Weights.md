---
title: "Open Weights"
type: concept
tags: [models, open-source, licensing, weights]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
Open Weights refers to models whose trained weights are publicly available, but which may have non-commercial or restrictive licenses. This sits on a spectrum: open weights (non-commercial) → open source (commercially available licenses like MIT, Apache 2.0) → fully open (code, agent harnesses, everything open). The distinction matters for deployment flexibility, privacy, and the ability to customize models.

## Key Information
- Merve Noyan defines three tiers on the openness spectrum:
  1. **Open Weights**: Models with publicly available weights but non-commercial licenses
  2. **Open Source**: Models with commercially available licenses (MIT, Apache 2.0) — example: DeepSeek with MIT license
  3. **Fully Open**: Models where code, agent harnesses, and everything is open
- Open weights enable shrinking, quantization, fine-tuning, and edge deployment
- Guaranteed privacy for end users since data doesn't leave the device when deployed locally
- Performance transparency: "nothing changes without you knowing" — no hidden degradation like with cloud APIs
- The 2026 AI Index shows open models (green) have caught up to closed models (black) in performance
- Openness matters for agent use cases because agents need reliable, customizable, and private model access

## Related
- [[OpenSourceModels]] — the broader open model ecosystem
- [[DeepSeek]] — example of open source model (MIT license)
- [[GLM 5.1]] — top-performing open model
- [[Model Quantization]] — enabled by weight access
- [[FineTuning]] — enabled by weight access
- [[Local Coding Agents]] — use case for open weight models
- [[summary-20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face]] — source
