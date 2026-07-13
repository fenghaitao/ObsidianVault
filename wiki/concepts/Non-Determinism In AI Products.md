---
title: "Non-Determinism In AI Products"
type: concept
tags: [ai, product-development, llm]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-11
---

## Definition

[[Aishwarya Naresh Reganti]] and [[Kiriti Badam]]'s framing of the first fundamental difference between AI products and traditional software: builders are working with a non-deterministic API on both the input side (unpredictable natural-language user intent) and the output side (a prompt-sensitive, black-box LLM), rather than the well-mapped, predictable decision engine of conventional software.

## Key Information

- **Traditional software comparison**: a product like booking.com has a well-mapped decision engine — a user's intention ("book a hotel in San Francisco for two nights") is converted into a fixed sequence of buttons/forms/options that reliably completes the intention the same way every time.
- **What changes with AI products**: the interaction layer becomes fluid, mostly natural language, so users can express the same intention in effectively unlimited ways — the input side becomes unpredictable. Simultaneously, the output comes from an LLM, which is "pretty sensitive to prompt phrasings" and largely a black box, so the output surface is also unpredictable.
- **Net effect**: "you're now working with an input, output, and a process... and you don't understand all the three very well. You're trying to anticipate behavior and build for it." This compounds further once agentic systems are introduced — see [[Agency Control Trade-off]].
- **The upside, not just the downside**: Badam frames natural language as "the most beautiful part of AI" — the bar to using AI products is lower because conversing is more natural than clicking through buttons — but this same fluidity is exactly why intent is harder to reliably capture and route to a deterministic outcome.
- Cited as the reason a traditional software life cycle (fixed PM/engineer/data-team handoffs, each optimizing their own separate feedback loop) breaks down for AI products — teams increasingly need to sit together and review agent traces jointly rather than working from separate specs.
- Serves as the root justification for staged-autonomy product design (see [[Continuous Calibration Continuous Development]]) and for treating evals/production monitoring as complementary tools for taming an otherwise unpredictable system (see [[Evals Vs Production Monitoring]]).

## Related

- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
- [[Aishwarya Naresh Reganti]] — co-articulates this concept
- [[Kiriti Badam]] — co-articulates this concept
- [[Agency Control Trade-off]] — the paired second difference between AI and traditional software
- [[Continuous Calibration Continuous Development]] — the development framework built around managing this unpredictability
- [[Evals Vs Production Monitoring]] — the two complementary tools used to observe non-deterministic system behavior
