---
title: "summary-20260316 - I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It"
type: source
tags: [source, original-material, context-management, claude-code, wisk, context-rot]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260316 - I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It.md"]
last_updated: 2026-06-20
---

## Core Summary

After 2,000+ hours in [[ClaudeCode]], [[ColeMedin]] distills his context-management strategies into the **[[WISKFramework|WISK framework]]** — **W**rite, **I**solate, **S**elect, **C**ompress — all aimed at the same goal: keep the context window as lean as possible while still giving the agent everything it needs. The premise: ~80% of agent mistakes come from poor context management ([[ContextRot]]), and the 1M-token limit does *not* fix it.

## Key Points

- **Why context rot is the focus**: the **Chroma Technical Report** ("how increasing input tokens impacts LLM performance") shows that *being able* to fit tokens doesn't mean you *should*. The **needle-in-haystack** problem worsens as the window fills, and large codebases (repeated patterns) breed **distractors** — similar-but-wrong info the LLM confidently retrieves. Applies to Claude Code's 1M limit too.
- **W — Write (externalize memory)**:
  1. **Git log as long-term memory** — a standardized `/commit` command produces consistent, detailed, *two-part* messages ("here's what we built" + "here's how we improved the AI layer") so `/prime` can read the log to guide what's next.
  2. **Fresh context window for implementation** — always plan in one session → emit a single structured-plan markdown → `/execute` it in a *new* session with that doc as the only context.
  3. **Progress files / decision logs** — `handoff.md` / `todo.md`; a `/handoff` command summarizes the session before context fills (e.g. e2e testing hit 200k/1M) so a fresh agent can continue without the bloat.
- **I — Isolate (sub-agents)**: use [[SubAgent]]s for *research* every session — they burn 10s–100s of thousands of tokens but return ~500-token summaries (Anthropic cites a **90.2%** context improvement; one example used 44k vs hundreds of thousands). Run in parallel for speed. Not for implementation. Plus the **scout pattern**: send a sub-agent to explore docs/codebase (e.g. `.claude/docs`, or Confluence/Drive) and *decide* what's worth loading into the main context before committing it.
- **S — Select (just-in-time, not just-in-case)** — a 4-layer context model:
  1. **Global rules** (always loaded; concise, ~500–700 lines: architecture, commands, testing/logging).
  2. **On-demand context** (per-task-type reference docs, e.g. frontend rules, API rules, workflow-YAML reference) — added only when working that area.
  3. **Skills** ([[ProgressiveDisclosure]]) — description upfront, full `SKILL.md` + scripts on demand (e.g. the agent-browser skill for e2e).
  4. **Prime commands** — live codebase exploration (via sub-agents) at session start; Cole keeps multiple specialized ones (`/prime`, `/prime-workflows`).
- **C — Compress** (avoid if possible — "the best compression strategy is not needing compression"): `/handoff` (custom summary → fresh session, best when you'd compact more than twice) and Claude Code's built-in `/compact` (optionally with summarization instructions to focus on, e.g., the edge cases just tested). After compacting, ask the agent what it remembers to confirm.
- **New Archon context**: Cole demos all this on the **new [[Archon]]** — his "AI command center" for creating/managing/executing long-running AI coding workflows (mission control, run logs, a workflow builder — "the N8N for AI coding," PR-validation workflows).

## Related

- [[WISKFramework]] — the W/I/S/C framework this video defines
- [[ContextRot]] — the problem WISK fights (Chroma report, distractors)
- [[ClaudeCode]] — the surface; 2,000+ hours of use
- [[SubAgent]] — the Isolate pillar + scout pattern
- [[ContextReset]] — fresh session for implementation (Write pillar)
- [[ProgressiveDisclosure]] — the skills layer of Select
- [[Archon]] — the demo codebase / AI command center
- [[fighting-context-rot]] — synthesis WISK slots into
