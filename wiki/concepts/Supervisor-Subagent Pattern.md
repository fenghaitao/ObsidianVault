---
title: "Supervisor-Subagent Pattern"
type: concept
tags: [ai, agentic-systems, architecture, multi-agent]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-11
---

## Definition

[[Aishwarya Naresh Reganti]]'s account of the multi-agent architecture that actually works in practice: a single supervisor agent orchestrating narrower sub-agents that execute delegated work — contrasted with the "misunderstood" (not overhyped, but widely mis-modeled) belief that peer-to-peer, function-divided agents can simply be wired together into an "agent utopia."

## Key Information

- Reganti's framing of the misunderstanding: people take a complex problem, divide it into "you are this agent, take care of this; you are this agent, take care of that," and assume connecting all these agents together produces a working system — she says current model capabilities and orchestration techniques aren't "right there" yet for this kind of peer-to-peer, function-divided decomposition to reliably work.
- The pattern she says *does* work reliably: a supervisor agent that delegates to sub-agents which do bounded work and report back — as opposed to sub-agents communicating with each other directly in something closer to a "gossip protocol."
- Lenny's paraphrase, confirmed by Reganti: it's more successful to have one agent (or a human) orchestrating sub-agent task-splitting than to let agents communicate peer-to-peer, especially in customer-facing domains like support — because peer-to-peer designs make it far harder to control which agent is ultimately responding to the customer and to apply guardrails consistently across all of them.
- Framed as a "misunderstood" rather than "overhyped" phenomenon in the episode's overrated/underrated lightning round — Reganti stresses there's no doubt some multi-agent systems are built successfully, just not via the naive fully-decentralized model many teams assume works out of the box.

## Related

- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
- [[Aishwarya Naresh Reganti]] — articulates this pattern
- [[Kiriti Badam]] — co-guest in the same discussion
- [[Agency Control Trade-off]] — related concern about guardrail consistency across delegated agents
- [[Continuous Calibration Continuous Development]] — broader framework this architecture choice feeds into
