---
title: "Eval Primitives"
type: concept
category: framework
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Eval Primitives are the three fundamental components that constitute any AI agent evaluation: a task (the agent or prompt under test), a dataset (examples that initiate the task), and scoring functions (methods to judge output quality). Every eval, regardless of complexity, is built from these three primitives.

## Key Information

### The Three Primitives

1. **Task**: The agent under test or the prompt under test — the system being evaluated. This is the subject of the evaluation.

2. **Dataset**: A collection of examples that initiate or invoke the task. These are inputs given to an LLM or agent to start its workflow. The dataset represents the scenarios the agent will encounter in production.

3. **Scoring functions**: Methods used to judge the utility or quality of the task's output. These can be:
   - Human annotation (thumbs up/down with justification)
   - LLM-as-judge (automated, non-deterministic)
   - Deterministic code-based checks (e.g., token count, tool call count)
   - Combined approaches

### Distinction from Unit Tests

- Unit tests aim for exhaustive coverage of every possible failure
- Evals focus on high-level failure modes — exhaustiveness is impossible because the space is infinite
- Eval results don't need to be perfect; directional trends are acceptable, especially with non-deterministic techniques like LLM-as-judge

## Related

- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — source
- [[EvalPracticePhases]] — how practitioners mature in using these primitives
- [[EvalEngineering]] — the practice of crafting effective evaluations
- [[LLM-as-Judge]] — one type of scoring function
- [[DeterministicEval]] — code-based scoring functions
- [[HumanAnnotation]] — human-based scoring
- [[EvalDataCapture]] — sourcing datasets from production
