---
title: "Model Prompting Styles"
type: concept
tags: [ai, llm, prompting, gpt, claude, prompt-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md"]
last_updated: 2026-06-29
---

## Definition

Model Prompting Styles refers to the observation that different AI model families respond differently to the same prompting conventions. Michael Arnaldi notes that GPT models perform better with lowercase, calm prompts while Claude/Opus models respond better to uppercase, emphatic instructions. This has implications for shared configuration files like agents.md and pattern files.

## Key Information

- **GPT models**: Use lowercase prompts — GPT "gets scared" if you scream at it, becoming passive and overly agreeable, which deoptimizes performance
- **Claude/Opus models**: Use uppercase for emphasis — Claude pays more attention to capitalized, emphatic instructions
- This difference means the agents.md standard is "kind of not a standard" because the same file works differently across models
- GPT 5.4 is more concise than Opus — the same task with Opus would produce 200 lines of agents.md vs much shorter with GPT
- Opus tends to take shortcuts (e.g., `as any`); GPT takes longer but output is often better
- No single model is universally better — sometimes one one-shots a solution the other couldn't solve for half a day
- Open weights models lag frontier models by 3-6 months
- Michael Arnaldi switched from Anthropic to OpenAI after Anthropic restricted usage of open-source coding agents
- Implication: pattern files and agents.md should ideally be generated per-model or per-model-family
- Effectful is considering a CLI that asks "which model do you use?" and optimizes context accordingly

## Related

- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source
- [[Michael Arnaldi]] — made the observations
- [[AgentsDotMd]] — the file format affected by these differences
- [[Pattern Files (AI)]] — should be generated per-model
- [[OpenAI]] — GPT model family
- [[Anthropic]] — Claude model family
- [[Vibe Engineering]] — the methodology that accounts for these differences
