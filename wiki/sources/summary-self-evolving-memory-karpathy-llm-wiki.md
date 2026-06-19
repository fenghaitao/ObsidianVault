---
title: "summary-self-evolving-memory-karpathy-llm-wiki"
type: source
tags: [source, transcript, karpathy, llm-wiki, memory, claude-code-hooks, second-brain]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260406 - I Built Self-Evolving Claude Code Memory w⧸ Karpathy's LLM Knowledge Bases.md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] walks through [[AndrejKarpathy]]'s **[[KarpathyLLMWiki|LLM knowledge base]]** pattern (from Karpathy's tweet) in detail, then builds a variant: **self-evolving Claude Code memory for *internal* data** (your conversations with the coding agent) rather than external data (articles/papers). Uses [[ClaudeCode|Claude Code hooks]] + the Claude Agent SDK to auto-capture session logs and promote them into a wiki. **This source documents the exact architecture this knowledge base is built on.**

## Key Points

### Karpathy's LLM Wiki — the compiler analogy

Karpathy's pattern, explained as a compiler pipeline:

| Compiler stage | LLM Wiki equivalent |
|---|---|
| **Source code** | `raw/` — articles, papers, transcripts as raw markdown (source of truth) |
| **Compiler** | An LLM that processes raw → summaries, links, structure |
| **Executable** | `wiki/` — compiled pages with backlinks; what you *query* |
| **Test suite (lint)** | Health checks: gaps, stale data, broken links, raw-not-yet-in-wiki |
| **Runtime** | Querying the wiki for what you're working on |

Karpathy uses [[Obsidian]] (Cole: "love seeing he uses Obsidian as a core part of his stack — I always call it my canvas").

### Key Karpathy insights

- **"I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files."** No vector DB, no semantic search needed at moderate scale. The `index.md` describes all folders/resources; the agent navigates from there.
- **The `index.md` is the most important file** — the agent's starting point for any query.
- **Spending more tokens manipulating knowledge (markdown/Obsidian) than manipulating code.** Knowledge work handled like code work.
- Karpathy shipped the whole thing as a **prompt (essentially a PRD)** in a follow-up tweet — send it to your coding agent and it one-shots the system for you.

### Cole's variant — self-evolving memory for *internal* data

Same architecture, but the "raw" input is your conversations with Claude Code (not external articles):

- **Session logs** = the raw folder. Captured automatically via **[[ClaudeCode|Claude Code hooks]]**:
  - **session-start hook** — loads `agents.md` (system description) + `index.md` (file list) into context.
  - **pre-compact hook** + **session-end hook** — send the latest messages to the Claude Agent SDK to summarize → write to the daily log (decisions, lessons, action items).
- **Flush process** (once/day) — extract concepts and connections from daily logs → populate the `wiki/` (concepts + connections folders).
- **`agents.md`** — global rules describing the *entire LLM-knowledge-base system* so the agent has meta-reasoning about what it's been dropped into.

### The compounding loop

1. Ask a question → agent searches across many wiki articles, synthesizes.
2. **File the answer back** into the wiki.
3. Wiki grows from both the synthesized answers and incoming session logs.
4. Search gets better over time. No manual maintenance.

"It just gets better and better and we really don't have to do anything to maintain this."

### Why this beats Claude Code's built-in memory

- Follows Karpathy's pattern "to a T" — simpler and (Cole argues) more effective.
- Fully customizable — you can edit the prompts sent to the Agent SDK (flush, compile).
- Self-contained and self-improving — the agent has `agents.md`, knows where the prompts are, can walk you through customizing itself.

## Related

- [[KarpathyLLMWiki]] — the pattern (this is the canonical source)
- [[AndrejKarpathy]] — pattern author
- [[SecondBrain]] — broader system this fits into
- [[ClaudeCode]] — substrate; hooks are the automation
- [[Obsidian]] — canvas
- [[RetrievalAugmentedGeneration]] — what Karpathy explicitly says you *don't* need (index files suffice)
- [[ColeMedin]] — author
