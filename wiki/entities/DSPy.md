---
title: "DSPy"
type: entity
tags: [framework, prompt-optimization, stanford, declarative, programming]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29

## Definition
DSPy is a declarative framework from Stanford for programming (not just prompting) language models. It provides programming abstractions — signatures, modules, optimizers, adapters, tools, and metrics — that enable building modular, composable, and optimizable AI applications with LLMs as first-class citizens.

## Key Information
- Created by Omar Khattab at Stanford with a "systems mindset": encoding intent in a transferable way that outlasts individual model releases.
- Core primitives: Signatures (declarative input/output specs), Modules (composable building blocks based on PyTorch patterns), Adapters (prompt formatters like JSON/BAML), Optimizers (iterative prompt improvement), Tools (Python functions exposed to LLMs), and Metrics (success definitions for optimization).
- Sits at a higher level of abstraction than LangChain — developers declare intent rather than writing choice messages, content strings, and parsers.
- Supports multiple modalities (images, audio, PDFs) natively through its signature system.
- Uses LiteLLM under the hood for LLM integration, providing usage tracking and model-agnostic access.
- Built-in modules include `dspy.Predict` (vanilla call), `dspy.ChainOfThought` (step-by-step reasoning), `dspy.ReAct` (tool calling), and `dspy.ProgramOfThought` (code-based reasoning).
- Enables model transferability: program logic stays stable while models can be swapped, with optimizers recovering performance on cheaper/smaller models.
- GEA/Jeepa is DSPy's prompt optimizer that is conceptually similar to prompt learning — both use English feedback to improve prompts.
- GEA uses evolutionary optimization: parent-based candidate selection, probabilistic merging of prompts, and a reflection LM that reviews evaluations and makes mutations.
- Unlike prompt learning, GEA keeps multiple top candidates rather than converging on a single best prompt.
- In a side-by-side benchmark, GEA required many more loops and rollouts compared to the Arize team's prompt learning approach.
- Prompt learning outperformed GEA in benchmarks, achieving better results in fewer optimization loops.
- The key difference was not the underlying approach (English feedback) but the quality of the eval prompts: Arize's approach invested heavily in crafting evals that produced better explanations.
- Research by Chris Potts shows DSPy optimizers can match or exceed fine-tuning methods like GRPO.
- Kevin Madura advocates DSPy for rapid iteration on diverse client problems: investigations, process improvement, contract analysis, and document processing.

## Related
- [[PromptLearning]] — technique that was benchmarked against DSPy's GEA
- [[GEA]] — DSPy's evolutionary prompt optimization technique
- [[LLMAsJudge]] — evaluation method used in both approaches
- [[EvalEngineering]] — the differentiator between the two approaches
- [[DSPySignatures]] — core abstraction for declaring intent
- [[DSPyModules]] — composable building blocks
- [[DSPyOptimizers]] — iterative prompt improvement
- [[DSPyAdapters]] — prompt formatting layer
- [[DeclarativePromptProgramming]] — the paradigm DSPy enables
- [[ModelTransferability]] — key benefit of DSPy's design
- [[OmarKhattab]] — founder and original developer
- [[LiteLLM]] — library used under the hood
- [[LangChain]] — alternative framework compared to DSPy
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source (GEPA comparison)
- [[GEPA]] — related optimization algorithm outside DSPy
