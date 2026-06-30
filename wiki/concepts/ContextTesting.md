---
title: "ContextTesting"
type: concept
tags: [context, testing, evals, llm-as-judge, non-deterministic]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
Context Testing is the practice of validating AI context (prompts, skills, instructions) through multiple levels of testing, analogous to the testing pyramid in traditional software development. It spans from simple format validation (linting) to comprehension checks to LLM-as-judge evaluations to full end-to-end agent tests in sandboxes.

## Key Information
- Part of the Context Development Life Cycle (CDLC) Test phase, introduced by Patrick Debois
- Multiple levels of testing:
  - **Linting**: Format validation — checking that skills have required fields (description, length limits), analogous to IDE squiggly lines
  - **Comprehension checks**: "Grammarly for context" — asking an LLM whether it understands the context, whether it's explicit enough, whether pieces are missing
  - **LLM-as-judge evaluations**: Asking an LLM to judge whether generated code follows rules specified in the context (e.g., "does every API endpoint use the /awesome prefix?")
  - **End-to-end tests**: Giving the LLM-as-judge tools (sandbox access) to actually run the generated code and verify behavior, not just inspect the code
- Context tests are non-deterministic because LLM outputs vary — tests must be run multiple times and success rates measured
- Context tests can be run in CI/CD, but require error budgets since exact pass/fail is unreliable
- Enables context optimization: when tests fail, use the feedback to improve the context

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextDevelopmentLifeCycle]] — the Test phase
- [[NonDeterministicTesting]] — key challenge in context testing
- [[ErrorBudgetsForContext]] — CI/CD approach for non-deterministic tests
- [[LLM-as-Judge]] — evaluation method used in context testing
- [[EvalEngineering]] — practice of crafting effective eval prompts
- [[ContextOptimization]] — using test feedback to improve context
