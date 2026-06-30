---
title: "Gotchas"
type: concept
tags: [agentic-engineering, skills, prompt-engineering, evals, workos]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-30
---

## Definition

Gotchas are targeted, concise hints about common pitfalls in a specific product or framework, used as an alternative to comprehensive documentation-based agent skills. They focus on what agents reliably get wrong rather than covering everything.

## Key Information

- Articulated by Nick Nisi after discovering that 10,000+ lines of docs-based skills produced worse results than 553 lines of gotchas
- Core insight: AI models already know how to code — they just need to know where the landmines are in your specific product
- Example gotcha: "When working in Next.js and you're in the proxy, do this. If you're not in the proxy, you can't call redirects."
- Eval results: 6 minutes per run with gotchas vs. 68 minutes with comprehensive skills; higher accuracy with gotchas
- A specific skill achieved 77% accuracy on a task, while the same task without any skill achieved 97% — the skill was actively harmful
- Gotchas are discovered through repeated eval runs, not by trying to cover documentation comprehensively
- For product builders: figure out what agents get reliably wrong about your product and write gotchas for those specific issues only
- Contrast with comprehensive skills: gotchas guide the model without prescribing or overwhelming it
- The gotchas approach is the implementation of "guide, don't prescribe"

## Related

- [[summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS]] — source
- [[NickNisi]] — coined the approach
- [[Guide Dont Prescribe]] — the principle gotchas implement
- [[Skills]] — the mechanism gotchas replaced
- [[EvalPrimitives]] — how gotchas are discovered and validated
- [[Agentic Experience]] — the product design context
- [[Retrospective Agent]] — the mechanism that captures gotchas automatically
- [[Case]] — agent harness that uses gotchas via memory
- [[WorkOS CLI]] — product using gotchas for agent guidance
