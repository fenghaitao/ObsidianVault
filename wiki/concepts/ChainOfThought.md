---
title: "ChainOfThought"
type: concept
tags: [prompting, llm, reasoning, dspy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
Chain of Thought is a prompting technique that encourages step-by-step reasoning in LLM outputs. In DSPy, it is a built-in module (`dspy.ChainOfThought`) that automatically adds reasoning fields to responses.

## Key Information
- In DSPy, `dspy.ChainOfThought` automatically injects a reasoning field into the output, even if not specified in the signature.
- The technique adds prompts like "let's think step by step" from academic literature to encourage structured reasoning.
- Kevin Madura notes that Chain of Thought may be less relevant with modern models that have internalized reasoning capabilities.
- When using `dspy.ChainOfThought`, the reasoning is exposed to the user and can be retained for debugging or other purposes.
- Switching from `dspy.ChainOfThought` to `dspy.Predict` removes the reasoning component, returning only the final output.

## Related
- [[DSPy]] — framework with built-in Chain of Thought module
- [[DSPyModules]] — module system including Chain of Thought
- [[ReAct]] — related reasoning+action pattern
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
