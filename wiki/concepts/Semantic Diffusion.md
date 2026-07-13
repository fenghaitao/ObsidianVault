---
title: "Semantic Diffusion"
type: concept
tags: [terminology, ai, evals]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-11
---

## Definition

A term [[Aishwarya Naresh Reganti]] attributes to Martin Fowler (originating around the 2000s): when a term becomes popular, different communities each adopt it and "butcher it with their own definitions," until the original precise meaning is lost. Reganti applies it to explain why the word "eval" now means different, sometimes incompatible things to different practitioners in AI.

## Key Information

- Cited directly in response to the observation that "eval" has had to carry enormous conceptual weight in AI discourse through 2025 — data-labeling companies claim "our experts write evals," commentators say "PMs should be writing evals, they're the new PRDs," and others claim evals are effectively the entire product feedback loop.
- Reganti's resolution: these aren't contradictory, they're describing different parts of the same process wearing the same overloaded label. A data-labeling company's experts "writing evals" typically means error analysis / annotated judgment notes, not building an LLM judge; "PMs writing evals" doesn't mean PMs build production-grade LLM judges either.
- Illustrated with a concrete anecdote: a client told Reganti "we do eval," but when asked to show the dataset, said they just checked LM Arena and Artificial Analysis (independent model benchmarks) — which Reganti says is not evaluation of your own product at all, just model selection via public benchmarks.
- Reganti's broader point: rather than getting stuck debating what "eval" precisely means, practitioners should agree on the underlying need (an actionable feedback loop for the AI product) and let the specific tooling (LLM judges, production monitoring, benchmarks, error analysis) depend on context — "don't be obsessed with prescriptions, they're going to change."
- Directly feeds the episode's "false dichotomy" argument that evals and production monitoring are complementary, not competing — see [[Evals Vs Production Monitoring]].

## Related

- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
- [[Aishwarya Naresh Reganti]] — introduces this term in the episode
- [[Evals Vs Production Monitoring]] — the concrete debate this term is used to defuse
- [[Continuous Calibration Continuous Development]] — the framework that operationalizes "evaluation metrics" precisely to avoid this ambiguity
