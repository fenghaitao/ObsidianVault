---
title: "CoEvolvingLoops"
type: concept
tags: [prompt-engineering, eval, optimization, iteration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md"]
last_updated: 2026-06-25
---

## Definition
Co-evolving loops are two parallel optimization cycles — one for agent prompts and one for eval prompts — that must both be maintained because the agent optimization loop only works as well as the eval signal feeding it.

## Key Information
- The agent prompt loop (blue loop): collect failure examples → annotate with human feedback → run prompt learning optimization → deploy improved prompt → repeat.
- The eval prompt loop (orange loop): collect eval failures → evaluate the evaluators (using log probabilities, jury-as-judge, or human review) → annotate where evals went wrong → optimize eval prompts → repeat.
- Both loops follow the same fundamental process but operate on different data: agent outputs vs. eval outputs.
- A common mistake is treating evals as a one-time setup; they require continuous refinement just like agent prompts.
- The quality of the eval loop directly determines the effectiveness of the agent loop — unreliable evals produce unreliable prompt improvements.

## Related
- [[PromptLearning]] — the agent optimization loop
- [[EvalEngineering]] — the practice of optimizing eval prompts
- [[LLMAsJudge]] — the evaluation method used in both loops
- [[HumanAnnotationFeedback]] — feedback source for both loops
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
