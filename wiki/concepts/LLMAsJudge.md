---
title: "LLM-as-Judge"
type: concept
tags: [eval, llm, evaluation, prompt-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-30
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
- **BullshitBench usage**: Peter Gostev used LLM-as-judge to grade model responses to 155 nonsense questions, validated by his own human review of the responses. The judge classified responses as green (clear pushback), amber (partial acceptance), or red (full compliance).
- **Chess coach evaluation**: The Play Magnus team uses LLM-as-judge to evaluate chess commentary across 16 scenarios covering tactical patterns, blunders, and hallucination limits. They extract scenarios from real games and use LLM-as-judge to assert whether the model correctly identifies and mentions specific chess features (e.g., knight forks). Models are compared via Open Router: Gemini 3 Flash (~75%), Claude with thinking (~60%), GPT-5 Mini (lower). Domain experts (the speakers, both strong chess players) serve as the final quality arbiter.
- **Rubric structure**: Laurie Voss defined five essential parts of a good LLM-as-judge rubric: (1) define the judge's role, (2) explicit, observable criteria mapped to actual trace failures, (3) clearly presented data with labeled fields (XML tags), (4) labeled examples of good and bad outputs (the most useful addition — LLMs learn patterns from examples better than from instructions), (5) constrained output (binary yes/no, avoid 1-10 scales)
- **Binary over scales**: LLMs are bad at numeric ratings — what's the difference between 6 and 7? Binary labels (yes/no) are much more reliable. If nuance is needed, use three categories (incorrect/partially correct/completely correct)
- **Chain of thought for judges**: Telling the judge to explain its reasoning before outputting the label demonstrably improves quality
- **Biases**: Position bias (favors first or last option), length bias (prefers longer responses), confidence bias (fooled by confident-sounding wrong answers), self-preference bias (prefers outputs from the same model)
- **Model choice**: Use a more capable model for judging than for generating. Using a different provider entirely (e.g., Claude for agent, OpenAI for judge) improves reliability by reducing self-preference bias
- **One eval per dimension**: Don't create a "god evaluator" that tests everything — split into separate evals for accuracy, completeness, tone, etc.
- **Guardrails vs North Star metrics**: Some evals are ship blockers (hallucinating a stock price), others are nice-to-have (recommending complimentary investments)

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
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source (BullshitBench grading)
- [[summary-20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust]] — source (data scientists uniquely qualified to validate LLM judges with labeled datasets)
- [[BullshitBench]] — benchmark graded by LLM-as-judge
- [[Peter Gostev]] — validated LLM judge against human review
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source (Colvin's critique: "lunatics running the asylum")
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source (rubric structure, biases, binary over scales)
- [[Golden Dataset]] — preferred alternative to LLM-as-judge for deterministic evals
- [[Code Evals]] — complementary deterministic eval type
- [[MetaEvaluation]] — validating LLM judges
- [[Actionability Eval]] — example of custom LLM-as-judge rubric
- [[Pairwise Evaluation]] — comparison-based LLM judging
- [[DataScientistsAsGuardrails]] — data scientists can validate LLM-as-judge with labeled datasets and traditional metrics
- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — source (trustworthiness warning: "putting a robe and cloak on an LLM doesn't make it trustworthy")
- [[DeterministicEval]] — complementary code-based evaluation approach
- [[EvalPracticePhases]] — Phase 2 where LLM-as-judge is introduced to scale evaluation
