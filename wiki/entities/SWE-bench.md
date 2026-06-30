---
title: "SWE-bench"
type: entity
tags: [benchmark, software-engineering, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR.md"]
last_updated: 2026-06-29
---

## Definition
SWE-bench (Software Engineering Benchmark) is a dataset of real-world GitHub issues used to evaluate the ability of coding agents and LLMs to resolve software engineering tasks.

## Key Information
- In the prompt learning experiments, SWE-bench Lite was used with 150 examples to benchmark Claude Code and Cline.
- SWE-bench Lite was also used in the Cline case study to validate that rule-based prompt improvements generalized beyond the training data.
- The benchmark measures the percentage of GitHub issues successfully resolved by the coding agent's generated patches.
- Also referenced as part of broader software engineering evaluation alongside BBH and other datasets.
- The prompt learning experiments used SWE-bench unit tests to determine pass/fail and generate LLM-as-judge explanations.
- Joel Becker notes that SWE-bench scoring is "algorithmic costless scoring at the margin" — it does not account for whether code is maintainable, matches quality standards, or would be accepted by human reviewers.
- This limitation means AI may be performant on SWE-bench but not on mergeability scoring, contributing to the gap between benchmark results and real-world productivity.

## Related
- [[ClaudeCode]] — evaluated on SWE-bench
- [[Cline]] — evaluated on SWE-bench
- [[PromptLearning]] — technique tested using SWE-bench
- [[RuleBasedPrompting]] — validated using SWE-bench Lite
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — source
- [[MergeabilityScoring]] — holistic evaluation beyond SWE-bench's unit test approach
- [[BenchmarkSaturation]] — related limitation of benchmarks
- [[Louis Knight-Webb]] — placed ahead of OpenAI on SWE-bench verified leaderboard
- [[summary-20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban]] — source
