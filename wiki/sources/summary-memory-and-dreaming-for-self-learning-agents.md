---
title: "Memory and Dreaming for Self-Learning Agents"
type: source
tags: [memory, dreaming, agents, managed-agents, self-learning]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/11 - Memory and dreaming for self learning agents.md]
last_updated: 2026-06-23
---

## Core Summary

Ravi from Anthropic's API knowledge team presents memory and dreaming as building blocks for agents that learn over time and improve from one task to the next. Memory lets agents carry forward learnings across tasks, environments, and other agents using a file-system-based approach optimized for Claude's strengths. Dreaming is a batch process that runs out-of-band to analyze session transcripts across agents, identify patterns of mistakes and inefficiency, and globally optimize shared memory stores. Together they form a frontier memory system that raises the floor for all agents and enables continuous self-learning at organizational scale.

## Key Points

- **Memory as a file system:** Claude excels at navigating file systems, so memory is modeled as files that agents can read, write, and organize using familiar tools like bash and grep.
- **Multi-agent memory:** Memory stores support read-only and read-write scopes, enabling organization-wide knowledge (SLO policies, runbooks) alongside per-agent working memory.
- **Optimistic concurrency control:** Prevents agents from clobbering each other's writes when multiple agents share the same memory store.
- **Enterprise controls:** Version history with diffs, attribution (which agent wrote what), audit trails, and a standalone API for CRUD, exports, and redactions.
- **Dreaming:** A decoupled batch process that analyzes cross-session, cross-agent transcripts to find common mistakes and inefficiencies, then proposes optimized memory updates.
- **Dreaming benefits:** Harvey saw a 6x increase in completion rates on their legal benchmark; Rakuten saw a 97% decrease in first-pass errors in production agents.
- **Architecture:** Dreaming is built on Claude Managed Agents itself, spawning sub-agents to analyze transcripts in parallel.
- **Vision:** Memory and dreaming form the basis for agents that run for days, continuously building and improving their understanding of the world around them.

## Related

- [[ClaudeManagedAgents]] — the platform memory and dreaming are built for
- [[AgenticMemory]] — the concept of persistent learning across agent sessions
- [[ClaudeCode]] — related agent tool
- [[Rakuten]] — customer achieving 97% error reduction with memory
