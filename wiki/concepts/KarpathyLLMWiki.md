---
title: "KarpathyLLMWiki"
type: concept
tags: [concept, knowledge-management, karpathy, wiki, second-brain, pattern, compiler]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260406 - I Built Self-Evolving Claude Code Memory w⧸ Karpathy's LLM Knowledge Bases.md"
last_updated: 2026-06-20
---

## Definition

The Karpathy LLM Wiki (a.k.a. "LLM knowledge base") is a knowledge-management pattern from [[AndrejKarpathy]]: instead of using an LLM as a real-time retrieval assistant ([[RetrievalAugmentedGeneration]] / NotebookLM model), use it to **compile** raw material into a persistent, internally-cross-linked wiki of markdown pages. Synthesis happens at *ingest* time, not query time. The wiki accumulates and improves; querying it is cheap because the work was already done.

> **This vault is built on the Karpathy LLM Wiki pattern.** The `CLAUDE.md` schema, the `raw/` → `wiki/` structure, the `index.md`/`log.md` files, and the ingest/query/lint skills all derive directly from it. The pages you're reading are the "compiled artifact" of this pattern.

## Key Information

### The compiler analogy (Karpathy's framing)

The clearest way to understand the pattern — knowledge handled like source code through a compiler:

| Compiler stage | LLM Wiki equivalent | In this vault |
|---|---|---|
| **Source code** | Raw articles, papers, transcripts as markdown — the source of truth, immutable | `raw/` |
| **Compiler** | An LLM that processes raw → summaries, links, structure | the `/ingest` skill |
| **Executable** | The wiki: compiled pages with backlinks; what you *query* | `wiki/` |
| **Test suite (lint)** | Health checks: gaps, stale data, broken links, raw-not-yet-compiled | the `/lint` skill |
| **Runtime** | Querying the wiki for current work | the `/query` skill |

### Key Karpathy insights

- **"I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files."** No vector database, no semantic search needed at moderate scale. An `index.md` describing all folders/resources is the agent's starting point; it navigates the markdown directly.
- **The `index.md` is the most important file** — the agent reads it first to know where to look.
- **Karpathy uses [[Obsidian]]** as a core part of his stack. The graph view lets the agent (and human) traverse backlinks, search better, and connect knowledge for more comprehensive answers.
- **He spends more tokens manipulating knowledge (markdown/Obsidian) than manipulating code.** Knowledge work handled with the same agentic rigor as code.
- **He shipped the whole pattern as a prompt** (essentially a PRD) in a follow-up tweet — send it to your coding agent and it one-shots the system. Simple by design.

### The data flow (Karpathy's external-data version)

```
External info (web article, paper)
  │ (Obsidian Web Clipper — Karpathy explicitly recommends it)
  ▼
raw/ ── LLM compiler ──▶ wiki/ (concepts, connections, index)
                              │
                         lint (health checks)
                              │
                         query (agent navigates index → reads pages → answers)
```

### Cole's variant: self-evolving memory for *internal* data

[[ColeMedin]]'s key contribution (in `summary-self-evolving-memory-karpathy-llm-wiki`): apply the *exact same architecture* but to **internal** data — your conversations with the coding agent — rather than external articles. This gives [[ClaudeCode]] a memory that evolves with your codebase.

- **Session logs** = the `raw/` equivalent. Captured automatically via [[ClaudeCode|Claude Code hooks]]:
  - **session-start hook** — loads `agents.md` (system description) + `index.md` into context.
  - **pre-compact + session-end hooks** — send latest messages to the Claude Agent SDK to summarize → write to daily log.
- **Flush process** (daily) — extract concepts and connections from daily logs → populate the wiki.
- **`agents.md`** — global rules describing the entire LLM-knowledge-base system, giving the agent meta-reasoning about what it's operating.

### The compounding loop

1. Ask a question → agent searches across wiki articles, synthesizes an answer.
2. **File the answer back** into the wiki.
3. Wiki grows from both synthesized answers and incoming raw material.
4. Search quality improves over time. **Near-zero manual maintenance.**

This is the defining property: a knowledge base that gets richer and more useful the more you use it, without you doing the bookkeeping.

### Why it beats RAG / NotebookLM for this use case

| Property | RAG / NotebookLM | Karpathy LLM Wiki |
|---|---|---|
| When synthesis happens | Query time (re-done every time) | Ingest time (once, persists) |
| State | Stateless | Stateful — compounds |
| Infrastructure | Vector DB, embeddings, retrieval pipeline | Just markdown files + an index |
| Human-inspectable | Opaque chunks | Designed-for-humans wiki pages |
| Cost trajectory | Flat per query | Front-loaded; cheap queries after |

(See [[RetrievalAugmentedGeneration]]'s Knowledge-Conflicts section — RAG and the Wiki pattern are compatible at different layers: RAG for ephemeral retrieval over huge corpora; Wiki for distilled, reusable, compounding knowledge.)

### Relationship to [[SecondBrain]]

[[ColeMedin]]'s [[SecondBrain]] is a Karpathy-LLM-Wiki implementation with extras (skills for capabilities, a heartbeat for proactivity, integrations). The knowledge-management core of a Second Brain *is* the Karpathy pattern. They're the same idea at different scopes: KarpathyLLMWiki is the knowledge architecture; SecondBrain is that architecture plus action capabilities.

### How this vault implements it

- `raw/` — immutable sources (e.g. the Cole Medin transcripts being ingested right now).
- `wiki/{concepts,entities,sources,syntheses}/` — the compiled artifact.
- `wiki/index.md` — the all-important navigation file.
- `wiki/log.md` — append-only operation history.
- `.claude/skills/{ingest,query,lint}/` — the compiler, runtime, and test-suite as skills.
- `CLAUDE.md` — the schema / `agents.md` equivalent giving the agent meta-reasoning.

The vault diverges from Karpathy's auto-maintained-by-hooks version in being **human-triggered** (you run `/ingest`) rather than hook-automated — a deliberate choice for control and cost visibility, exactly the tradeoff discussed when this vault was set up.

## Related

- [[AndrejKarpathy]] — pattern author
- [[SecondBrain]] — the pattern + action capabilities
- [[ColeMedin]] — primary articulator/implementer in this corpus
- [[Obsidian]] — the canvas (Karpathy and Cole both use it)
- [[ClaudeCode]] — agent layer; hooks enable the self-evolving variant
- [[ClaudeSkills]] — capability layer
- [[RetrievalAugmentedGeneration]] — the counterpoint pattern
- [[ContextRot]] — what compiling-to-wiki helps avoid (query reads a focused page, not a giant corpus)
- [[summary-self-evolving-memory-karpathy-llm-wiki]] — canonical source
- [[summary-second-brain-with-claude-code-obsidian-skills]] — second-brain framing
