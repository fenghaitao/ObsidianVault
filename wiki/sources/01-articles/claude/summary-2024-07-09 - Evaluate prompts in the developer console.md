---
title: "Evaluate prompts in the developer console"
type: source
tags: [prompt-engineering, console, testing, evaluation]
sources: [raw/01-articles/claude/2024-07-09 - Evaluate prompts in the developer console.md]
last_updated: 2026-06-28
---

## Summary

Anthropic released new prompt evaluation features in the [[AnthropicConsole]], enabling developers to generate, test, and evaluate prompts without leaving the development environment. The feature set includes automatic [[TestCaseGeneration]], side-by-side output comparison, and expert grading workflows.

## Key Features

### Prompt Generation
- Built-in prompt generator powered by Claude 3.5 Sonnet
- Describe a task (e.g., "Triage inbound customer support requests")
- Claude automatically generates a high-quality starting prompt
- Significantly reduces the time to craft initial prompts

### Test Case Generation
- Automatic generation of input variables for testing
- Examples: generating sample customer support messages for a triage task
- Manual entry option for test cases
- CSV import capability
- Adjustable generation parameters for granular control

### Prompt Evaluation Workflow
- Run test suites directly in the console
- Create multiple prompt versions and re-run tests against each
- Side-by-side output comparison for different prompt variants
- 5-point scale grading by subject matter experts
- Faster iteration cycle than manual spreadsheet management

## Value Proposition

- **Quality impact**: Prompt quality significantly impacts AI application results
- **Accessibility**: Reduces expertise barrier — users don't need deep LLM knowledge
- **Iteration speed**: Consolidates multi-step workflow (task description → prompt generation → test suite creation → evaluation) into the console
- **Confidence**: Testing against real-world inputs before production deployment builds quality confidence
- **Comparison-driven improvement**: Side-by-side output comparison and expert grading create concrete feedback signals for refinement

## Availability & Integration

- Available to all Anthropic Console users (no paywall mentioned)
- Documentation available in Anthropic docs portal
- Integration point: [[PromptEngineering]] workflow in the broader Anthropic ecosystem

## Related

- [[PromptEngineering]] — the broader discipline of designing effective prompts
- [[PromptEvaluation]] — the evaluation methodology
- [[TestCaseGeneration]] — automatic test case generation for prompts
- [[AnthropicConsole]] — the developer console platform
- [[Anthropic]] — the company behind the console
