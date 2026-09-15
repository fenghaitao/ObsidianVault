---
title: "Declarative Configuration"
type: concept
tags: [infrastructure, Kubernetes, devops, systems-design]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns.md"]
last_updated: 2026-09-14
---

## Definition

Declarative configuration expresses the desired state of a system ("I want three replicas running") rather than imperative steps, letting the system reconcile toward that state. Kubernetes embraced this pattern from the broader infrastructure-as-code movement.

## Key Information

- You write down the objective, creating a record of intent ("I'm trying to create a reliable website, and here's what a reliable website looks like").
- Benefits: self-healing (the system knows where to return to after a failure), and code review and unit tests apply once the declaration is written down.
- Because users declare replicas rather than machine-specific processes, a failing machine can be replaced transparently — intent is captured without guessing.
- Main downside: complexity and a YAML learning curve (mitigated later by educational material and GenAI).
- Pairs with control-loop design (desired state vs current state) rather than an imperative state machine.

## Related

- [[summary-20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns]] — source summary
- [[Kubernetes]] — the system built on this pattern
- [[State Machine]] — the imperative alternative
- [[Distributed Systems]] — the control-loop context
