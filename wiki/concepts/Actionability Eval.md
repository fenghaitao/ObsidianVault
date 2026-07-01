---
title: "Actionability Eval"
type: concept
tags: [eval, llm-as-judge, custom-eval, rubric, actionability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
An actionability eval is a custom LLM-as-judge evaluation that checks whether an AI agent's output provides actionable recommendations — not just summaries or descriptions. It was demonstrated as a hands-on example of writing a custom eval rubric in Laurie Voss's workshop.

## Key Information
- Custom eval written to test whether a financial analysis agent provides buy/sell/hold recommendations, not just descriptive summaries
- Built using Phoenix's `classification_evaluator` helper with a custom prompt template (rubric)
- The rubric follows the five-part structure: (1) define judge's role, (2) explicit criteria (specific and observable), (3) clearly presented data (XML tags), (4) labeled examples of actionable and not-actionable outputs, (5) constrained binary output
- Criteria for "actionable": contains specific recommendations, includes forward-looking analysis (not just historical data), identifies concrete risks with numbers
- Criteria for "not actionable": only summarizes publicly available data without interpretation, lacks explicit buy/sell/hold recommendation
- Each criterion maps to an actual failure observed in traces — not hypothetical rules
- Initial result: 6/13 actionable — a capability eval with room for improvement
- After prompt improvements (explicitly demanding financial ratios, recent news, buy/sell/hold), the agent one-shotted to 6/6 on previously failing tests
- Demonstrates the power of data-driven prompt engineering: evals don't just tell you what's wrong, they tell you what to fix

## Related
- [[LLMAsJudge]] — evaluation technique
- [[Code Evals]] — complementary deterministic eval type
- [[Capability Evals]] — initial actionability eval served as a capability eval
- [[Phoenix]] — platform supporting custom classification evals
- [[EvalEngineering]] — practice of crafting eval prompts
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
