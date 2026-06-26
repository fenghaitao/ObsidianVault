---
title: "HumanAnnotationFeedback"
type: concept
tags: [eval, annotation, feedback, prompt-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md"]
last_updated: 2026-06-25
---

## Definition
Human annotation feedback is the practice of having subject matter experts provide detailed English-language explanations of why agent outputs failed, going beyond binary correct/incorrect labels to identify specific instruction violations and missing context.

## Key Information
- Human annotators provide not just labels but explanations: "it failed to adhere to this key instruction," "it didn't adhere to the context," "it's missing X."
- This rich text feedback operates in the same domain as the prompts themselves, making it directly actionable for prompt optimization.
- Combined with LLM-as-judge explanations, human feedback provides the most valuable signal for the prompt learning optimizer.
- The process involves domain experts, AI product managers, and subject matter experts who understand the user experience and product success criteria.
- In the workshop, the data set includes input/output pairs with correctness labels, explanations, and rule violation annotations.

## Related
- [[PromptLearning]] — the technique that depends on human annotation feedback
- [[LLM-as-Judge]] — complementary automated feedback source
- [[CoEvolvingLoops]] — both loops benefit from human annotation
- [[EvalEngineering]] — related practice for optimizing automated evaluations
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
