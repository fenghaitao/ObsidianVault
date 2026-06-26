---
title: "DSPyModules"
type: concept
tags: [dspy, llm, programming, composability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
DSPy Modules are composable building blocks for DSPy programs, based on signatures and structured similarly to PyTorch modules. They encapsulate LLM calls and business logic into reusable, optimizable components.

## Key Information
- Modules are the base abstraction layer for DSPy programs, wrapping signatures into replicable logic.
- Built-in modules include `dspy.Predict` (vanilla LLM call), `dspy.ChainOfThought` (step-by-step reasoning), `dspy.ReAct` (tool calling), and `dspy.ProgramOfThought` (code-based reasoning).
- Custom modules can be created by subclassing `dspy.Module`, defining signatures in `__init__`, and implementing logic in the `forward` method.
- The `forward` method allows interspersing LLM calls with hard-coded business logic, database actions, or control flow.
- Modules are designed to be composable: multiple modules can be combined into larger programs.
- Because modules follow a consistent structure, DSPy can automatically optimize all components of a composed program.

## Related
- [[DSPy]] — framework using modules
- [[DSPySignatures]] — building blocks of modules
- [[DSPyOptimizers]] — optimize module performance
- [[ChainOfThought]] — built-in module type
- [[ReAct]] — built-in module type for tool calling
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
