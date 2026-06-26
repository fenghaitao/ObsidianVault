---
title: "PromptOptimizationLoop"
type: concept
tags: [prompt-engineering, optimization, iteration, workshop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md"]
last_updated: 2026-06-25
---

## Definition
The prompt optimization loop is a three-part iterative process for improving system prompts: (1) generate outputs and evaluate correctness, (2) train and optimize using feedback, (3) iterate until a target accuracy threshold is met or max loops are exhausted.

## Key Information
- **Phase 1 — Generate & Evaluate**: Run the current prompt on test data, evaluate correctness using LLM-as-judge with binary labels (correct/incorrect) and detailed explanations.
- **Phase 2 — Train & Optimize**: Generate outputs on the training set, collect correctness labels, explanations, and rule violations, then feed all feedback into the prompt learning optimizer to produce an improved prompt.
- **Phase 3 — Iterate**: Evaluate the new prompt on test data, compare against the target accuracy threshold, and repeat until satisfied or max loops reached.
- The workshop implementation used OpenAI models with JSON response format and zero temperature for consistency.
- The loop tracks metrics (accuracy, F1, precision, recall) across all iterations and saves results including the best-performing prompt.
- Configurable parameters include: number of samples, train/test split ratio, number of rules, number of optimization loops, and target accuracy threshold.

## Related
- [[PromptLearning]] — the broader technique this loop implements
- [[LLM-as-Judge]] — the evaluation method used in Phase 1
- [[CoEvolvingLoops]] — the parallel eval optimization loop that should run alongside
- [[RuleBasedPrompting]] — the output of the optimization loop
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
