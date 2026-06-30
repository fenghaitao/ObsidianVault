---
title: "Stop Fighting the Model"
type: concept
tags: [agents, llm, workflow, prompt-engineering, flexibility]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition

Stop Fighting the Model is the principle that agent builders should not force LLMs into rigid, step-by-step workflows that mirror traditional deterministic software. Instead, they should leverage the model's native ability to understand goals and adapt dynamically, providing guidance rather than prescription.

## Key Information

- **Articulated by Philipp Schmid** as a core principle for agent building
- **The trap**: Engineers accustomed to deterministic systems try to enforce specific workflows: "Step 1 do this, Step 2 do the other thing." This fights against the model's strength — its ability to reason about goals and adapt
- **Why it fails**: LLMs are non-deterministic reasoning engines, not procedural execution engines. Forcing rigid steps constrains their ability to find optimal paths and handle edge cases
- **Guidance over prescription**: Provide goals, constraints, and principles rather than step-by-step instructions. Let the model figure out the how
- **The dispatcher model**: Define where you want to go, not exactly which roads to take. The agent may find better routes than you would prescribe
- **Trust the model's reasoning**: Modern LLMs are capable of sophisticated planning and adaptation. Over-constraining them reduces their effectiveness
- **Related to prompt engineering**: Good prompts guide the model's reasoning without micromanaging. Bad prompts try to program the model like a deterministic system

## Related

- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker
- [[Handing Over Control]] — the broader principle this supports
- [[Traffic Controller vs Dispatcher]] — the metaphor illustrating this shift
- [[Trust But Verify]] — complementary: guide don't prescribe, but verify outcomes
- [[Non-Deterministic Agents]] — the technical reality behind this principle
- [[Guide Dont Prescribe]] — closely related principle from harness engineering
