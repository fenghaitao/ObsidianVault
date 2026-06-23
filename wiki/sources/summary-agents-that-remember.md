---
title: "Agents That Remember"
type: source
tags: [memory, dreaming, managed-agents, multi-session, self-improvement]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/05 - Agents that remember.md]
last_updated: 2026-06-23
---

## Core Summary

Kevin from Anthropic presents a hands-on workshop on building agents with persistent memory using Claude Managed Agents' memory stores and dreaming features. The session demonstrates the base case of isolated sessions (no information transfer), then introduces memory stores as persistent file-system-like stores that agents can read and write across sessions. Dreaming is introduced as an asynchronous batch process that analyzes session transcripts, fact-checks, enriches, deduplicates, and organizes memory stores to prevent unbounded growth. The workshop walks through creating memory stores, attaching them to sessions, running dream jobs, and using the output memory store for improved future sessions.

## Key Points

- **Base case problem:** Agents in isolated sessions cannot transfer information between sessions — telling one session something and asking another yields no recall.
- **Memory stores:** Persistent file-system-like stores mounted into session containers. Agents use bash, grep, and file read/write tools to interact with memory, leveraging Claude's strength with file systems.
- **Memory store configuration:** Per-session access control (read-write or read-only), optional prompt to steer what agents should remember, and the ability to create multiple stores per organization/user/workspace.
- **Dreaming architecture:** Multi-agent harness with orchestrator spawning one sub-agent per input session transcript. Each sub-agent analyzes transcripts for missed details, fact-checks, and enrichment opportunities.
- **Dreaming is non-destructive:** Input memory store is cloned; dreaming writes to a new output memory store. Humans can review diffs in the console before adopting.
- **Dreaming outputs:** Creates index files for efficient retrieval, adds metadata (dates, identifiers), reformats memory files with slugs and descriptions, and enriches with details agents missed during live sessions.
- **Token efficiency:** ~95% cache hit rate on dream sessions due to agentic processing patterns. Batch API-style discounts being explored.
- **Three composable layers:** Sessions (isolated, ephemeral) → Memory stores (cross-session persistence) → Dreaming (organization, enrichment, improvement over time).

## Related

- [[ClaudeManagedAgents]] — the platform for memory and dreaming
- [[AgenticMemory]] — the concept of persistent agent learning
- [[summary-memory-and-dreaming-for-self-learning-agents]] — London Day 1 talk on same topic
