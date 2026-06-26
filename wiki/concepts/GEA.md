---
title: "GEA"
type: concept
tags: [prompt-engineering, optimization, dspy, evolutionary]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md"]
last_updated: 2026-06-25
---

## Definition
GEA (Genetic Evolutionary Algorithm) is DSPy's prompt optimization technique that uses parent-based candidate selection, probabilistic merging of prompts, and a reflection LM to iteratively improve prompts through evolutionary optimization.

## Key Information
- Part of DSPy's optimizer suite, representing an evolutionary approach to prompt optimization.
- Process: take candidate prompts → evaluate them → a reflection LM reviews evaluations → make mutations/changes → repeat until optimal prompts are found.
- Unlike prompt learning, GEA keeps multiple top candidates rather than converging on a single best prompt.
- Benchmarked against prompt learning: prompt learning achieved better results in fewer optimization loops.
- Key difference: GEA uses positive reflection and evaluation during optimization, but prompt learning's richer English feedback (human annotations + eval explanations) proved more effective.
- The comparison highlighted that eval quality matters more than the optimization algorithm itself.

## Related
- [[DSPy]] — the Stanford framework containing GEA
- [[PromptLearning]] — the technique that outperformed GEA in benchmarks
- [[EvalEngineering]] — the practice that made the difference in the comparison
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
