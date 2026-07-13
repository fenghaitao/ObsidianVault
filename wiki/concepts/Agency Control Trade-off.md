---
title: "Agency Control Trade-off"
type: concept
tags: [ai, agentic-systems, product-development, risk]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-11
---

## Definition

[[Aishwarya Naresh Reganti]] and [[Kiriti Badam]]'s term for the second of two fundamental ways AI products differ from traditional software (the first being [[Non-Determinism In AI Products|non-determinism]]): every time a product hands decision-making capability ("agency") to an agentic system, the builder relinquishes a corresponding amount of human control. Because the agent's reliability can't be verified up front, agency should be extended only in proportion to demonstrated trust.

## Key Information

- Framed as a deliberate design axis, not a one-time decision: "if you give your AI agent more agency... you're also losing some control, and you want to make sure that the agent... has earned that ability or has built up trust over time."
- Reganti's hiking analogy: you don't attempt to summit Half Dome on day one — you train incrementally in low-stakes settings first, building a "good grip" on current capabilities before adding tools/context and leaning into more agency.
- **Two illustrative examples of how to constrain autonomy**:
  - Customer support: start with the agent only suggesting responses to human agents (high control), graduate to direct customer-facing answers, then extend to consequential actions (issuing refunds, raising engineering feature requests) — see the worked example on [[Continuous Calibration Continuous Development]].
  - Insurance pre-authorization: low-risk approvals (e.g., routine blood tests/MRIs, easy to approve once patient info is known) can be automated sooner; high-risk decisions (e.g., authorizing invasive surgery) stay firmly human-in-the-loop.
- **Constraint axes are flexible**: autonomy can be limited by the number of actions the agent is allowed to take, by topic/domain (some domains are low-risk enough to fully automate, others aren't), or by other dimensions chosen jointly by product, engineering, and subject-matter experts depending on problem complexity.
- **Benefits beyond risk reduction**: starting with low agency forces teams to articulate the actual problem being solved (see [[Problem First Approach]]) rather than getting seduced by solution complexity; it also generates a "flywheel" of logged human behavior (what humans accepted/edited/rejected) that becomes training/calibration data for later stages, effectively yielding free error analysis.
- Sits alongside non-determinism as the reason "this significantly changes the way you should be building product" relative to deterministic software.
- Directly informs the staged-version design pattern in [[Continuous Calibration Continuous Development]] and is the reasoning behind why "one-click agents" promising full autonomy on day one are considered marketing rather than credible engineering (see [[Pain Is The New Moat]]).

## Related

- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
- [[Aishwarya Naresh Reganti]] — co-articulates this concept
- [[Kiriti Badam]] — co-articulates this concept
- [[Non-Determinism In AI Products]] — the paired first difference between AI and traditional software
- [[Continuous Calibration Continuous Development]] — the framework this trade-off is layered onto
- [[Air Canada]] — cautionary example of over-extended agency (hallucinated refund policy)
- [[Agency]] — related but distinct concept: individual human disposition to act, vs. this concept's system-design trade-off
