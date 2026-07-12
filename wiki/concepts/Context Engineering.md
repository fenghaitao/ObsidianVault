---
title: "Context Engineering"
type: concept
tags: [AI, agent, context, data-engineering]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-10
---

## Definition

Context engineering is the practice of giving AI agents the right context — data, taxonomies, historical documents, unwritten rules — to understand workflows and make good decisions. It is a critical part of building successful AI products because enterprise data and infrastructure is messy, and agents need contextual understanding that goes beyond what's documented.

## Key Information

- **Why it matters**: "AI is failing to create value today mainly about not understanding the context. And the reason it's not understanding the context is it's not plugged into the right places where actual work is happening."
- **Enterprise data is messy**: Taxonomies are inconsistent (e.g., "shoes" → "women's shoes" and "men's shoes" at the same level, AND another section under shoes that says "for women" and "for men"). Human agents know to check last-updated dates to identify dead nodes; AI agents need this context programmed in.
- **Unwritten rules**: "There are really weird rules within enterprises that are not documented anywhere."
- **The routing example**: Even simple routing is complex in enterprises because of hierarchical taxonomies with messy structures. You discover these problems only when you start building.
- **Proactive agents depend on context**: As agents get plugged into more data sources (Slack, DataDog, calendars, CRM), they gain more context and can become more proactive.
- **The progression**: As you give agents more context over time, they "start to see the world around you" and understand what metrics you're optimizing for.

## Related

- [[Proactive Agents]] — agents that need rich context to anticipate needs
- [[AI Flywheel]] — context improves as the flywheel spins
- [[Problem-First Approach (AI)]] — understanding workflows is understanding context
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
