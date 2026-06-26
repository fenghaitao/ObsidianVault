---
title: "Nested Context"
type: concept
tags: [ai, agents, context-management, design-pattern]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md"]
last_updated: 2026-06-26
---

## Definition
Nested Context is Kitze's design pattern in Wolfer where hierarchical topic trees inject parent topic descriptions into child topic conversations. Instead of relying on memory retrieval, the first prompt in a child topic includes descriptions of all ancestor topics, giving the agent immediate context about the broader purpose.

## Key Information
- Implemented in Wolfer as an alternative to agent memory systems
- Hierarchical topic tree: work → projects → Benji → Benji customer support
- When chatting in a child topic, the first prompt injects descriptions of all parent topics
- "It doesn't need to pull from memory or some magical place. It just looks at the topic, the parent topic, the parent topic."
- "It takes all the descriptions together and it immediately knows what is my work, what is Benji, what are my projects, and how do I do customer support."
- Kitze: "I can get more out of that than hoping for some memory system that's going to pull the right context out of the right place."
- Kitze does not believe in agent memory: "People are like, 'Oh, we finally saw Mila Yov which solved memory.' I'm like, 'No, absolutely she didn't solve memory.'"

## Related
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — source
- [[Wolfer]] — implementation
- [[Kitze]] — designer
- [[AgentMemory]] — the approach Nested Context replaces
- [[ContextEngineering]] — broader discipline
- [[AgentSpecialization]] — related multi-agent pattern
