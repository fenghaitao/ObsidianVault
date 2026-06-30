---
title: "Triage Agent"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md"]
last_updated: 2026-06-29
---

# Triage Agent

## Definition

A triage agent is an autonomous agent within Raindrop that monitors signal data daily, detects spikes or anomalies, investigates root causes, and creates automatic issues. It functions like an automated on-call engineer for agent observability, digging into patterns when implicit or explicit signals indicate a problem.

## Key Information

### How It Works

1. Every day, the triage agent looks at all configured signals (user frustration, refusals, regex signals, etc.)
2. If it sees a spike in any signal, it launches an investigation
3. It has a set of tools to look into traces, trajectories, and patterns
4. It can detect issues the team didn't know about
5. It creates automatic issues with root cause analysis

### Real-World Example

Raindrop observed this working live for customers: a database provider started failing, causing a spike in user frustration. The triage agent automatically detected the spike, investigated patterns, identified that users dealing with a specific database provider were affected, and created an automatic issue — all without human intervention.

### Capabilities

- **Pattern detection**: Finds commonalities among frustrated users (same provider, same tool, same use case)
- **Root cause analysis**: Digs into trajectories to understand what went wrong
- **Unknown issue discovery**: Surfaces problems the team hasn't explicitly defined signals for
- **Automatic alerting**: Creates issues similar to how Sentry creates issues for new exceptions

### Vision for the Future

Raindrop envisions closing the loop: triage agent finds issues → creates a PR to fix them → runs experiments on the fix → verifies improvement → repeats. An infinitely self-improving agent observability loop.

## Related

- [[AgentObservability]] — parent concept
- [[Raindrop]] — platform providing the triage agent
- [[Trajectories]] — data source for investigation
- [[ImplicitSignals]] — signals the triage agent monitors
- [[ExplicitSignals]] — signals the triage agent monitors
- [[Sentry]] — analogous issue creation for traditional exceptions
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source transcript
