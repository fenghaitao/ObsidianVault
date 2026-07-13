---
title: "Evals Vs Production Monitoring"
type: concept
tags: [ai, evals, observability, product-development]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-11
---

## Definition

[[Kiriti Badam]]'s rejection of the "false dichotomy" that either evals or production monitoring alone can solve AI product reliability — his argument that the two are complementary tools catching different classes of problems, and that "this notion [that] only one of them is going to solve things for you... is completely dismissible."

## Key Information

- **Evals**: encode the team's trusted product knowledge — "this is what matters to me, this is the kind of problem my agent should not do" — into a concrete dataset. A team can't practically evaluate every production trace, so evals act as a pre-committed regression gate: does a new change break something already known to matter?
- **Production monitoring**: deploying the system and watching key metrics that reflect how real customers actually use it. Predates AI (it's existed for products "for a long time"), but AI systems require monitoring at much finer granularity, including implicit signals beyond explicit feedback — e.g. in [[ChatGPT]], a user "regenerating" an answer (rather than giving a thumbs-down) is a clear implicit signal the first answer didn't meet expectations.
- **Why you need both, in sequence**: no one deploys without some initial testing (an eval dataset of "wipes"/must-pass questions). Once deployed, especially at high transaction volume, you can't manually review every trace — production monitoring's implicit/explicit signals tell you *which* traces to examine. Once you spot a systematic failure pattern in those traces (e.g., an agent improperly offering refunds it was configured not to), *that's* when you build a new evaluation dataset targeting it — and even after fixing and shipping v2, "there is no guarantee this is the only problem you're going to see," so production monitoring keeps running to catch the next emerging pattern.
- **Practical implication for [[Codex]]** (OpenAI's coding-agent product), as an example of applying this in a complex, highly-customizable-by-design product: the team keeps targeted regression evals so a change doesn't break something core, but relies heavily on direct customer signal (social media, bug reports) and per-model "vibes" testing against a shared list of hard problems, because it's "extremely hard to build LLM judges" for the open-ended range of ways developers actually use a coding agent.
- Related terminological point: see [[Semantic Diffusion]] for why "eval" itself means different things to different practitioners, which fuels confusion about whether evals or monitoring "wins."

## Related

- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
- [[Kiriti Badam]] — articulates this argument
- [[Aishwarya Naresh Reganti]] — co-guest, extends the discussion to "eval" terminology confusion
- [[Semantic Diffusion]] — why "eval" is a contested, overloaded term
- [[Continuous Calibration Continuous Development]] — the broader framework this evals/monitoring loop sits inside
- [[Codex]] — worked example of applying both together on a highly customizable product
- [[Evals As Product Definition]] — related concept (from a different episode) on using a small eval set to define feature success
