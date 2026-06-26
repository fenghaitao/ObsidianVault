---
title: "DeclarativePromptProgramming"
type: concept
tags: [dspy, prompt-engineering, programming, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
Declarative Prompt Programming is the paradigm enabled by DSPy where developers express intent through signatures and modules rather than manually crafting prompt strings. The "how" of implementation is deferred to the LLM and the framework.

## Key Information
- Instead of writing prompt strings, developers declare what they want (inputs, outputs, types) and let DSPy handle prompt construction.
- Field names and type annotations serve as implicit prompts, becoming part of what is sent to the model.
- This approach shifts focus from prompt engineering to program construction: building proper Python programs that happen to use LLMs.
- The paradigm enables rapid experimentation: a shorthand signature like `"text -> sentiment: int"` is all that's needed to start.
- Additional instructions can be layered on via docstrings and descriptions for more control.
- The approach is described as building with a "systems mindset" — encoding intent in a transferable way.

## Related
- [[DSPy]] — framework enabling this paradigm
- [[DSPySignatures]] — the mechanism for declarative specification
- [[DSPyAdapters]] — translate declarations into prompts
- [[PromptOptimization]] — the alternative paradigm being replaced
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
