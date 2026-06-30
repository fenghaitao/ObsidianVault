---
title: "Haiku"
type: entity
tags: [model, llm, anthropic, claude]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition

Haiku refers to Claude Haiku, Anthropic's smaller, faster, and less expensive model tier. In the context of Cursor's work tree feature, Haiku is noted for frequently deviating from instructions and working outside its designated work tree.

## Key Information

- Described by David Gomes as a "smaller, less intelligent model" that "will very often deviate and start working in the primary checkout"
- Used as a baseline in work tree evals — its poor performance contrasts with stronger models like Composer and Grok
- Demonstrates the "vibes-based safety" problem: weaker models are less reliable at following markdown-based isolation instructions
- Laurie Voss deliberately chose Haiku as the agent model in his eval workshop because it is "reliably dumb" — cheap, fast, and makes mistakes that give evaluators something to test against
- In the workshop, Haiku powered a financial analysis agent with two sub-agents (research + write report), making errors like writing to disk instead of output, confusing AWS for Amazon, and producing non-actionable reports

## Related

- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
- [[Cursor]] — the product
- [[Anthropic]] — the company behind Claude Haiku
- [[AgentIsolation]] — the problem Haiku struggles with
- [[VibesBasedSafety]] — the trust-based approach Haiku fails at
- [[Sonnet]] — more capable model used as judge in the workshop
