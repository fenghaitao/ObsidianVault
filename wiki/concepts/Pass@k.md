---
title: "Pass@k"
type: concept
tags: [evaluation, metric, benchmark, coding-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius.md"]
last_updated: 2026-06-30
---

## Definition
Pass@k is an evaluation metric measuring whether a coding agent successfully solves a task in at least k out of N independent runs, providing a more nuanced view of capability than single-run pass/fail rates.

## Key Information
- **Pass@5**: Task is considered successful if the agent solves it in at least 1 out of 5 runs. Measures potential — whether the model can solve the task at all, accounting for non-determinism.
- **Pass all 5**: Task is considered successful only if the agent solves it in all 5 runs. Measures reliability — whether the model consistently solves the task.
- **Used in SWE-rebench**: 5 runs per task with confidence intervals reported, alongside mean resolved rate, tokens per problem, and tries per problem.
- **Value**: Accounts for non-deterministic agent behavior, distinguishing between models that can occasionally solve a task from those that reliably do so.
- **Trade-off**: Pass@5 captures model potential but may overstate practical reliability; pass all 5 captures reliability but may understate capability.

## Related
- [[SWERebench]] — benchmark using this metric
- [[Trajectory Analysis]] — complementary analysis approach
- [[summary-20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius]] — source transcript
