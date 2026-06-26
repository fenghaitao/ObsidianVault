---
title: "LLM-as-Judge"
type: concept
tags: [eval, llm, evaluation, prompt-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-25
---

## Definition
LLM-as-Judge is an evaluation technique where a language model is used to assess the quality of another model's outputs, providing both a pass/fail verdict and an English-language explanation of the reasoning.

## Key Information
- In the prompt learning workflow, LLM-as-judge evals receive: the problem statement, the coding agent's solution, the unit test results, and the actual solution. The eval then outputs whether the solution passed or failed, plus a detailed explanation of why.
- The explanation component is critical — it identifies specific error categories (e.g., parsing errors, library-specific mistakes, missing edge cases) that can be fed back into the prompt learning loop.
- The quality of the LLM-as-judge eval prompt directly determines the quality of the feedback and thus the effectiveness of prompt learning.
- Used in both the Arize team's prompt learning approach and DSPy's GEA/Jeepa optimizer, but the Arize approach invested more in eval prompt quality.
- In the workshop, two evaluators were used: a comprehensive evaluator (correct/incorrect with explanations) and a rule checker (granular rule-by-rule compliance analysis).
- The evaluators can use binary labels (correct/incorrect) or multi-class labels, with optional score mapping for metric calculation.
- Aman Khan demonstrated the four-part structure of an LLM-as-judge eval: role (task definition), context (text to evaluate), goal (what to determine), and terminology/labels (text labels, not numeric scores — LLMs are bad at numbers).
- LLM judges must be validated against human labels (human-in-the-loop evaluation) because they hallucinate too. Khan's demo showed near-zero agreement between his friendly/robotic eval and human labels.
- Variance in LLM judge outputs can be reduced by lowering temperature or running evals multiple times to profile variance.
- Few-shot examples in eval prompts improve classification accuracy and reduce variance.
- In the 2024 AI Engineer Summit keynote, Eugene Yan was "super bullish" on LLM-as-judge for quick prototyping with minimal dev effort but acknowledged key limitations: difficult to align to specific business criteria, requires chain-of-thought (5-8 seconds latency), and needs ongoing maintenance of dynamic few-shot examples. He recommended fine-tuned classifiers/reward models for production use (100x lower latency in milliseconds, higher precision).
- The keynote's verdict: LLM-as-judge is a resources question — use it for low-volume prototyping, invest in fine-tuned evaluators for sticky production products.

## Related
- [[PromptLearning]] — the technique that depends on LLM-as-judge feedback
- [[EvalEngineering]] — the practice of crafting effective LLM-as-judge prompts
- [[MetaPrompt]] — consumes LLM-as-judge explanations to generate improved rules
- [[CoEvolvingLoops]] — LLM-as-judge is used in both optimization loops
- [[HumanInTheLoopEvaluation]] — validating LLM judges against human labels
- [[FewShotExamples]] — technique to improve LLM-as-judge accuracy
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source (prototyping vs production trade-offs, latency comparison)
- [[EugeneYan]] — presented the LLM-as-judge analysis in the keynote
- [[ChainOfThought]] — required for precise LLM-as-judge but adds latency
- [[FineTuning]] — recommended as production alternative to LLM-as-judge
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
