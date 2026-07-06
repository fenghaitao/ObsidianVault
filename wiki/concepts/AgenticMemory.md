---
title: "AgenticMemory"
type: concept
tags: [memory, agents, self-learning, dreaming, managed-agents]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/11 - Memory and dreaming for self learning agents.md, raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/05 - Agents that remember.md, raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/18 - Memory and dreaming for self-learning agents.md, raw/01-articles/claude/2026-04-23 - Built-in memory for Claude Managed Agents.md, raw/01-articles/claude/2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration.md]
last_updated: 2026-07-05
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
- **Public beta (April 23, 2026):** memory on Claude Managed Agents reached public beta, available via the Claude Console (workspaces/default/memory-stores) or a new CLI. Memories are exportable files independently manageable via API; every change is tracked in a detailed audit log identifying the source agent/session, with support for rolling back to an earlier version or redacting content from history. Console surfaces memory updates as session events.
- **Additional customer evidence:** [[Netflix]] uses memory to carry context across sessions — including insights that took multiple turns to uncover and mid-conversation human corrections — instead of manually updating prompts/skills. [[Wisedocs]] built a document-verification pipeline on cross-session memory to spot and remember recurring document issues, speeding up verification by 30%. [[Ando]] is building a workplace messaging platform on Managed Agents, using memory to capture how each organization interacts rather than building memory infrastructure themselves. This restates and specifies the Rakuten 97% first-pass-error-reduction figure as arising from task-based long-running agents learning from every session within workspace-scoped, observable boundaries.
- **Dreaming launches as a named, standalone research preview (May 19, 2026)**: previously described only as an in-context-window bullet ("agents look back over all past sessions, update memory and skills"), dreaming is now specified as a **scheduled** process that reviews both past sessions and memory stores, extracts patterns (recurring mistakes, workflows agents converge on, preferences shared across a team), and curates/restructures memory to stay high-signal as it evolves — with developer-controlled autonomy (fully automatic updates, or human review before changes land). Anthropic frames memory and dreaming as a two-part system: memory captures learning *as* an agent works; dreaming refines that memory *between* sessions, pulling shared learnings across agents. Especially useful for long-running work and multiagent orchestration. [[Harvey]] is cited as a dreaming customer: agents remember filetype workarounds and tool-specific patterns between long-form legal-drafting sessions, corroborating (via an independent source) the existing ~6x completion-rate figure above. See [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]].

## Related

- [[ClaudeManagedAgents]] — the platform where memory and dreaming are implemented
- [[summary-18 - Memory and dreaming for self-learning agents]] — London Day 1 talk
- [[summary-05 - Agents that remember]] — London Day 2 workshop
- [[summary-18 - Memory and dreaming for self-learning agents]] — San Francisco talk
- [[ClaudeFable5]] — Opus 4.7 state-of-the-art at file-system memory
- [[ContextWindow]] — related constraint that memory helps address
- [[analysis-agent-evolution-loop-to-self-learning]] — the evolution culminating in memory and dreaming
- [[summary-2026-04-23 - Built-in memory for Claude Managed Agents]] — public-beta memory launch article
- [[Netflix]] — memory customer, cross-session context continuity
- [[Wisedocs]] — memory customer, document-verification pipeline
- [[Ando]] — memory customer, workplace messaging platform
- [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]] — dreaming's research-preview launch article
- [[Harvey]] — dreaming customer, cross-session legal-drafting pattern recall
