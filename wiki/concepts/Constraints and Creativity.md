---
title: "Constraints and Creativity"
type: concept
tags: [ai, agent-design, creativity, context, engineering-principles]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Bounded Autonomy： Between Free Will and Determinism — Angus J. McLean, Oliver.md"]
last_updated: 2026-06-30
---

## Definition
Constraints and creativity is the principle that limitations — particularly context window constraints — drive innovation and better solutions in AI engineering. Abundance of resources (tokens, compute, tool access) can lead to lazy design, while scarcity forces scrappiness, deeper understanding, and more elegant solutions.

## Key Information
- Introduced by Angus J. McLean as a counter-intuitive design principle for AI engineering.
- "Abundance stops you being scrappy" — when resources are unlimited, there's less incentive to optimize.
- Self-imposed constraints are valuable: instead of asking "how much context can I use?", ask "how little context can I use and still get the task done?"
- Historical parallels from early computing:
  - Space War was built with only 4,000 words of memory.
  - Crash Bandicoot developers used creative memory tricks on the PS2 for massive performance improvements.
- Practical constraint experiments for agent builders:
  - Use older, smaller model versions to understand model behavior more intimately.
  - Build your own harness, memory, and compaction systems.
  - Preprocess and archive data — understand file systems, knowledge graphs, and retrieval.
- Working within constraints improves prompting ability, model control, fundamentals, and understanding of data.
- You never know what will come in handy later — Rosenblatt's work on the perceptron later formed the basis of dropout.
- The principle applies to context windows specifically: the challenge has shifted from getting context in to keeping noise out, and constraints help with that filtering.

## Related
- [[Angus J. McLean]] — speaker who introduced the concept
- [[summary-20260525 - Bounded Autonomy： Between Free Will and Determinism — Angus J. McLean, Oliver]] — source
- [[Bounded Autonomy]] — the parent framework where constraints are a feature, not a bug
- [[SimpleDesignPhilosophy]] — the parallel principle of keeping things simple
- [[ContextEngineering]] — the discipline of deliberate context curation
- [[Context Budget]] — practical application of context constraints
- [[Token Billionaire]] — the opposite extreme of abundant token usage
