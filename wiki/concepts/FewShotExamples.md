---
title: "FewShotExamples"
type: concept
tags: [prompt-engineering, eval, llm, classification]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md"]
last_updated: 2026-06-25
---

## Definition
Few-Shot Examples are labeled examples provided within an eval prompt to help an LLM-as-judge system better understand the classification task. They are a best practice for improving eval accuracy and reducing variance.

## Key Information
- Aman Khan identified the lack of few-shot examples as a clear gap in his initial friendly/robotic eval that caused poor agreement with human labels.
- Providing examples of "friendly text" and "robotic text" in the eval prompt helps the judge calibrate its classifications.
- Arize's co-pilot can auto-generate eval prompts with few-shot examples based on best practices.
- Combined with human-in-the-loop evaluation: human-labeled examples from the dataset can become few-shot examples in the eval prompt.
- Part of the iterative eval improvement loop: identify where the judge disagrees with humans, add those as few-shot examples, and re-run.

## Related
- [[LLMAsJudge]] — the evaluation technique that benefits from few-shot examples
- [[EvalEngineering]] — the practice of including few-shot examples in eval prompts
- [[HumanInTheLoopEvaluation]] — source of labeled examples for few-shot prompting
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
