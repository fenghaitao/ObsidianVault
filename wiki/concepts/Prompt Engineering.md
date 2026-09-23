---
title: "Prompt Engineering"
type: concept
tags: [AI, prompting, LLM, engineering]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar.md"]
last_updated: 2026-09-23
---

## Definition

Prompt engineering is the skill of directing a model to produce good output — spanning the literal prompt, giving permission, providing references, and adapting to each model's quirks.

## Key Information

- Thariq argues that mastering today's specific model is not durable, but the meta-skill of learning how to work with models is: you re-learn each new model much faster.
- Prompts are more than the text: they include skills, added data, and accumulated context built beforehand.
- Each model is "its own almost organic digital thing" with quirks you learn and then must unlearn.
- Example of unlearning: Anthropic removed ~80% of Claude Code's system prompt; examples in tool descriptions (once the only way to get good output) are now mostly negative because models are more imaginative and stick to intention better.
- Practical tips from the episode: give the model permission to spend compute / use subagents / workflows; say "don't do work yet, brainstorm with me" to force planning; "believe in yourself" really means "you're allowed to use compute."
- Models default to what the average user wants — respond and start work fast — so you must nudge how much planning and compute to spend.
- Verification of prompt changes uses user metrics, internal/external evals, and reported internal behavior (e.g., "Claude told the user to go to sleep" — no eval exists for that).

## Related

- [[Context Engineering]]
- [[Harness Engineering]]
- [[Claude]]
- [[Claude Code]]
- [[Thariq Shihipar]]
- [[summary-20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar]]
