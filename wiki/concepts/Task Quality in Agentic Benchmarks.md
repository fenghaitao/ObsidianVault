---
title: "Task Quality in Agentic Benchmarks"
type: concept
tags: [data-quality, benchmarks, agentic-tasks, evaluation, task-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel.md"]
last_updated: 2026-06-30
---

## Definition
Task Quality in Agentic Benchmarks is a framework for evaluating the quality of agentic benchmark tasks using four criteria: achievable, non-trivial, functionally correct, and environment reliable. Tasks meeting all criteria are "accepted" (high-quality); those failing any are "rejected" (low-quality). The framework was developed and empirically validated by Snorkel as part of their task fidelity scaling laws research.

## Key Information
- **Four criteria**: (1) Achievable — the task can actually be completed, (2) Non-trivial — it requires meaningful effort, (3) Functionally correct — the task logic plays as expected with tests matching the requested behavior, (4) Environment reliable — the containerized environment is stable and reproducible
- **Verification process**: Snorkel built a research harness with tests that verify all four criteria. Tasks passing all tests are accepted; failing any are rejected
- **Quality signals**: Accepted tasks showed 2x more tool calls, lower pass rates, and more output tokens — indicating genuine difficulty rather than environmental noise
- **Failure mode distinction**: Accepted tasks produce "cleaner" failures — failures due to genuine task difficulty rather than underspecification or environmental problems. Rejected tasks overrepresent logic errors and environmental failures
- **Training impact**: RL training with accepted tasks produced ~6% improvement vs ~1% with rejected tasks (5x difference)
- **Containerization**: Tasks run in containerized environments for reproducibility, isolation, and parallelization for rollouts
- **Application scope**: Framework applies to terminal-bench-style tasks in containerized environments, such as those evaluated by Harbor framework and OpenEnv

## Related
- [[Task Fidelity Scaling Laws]] — the empirical research validating this framework
- [[Underspecification in Agentic Tasks]] — common cause of rejected tasks
- [[Benchmark Noise from Task Quality]] — consequence of low-quality tasks in benchmarks
- [[Snorkel]] — company that developed the framework
- [[summary-20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel]] — source transcript
- [[TerminalBench]] — benchmark affected by task quality issues
- [[Expert in the Loop]] — approach for ensuring task quality
- [[AgentHarness]] — related concept for agent evaluation infrastructure
