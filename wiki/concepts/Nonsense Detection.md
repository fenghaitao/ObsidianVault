---
title: "Nonsense Detection"
type: concept
tags: [model-capability, bullshit-detection, pushback, judgment, model-behavior]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md"]
last_updated: 2026-06-29
---

## Definition
Nonsense Detection is the capability of an AI model to recognize when a prompt is ill-posed, nonsensical, or based on false premises, and to push back rather than compliantly attempting to answer. It is a form of judgment that standard benchmarks rarely measure but that has significant practical implications for agent reliability.

## Key Information
- **Measured by**: BullshitBench (155 nonsense questions)
- **Current state**: Only Claude/Sonnet models perform well; GPT and Gemini models comply ~50% of the time; smaller models comply almost always
- **Relationship to reasoning**: Counterintuitively, more reasoning often makes nonsense detection worse — models overthink and try to solve anyway
- **Training gap**: Models are extensively trained to solve tasks but rarely trained to say "this doesn't make sense"
- **Agent implications**: Agents that can't detect nonsense will execute tasks in wrong contexts, wrong projects, or based on bad premises — a major source of agent unreliability
- **Not captured by standard benchmarks**: Most benchmarks assume well-formed questions with correct answers
- **User experience impact**: Contributes to the "slight unease" users feel with models that are otherwise impressive on benchmarks

## Related
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source
- [[BullshitBench]] — benchmark measuring this capability
- [[Reasoning Limits]] — finding that reasoning worsens this capability
- [[ModelBehavior]] — solve-at-any-cost training pattern
- [[Agent Unreliability]] — practical consequence
- [[Model Evaluation]] — broader context of capability measurement
- [[SayingNo]] — related concept about models declining tasks
