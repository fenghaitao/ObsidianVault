---
title: "EvalEngineering"
type: concept
tags: [eval, prompt-engineering, llm, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
Eval engineering is the practice of carefully crafting LLM-as-judge evaluation prompts to produce rich, actionable, and accurate explanations of model failures, rather than just pass/fail verdicts.

## Key Information
- Aparna Dhinakaran emphasized that eval engineering was the critical differentiator in their prompt learning approach compared to DSPy's GEA/Jeepa optimizer.
- While both approaches use English feedback, the Arize team's investment in eval prompt quality resulted in far fewer training loops and rollouts needed to achieve improvements.
- Good eval prompts ask not just "did it pass?" but "why did it fail?" — requesting specific error categories, examples of common failure scenarios, and actionable guidance.
- Eval engineering is positioned as a distinct discipline that teams building LLM agents should invest in to get the best insights for improvement.
- The workshop demonstrated two evaluator types: a comprehensive output evaluator and a specialized rule checker for granular rule-by-rule analysis.
- For subjective use cases (e.g., Booking.com's property photo quality), the recommendation is to start with binary classification and iteratively refine into more granular criteria.
- Aman Khan demonstrated the iterative eval engineering workflow: write an eval prompt, run it on a dataset, compare against human labels, identify gaps (e.g., missing few-shot examples), refine the eval prompt, and re-run.
- Arize's co-pilot can auto-generate eval prompts with best practices, and the prompt playground can be used to iterate on eval prompts just like application prompts.
- Khan noted it may take 5-10 tries to get an eval that matches human labels, and that's expected given system complexity.
- **Demand-Driven Context**: Raj observes that engineers building MCP servers and RAG pipelines don't do evals — "it's more like a data machine learning concept but we don't do evals." Teams check whether MCP output is coming, not whether it's valuable. This is a major gap in enterprise AI adoption.

## Related
- [[LLM-as-Judge]] — the evaluation method that eval engineering optimizes
- [[PromptLearning]] — the technique that depends on eval engineering for quality feedback
- [[MetaPrompt]] — consumes the output of well-engineered evals
- [[CoEvolvingLoops]] — eval engineering is the practice behind the eval optimization loop
- [[HumanInTheLoopEvaluation]] — validating engineered evals against human labels
- [[FewShotExamples]] — key technique in eval engineering
- [[Arize]] — company that publishes content on eval prompt optimization
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source (deterministic custom evaluators preferred over LLM-as-judge)
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[Golden Dataset]] — preferred foundation for deterministic evals
- [[Agent Optimization]] — optimization depends on eval quality
- [[MCP]] — MCP outputs lack evals in practice
- [[MCPEnterpriseChallenges]] — related challenge
