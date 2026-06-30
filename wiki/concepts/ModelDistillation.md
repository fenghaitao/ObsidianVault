---
title: "ModelDistillation"
type: concept
tags: [fine-tuning, models, coding-agents, cursor, openai, zed]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
Model distillation is the technique of fine-tuning a model for speed and specific task performance using proprietary data. Cursor's Composer model demonstrated that distillation can build defensibility based on data, reviving interest in fine-tuning after a period where it was rarely recommended.

## Key Information
- Cursor's Composer is a distilled model that is "so fast it's almost too fast" — Zoneraich accidentally pushed to master on a personal project because of the speed
- Cursor has the data advantage from being a popular IDE, enabling effective distillation
- OpenAI's Codex models are similarly optimized for coding agents and distilled
- Before Composer, fine-tuning was "almost never recommended to customers"
- Composer shows you can "actually build defensibility based on your data again"
- The speed advantage is significant enough that Zoneraich has been "almost switching completely to it"
- OpenAI could come out with a similarly fast model because they also have the data
- Distillation enables the "fast" tier in multi-tier reasoning budget systems
- [[Pruna]] uses distillation as one of several techniques (alongside [[Quantization]], [[Model Pruning]], and step caching) to reduce denoising steps in image/video models from 50 down to 4-20, building [[Performance Models]]

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[summary-20260530 - How We Built Zeta2： Training an Edit Prediction Model in Production — Ben Kunkle, Zed]] — source (teacher-student distillation for edit prediction)
- [[Cursor]] — the product using distillation
- [[OpenAI]] — also using distillation for Codex models
- [[ReasoningBudgets]] — distillation enables the fast tier
- [[AITherapistProblem]] — distillation as one approach to differentiation
- [[TeacherStudentDistillation]] — specialized variant for edit prediction training
- [[Zed]] — uses teacher-student distillation for Zeta2
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source (denoising step reduction)
- [[Pruna]] — uses distillation for performance models
- [[Performance Models]] — concept enabled by distillation
