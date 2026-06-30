---
title: "summary-20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked"
type: source
tags: [source, transcript, context-engineering, agents, context-engine, social-graph]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked.md"]
last_updated: 2026-06-30
---

## Core Summary

Brandon Waselnuk from Unblocked presents on stopping the practice of "babysitting" AI agents. He frames the problem as a context gap: agents spawn with zero organizational knowledge, and engineers become the context engine manually feeding them information. The solution is a context engine that provides curated, exhaustive, and personalized context at runtime. He debunks three myths about building context: naive RAG (fails due to satisfaction of search), just connecting enough MCPs (provides access, not understanding), and bigger context windows (agents cannot reason over massive context). He shares three hard-won lessons from building Unblocked's context engine and demonstrates an open-source social graph component that maps engineering relationships to power context retrieval.

## Key Points

- The "care and feeding" problem: agents spawn with zero context; engineers become the context engine.
- Three myths about context: naive RAG fails due to satisfaction of search; MCPs alone provide access without understanding; larger context windows don't solve reasoning.
- Without a context engine, agents produce code that compiles but is architecturally wrong — a senior engineer would reject it.
- A context engine must: reason across all systems of record, do targeted exhaustive retrieval, resolve conflicts, respect data governance, personalize via social graphs, and optimize tokens.
- Conflict resolution is critical: code may say one thing, a CTO's Slack message another; the engine must weigh authority.
- Social graphs (expert graphs) map who works with whom, code review relationships, and PR history to personalize context.
- Caching correct answers is dangerous: context changes within 24 hours; cached answers become stale lies.
- Open-source social graph tool demonstrated: procedurally generates expert graphs from code repos, showing author-reviewer relationships and heat maps.
- With a context engine, PRs get nitpicks instead of "this would break our system" rejections.

## Related

- [[Brandon Waselnuk]] — speaker
- [[Unblocked]] — company building context engines
- [[ContextEngine]] — core technology presented
- [[Satisfaction of Search]] — phenomenon that undermines naive RAG
- [[Social Graph]] — key component of a context engine
- [[Conflict Resolution]] — handling conflicting signals across data sources
- [[Token Optimization]] — sending compressed, relevant context to agents
- [[DoomLoop]] — failure mode addressed by context engines
- [[summary-20260503 - Mergeable by default： Building the context engine to save time and tokens — Peter Werry, Unblocked]] — related talk by Unblocked founder
