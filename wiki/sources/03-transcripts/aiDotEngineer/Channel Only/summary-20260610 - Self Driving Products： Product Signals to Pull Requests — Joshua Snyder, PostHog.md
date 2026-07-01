---
title: "summary-20260610 - Self Driving Products： Product Signals to Pull Requests — Joshua Snyder, PostHog"
type: source
tags: [source, transcript, observability, automation, pr-automation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260610 - Self Driving Products： Product Signals to Pull Requests — Joshua Snyder, PostHog.md"]
last_updated: 2026-06-30
---

## Core Summary

Joshua Snyder from PostHog presents a pipeline that turns observability signals into pull requests automatically. Instead of dashboards that humans check days later, product signals (errors, session replays, experiments) trigger background agents that research the issue and create PRs. The vision: self-driving products where your product builds itself.

## Key Points

- Current observability is slow: signal → dashboard → human notices days later → creates issue → creates PR. Takes hours to days.
- Pipeline: ingest signals (trillions/month) → safety filter (LLM classifier) → normalize → group related signals → research agent identifies root cause → create PR → iterate until green.
- Safety filter at pipeline entry: LLM checks for adversarial inputs before processing.
- Signals include errors, session replays, experiments, logs — normalized to unified structure with weight and embeddings.
- Goal: never look at dashboards again — just review PRs that appear in GitHub, optionally auto-shipped behind feature flags.

## Related

- [[JoshuaSnyder]] — speaker, PostHog
- [[PostHog]] — product analytics company
- [[SelfDrivingProducts]] — concept
- [[ObservabilityAutomation]] — automated observability
- [[SignalToPR]] — pipeline pattern
