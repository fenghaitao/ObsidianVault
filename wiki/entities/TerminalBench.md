---
title: "TerminalBench"
type: entity
tags: [benchmark, agents, cli, computer-use, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
last_updated: 2026-06-30
---

## Definition
Terminal Bench is a benchmark that evaluates AI agents' ability to use the command-line interface (CLI) for general-purpose computer use, not just coding. It represents a bet on the CLI as a core abstraction and affordance for agents to interact with the real world.

## Key Information
- A bet on the CLI as the primary interface for general-purpose agent computer use
- The bet has proven largely correct as teams build enterprise capabilities on CLI-based tools (Claude Code, Codex, etc.)
- Terminal Bench 2.0 shipped with [[HarborEval]], a de facto evaluation harness for agent builders
- Remains one of the most robust and important benchmarks measured on recent model cards
- **Task quality noise**: Snorkel's research found that Terminal Bench (v1 and v2) contains tasks that can never be completed, which becomes a source of noise masking whether models are actually improving. This was identified through internal analysis comparing various public benchmarks.
- Cited by [[VincentChen]] as an exemplar of [[Benchmark Thesis]] — having a research question about where the field is going
- Created by researchers at [[Stanford]] University
- Contains 89 real-world programming problems including race conditions, database issues, and infrastructure problems
- Tasks can take 30-40 minutes to run, reflecting genuine agentic complexity
- Used by [[Cline]] as part of their evaluation pipeline alongside [[Harbor]] for parallel execution
- Represents the type of "new and precise" eval that still measures frontier capabilities, unlike saturated benchmarks like [[SWEBench]]

## Related
- [[Benchmarking Agents]] — framework that cites Terminal Bench as exemplar
- [[Benchmark Thesis]] — the concept Terminal Bench exemplifies
- [[HarborEval]] — evaluation infrastructure shipped with Terminal Bench 2.0
- [[CLI for Agents]] — the broader concept of CLI as agent interface
- [[summary-20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI]] — source transcript
- [[summary-20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel]] — task quality noise findings
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source transcript (Cline's usage)
- [[Task Fidelity Scaling Laws]] — research on task quality impact
- [[Benchmark Noise from Task Quality]] — related concept
- [[Stanford]] — university that created TerminalBench
- [[Cline]] — coding agent that uses TerminalBench for evaluation
- [[Harbor]] — eval infrastructure used alongside TerminalBench
- [[SWEBench]] — saturated benchmark contrasted with TerminalBench
- [[Eval Heuristics]] — TerminalBench as example of new and precise eval
