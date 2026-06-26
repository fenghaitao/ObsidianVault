---
title: "SimpleDesignPhilosophy"
type: concept
tags: [agent-architecture, design-philosophy, coding-agents, engineering-principles]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md"]
last_updated: 2026-06-25
---

## Definition
Simple design philosophy is the principle that simple architecture beats complex architecture in coding agent design, inspired by the Zen of Python: "Simple is better than complex, complex is better than complicated, flat is better than nested." This philosophy underpins Claude Code's success — rather than building elaborate DAGs, classifiers, and RAG pipelines, the team built a simple while-loop and trusted better models.

## Key Information
- Directly inspired by the Zen of Python (`import this`)
- Core tenets: simple > complex > complicated, flat > nested
- Applies equally to database schema design and autonomous coding agent design
- Claude Code's genius: they scrapped embeddings, classifiers, pattern matching, and RAG, saying "we don't need all these fancy paradigms to get around how the model's bad — let's just make a better model and let it cook"
- The philosophy extends to Claude.md: instead of building a system where the model researches the repo (like Cursor 1.0's vector DB), just use a markdown file
- Tagline: "give it tools and get out of the way" and "less scaffolding, more model"
- Jared Zoneraich warns engineers against over-optimizing: when you first build an agent, resist the urge to add prompts preventing every hallucination
- Anthropic's "AGI pill" philosophy: don't over-engineer around model flaws today because models will get better

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[MasterWhileLoop]] — the architecture that embodies this philosophy
- [[DAGvsLoopArchitecture]] — the trade-off this philosophy addresses
- [[BashAsUniversalAdapter]] — tool minimalism as an expression of this philosophy
- [[ClaudeCode]] — the agent built on this philosophy
