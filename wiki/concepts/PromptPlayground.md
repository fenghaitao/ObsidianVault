---
title: "PromptPlayground"
type: concept
tags: [prompt-engineering, iteration, tooling, development]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md"]
last_updated: 2026-06-25
---

## Definition
A Prompt Playground is an interactive interface for iterating on prompts using production data. It combines prompt templates with real input variables, allowing PMs and engineers to tweak prompts and see outputs without touching production code.

## Key Information
- Key capability: take a production trace, pull its prompt template and variables into the playground, and iterate without code changes.
- Supports versioning: save prompt versions, duplicate them, and compare outputs across versions.
- Allows changing the model (e.g., GPT-4o to GPT-4.1 mini) and prompt variables independently.
- Aman Khan argues PMs should control prompts because they are ultimately responsible for the product outcome — the playground gives them that control.
- Integrated with Arize's platform: playground prompts can be saved to a prompt hub and used by engineering in production code.
- Can also host eval prompts, enabling the same iteration workflow for improving LLM-as-judge systems.

## Related
- [[Arize]] — platform providing the prompt playground
- [[EvalEngineering]] — eval prompts can be iterated in the playground
- [[AIPM]] — the role that benefits from prompt playground access
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
