---
title: "AgenticMemory"
type: concept
tags: [memory, agents, self-learning, dreaming, managed-agents]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/11 - Memory and dreaming for self learning agents.md, raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/05 - Agents that remember.md, raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/18 - Memory and dreaming for self-learning agents.md]
last_updated: 2026-06-23
---

## Definition

Agentic memory is the capability for AI agents to persistently learn from their tasks, environments, and other agents across sessions. It enables agents to carry forward learnings, avoid repeating mistakes, and build shared understanding in multi-agent systems. The concept encompasses both real-time memory (reading/writing during tasks) and dreaming (asynchronous batch optimization of memory stores).

## Key Information

- **File-system-based:** Memory is modeled as files that agents manage using familiar tools (bash, grep, read, write), leveraging Claude's strength with file systems.
- **Permission scopes:** Read-only for organization-wide knowledge (runbooks, SLOs, policies); read-write for per-agent working memory.
- **Multi-agent memory:** Shared memory stores with optimistic concurrency control prevent agents from clobbering each other's writes.
- **Dreaming:** Out-of-band batch process that analyzes cross-session transcripts, identifies patterns of mistakes and inefficiencies, deduplicates, verifies, and enriches memory. Built on Claude Managed Agents itself.
- **Enterprise controls:** Version history with diffs, attribution (which agent wrote what), audit trails, standalone API for external management.
- **Results:** Rakuten saw 97% decrease in first-pass errors; Harvey saw 6x increase in legal benchmark completion rates with dreaming.
- **Long-term memory (Emergent):** Agents learn across all apps being built, not just within a single user session — first-time errors learned once and applied everywhere.
- **Vision:** Memory and dreaming form the basis for agents running for days, continuously building organizational-scale knowledge.

## Related

- [[ClaudeManagedAgents]] — the platform where memory and dreaming are implemented
- [[summary-memory-and-dreaming-for-self-learning-agents]] — London Day 1 talk
- [[summary-agents-that-remember]] — London Day 2 workshop
- [[summary-memory-and-dreaming-sf]] — San Francisco talk
- [[ClaudeFable5]] — Opus 4.7 state-of-the-art at file-system memory
- [[ContextWindow]] — related constraint that memory helps address
