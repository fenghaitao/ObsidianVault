---
title: "Bad Vs Sad Framework"
type: concept
tags: [quality, engineering-management, framework, verification]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork).md"]
last_updated: 2026-07-10
---

## Definition

The "bad vs. sad" framework is a high-level quality-classification scheme introduced by [[Fiona Fung]] on [[Anthropic]]'s [[Claude Code]] and [[Claude Cowork]] teams, distinguishing severe/irrecoverable failures ("bad") from recoverable pain points ("sad") to make quality trends legible across many different product surfaces.

## Key Information

- "Bad" = a very bad, irrecoverable error — Fung's example: a CLI crash that causes lost work.
- "Sad" = a pain point that is recoverable but degrades experience — Fung's example: UI flickering.
- Stacking enough "sad" incidents can effectively become "bad" — the framework treats severity as cumulative, not just binary.
- Designed to solve a specific problem with raw metrics dashboards (load time, reliability numbers, etc.): across many different product surfaces it's hard to tell at a glance "is that a good number or not," whereas a shared bad/sad vocabulary gives a consistent, qualitative read on experience quality.
- Each team is given agency (see [[High Agency High Accountability]]) to define what constitutes "bad" and "sad" for its own surface area/service, and to set its own improvement goals against those definitions, rather than being handed one universal metric.
- Positioned by Fung as part of a broader shift toward proactive, earlier quality detection, alongside investment in tests/evals and automated monitoring, rather than relying primarily on manual code review to catch problems (review time is scarce given ~8x higher shipping throughput).

## Related

- [[summary-04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork)]] — source summary
- [[Fiona Fung]] — introduced this framework
- [[Anthropic]] — organizational context
- [[Claude Code]] — product/team where this framework is applied
- [[High Agency High Accountability]] — related value (each team gets agency to define its own thresholds)
- [[Trust But Verify]] — broader verification philosophy this framework supports
