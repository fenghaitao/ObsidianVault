---
title: "Meta-Evaluation"
type: concept
tags: [eval, validation, llm-as-judge, human-in-the-loop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition
Meta-evaluation is the practice of evaluating the evaluator — measuring how well an LLM judge's assessments align with human judgment (ground truth). It treats the judge as a classifier and uses precision, recall, and golden datasets to validate its performance.

## Key Information
- The judge is a classifier: it takes input and makes a prediction (pass/fail). Meta-evaluation measures how accurate those predictions are
- Ground truth comes from human judgment — comparing LLM judge labels against human annotations
- Uses precision and recall: precision = when judge says fail, is it right? Recall = of all real fails, how many does the judge catch?
- In most eval scenarios, prioritize recall over precision — better to flag false positives (human reviews something fine) than miss real failures (bad output reaches users)
- Human inter-rater reliability is often only 0.2-0.3 — if an LLM judge achieves higher consistency than that, it's doing well
- Golden datasets should be split 75/25 into training and test sets to avoid overfitting
- Anthropic example: Claude Opus scored 42% on CoreBench, but the eval was wrong — it rejected "96.124991" when expecting "96.12". After fixing, score jumped to 95%
- Key lesson: don't take evals at face value. Always look at explanations, check against golden datasets, verify that failures seem fair
- Known LLM judge biases: position bias (favors first/last option), length bias (prefers longer responses), confidence bias (fooled by confident-sounding wrong answers), self-preference bias (model prefers its own outputs)
- Mitigations: use different model for judging than for generating, use different provider entirely, track accuracy across input categories, benchmark against human performance (not perfection)

## Related
- [[LLMAsJudge]] — the evaluation technique being validated
- [[Golden Dataset]] — ground truth for meta-evaluation
- [[CoreBench]] — benchmark with flawed eval discovered through meta-evaluation
- [[Precision and Recall]] — metrics for judge quality
- [[EvalEngineering]] — practice of crafting eval prompts
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — source (LLM judge trustworthiness warning)
- [[EvalPracticePhases]] — Phase 2 where the need for meta-evaluation is introduced
