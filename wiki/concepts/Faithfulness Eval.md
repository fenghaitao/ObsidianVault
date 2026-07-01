---
title: "Faithfulness Eval"
type: concept
tags: [eval, llm-as-judge, faithfulness, rag, hallucination]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
A faithfulness eval checks whether an AI agent's output is grounded in and faithful to its source material. It verifies that the agent used only the information it was given and did not hallucinate or introduce unsupported claims. It is a built-in eval type in Phoenix.

## Key Information
- Checks whether output is based on provided context/research and only that context — "Did it stick to its source material?"
- Essential for RAG applications and multi-step agents where research feeds into output
- In Laurie Voss's workshop, the faithfulness eval scored 13/13 (100%) on the financial analysis agent — much more appropriate than the correctness eval (0/13) for forward-looking financial data
- Requires a context column: the output of the research step fed as context to the faithfulness evaluator
- Contrast with correctness eval: correctness checks factual accuracy against the model's training data; faithfulness checks grounding in provided data regardless of whether that data is factually correct
- Built into Phoenix as a pre-built evaluator — no custom rubric needed
- Particularly useful when dealing with time-sensitive or proprietary data that the judge model wouldn't have in its training data

## Related
- [[Correctness Eval]] — complementary eval that checks factual accuracy
- [[LLMAsJudge]] — the evaluation technique used
- [[Phoenix]] — platform providing built-in faithfulness eval
- [[Actionability Eval]] — custom eval example from same workshop
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
