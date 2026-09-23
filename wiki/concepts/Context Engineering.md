---
title: "Context Engineering"
type: concept
tags: [AI, prompting, LLM, Anthropic]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar.md"]
last_updated: 2026-09-23
---

## Definition

Context engineering is deliberately building up everything a model relies on — skills, data, harness, examples, memory, and accumulated prior work — so that a small prompt carries the context needed to act well.

## Key Information

- Thariq's framing: "prompting is a little bit more than just a prompt you put in… it's everything you've done before that builds up into your context."
- Outside observers sometimes see small prompts and mistake them for the whole picture, missing the harness, verification, and skills already built around them.
- Core onboarding principle: "if you treat Claude like a thought partner and give it the context that you need, then you can usually figure out the next steps."
- Practical examples: annotate a feature with events so Claude can read them; run a morning loop to check which events fired and propose improvements; compile a pre-1:1 report from Slack/GitHub/PR activity.
- As models get more imaginative and better at sticking to intention, heavy example-laden prompting is needed less — but context about goals, domain, and taste is what compounds over time.

## Related

- [[Prompt Engineering]]
- [[Harness Engineering]]
- [[Loop Engineering]]
- [[Claude]]
- [[Thariq Shihipar]]
- [[summary-20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar]]
