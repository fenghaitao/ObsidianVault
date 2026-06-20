---
title: "fighting-context-rot"
type: synthesis
tags: [synthesis, analysis, context-rot, context-management, techniques]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20251218 - Are Agent Harnesses Bringing Back Vibe Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260528 - Harness Engineering： What Separates Top Agentic Engineers Right Now.md"
last_updated: 2026-06-20
---

# Every Way Cole Fights Context Rot

[[ContextRot]] — the degradation of LLM reasoning as context fills, "the dumb zone" — is the single problem the largest number of [[ColeMedin]]'s techniques are designed to attack. This synthesis collects all of them in one place, organized by the layer they operate at.

## Why it's the central problem

Even with huge context windows (200K-1M+ tokens), attention is finite. As context grows, signal-to-noise drops, middle-of-context content gets neglected, and reasoning capacity spent *parsing* context is capacity not spent on the *task*. Almost every advanced technique in this corpus is, at root, a context-rot mitigation. Source: [[ContextRot]].

## Layer 1: Within a single session ([[ContextEngineering]])

| Technique | How it fights context rot |
|---|---|
| **[[ModularRulesArchitecture]]** | Keep `CLAUDE.md` short (<200 lines); push task-specific rules into reference docs loaded *only when relevant*. Don't load 1000 lines of API rules during frontend work. |
| **[[ContextReset]]** | `/clear` between planning and execution. Planning balloons context; the executor starts clean with just the plan doc. |
| **[[Commandification]]** | Reuse compact command markdown instead of re-explaining workflows in-context every time. |
| **[[ProgressiveDisclosure]]** ([[ClaudeSkills]]) | Only short skill descriptions load upfront; full instructions load on-demand. A 50-skill system costs ~1500 tokens upfront, not 40,000. |
| **Smart chunking + [[Reranking]]** ([[RetrievalAugmentedGeneration]]) | Retrieve only relevant chunks; rerank to deliver a few rather than dumping 50 on the LLM. |

## Layer 2: Across sessions ([[AgentHarness]])

When one session isn't enough, the harness layer fights rot by *not keeping everything in one context*:

| Technique | How it fights context rot |
|---|---|
| **Session boundaries** | Fresh context window per session; explicit handoff artifacts carry forward only what's needed. |
| **Memory compaction** | Summarize old sessions at handoff. Lossy but bounded. |
| **Sub-agents for isolation** | Research/exploration in a [[SubAgent]]'s own context; only the *result* returns to the parent. |
| **File system as memory** | Write what you'll need later to disk (progress files, git log, codebase) rather than holding it in context. The [[KarpathyLLMWiki]] / [[SecondBrain]] pattern is this taken to its logical end. |

## Layer 3: The architectural patterns built on rot-avoidance

- **[[RalphLoop]]** — explicitly exists because handing a massive PRD to one session overwhelms the LLM "regardless of how good your [[AILayer]] is." Each looped session gets one focused task with a fresh window.
- **[[AdversarialDev]]** — the evaluator runs in *its own context session*, uncontaminated by the generator's accumulated context (this also fights [[Sycophancy]], but the separate-context design is a rot mitigation too).
- **[[SecondBrain]]** — uses [[ClaudeSkills]] over MCP specifically *because* MCP loads all tool descriptions upfront (context bloat) while skills are lazy.

## The honest limit: you can't fully win

[[ColeMedin]] is clear ([[AgentHarness]], [[ContextRot]]) that mitigation only pushes the problem further out — it never eliminates it:

> "You can't predict which observation becomes critical 10 steps later." — Manus (quoted by Cole)

Summarization in handoffs is always lossy. The same mistake recurs across sessions when a handoff drops how a failure was resolved. The compensating control is [[HumanInTheLoop]] — a human catches what the rotted/summarized context missed.

## The meta-point

Notice that fighting context rot is the *unifying thread* connecting otherwise-separate techniques. [[ModularRulesArchitecture]], [[ContextReset]], [[ProgressiveDisclosure]], [[Reranking]], [[SubAgent]] isolation, [[RalphLoop]], [[KarpathyLLMWiki]] — these all look like different topics, but they're all answers to the same question: *how do we keep the LLM's working context small, relevant, and uncontaminated?* That's why [[ContextRot]] sits near the center of this knowledge base's graph.

[[ColeMedin]]'s most explicit packaging of all this is the [[WISKFramework]] (**W**rite / **I**solate / **S**elect / **C**ompress) — git-log-as-memory and fresh-session implementation (Write), research sub-agents and the scout pattern (Isolate), just-in-time layered context (Select), and `/handoff` + `/compact` as a last resort (Compress). Every WISK pillar is a context-rot mitigation; he estimates poor context management causes ~80% of agent mistakes.

## Related

- [[ContextRot]] — the problem itself
- [[ContextEngineering]] — single-session mitigation discipline
- [[AgentHarness]] — multi-session mitigation architecture
- [[ModularRulesArchitecture]], [[ContextReset]], [[Commandification]], [[ProgressiveDisclosure]] — the per-session techniques
- [[RalphLoop]], [[AdversarialDev]], [[SubAgent]] — architectural rot-avoidance
- [[WISKFramework]] — Cole's packaged Write/Isolate/Select/Compress anti-rot framework
- [[SecondBrain]], [[KarpathyLLMWiki]] — file-system-as-memory taken to its conclusion
- [[HumanInTheLoop]] — the backstop when mitigation isn't enough
- [[ColeMedin]] — articulator
