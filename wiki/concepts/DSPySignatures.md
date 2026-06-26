---
title: "DSPySignatures"
type: concept
tags: [dspy, llm, programming, declarative]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
DSPy Signatures are declarative specifications of what an LLM function should do, defining inputs and outputs while deferring implementation to the model. They are the fundamental abstraction in DSPy for expressing intent.

## Key Information
- Signatures can be expressed as simple strings (e.g., `"text -> sentiment: int"`) or as class-based Pydantic objects with typed fields.
- Field names in class-based signatures serve as mini-prompts, becoming part of the prompt sent to the model.
- The shorthand string format enables rapid experimentation and iteration without writing full prompt strings.
- Signatures support typed inputs and outputs, providing guarantees about the structure of LLM responses.
- Additional instructions can be added via docstrings or description fields for more control.
- Signatures are the building blocks that modules compose and optimizers improve.

## Related
- [[DSPy]] — framework using signatures
- [[DSPyModules]] — modules built from signatures
- [[DSPyAdapters]] — translate signatures into model prompts
- [[DeclarativePromptProgramming]] — the paradigm signatures enable
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
