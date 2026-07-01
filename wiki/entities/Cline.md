---
title: "Cline"
type: entity
tags: [tool, coding-agent, open-source, evals]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
last_updated: 2026-06-30
---

## Definition
Cline is an open-source coding agent that uses LLMs to autonomously write and edit code. It supports customizable rules that can be appended to its system prompt.

## Key Information
- In prompt learning experiments, vanilla Cline (with no rules added) resolved approximately 30% of SWE-bench GitHub issues using Claude Sonnet.
- After prompt learning with 150 training examples, Cline improved to approximately 45% — a 15 percentage point gain, the largest improvement observed.
- A case study demonstrated that Cline's original system prompt had no rules section — just a basic role description. Adding explicit rules (error handling, system design alignment, test requirements) drove the 15% improvement.
- The improvement was achieved with no fine-tuning, no tool changes, and no architecture changes — purely through system prompt iteration.
- Uses a rules mechanism similar to Claude Code's Claude.md file, allowing users to append repository-specific instructions.
- The large improvement from prompt learning suggests Cline benefits particularly strongly from well-crafted system prompt rules.

### Eval Journey

- Initially, Cline (like the [[Codex]] team) ignored evals entirely, considering them unnecessary and a waste of time
- Transitioned to building custom evaluation datasets from scratch using real user coding problems (opt-in, paid data collection)
- Parsed and cleaned massive datasets of actual coding problems users were solving
- Uses [[TerminalBench]] (89 real-world programming problems from [[Stanford]]) for standardized evaluation
- Uses [[Harbor]] (from the Loda Institute) for parallelized evaluation infrastructure on [[Modal]]
- Maintains an internal benchmark for all kinds of models (open-source and frontier)
- Uses [[Hill Climbing (Evals)]] methodology: get a score, triage failures, pull improvement levers, repeat
- [[AraKhan]] presented Cline's eval philosophy at [[aiDotEngineer]]: evals are broken, use them anyway

## Related
- [[ClaudeCode]] — another coding agent benchmarked alongside Cline
- [[SWEBench]] — benchmark used to evaluate Cline
- [[PromptLearning]] — technique used to improve Cline's performance
- [[RuleBasedPrompting]] — the approach that drove Cline's improvement
- [[AraKhan]] — engineer at Cline who presented on evals
- [[TerminalBench]] — benchmark used by Cline for agent evaluation
- [[Harbor]] — eval infrastructure used by Cline
- [[HarborEval]] — de facto evaluation harness
- [[Modal]] — compute infrastructure for Cline's eval runs
- [[Hill Climbing (Evals)]] — methodology used by Cline
- [[Three Zones of Improvement]] — framework from Cline's eval practice
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source
