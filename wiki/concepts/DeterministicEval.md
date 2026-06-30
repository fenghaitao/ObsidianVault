---
title: "Deterministic Eval"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Deterministic Eval is an evaluation approach that uses code-based, rule-driven scoring functions to assess agent outputs against objective criteria, as opposed to [[LLM-as-Judge]] which uses language models for subjective assessment. It is applied to failure modes that can be measured deterministically without relying on non-deterministic LLM judgment.

## Key Information

- **Nature**: Code-based scoring functions that produce consistent, repeatable results
- **Contrast with LLM-as-Judge**: Deterministic evals are reliable and objective; LLM-as-judge is non-deterministic and requires its own evaluation
- **When to use**: For objective, measurable failure modes where a rule can be clearly defined

### Example Use Cases

- **Tool call count**: Fail the eval if the agent uses too many tool calls (cost/resource concern)
- **Token usage**: Fail the eval if the agent consumes too many tokens (cost concern)
- **Output format**: Validate that the output conforms to a specific schema or format
- **Presence/absence checks**: Verify specific required elements exist in the output
- **Numerical constraints**: Check that numerical outputs fall within expected ranges

### Relationship to LLM-as-Judge

- Deterministic evals complement LLM-as-judge — they are not competitors
- Some failure modes are objective (lend themselves to deterministic scoring), others are subjective (require LLM-as-judge)
- Deterministic evals provide reliable signals; LLM-as-judge provides coverage for subjective dimensions
- A mature eval strategy uses both in combination, targeting each to its appropriate failure mode

## Related

- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — source
- [[LLM-as-Judge]] — complementary non-deterministic evaluation approach
- [[EvalPrimitives]] — scoring functions as one of the three eval components
- [[EvalPracticePhases]] — Phase 2 where both deterministic and LLM-as-judge scoring are introduced
- [[Code Evals]] — related concept of code-based evaluation
- [[FailureModeAnalysis]] — identifying which failure modes are objective vs subjective
