---
title: "Trust But Verify"
type: concept
tags: [verification, engineering-management, quality, ai-coding]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork).md"]
last_updated: 2026-07-10
---

## Definition

Trust but verify is [[Fiona Fung]]'s stated philosophy for working with AI-generated code and output at [[Anthropic]]: the underlying models are described as very capable, but there remain areas — particularly ones requiring deep subject-matter/systems expertise — that still need active human verification rather than blind trust.

## Key Information

- Directly shapes hiring on the [[Claude Code]] team: alongside creative builders with product sense, Fung specifically hires deep systems/distributed-systems experts for "whatever are the parts that it's all about trust but verify" — areas where verification still requires deep expertise.
- Framed as the reason coding is no longer the bottleneck but verification is: as throughput rises roughly 8x and more disciplines (not just engineers) check in code, "how do we think about verification?" becomes the central open question.
- Manifests concretely as: checking specs/frameworks ("what good looks like") into the repo so automated [[Claude Code]] review can validate against them; the [[Bad Vs Sad Framework|bad-vs-sad]] quality framework for classifying failure severity; and investment in tests/evals/monitoring for earlier, more proactive detection rather than relying on manual review alone.
- Also invoked in the context of engineer skill retention: Fung says engineers should still take time to understand the architecture/dependencies they rely on ("always take that time to learn about your dependencies") even as AI does more of the implementation work, because that understanding is what makes trust-but-verify possible at all.
- Connected to extending autonomy: Fung notes that as verification quality improves for a given workflow, the team can grant agents more autonomy ("if the verification is really good, go for it") — i.e., verification capability is the gating factor for how much agency can safely be extended.

## Related

- [[summary-04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork)]] — source summary
- [[Fiona Fung]] — states this philosophy
- [[Anthropic]] — organizational context
- [[Claude Code]] — where this philosophy is applied to code review and hiring
- [[Bad Vs Sad Framework]] — concrete quality framework supporting verification
- [[High Agency High Accountability]] — related value; verification quality gates how much agency can be extended
