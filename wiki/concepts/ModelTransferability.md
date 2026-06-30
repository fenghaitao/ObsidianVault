---
title: "ModelTransferability"
type: concept
tags: [dspy, llm, optimization, model-switching]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
Model Transferability is the ability to swap the underlying LLM in a DSPy program while preserving program logic, using optimizers to recover or maintain performance across different models.

## Key Information
- DSPy's design separates program logic (signatures, modules, control flow) from the specific model being used.
- When switching from a powerful model (e.g., GPT-4.1) to a cheaper one (e.g., GPT-4.1 Nano), optimizers can recover lost performance.
- This enables cost optimization: run the optimizer on the cheaper model to bring performance from, say, 70% back up to 87%.
- The optimizer achieves this by finding model-specific prompt patterns that work best for the target model.
- Model mixing within a single program is also supported: different modules can use different LLMs optimized for specific workloads (e.g., Gemini for images, Claude for text).
- Transferability is enabled by DSPy's systems mindset: program design outlasts model releases.

## Related
- [[DSPy]] — framework enabling transferability
- [[DSPyOptimizers]] — mechanism for recovering performance
- [[DeclarativePromptProgramming]] — paradigm that separates logic from models
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source (optimization is model-specific; changing models requires re-optimization)
- [[Agent Optimization]] — broader optimization context
- [[GEPA]] — optimization algorithm tied to specific models
