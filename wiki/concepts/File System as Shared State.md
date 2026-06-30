---
title: "File System as Shared State"
type: concept
tags: [ai, agents, state-management, inter-agent-communication, harness, long-running-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
File System as Shared State is a pattern for long-running multi-agent systems where agents communicate and persist state through files on disk rather than relying on context windows or in-memory state. Files serve as persistent, greppable, and accessible records that any agent or human can pick up at any time.

## Key Information
- **Why File System**: Anthropic is a "big fan of using a file system for shared state instead of leaning on context windows for very long-running agents." Files persist across sessions and are accessible to any process
- **Contract Negotiation Medium**: Generator and evaluator agents exchange contracts as markdown files on disk — one writes, the other reads, iterating until agreement
- **Progress Tracking**: Feature lists (JSON preferred over markdown to prevent accidental overwrite), progress files with completion status, Git commits as state markers
- **Breadcrumbing**: Harness instructs agents to write learnings and state to structured files (JSON preferred) as a time-stamped log — "tried this, evaluated, found this bug, implemented this fix, this fix worked." Leaves breadcrumbs for humans and future agents
- **Live-Updating Docs**: High-level file structure documentation that updates as the agent works — enough for Claude Code and a human to come in and start iterating
- **Grepability**: File system state is easy for another model to grep through and pick up what's been happening — much more practical than parsing conversation transcripts
- **Context Window Alternative**: Files decouple state from the ephemeral context window. When a session ends or compacts, file state remains intact
- **Handoff Pattern**: Structured hand-offs via files provide clean context boundaries between agent roles — no "muddying of thoughts between model streams"
- **JSON Preference**: JSON files are preferred over markdown for critical state because models are less likely to accidentally overwrite them

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[Generator-Evaluator Pattern]] — harness pattern using this technique
- [[Contract Negotiation]] — uses file system as negotiation medium
- [[FileSystemAsContextEngineering]] — related concept about files as context
- [[Breadcrumbing]] — related pattern of leaving traces
- [[Agent Memory]] — broader category of agent state management
- [[Context Management]] — alternative approach using context windows
- [[Sprint Decomposition]] — progress tracking via file system
