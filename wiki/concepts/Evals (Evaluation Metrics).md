---
title: "Evals (Evaluation Metrics)"
type: concept
tags: [AI, evaluation, testing, LLM, product-development]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-10
---

## Definition

Evals (evaluation metrics) are datasets and tests used to measure AI system performance against expected behavior. They encode trusted product thinking into testable datasets. However, evals only catch errors you already know about — they cannot anticipate emerging production patterns. The term has suffered from semantic diffusion, meaning different things to different stakeholders.

## Key Information

- **What evals are**: Your trusted product knowledge encoded into datasets — "this is what matters to me, this is the kind of problems my agent should not do."
- **What evals are NOT**: LM Arena benchmarks, Artificial Analysis benchmarks — those are model selection tools, not evals. "You're not doing eval. That's not eval. Those are model selection."
- **The false dichotomy**: "Either evals will solve everything or production monitoring will solve everything." Both are needed — neither alone is sufficient.
- **Evals catch known errors**: They test against what you already know could go wrong. They are essential for regression testing before deploying changes.
- **Production monitoring catches unknowns**: Implicit and explicit user signals catch emerging patterns you never anticipated.
- **The feedback loop**: Production monitoring surfaces failure patterns → examine those traces → build eval datasets for the patterns that matter → deploy with evals → still need production monitoring for new unknowns.
- **Semantic diffusion**: The term "evals" has been diluted — data labeling companies say "experts write evals" (meaning error analysis), PMs are told to "write evals" (meaning product specs), some say "evals are everything" (meaning the entire feedback loop). [[Martin Fowler]] coined "semantic diffusion" to describe this phenomenon.
- **LLM judges**: One form of eval — using an LLM to score another LLM's outputs. But for complex use cases, LLM judges miss emerging patterns and you end up building too many of them.
- **When to build evals vs. use user signals**: For complex use cases where you see many emerging patterns, it may make more sense to look at user signals, fix issues, and check for regressions rather than building comprehensive LLM judges.
- **Codex approach**: Balanced — evals for core product safety ("at least don't damage something core") + heavy customer feedback monitoring + social media listening.

## Related

- [[Production Monitoring (AI)]] — complementary to evals
- [[LLM Judges]] — a specific form of eval
- [[Semantic Diffusion]] — why the term is confusing
- [[Continuous Calibration Continuous Development (CCCD)]] — framework where evals play a role
- [[Behavior Calibration]] — the calibration process that evals support
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
