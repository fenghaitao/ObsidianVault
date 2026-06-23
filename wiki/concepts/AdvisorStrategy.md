---
title: "AdvisorStrategy"
type: concept
tags: [claude, cost-optimization, model-strategy, api]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/01 - Code with Claude London 2026： Opening Keynote.md]
last_updated: 2026-06-23
---

## Definition

The advisor strategy is a Claude API pattern that splits execution from advising: a smaller model (Haiku or Sonnet) executes tasks, and when it needs help, it reaches out to a larger model (Opus) for advice. This delivers frontier model quality at significantly lower cost.

## Key Information

- **How it works:** update the tools array on the Messages API. The smaller model executes; when stuck, it calls the larger model as an advisor.
- **Results:** Sonnet + Opus advisor performed better than Sonnet alone and was cheaper because Opus advised it to complete work more efficiently.
- **Eve Legal case study:** achieved frontier model quality at 5x lower cost using the advisor strategy.
- **Use cases:** premium product experiences where cost matters, extremely high-volume agentic workloads where ROI must be tracked.
- **Implementation:** simple -- just update the tools configuration; no complex orchestration needed.

## Related

- [[summary-code-with-claude-london-2026-keynote]] — keynote where it was introduced
- [[summary-picking-the-right-model]] — related model selection framework
- [[ClaudeManagedAgents]] — platform that can leverage this strategy
