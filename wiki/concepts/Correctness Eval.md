---
title: "Correctness Eval"
type: concept
tags: [eval, llm-as-judge, correctness, factual-accuracy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
A correctness eval checks whether an AI agent's response is factually accurate, complete, and logically consistent. It is a built-in LLM-as-judge eval type in Phoenix that compares the output against the model's own knowledge of what is correct.

## Key Information
- Checks factual accuracy, completeness, and logical consistency of agent outputs
- Built into Phoenix as a pre-built evaluator — uses an LLM judge to assess correctness
- In Laurie Voss's workshop, the correctness eval completely failed (0/13) when applied to a financial analysis agent making forward-looking predictions for 2026
- Failure cause: the judge model (Claude Sonnet) was trained on data through 2025 and didn't know 2026 financial data — it judged all outputs as incorrect because it couldn't verify future-looking claims
- Lesson: correctness evals are unreliable when the output depends on information newer than the judge model's training cutoff
- For time-sensitive or forward-looking data, a faithfulness eval (checking grounding in provided research) is more appropriate than a correctness eval
- Choosing the right eval type matters more than tuning the eval prompt
- Like all LLM judges, the correctness eval can be wrong — its judgments must be validated against human labels (meta-evaluation)

## Related
- [[Faithfulness Eval]] — complementary eval for grounding in source material
- [[LLM-as-Judge]] — the evaluation technique used
- [[Phoenix]] — platform providing built-in correctness eval
- [[Meta-Evaluation]] — validating eval accuracy
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
