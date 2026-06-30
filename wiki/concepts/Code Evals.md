---
title: "Code Evals"
type: concept
tags: [eval, deterministic, testing, code]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Code evals are deterministic evaluation functions written in code (Python or TypeScript) that test AI agent outputs. They are the simplest, fastest, and cheapest type of eval — running in milliseconds at near-zero cost — and serve as the first line of defense in an eval suite.

## Key Information
- Deterministic functions that always produce the same result for the same input — fully reproducible
- Run in milliseconds and cost essentially nothing to execute
- Implemented as regular Python or TypeScript functions using Phoenix's `create_evaluator` decorator with `kind="code"`
- Use cases: JSON parsing validation, length limits, forbidden phrases (e.g., "as an AI language model"), required fields, regex pattern matching (e.g., stock ticker mentions), database queries for pricing verification, API calls for stock price checking
- Any task with a deterministic answer can use a code eval
- Example: checking if output mentions the expected stock ticker using regex — found 11/13 passes, revealing failures where the agent wrote to disk instead of output or confused AWS for Amazon
- Best practice: test what the agent produced, not the path it took. Don't verify specific tool call sequences — verify the final answer
- Be flexible in string parsing: "2 hours", "120 minutes", or "a very large number of seconds" all answer the same question
- Downside: brittle for complex or highly non-deterministic outputs — when outputs become too variable, LLM judges are needed
- Part of a layered defense: code evals catch basic issues first, then LLM judges handle semantic understanding, then humans review edge cases

## Related
- [[LLM-as-Judge]] — complementary eval type for semantic understanding
- [[Faithfulness Eval]] — built-in LLM eval
- [[Correctness Eval]] — built-in LLM eval
- [[Actionability Eval]] — custom LLM eval example
- [[Swiss Cheese Model]] — layered defense strategy
- [[Phoenix]] — platform supporting code evals
- [[EvalEngineering]] — practice of crafting eval prompts
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
