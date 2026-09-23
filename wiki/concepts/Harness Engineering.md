---
title: "Harness Engineering"
type: concept
tags: [AI, agents, engineering, Anthropic]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar.md"]
last_updated: 2026-09-23
---

## Definition

Harness engineering is the work of building the scaffolding around a model — permission classifiers, sandboxing, artifacts, workflows, and verification — so the model can do more, more safely. Thariq Shihipar argues it grows in importance and complexity as the models themselves improve.

## Key Information

- The model-vs-harness distinction: the model is necessary but not sufficient; the harness is what lets the model act on tasks and represents its work.
- Counterintuitive claim: "the models get better and better, so the harness needs to become more and more complicated to allow the model to do more things" — not less.
- Concrete examples: auto mode (a classifier that runs after every task to replace manual permission prompts, so Claude can run for hours safely), sandboxing, workflows, and artifacts.
- Artifacts are themselves a form of prompting — there are many ways Claude could represent completed work, and the harness steers which representation it produces.
- "Harness engineering is definitely this mix of science and art… very unintuitive in a lot of different ways."
- Load-bearing harness components (auto mode, workflows) are genuinely complicated software; ironically, harnesses have gotten harder to "vibe code" yourself even as models improved.
- A good harness is also a context/verification substrate: skills and a strong verification harness determine whether an autonomous loop can safely land changes.

## Related

- [[Anthropic]]
- [[Claude Code]]
- [[Claude]]
- [[Claude Tag]]
- [[Loop Engineering]]
- [[Context Engineering]]
- [[Prompt Engineering]]
- [[Agentic AI]]
- [[Vibe Coding]]
- [[Thariq Shihipar]]
- [[summary-20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar]]
