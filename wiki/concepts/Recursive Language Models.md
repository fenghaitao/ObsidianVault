---
title: "Recursive Language Models"
type: concept
tags: [technique, long-context, context-management, mit, research]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md"]
last_updated: 2026-06-30
---

## Definition
Recursive Language Models are a technique from a seminal MIT paper (October 2024) that addresses context degradation by treating the context as an environment rather than placing it entirely in the prompt. A coding agent interacts with context programmatically (Python REPL, keyword search, regex), extracts sub-context, and passes it to an identical recursive agent for processing.

## Key Information
- Seminal paper from MIT, October 2024
- Solves context rot: even small context window occupancy can cause dramatic degradation depending on information complexity
- For O(1) tasks (needle in a haystack): context scales well regardless of prompt size
- For O(N) tasks (e.g., summing rows): performance degrades at 60-30% context usage
- For O(N²) tasks: degradation is even more severe
- Implementation: context is presented in a file, coding agent interacts programmatically via Python REPL, extracts sub-context, spawns identical recursive agent
- Extended by [[Callosum]] into [[Heterogeneous Recursion]], which maps sub-contexts to different models and chips instead of identical agents

## Related
- [[Heterogeneous Recursion]] — extension mapping to heterogeneous models/chips
- [[Context Rot]] — the problem recursive language models solve
- [[Callosum]] — company that extended the technique
- [[summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum]] — source
