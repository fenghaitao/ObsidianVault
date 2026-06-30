---
title: "Guide Dont Prescribe"
type: concept
tags: [agentic-engineering, skills, evals, prompt-engineering, workos]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-30
---

## Definition

"Guide, don't prescribe" is an agentic engineering principle articulated by Nick Nisi (WorkOS): provide agents with targeted gotchas and hints about common pitfalls rather than comprehensive documentation or exhaustive instructions. The model already knows how to code — it just needs to know the landmines in your specific product.

## Key Information

- Coined by Nick Nisi based on the experience of deleting 95% of agent skills (10,000+ lines → 553 lines) and getting better results
- Core insight: AI models already know how to code. Comprehensive docs-based skills send the model on "wild goose chases" by having it check too many things
- The 95% deletion was validated by evals: a specific skill achieved 77% accuracy, but the same task without the skill achieved 97%
- 553 lines of gotchas cover only the most common pitfalls identified through repeated eval runs
- Example gotcha: "When working in Next.js and you're in the proxy, do this. If you're not in the proxy, you can't call redirects."
- Contrast with "prescribe" approach: generating skills from entire documentation sections (10,000+ lines), which overwhelmed the model with irrelevant information
- Eval results: 6 minutes per run with gotchas vs. 68 minutes with comprehensive skills
- For product builders: figure out what agents get reliably wrong about your product and focus on those gotchas only

## Related

- [[summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS]] — source
- [[NickNisi]] — coined the term
- [[Gotchas]] — the implementation of this principle
- [[Skills]] — the mechanism that can hurt if overused
- [[Enforce Dont Instruct]] — the companion principle for enforcement
- [[EvalPrimitives]] — measurement that validated this approach
- [[Agentic Experience]] — the product design philosophy this supports
