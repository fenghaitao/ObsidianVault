---
title: "Harbor"
type: entity
tags: [tool, benchmark, terminal, evaluation-format]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
last_updated: 2026-06-30
---

## Definition
Harbor is a terminal bench format created by Nebius that provides a convenient interface for running coding agent evaluations and training on software engineering tasks.

## Key Information
- Terminal bench format used by [[Nebius]] for running evaluations
- SWE-Rehab and SWE-Rehab V2 datasets include adapters for Harbor
- Designed to be a convenient, standardized format for both evaluation and training workflows
- Used as the runtime format for [[SWERebench]] leaderboard evaluations
- Also developed by the Loda Institute for parallelized agent evaluation infrastructure
- Provides standardized configuration (Linux machines, RAM, CPU) defined in infrastructure for each task
- Enables splitting tasks (e.g., 89 from [[TerminalBench]]) to run in parallel, making the slowest task the limiting factor
- Used by [[Cline]] alongside [[Modal]] for running parallelized eval pipelines

## Related
- [[Nebius]] — creator
- [[SWERebench]] — leaderboard using Harbor
- [[TerminalBench]] — broader category of terminal-based benchmarks
- [[Cline]] — coding agent using Harbor for eval infrastructure
- [[Modal]] — compute platform used with Harbor
- [[summary-20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius]] — source transcript
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source transcript (Cline's usage)
