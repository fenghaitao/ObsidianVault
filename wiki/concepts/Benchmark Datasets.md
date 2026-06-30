---
title: "Benchmark Datasets"
type: concept
tags: [hugging-face, benchmarks, evaluation, models, comparison]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
Benchmark Datasets is a Hugging Face Hub feature that aggregates and displays model rankings across popular benchmarks such as SWE-Bench Pro, Humanity's Last Exam, and AIMEE. It allows users to filter and compare open model performance, making model selection easier among the ~3 million models on the Hub.

## Key Information
- Accessible via the "Benchmark" button at the bottom of the datasets page on Hugging Face Hub
- Includes popular benchmarks: SWE-Bench Pro (coding/agent performance), Humanity's Last Exam, AIMEE, and others
- Models are ranked by score, making it easy to identify top performers for specific tasks
- As of May 2026, GLM 5.1 was at the top of the SWE-Bench leaderboard
- Addresses the challenge of model selection among 3 million+ models on the Hub
- OCR Bench is another benchmark dataset available for comparing OCR models
- A new skill was recently shipped that can recommend models from benchmarks for fine-tuning use cases

## Related
- [[HuggingFace]] — platform hosting the feature
- [[GLM 5.1]] — top-ranked model on SWE-Bench at time of talk
- [[Hugging Face Skills]] — skill for benchmark-based model recommendations
- [[BenchmarkSaturation]] — related concept about benchmark limitations
- [[summary-20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face]] — source
