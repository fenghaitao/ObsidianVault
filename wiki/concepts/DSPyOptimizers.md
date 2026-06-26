---
title: "DSPyOptimizers"
type: concept
tags: [dspy, optimization, prompt-engineering, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
DSPy Optimizers are components that iteratively improve the prompts within a DSPy program using defined metrics, achieving performance gains comparable to fine-tuning without modifying model weights.

## Key Information
- Optimizers work by iteratively tweaking the prompt strings under the hood, guided by metrics that define success.
- They can optimize across multiple modules in a composed program, improving each component's performance.
- Jeepa (also called GEA) is a key optimizer that uses feedback from a teacher model, providing textual explanations for why outputs were wrong.
- Research by Chris Potts shows DSPy optimizers can match or exceed fine-tuning methods like GRPO.
- Optimizers enable model transferability: swapping to a smaller/cheaper model and using the optimizer to recover performance.
- The optimization process leverages the model's ability to find "nooks and crannies" — adversarial patterns that improve performance against a dataset.
- Metrics can be rigorous (exact equality checks) or subjective (LLM-as-judge evaluations against criteria).
- A typical optimization flow: construct program with modules, define metrics, run optimizer, evaluate improved performance.

## Related
- [[DSPy]] — framework providing optimizers
- [[DSPyModules]] — what optimizers improve
- [[GEA]] — DSPy's evolutionary optimizer
- [[PromptOptimization]] — the broader concept
- [[ModelTransferability]] — enabled by optimizers
- [[GRPO]] — fine-tuning method compared to optimizers
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
