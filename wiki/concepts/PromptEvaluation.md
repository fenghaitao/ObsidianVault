---
title: "Prompt Evaluation"
type: concept
tags: [prompting, testing, evaluation, quality-assurance, iteration]
sources: [raw/01-articles/claude/2024-07-09 - Evaluate prompts in the developer console.md, raw/01-articles/claude/2024-10-14 - Improve your prompts in the developer console.md]
last_updated: 2026-06-28
---

## Definition

Prompt evaluation is the systematic process of testing and measuring prompt quality through structured test cases, output comparison, and expert assessment. It bridges the gap between prompt development and production deployment by providing concrete feedback signals for iterative refinement.

## Core Workflow

### Test Suite Development
- Create diverse test cases representing real-world inputs
- Define expected or acceptable output criteria
- Organize test cases for comprehensive coverage
- Use automated test case generation to speed up suite creation

### Execution & Comparison
- Run test suites against prompt variants
- Compare outputs side-by-side across multiple prompt versions
- Identify which variations produce better results
- Iterate quickly based on concrete evidence rather than intuition

### Grading & Assessment
- Subject matter experts grade responses on a 5-point scale
- Aggregate grades across test cases to measure overall improvement
- Track quality metrics across prompt iterations
- Build confidence in production readiness
- **Ideal output specification**: Optional "ideal output" column allows users to specify expected or benchmark outputs for each test case, enabling consistent and objective evaluation of model outputs

## Benefits Over Manual Testing

| Manual approach | Evaluation framework |
|---|---|
| Spreadsheet management | Centralized console |
| Anecdotal comparison | Side-by-side output view |
| Ad-hoc grading | Structured expert assessment |
| Slow iteration | Rapid test-and-measure loops |
| Difficult reproducibility | Reproducible, auditable results |

## Integration with Prompt Engineering

[[PromptEvaluation]] complements [[PromptEngineering]] by:
- Providing data-driven feedback for prompt refinement
- Replacing intuition-based tweaking with measured improvement
- Creating feedback loops that reduce the expertise barrier (less need for LLM knowledge)
- Enabling team collaboration through expert grading

## Tools & Platforms

- [[AnthropicConsole]] — primary platform offering integrated evaluation workflows
- Anthropic docs: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview

## Related

- [[PromptEngineering]] — broader discipline of prompt design
- [[TestCaseGeneration]] — automated test case creation for evaluation
- [[AnthropicConsole]] — platform for evaluation workflows
- [[summary-2024-07-09 - Evaluate prompts in the developer console]] — announcement of console evaluation features
- [[summary-2024-10-14 - Improve your prompts in the developer console]] — ideal output feature for evaluation and prompt improver integration
