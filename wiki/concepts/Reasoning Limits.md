---
title: "Reasoning Limits"
type: concept
tags: [reasoning, thinking, model-behavior, overthinking, bullshit-detection]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md"]
last_updated: 2026-06-29
---

## Definition
Reasoning Limits refers to the counterintuitive finding that increased reasoning/thinking in AI models can degrade performance on certain tasks — particularly tasks requiring judgment about whether a question is valid, rather than tasks requiring complex problem-solving. More thinking can lead to worse outcomes when the correct answer is "this doesn't make sense."

## Key Information
- **Observed in BullshitBench**: High reasoning models performed worse than no-reasoning variants on nonsense detection
- **GPT-5.4 traces**: Model would question the premise in one line, then spend 20 paragraphs trying to solve it anyway — even after concluding "maybe this doesn't make sense"
- **Hypothesized cause**: Models are trained to solve tasks at any cost, with insufficient training on saying "don't solve this"
- **Practical manifestation**: Agents executing tasks in wrong projects rather than pushing back
- **Contrasts with common belief**: "Just crank up the reasoning" does not fix all problems — for some tasks, it actively makes things worse
- **Implication**: Reasoning is not a universal solution; different tasks require different cognitive approaches

## Related
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source
- [[BullshitBench]] — benchmark where this was observed
- [[Nonsense Detection]] — the specific capability where reasoning backfires
- [[ModelBehavior]] — solve-at-any-cost training pattern
- [[Agent Unreliability]] — practical consequence in agent systems
- [[Thinking Levels]] — related concept about reasoning depth
- [[ReasoningBudgets]] — related concept about controlling reasoning
