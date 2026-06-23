---
title: "WISKFramework"
type: concept
tags: [concept, context-management, claude-code, context-rot, framework]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260316 - I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It.md"
last_updated: 2026-06-20
---

## Definition

The WISK framework is [[ColeMedin]]'s battle-tested system (from 2,000+ hours in [[ClaudeCode]]) of context-management strategies for AI coding — **W**rite, **I**solate, **S**elect, **C**ompress. Every pillar serves one question: *how do we keep the context window as lean as possible while still giving the agent all the context it needs?* It is the most concrete operational answer in the corpus to [[ContextRot]] (which Cole estimates causes ~80% of agent mistakes).

## Key Information

### W — Write (externalize the agent's memory)

- **Git log as long-term memory** — a standardized `/commit` command writes detailed, two-part messages (what was built + how the [[AILayer]] was improved); `/prime` later reads the log to decide what's next.
- **Fresh context window per implementation** — plan in one session → single structured-plan markdown → `/execute` it in a new session with that doc as the *only* context. See [[ContextReset]].
- **Progress files / decision logs** — `handoff.md` / `todo.md`; a `/handoff` command summarizes a session before context fills so a fresh agent continues without bloat.

### I — Isolate (sub-agents)

- Use [[SubAgent]]s for *research* (not implementation): they consume huge context but return a small summary (Anthropic cites ~**90.2%** improvement; e.g. 44k tokens used instead of hundreds of thousands). Run in parallel for speed.
- **Scout pattern** — dispatch a sub-agent to explore docs/codebase and *decide* what's relevant to load into the main context before committing it.

### S — Select (just-in-time, not just-in-case)

A 4-layer context model — load a piece only if you're confident it's needed now:

| Layer | Loads | When |
|---|---|---|
| **Global rules** | architecture, commands, testing/logging (~500–700 lines) | always |
| **On-demand context** | per-task-type reference docs (frontend, API, workflow YAML) | when working that area |
| **Skills** ([[ProgressiveDisclosure]]) | description upfront; full `SKILL.md` + scripts on demand | when the capability is needed |
| **Prime commands** | live codebase exploration via sub-agents | at session start (multiple specialized variants) |

### C — Compress (last resort)

"The best compression strategy is not needing compression." If you must: `/handoff` (custom summary → fresh session; best when you'd otherwise compact more than twice) and Claude Code's built-in `/compact` (optionally with summarization instructions). After compacting, ask the agent what it remembers to verify.

## Related

- [[ContextRot]] — the problem WISK is built to fight
- [[ClaudeCode]] — the primary surface
- [[SubAgent]] — the Isolate pillar (+ scout pattern)
- [[ContextReset]] — the fresh-session practice in Write
- [[ProgressiveDisclosure]] — the skills layer of Select
- [[AILayer]] — what the Select layers populate
- [[ContextEngineering]] — the discipline WISK operationalizes
- [[ColeMedin]] — articulator
- [[fighting-context-rot]] — synthesis this framework anchors
- [[summary-20260316 - I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It]] — primary source
- [[summary-20260319 - The Subagent Era Is Officially Here - Learn this Now]] — the "Isolate" pillar at industry scale (cheap sub-agent models)
