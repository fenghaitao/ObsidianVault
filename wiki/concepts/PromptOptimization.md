---
title: "PromptOptimization"
type: concept
tags: [prompt-engineering, optimization, llm, dspy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
Prompt Optimization is the process of iteratively improving the prompts sent to LLMs using metrics and feedback, as opposed to manually tweaking prompt strings. DSPy's optimizers automate this process.

## Key Information
- DSPy optimizers iteratively tweak prompt strings under the hood, guided by metrics that measure success.
- The optimization process leverages the model's ability to find adversarial patterns ("nooks and crannies") that improve performance against a dataset.
- Kevin Madura draws a parallel to Andrej Karpathy's observation about LLM-as-judge: models find cracks to cheat evaluation, and optimizers exploit this same property to improve performance.
- Optimization can be done with as few as 10-100 input/output examples.
- The Jeepa optimizer uses teacher model feedback with textual explanations of errors to tighten the iteration loop.
- Prompt optimization is positioned as an alternative to fine-tuning, with research showing competitive or superior results.
- Metrics can be exact (equality checks) or subjective (LLM-as-judge), and optimizers can break down performance by individual metric.

## Related
- [[DSPy]] — framework providing prompt optimization
- [[DSPyOptimizers]] — DSPy's implementation
- [[GEA]] — DSPy's evolutionary optimizer
- [[PromptOptimizationLoop]] — the iterative process
- [[ModelTransferability]] — enabled by optimization
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
