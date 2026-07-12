---
title: "Non-determinism in AI Products"
type: concept
tags: [AI, product-design, LLM, software-engineering]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-10
---

## Definition

Non-determinism in AI products refers to the fundamental unpredictability on both the input side (users can express intentions in countless natural language variations) and the output side (LLMs are probabilistic, sensitive to prompt phrasing, and behave as black boxes). This is the key difference between AI and traditional software products.

## Key Information

- **Input non-determinism**: Users communicate intentions through natural language, which can be expressed in countless ways — unlike traditional software where users click through predetermined buttons, options, and forms. You don't know how your user will behave with your product.
- **Output non-determinism**: LLMs are probabilistic APIs — they are sensitive to prompt phrasings and are essentially black boxes. You don't know how the AI will respond to any given input.
- **Process non-determinism**: With agentic systems, the AI makes multi-step decisions, compounding the unpredictability.
- In traditional software (e.g., booking.com), you have a well-mapped decision engine — user intention → specific action via buttons/forms. In AI products, this layer is replaced by a fluid natural language interface.
- The bar to using AI products is lower because natural language is intuitive, but the challenge is that you need to achieve deterministic outcomes with non-deterministic technology.
- The non-determinism is "also the most beautiful part of AI" — users are more comfortable talking than following buttons.
- This is one of the two fundamental differences between AI and traditional software (alongside the [[Agency-Control Trade-off]]).

## Related

- [[Agency-Control Trade-off]] — the second fundamental difference
- [[Behavior Calibration]] — the process of managing non-determinism
- [[Continuous Calibration Continuous Development (CCCD)]] — framework for handling non-determinism
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
