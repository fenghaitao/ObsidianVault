---
title: "LLM Judges"
type: concept
tags: [AI, evaluation, LLM, testing]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-10
---

## Definition

LLM judges are automated evaluation systems that use one LLM to score or assess the outputs of another LLM. They are one form of eval, but have limitations: for complex use cases, they miss emerging patterns and teams can end up building too many of them.

## Key Information

- A form of eval — using an LLM to evaluate another LLM's outputs
- PMs being told to "write evals" doesn't mean they need to write an LLM judge good enough for production
- **Limitation**: When you build an LLM judge for a specific concern (e.g., verbosity), you discover newer patterns that the judge can't catch
- **The trap**: You end up building too many LLM judges chasing emerging patterns
- **Alternative**: At some point, it makes more sense to look at user signals, fix issues, and check for regressions rather than building comprehensive LLM judges
- **Context matters**: Whether to use LLM judges depends on the application — for complex use cases with many emerging patterns, they're less effective
- Lawyers and doctors writing "evals" doesn't mean they're building LLM judges — they're doing error analysis

## Related

- [[Evals (Evaluation Metrics)]] — the broader category LLM judges belong to
- [[Production Monitoring (AI)]] — alternative/complement to LLM judges
- [[Implicit User Signals]] — what to use instead of excessive LLM judges
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
