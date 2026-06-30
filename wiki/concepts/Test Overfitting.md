---
title: "Test Overfitting"
type: concept
tags: [evaluation, testing, benchmark-quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius.md"]
last_updated: 2026-06-30
---

## Definition
Test overfitting in benchmark evaluation occurs when verifier tests are too tightly coupled to a specific implementation, causing correct but differently-styled solutions to fail.

## Key Information
- **Common in human-written tests**: Developers typically write tests after implementing solutions, making them implicitly over-fitted to their specific approach.
- **Example from SWE-rebench**: A test required the agent to generate an exact substring in an error message. Even a functionally correct solution would fail if it produced a different error message format.
- **Impact**: Reduces benchmark validity by penalizing valid alternative implementations.
- **Detection**: Often only visible after running multiple models/agents against tasks and analyzing failure patterns.
- **Mitigation**: Manual verification of tasks, oversampling (collecting ~10% more tasks than needed for final runs), and analyzing results across multiple model families.

## Related
- [[SWE-rebench]] — benchmark dealing with this issue
- [[Code Quality in Agentic Patches]] — related problem of agent output quality
- [[Benchmark Decontamination]] — related benchmark quality concern
- [[summary-20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius]] — source transcript
